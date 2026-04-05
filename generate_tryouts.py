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
from english_pool import POOL as POOL1
from english_pool_part2 import POOL_PART2 as POOL2

# Combine and group into 4 sets of 7
# Each pool has sets of 7 or 8. Total here is 8 + 7 = 15.
# We need 28 passages (7 per tryout * 4 tryouts).
# Since we only have 15 long passages, we will cycle/reuse them but they will have mutated text.
LONG_PASSAGES = POOL1 + POOL2 # Total 15 long, high-quality passages

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

    # Process English (Exactly 20 Qs from 7 long passages)
    english_qs = []
    
    # Select 7 passages for this tryout (using modulo to cycle through the 15 available)
    tryout_passages = []
    for j in range(7):
        p_idx = ((i - 1) * 7 + j) % len(LONG_PASSAGES)
        tryout_passages.append(copy.deepcopy(LONG_PASSAGES[p_idx]))

    # Flatten questions and assign passage text
    flat_questions = []
    for p in tryout_passages:
        for q in p['questions']:
            q['passage'] = p['passage_text']
            flat_questions.append(q)
    
    # Randomly select exactly 20 questions if there are more
    if len(flat_questions) > 20:
        random.shuffle(flat_questions)
        english_qs = flat_questions[:20]
    else:
        english_qs = flat_questions

    # Mutate and format
    for q in english_qs:
        q['id'] = f"{q.get('id','eq')}_gen_{i}"
        q['passage'] = mutate_text(q['passage'])
        q['question_text'] = mutate_text(q['question_text'])
        for opt in q.get('options', []):
            opt['text'] = mutate_text(opt['text'])
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

print("\nSuccess: Generated 4 tryouts with 20 high-quality LONG passages/questions each.")
