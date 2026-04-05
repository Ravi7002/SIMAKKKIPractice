"""
generate_tryouts.py
Builds 20 practice tryout JSON files under quiz-app/src/GeneratedTryouts/.

English section  → drawn from the 15-passage pool (unique combo of 4 passages per tryout)
All other sections → drawn from realQ1 / realQ2, alternating per tryout
"""

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
from english_pool import POOL
from english_pool_part2 import POOL_PART2
ALL_PASSAGES = POOL + POOL_PART2            # 15 passage sets, 5 questions each

# Pre-compute 20 unique 4-passage combinations (gives us exactly 20 English qs per tryout)
from itertools import combinations
COMBO_SEED = list(combinations(range(15), 4))   # C(15,4) = 1365
# Use a fixed shuffled order so sets are stable across re-runs
rng = random.Random(42)
rng.shuffle(COMBO_SEED)
TRYOUT_COMBOS = COMBO_SEED[:20]                 # first 20 unique combos

# ─── Text mutation ───────────────────────────────────────────────────────────
def mutate_text(text, skip_numbers=False):
    if not isinstance(text, str):
        return text

    def rep_num(m):
        start, end = m.start(), m.end()
        if start > 0 and text[start-1] in '.,': return m.group(0)
        if end < len(text) and text[end] in '.,':  return m.group(0)
        n = int(m.group(0))
        if n == 0: return "0"
        if n < 10:  return str(n + random.randint(1, 3))
        if n < 100: return str(n + random.randint(1, 10))
        return str(n + random.randint(10, 100))

    if not skip_numbers:
        text = re.sub(r'(?<![.,])\b(\d+)\b(?![.,])', lambda m: rep_num(m), text)

    swaps = {
        "John": "Michael", "Mary": "Sarah",
        "apples": "oranges", "cars": "bicycles",
        "company": "corporation",
        "profit": "revenue", "loss": "deficit",
        "increase": "change", "decrease": "drop",
    }
    for k, v in swaps.items():
        text = re.sub(rf'\b{re.escape(k)}\b', v, text)
    return text

# ─── Auto-hints ──────────────────────────────────────────────────────────────
def generate_hints(q):
    subject = str(q.get('subject', '')).lower()
    topic   = str(q.get('topic', '')).lower()
    q_text  = str(q.get('question_text', '')).lower()

    if 'english' in subject:
        if 'paragraph' in q_text and ('relationship' in q_text or 'connection' in q_text):
            return [
                "Read the LAST sentence of the first paragraph and the FIRST sentence of the second paragraph — these transition sentences reveal the logical link.",
                "Ask: Does paragraph B explain, contradict, extend, or give examples of paragraph A?",
                "Common relationships: Cause→Effect, Problem→Solution, General→Specific, Contrast.",
            ]
        if 'title' in q_text or 'best title' in q_text or 'appropriate title' in q_text:
            return [
                "A good title captures the MAIN IDEA across ALL paragraphs — not just one detail.",
                "Eliminate titles that are too narrow (one paragraph only) or too broad (not in the text).",
            ]
        if 'infer' in q_text or 'implied' in q_text:
            return [
                "Inference = what the author implies, not what is stated outright.",
                "Eliminate options that directly contradict the passage or go too far beyond it.",
            ]
        if 'irrelevant' in q_text or 'does not belong' in q_text:
            return [
                "Read the topic sentence first. Every other sentence should directly support this idea.",
                "The irrelevant sentence will introduce a subject the paragraph never discusses.",
            ]
        if 'fill in' in q_text or 'blank' in q_text or '(a)' in q_text or '(b)' in q_text:
            return [
                "Identify the time frame using time-marker words (in the past, currently, by next year).",
                "Check the modal verb — 'can / will / have' each demand a specific verb form.",
                "Read the full sentence aloud with each option; the correct one fits grammatically.",
            ]
        if 'tone' in q_text or 'attitude' in q_text:
            return [
                "Look at the adjectives and adverbs — they carry the author's emotional charge.",
                "Is the language alarming, neutral, hopeful, critical, or humorous overall?",
            ]
        if 'purpose' in q_text or ('author' in q_text and 'write' in q_text):
            return [
                "Ask: Is the author informing, persuading, or describing? Check the conclusion for the stated aim.",
            ]
        if 'placed' in q_text or 'position' in q_text or 'inserted' in q_text:
            return [
                "The inserted sentence must follow logically from the sentence before it AND lead into the sentence after.",
                "Look for pronoun or keyword references that connect the new sentence to its neighbours.",
            ]
        return [
            "Re-read the specific paragraph referenced before selecting your answer.",
            "Eliminate options that contradict anything stated in the passage.",
        ]

    if 'logical' in subject:
        if 'sequencing' in topic or 'analytic' in topic or 'arrangement' in topic:
            return [
                "Chain all inequality conditions: A > B > C. Find the fixed anchor (first or last) and build from there.",
                "Draw a simple ranked list or table to visualise the order.",
            ]
        if 'syllogism' in topic or 'deductive' in topic:
            return [
                "Structure: Premise 1 + Premise 2 → Conclusion. Check if the conclusion logically must follow.",
                "'All A are B' does NOT mean 'All B are A' — avoid reversing the conditional.",
            ]
        if 'spatial' in topic:
            return [
                "Identify any fixed/certain placements first, then use process of elimination.",
            ]
        if 'rate' in topic or 'distance' in topic or 'time' in topic:
            return [
                "Formula: Distance = Speed × Time. Write one equation per object.",
                "Moving toward each other → speeds ADD. Same direction → speeds SUBTRACT.",
            ]
        return [
            "List all conditions, then test each answer choice systematically.",
            "Eliminate any choice that violates even one stated condition.",
        ]

    if 'math' in subject or 'mathematics' in subject:
        if 'probability' in topic or 'combinatoric' in topic:
            return [
                "Does order matter? YES → Permutation. NO → Combination.",
                "For 'at least one' → use complement: 1 - P(none).",
            ]
        if 'quadratic' in topic or 'equation' in topic:
            return [
                "If p is a root of f(x) = 0, then f(p) = 0. Use this substitution to simplify.",
                "Sum of roots = -b/a; Product of roots = c/a.",
            ]
        return [
            "Write the key formula first, then substitute values step by step.",
            "Check your answer by substituting back into the original equation.",
        ]

    if 'quantitative' in subject:
        return [
            "Estimate first — answer choices are usually spread far enough to allow rounding.",
            "Convert all units consistently before calculating.",
        ]
    return []

# ─── Build English questions for one tryout ──────────────────────────────────
def build_english_section(tryout_index, gen_num):
    combo = TRYOUT_COMBOS[tryout_index]     # 4 passage indices
    questions = []
    for passage_idx in combo:
        ps = copy.deepcopy(ALL_PASSAGES[passage_idx])
        passage_text = ps['passage_text']
        for q in ps['questions']:
            q['id']      = f"{q['id']}_gen_{gen_num}"
            q['passage'] = passage_text
            q['passage_id'] = ps['passage_id']
            if not q.get('hints'):
                q['hints'] = generate_hints(q)
            # Shuffle answer options
            if 'options' in q and 'correct_answer' in q:
                ca = q['correct_answer']
                correct_text = next(o['text'] for o in q['options'] if o['letter'] == ca)
                texts = [o['text'] for o in q['options']]
                random.shuffle(texts)
                letters = ["A","B","C","D","E"]
                for j, opt in enumerate(q['options']):
                    opt['text'] = texts[j]
                    if texts[j] == correct_text:
                        q['correct_answer'] = letters[j]
            questions.append(q)
    return questions

# ─── Flatten non-English questions from a real-exam base ─────────────────────
def flatten_non_english(raw_base):
    flat = []
    for item in raw_base:
        if isinstance(item, dict) and 'passages' in item and 'questions' in item:
            pmap = {p['id']: p['text'] for p in item['passages']}
            for q in item['questions']:
                if str(q.get('subject','')).lower() == 'english':
                    continue
                pid = q.get('passage_id')
                if pid and pid in pmap and not q.get('passage'):
                    q['passage'] = pmap[pid]
                flat.append(q)
        else:
            if isinstance(item, dict) and str(item.get('subject','')).lower() != 'english':
                flat.append(item)
    return flat

# ─── Main generation loop ────────────────────────────────────────────────────
SUBJECT_ORDER = ['Basic Mathematics', 'English', 'Quantitative Reasoning', 'Logical Reasoning']

for i in range(1, 21):
    raw_base = copy.deepcopy(bases[i % 2])
    non_english = flatten_non_english(raw_base)

    for q in non_english:
        q['id'] = f"{q.get('id','q')}_gen_{i}"
        subject   = str(q.get('subject','')).lower()
        skip_nums = 'logical' in subject
        q['question_text'] = mutate_text(q.get('question_text',''), skip_nums)
        if 'passage' in q:
            q['passage'] = mutate_text(q['passage'], skip_nums)
        for opt in q.get('options', []):
            opt['text'] = mutate_text(opt.get('text',''), skip_nums)
        if 'explanation' in q:
            q['explanation'] = mutate_text(q['explanation'], skip_nums)
        if 'chart' in q:
            chart = q['chart']
            if 'bar' in chart:
                for ds in chart['bar'].get('datasets',[]):
                    ds['values'] = [v + random.randint(1,10) for v in ds.get('values',[])]
            if 'pie' in chart:
                for ds in chart['pie'].get('segments',[]):
                    ds['value'] = ds.get('value',0) + random.randint(1,5)
        if not q.get('hints'):
            q['hints'] = generate_hints(q)
        # Shuffle options
        if 'options' in q and 'correct_answer' in q:
            ca = q['correct_answer']
            correct_text = next((o['text'] for o in q['options'] if o['letter'] == ca), None)
            if correct_text:
                texts = [o['text'] for o in q['options']]
                random.shuffle(texts)
                letters = ["A","B","C","D","E"]
                for j, opt in enumerate(q['options']):
                    opt['text'] = texts[j]
                    if texts[j] == correct_text:
                        q['correct_answer'] = letters[j]

    english_qs = build_english_section(i - 1, i)   # i-1 because combos are 0-indexed

    all_qs = english_qs + non_english
    all_qs.sort(key=lambda q: (
        SUBJECT_ORDER.index(q.get('subject','')) if q.get('subject','') in SUBJECT_ORDER else 99
    ))

    path = f'quiz-app/src/GeneratedTryouts/tryout_{i}.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"  Tryout {i:>2} — {len(all_qs)} questions ({len(english_qs)} English from combo {TRYOUT_COMBOS[i-1]})")

print("\nDone — 20 tryouts generated.")
