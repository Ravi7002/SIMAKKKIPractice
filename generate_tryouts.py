import json
import random
import re
import os
import copy

with open('realQ1.json', 'r', encoding='utf-8') as f:
    q1 = json.load(f)
with open('realQ2.json', 'r', encoding='utf-8') as f:
    q2 = json.load(f)

bases = [q1, q2]

os.makedirs(os.path.join('quiz-app', 'src', 'GeneratedTryouts'), exist_ok=True)

def mutate_text(text, skip_numbers=False):
    if not isinstance(text, str):
        return text
    
    # Only replace standalone integers (not decimals, not inside words, not inside currency like 50.000)
    def rep_num(m):
        if skip_numbers:
            return m.group(0)
        # Skip if preceded or followed by . or , (decimal/thousands separator)
        start = m.start()
        end = m.end()
        if start > 0 and text[start-1] in '.,':
            return m.group(0)
        if end < len(text) and text[end] in '.,':
            return m.group(0)
        n = int(m.group(0))
        if n == 0: return "0"
        if n < 10: return str(n + random.randint(1, 3))
        if n < 100: return str(n + random.randint(1, 10))
        return str(n + random.randint(10, 100))
    
    if not skip_numbers:
        text = re.sub(r'(?<![.,])\b(\d+)\b(?![.,])', lambda m: rep_num(m), text)
    
    # Safe whole-word-only swaps - only multi-character words to avoid corrupting text
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

def generate_hints(q):
    """Generate smart pedagogical hints based on question subject/topic/text."""
    subject = str(q.get('subject', '')).lower()
    topic = str(q.get('topic', '')).lower()
    q_text = str(q.get('question_text', '')).lower()
    passage = str(q.get('passage', ''))

    hints = []

    # ── English ──────────────────────────────────────────────
    if 'english' in subject:
        if 'paragraph' in q_text and ('relationship' in q_text or 'connection' in q_text):
            # Paragraph-relationship question
            hints = [
                "Read the LAST sentence of the first paragraph and the FIRST sentence of the second paragraph — these transition sentences reveal the logical connection.",
                "Ask yourself: Does paragraph 2 explain, contradict, extend, or give examples of what paragraph 1 said?",
                "Common relationships: Cause→Effect, Problem→Solution, General→Specific, Contrast. Match the tone shift between paragraphs to one of these.",
            ]
        elif 'title' in q_text or 'best title' in q_text or 'appropriate title' in q_text:
            hints = [
                "A good title captures the MAIN IDEA — not just one detail. Read every paragraph's topic sentence.",
                "Eliminate titles that are too narrow (only one paragraph) or too broad (mentioned nowhere).",
                "The correct title will apply to ALL parts of the passage, not just the introduction.",
            ]
        elif 'infer' in q_text or 'implied' in q_text or 'suggests' in q_text:
            hints = [
                "Inference = something the author implies but doesn't say directly. Do NOT pick an answer that is stated word-for-word.",
                "Choose the answer that must be true based on the text — avoid answers that go beyond what the evidence supports.",
                "Eliminate any option that contradicts the passage, even if it sounds logical in real life.",
            ]
        elif 'purpose' in q_text or 'author' in q_text and 'write' in q_text:
            hints = [
                "Ask: Is the author informing, persuading, entertaining, or describing? The overall structure of the passage reveals the purpose.",
                "Look at the conclusion — authors usually restate their main purpose in the final paragraph.",
            ]
        elif 'tone' in q_text or 'attitude' in q_text:
            hints = [
                "Identify the emotional charge of the words. Are they positive/negative/neutral? This reveals the tone.",
                "Look for adjectives and adverbs — they carry the author's attitude. Words like 'unfortunately' or 'remarkably' signal sentiment.",
            ]
        elif 'irrelevant' in q_text or 'does not belong' in q_text:
            hints = [
                "Read the topic sentence (usually sentence 1). Every other sentence should directly support this main idea.",
                "The irrelevant sentence will introduce a completely different topic or subject that the paragraph does not discuss.",
            ]
        elif 'fill in' in q_text or 'blank' in q_text or '(a)' in q_text or '(b)' in q_text:
            if 'tense' in topic or 'grammar' in topic:
                hints = [
                    "Identify the time frame: look for time-marker words like 'in the past', 'currently', 'by next year'.",
                    "Check subject-verb agreement: singular subject → singular verb form.",
                    "For past events completed before another past event, use Past Perfect (had + verb3).",
                ]
            else:
                hints = [
                    "Read the full sentence for context clues before and after the blank.",
                    "Try each option aloud — the correct one will fit both grammatically and logically.",
                ]
        elif 'addressed' in q_text or 'audience' in q_text:
            hints = [
                "Consider the vocabulary level and examples used. Technical jargon points to an expert audience; simple everyday advice points to the general public.",
                "Notice the writing style: instructions with 'you should' suggest a self-help audience.",
            ]
        elif 'passage sentence' in q_text or 'placed' in q_text or 'position' in q_text:
            hints = [
                "A sentence placed at the beginning of a paragraph introduces/sets up the context. At the end, it summarizes or concludes.",
                "Check if the sentence acts as a bridge — does it follow logically from what comes before AND lead into what comes after?",
            ]
        elif 'paragraph' in q_text and any(w in q_text for w in ['discuss', 'mentioned', 'explained', 'found']):
            hints = [
                "Scan each paragraph quickly for the key noun/concept asked about in the question.",
                "The correct paragraph will explicitly discuss this concept — not just mention the word in passing.",
            ]
        else:
            # Generic English hints
            hints = [
                "Read the question carefully — underline the key phrase it is asking about.",
                "Eliminate answers that directly contradict information in the passage.",
                "Return to the specific paragraph or sentence referenced in the question to verify your choice.",
            ]

    # ── Logical Reasoning ─────────────────────────────────────
    elif 'logical' in subject:
        if 'sequencing' in topic or 'arrangement' in topic or 'order' in topic or 'analytic' in topic.lower():
            hints = [
                "List all the given conditions as simple inequality chains (A > B > C). Then combine them step by step.",
                "Find the anchor: is there someone who is definitively first, last, or fixed at a position? Start there.",
                "Draw a simple diagram or table with positions/slots to place names as you confirm each condition.",
            ]
        elif 'syllogism' in topic or 'deductive' in topic:
            hints = [
                "Structure the argument: identify Premise 1, Premise 2, and the Conclusion. Does the conclusion follow logically?",
                "Watch out for overgeneralization — 'All A are B' does NOT mean 'All B are A'.",
                "If a condition says 'Only if X, then Y', then Not-Y guarantees Not-X (modus tollens).",
            ]
        elif 'spatial' in topic:
            hints = [
                "Read all the placement rules first before deciding anything.",
                "Work from fixed/certain placements first, then use process of elimination for the flexible ones.",
            ]
        elif 'conditional' in topic:
            hints = [
                "A conditional 'If P then Q' means: whenever P is true, Q must also be true.",
                "Work through each condition independently and check if the scenario satisfies ALL rules simultaneously.",
            ]
        elif 'rate' in topic or 'distance' in topic or 'time' in topic:
            hints = [
                "Use the formula: Distance = Speed × Time. Write it for each person/vehicle separately.",
                "When two objects move TOWARD each other, their speeds ADD up (closing speed = speed1 + speed2).",
                "When moving in the SAME direction, subtract the slower speed from the faster speed to find the gap-closing rate.",
            ]
        elif 'mathematical' in topic:
            hints = [
                "Define variables for the unknown quantities and write equations from the word problem.",
                "Check your answer by substituting back into the original conditions.",
            ]
        else:
            hints = [
                "Map out all conditions systematically before attempting to choose an answer.",
                "Eliminate answer choices that violate even one rule or condition.",
            ]

    # ── Basic Mathematics ─────────────────────────────────────
    elif 'math' in subject or 'mathematics' in subject:
        if 'probability' in topic or 'combinatoric' in topic:
            hints = [
                "Identify if order matters: if YES → Permutation (P). If NO → Combination (C).",
                "For 'at least 1' problems, use the complement: P(at least 1) = 1 - P(none).",
            ]
        elif 'quadratic' in topic or 'equation' in topic:
            hints = [
                "If p is a root of f(x) = 0, then f(p) = 0. Use this to simplify complex expressions.",
                "Factor or use the quadratic formula. Remember: sum of roots = -b/a, product of roots = c/a.",
            ]
        elif 'sequence' in topic or 'series' in topic:
            hints = [
                "Identify if it's Arithmetic (constant difference) or Geometric (constant ratio) first.",
                "Arithmetic: Sn = n/2 × (2a + (n-1)d). Geometric: Sn = a(rⁿ-1)/(r-1).",
            ]
        else:
            hints = [
                "Identify the key formula needed and write it before substituting values.",
                "Check your arithmetic at each step — careless errors are the most common mistake.",
            ]

    # ── Quantitative Reasoning ─────────────────────────────────
    elif 'quantitative' in subject:
        hints = [
            "Estimate first — the answer choices are often far enough apart that a rough calculation points you to the right one.",
            "Convert all units to be consistent before comparing or calculating.",
            "Look for patterns or ratios rather than doing lengthy exact arithmetic.",
        ]

    return hints

for i in range(1, 21):
    raw_base = copy.deepcopy(bases[i % 2])
    base = []
    for item in raw_base:
        if isinstance(item, dict) and 'passages' in item and 'questions' in item:
            passages_map = {p['id']: p['text'] for p in item['passages']}
            for q in item['questions']:
                pid = q.get('passage_id')
                if pid and pid in passages_map and not q.get('passage'):
                    q['passage'] = passages_map[pid]
                base.append(q)
        else:
            base.append(item)

    for q in base:
        q['id'] = f"{q.get('id', 'q')}_gen_{i}"
        subject = str(q.get('subject', '')).lower()
        skip_nums = 'english' in subject or 'logical' in subject
        
        q['question_text'] = mutate_text(q.get('question_text', ''), skip_nums)
        
        if 'passage' in q:
            q['passage'] = mutate_text(q.get('passage', ''), skip_nums)
        
        for opt in q.get('options', []):
            opt['text'] = mutate_text(opt.get('text', ''), skip_nums)
            
        if 'explanation' in q:
            q['explanation'] = mutate_text(q['explanation'], skip_nums)
            
        if 'chart' in q:
            chart = q['chart']
            if 'bar' in chart:
                for ds in chart['bar'].get('datasets', []):
                    ds['values'] = [v + random.randint(1, 10) for v in ds.get('values', [])]
            if 'pie' in chart:
                for ds in chart['pie'].get('segments', []):
                    ds['value'] = ds.get('value', 0) + random.randint(1, 5)
            
        # Add hints if none exist
        if not q.get('hints'):
            q['hints'] = generate_hints(q)

        # Shuffle options
        if 'options' in q and 'correct_answer' in q:
            correct_opt = next((o for o in q['options'] if o['letter'] == q['correct_answer']), None)
            if correct_opt:
                correct_text = correct_opt['text']
                opts_text = [o['text'] for o in q['options']]
                random.shuffle(opts_text)
                
                letters = ["A", "B", "C", "D", "E"]
                for j, opt in enumerate(q['options']):
                    opt['text'] = opts_text[j]
                    if opts_text[j] == correct_text:
                        q['correct_answer'] = letters[j]
    
    with open(f'quiz-app/src/GeneratedTryouts/tryout_{i}.json', 'w', encoding='utf-8') as f:
        json.dump(base, f, indent=2, ensure_ascii=False)

print("Generated 20 tryouts.")

