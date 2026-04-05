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

def mutate_text(text):
    if not isinstance(text, str):
        return text
    
    # Only replace standalone integers (not decimals, not inside words, not inside currency like 50.000)
    def rep_num(m):
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

for i in range(1, 6):
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
        q['question_text'] = mutate_text(q.get('question_text', ''))
        
        if 'passage' in q:
            q['passage'] = mutate_text(q.get('passage', ''))
        
        for opt in q.get('options', []):
            opt['text'] = mutate_text(opt.get('text', ''))
            
        if 'explanation' in q:
            q['explanation'] = mutate_text(q['explanation'])
            
        if 'chart' in q:
            # Also mutate chart data slightly if possible
            chart = q['chart']
            if 'bar' in chart:
                for ds in chart['bar'].get('datasets', []):
                    ds['values'] = [v + random.randint(1, 10) for v in ds.get('values', [])]
            if 'pie' in chart:
                for ds in chart['pie'].get('segments', []):
                    ds['value'] = ds.get('value', 0) + random.randint(1, 5)
            
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

print("Generated 5 tryouts.")
