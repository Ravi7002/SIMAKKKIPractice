import json, random, re, os, copy, sys

# ─── Load real exam bases ────────────────────────────────────────────────────
with open('realQ1.json', 'r', encoding='utf-8') as f:
    q1 = json.load(f)
with open('realQ2.json', 'r', encoding='utf-8') as f:
    q2 = json.load(f)

bases = [q1, q2]
os.makedirs(os.path.join('quiz-app', 'src', 'GeneratedTryouts'), exist_ok=True)

# ─── Load English passage pools ──────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from english_pool_v4 import POOL as LONG_PASSAGES

# ─── Text mutation ───────────────────────────────────────────────────────────
def mutate_text(text, skip_numbers=False):
    if not isinstance(text, str): return text
    def rep_num(m):
        start, end = m.start(), m.end()
        if start > 0 and text[start-1] in '.,': return m.group(0)
        if end < len(text) and text[end] in '.,': return m.group(0)
        n = int(m.group(0))
        if n == 0: return "0"
        if n < 10: return str(n + random.randint(1, 2))
        if n < 100: return str(n + random.randint(1, 5))
        return str(n + random.randint(5, 15))
    if not skip_numbers:
        text = re.sub(r'(?<![.,])\b(\d+)\b(?![.,])', lambda m: rep_num(m), text)
    return text

# ─── Auto-hints ──────────────────────────────────────────────────────────────
def generate_hints(q):
    subject = str(q.get('subject', '')).lower()
    topic   = str(q.get('topic', '')).lower()
    q_text  = str(q.get('question_text', '')).lower()
    if 'english' in subject:
        if 'grammar' in topic or 'fill' in q_text:
            return ["Identify the subject and its number (singular or plural).", "Check the tense marker (is, was, have been)."]
        if 'reading' in topic:
            return ["Look for the specific keywords in the passage.", "Eliminate answers that are not mentioned in the text."]
        if 'cohesion' in topic or 'relationship' in q_text or 'paragraph' in q_text:
            return ["Identify the main idea of each paragraph first.", "Check if the second paragraph provides evidence, a contrast, or a solution to the first."]
        return ["Re-read the relevant part of the passage carefully."]
    if 'logical' in subject:
        return ["Draw a diagram or list the conditions systematically.", "If-then statements are keys to the sequence."]
    return ["Identify the core formula needed for this problem."]

# ─── Main generation ─────────────────────────────────────────────────────────
SUBJECT_ORDER = ['Basic Mathematics', 'English', 'Quantitative Reasoning', 'Logical Reasoning']

for i in range(1, 5): 
    raw_base = copy.deepcopy(bases[i % 2])
    
    # Process non-English (60 Qs total)
    non_english = []
    for item in raw_base:
        if isinstance(item, dict) and 'passages' in item and 'questions' in item:
            pmap = {p['id']: p['text'] for p in item['passages']}
            for q in item['questions']:
                if str(q.get('subject','')).lower() == 'english': continue
                if q.get('passage_id') and not q.get('passage'): q['passage'] = pmap.get(q['passage_id'])
                non_english.append(q)
        elif isinstance(item, dict) and str(item.get('subject','')).lower() != 'english':
            non_english.append(item)

    # Process English (Exactly 20 Qs from 7 distinct passages per tryout)
    english_qs = []
    
    # Select 7 distinct passages for this tryout
    start_idx = (i - 1) * 7
    tryout_passages = []
    for j in range(7):
        p_idx = (start_idx + j) % 28 # Rotate through main 28 passages
        if j == 3:
            # Force the 4th passage to be the specially structured ones (indices 28-31)
            # This aligns exactly with questions 11 and 12 (Test #31 and #32)
            p_idx = 28 + (i - 1)
        tryout_passages.append(copy.deepcopy(LONG_PASSAGES[p_idx]))

    # Flatten questions and assign passage text
    flat_questions = []
    
    # We want exactly 20 questions from 7 passages.
    # A pattern of [3, 4, 3, 2, 3, 3, 2] yields exactly 20.
    q_counts = [3, 4, 3, 2, 3, 3, 2]
    
    for idx, p in enumerate(tryout_passages):
        count_target = q_counts[idx]
        passage_qs = copy.deepcopy(p['questions'])
        
        while len(passage_qs) > count_target:
            passage_qs.pop() # Remove questions if we need fewer (e.g. 2 instead of 3)
            
        while len(passage_qs) < count_target:
            # Generate a 4th question if we need more (e.g. 4 instead of 3)
            passage_qs.append({
                "subject": "English",
                "topic": "Reading Comprehension",
                "question_text": "Which of the following best captures the main theme of the passage?",
                "options": [
                    {"letter": "A", "text": "The specific detail mentioned in paragraph 2"},
                    {"letter": "B", "text": "The historical background mentioned in paragraph 1"},
                    {"letter": "C", "text": "The overall conceptual framework unifying all paragraphs"},
                    {"letter": "D", "text": "The future challenges outlined in paragraph 3"},
                    {"letter": "E", "text": "None of the above accurately describes the main theme"}
                ],
                "correct_answer": "C",
                "explanation": "To capture the main theme, you must select the option that encompasses the overarching narrative of all paragraphs combined, rather than an isolated detail."
            })
            
        for q in passage_qs:
            q['passage'] = p['text']
            q['passage_id'] = p['id']
            flat_questions.append(q)
    
    english_qs = flat_questions

    # Mutate and format
    for idx, q in enumerate(english_qs):
        base_id = q.get('id', f'eng_{idx+1:02d}')
        q['id'] = f"{base_id}_gen_{i}"
        # Disable text mutation for English questions because it corrupts paragraph and sentence indices!
        # q['passage'] = mutate_text(q['passage'])
        # q['question_text'] = mutate_text(q['question_text'])
        # for opt in q.get('options', []):
        #     opt['text'] = mutate_text(opt['text'])
        q['hints'] = generate_hints(q)

    # Combine and Sort
    all_qs = english_qs + non_english
    all_qs.sort(key=lambda q: (SUBJECT_ORDER.index(q.get('subject','')) if q.get('subject','') in SUBJECT_ORDER else 99))

    # Save
    with open(f'quiz-app/src/GeneratedTryouts/tryout_{i}.json', 'w', encoding='utf-8') as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    
    print(f"Tryout {i}: English ({len(english_qs)}), Others ({len(non_english)}), Total ({len(all_qs)})")

# Clean up
for i in range(5, 21):
    path = f'quiz-app/src/GeneratedTryouts/tryout_{i}.json'
    if os.path.exists(path): os.remove(path)

print("\nSuccess: Generated 4 tryouts with exactly 7 distinct passages / 20 English questions each.")
