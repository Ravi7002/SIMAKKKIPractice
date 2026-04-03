import json, os
from collections import defaultdict, Counter

def load(f):
    with open(f, encoding='utf-8') as fh:
        return json.load(fh)

q1 = load('realQ1.json')
q2 = load('realQ2.json')

def summarize(qs, label):
    by_sub = defaultdict(Counter)
    for q in qs:
        sub = q.get('subject', '?')
        top = q.get('topic', '?')
        by_sub[sub][top] += 1
    print(f'### {label} ###')
    for sub in sorted(by_sub):
        print(f'  [{sub}]')
        for top, cnt in sorted(by_sub[sub].items(), key=lambda x: -x[1]):
            print(f'    - {top} (x{cnt})')
    print()

summarize(q1, 'realQ1')
summarize(q2, 'realQ2')

# List practice files
print("### PracticeQuestions Files ###")
root = 'PracticeQuestions'
for d in sorted(os.listdir(root)):
    dp = os.path.join(root, d)
    if os.path.isdir(dp):
        print(f'  [{d}]')
        for f in sorted(os.listdir(dp)):
            if f.endswith('.json'):
                print(f'    - {f.replace(".json","")}')
