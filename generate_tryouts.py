import json, random, re, os, copy, sys

# ─── Load real exam bases ────────────────────────────────────────────────────
with open('realQ1.json', 'r', encoding='utf-8') as f:
    q1 = json.load(f)
with open('realQ2.json', 'r', encoding='utf-8') as f:
    q2 = json.load(f)

bases = [q1, q2]
os.makedirs(os.path.join('quiz-app', 'src', 'GeneratedTryouts'), exist_ok=True)

# ─── Load English passage pool ───────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from english_pool_v2 import POOL
ALL_PASSAGES = POOL # 28 passage sets

# ─── Text mutation ───────────────────────────────────────────────────────────
def mutate_text(text, skip_numbers=False):
    if not isinstance(text, str): return text
    def rep_num(m):
        start, end = m.start(), m.end()
        if start > 0 and text[start-1] in '.,': return m.group(0)
        if end < len(text) and text[end] in '.,': return m.group(0)
        n = int(m.group(0))
        if n == 0: return "0"
        if n < 10: return str(n + random.randint(1, 3))
        if n < 100: return str(n + random.randint(1, 10))
        return str(n + random.randint(10, 100))
    if not skip_numbers:
        text = re.sub(r'(?<![.,])\b(\d+)\b(?![.,])', lambda m: rep_num(m), text)
    swaps = {"John": "Michael", "Mary": "Sarah", "apples": "oranges"}
    for k, v in swaps.items():
        text = re.sub(rf'\b{re.escape(k)}\b', v, text)
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
        if 'cohesion' in topic or 'irrelevant' in q_text:
            return ["Read each sentence and check if it follows the main theme.", "The odd one out usually introduces a completely different subject."]
        return ["Re-read the relevant part of the passage carefully."]
    if 'logical' in subject:
        return ["Draw a diagram or list the conditions systematically.", "If-then statements are keys to the sequence."]
    return ["Identify the core formula needed for this problem."]

# ─── Main generation ─────────────────────────────────────────────────────────
SUBJECT_ORDER = ['Basic Mathematics', 'English', 'Quantitative Reasoning', 'Logical Reasoning']

for i in range(1, 5): # Generate only 4 tryouts
    raw_base = copy.deepcopy(bases[i % 2])
    
    # Process non-English
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

    for q in non_english:
        q['id'] = f"{q.get('id','q')}_gen_{i}"
        subject = str(q.get('subject','')).lower()
        skip_nums = 'logical' in subject
        q['question_text'] = mutate_text(q.get('question_text',''), skip_nums)
        if 'passage' in q: q['passage'] = mutate_text(q['passage'], skip_nums)
        for opt in q.get('options', []): opt['text'] = mutate_text(opt.get('text',''), skip_nums)
        if 'explanation' in q: q['explanation'] = mutate_text(q['explanation'], skip_nums)
        if not q.get('hints'): q['hints'] = generate_hints(q)

    # Process English (7 passages per tryout)
    english_qs = []
    start_idx = (i - 1) * 7
    for p_idx in range(start_idx, start_idx + 7):
        ps = copy.deepcopy(ALL_PASSAGES[p_idx])
        for q in ps['questions']:
            q['id'] = f"{ps['id']}_{ps['questions'].index(q)}_gen_{i}"
            q['passage'] = ps['text']
            q['passage_id'] = ps['id']
            q['hints'] = generate_hints(q)
            english_qs.append(q)

    all_qs = english_qs + non_english
    all_qs.sort(key=lambda q: (SUBJECT_ORDER.index(q.get('subject','')) if q.get('subject','') in SUBJECT_ORDER else 99))

    with open(f'quiz-app/src/GeneratedTryouts/tryout_{i}.json', 'w', encoding='utf-8') as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)

# Clean up old tryouts
for i in range(5, 21):
    path = f'quiz-app/src/GeneratedTryouts/tryout_{i}.json'
    if os.path.exists(path): os.remove(path)

print("Generated 4 tryouts with 7 unique English passages each.")
