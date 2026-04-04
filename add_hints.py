import json
import glob
import re

def split_to_steps(text):
    if not isinstance(text, str):
        return ["Calculate carefully."]
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    if not sentences: return ["Calculate carefully."]
    return sentences

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for q in data:
        exp = q.get('explanation', '')
        if 'hints' not in q or not q['hints']:
            hints = split_to_steps(exp)
            q['hints'] = hints[:3] if len(hints) >= 3 else (hints + ["Check your calculations."] * (3 - len(hints)))

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Added hints to {path}")

files = glob.glob('quiz-app/src/GeneratedTryouts/*.json')
for f in files:
    process_file(f)
