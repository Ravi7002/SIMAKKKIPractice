import json, glob

for f in sorted(glob.glob('quiz-app/src/GeneratedTryouts/tryout_*.json')):
    d = json.load(open(f, encoding='utf-8'))
    lr = [q for q in d if q.get('subject') == 'Logical Reasoning']
    with_passage = [q for q in lr if q.get('passage')]
    print(f.split('\\')[-1], 'LR:', len(lr), 'with_passage:', len(with_passage))
    for q in lr[:3]:
        print(' -', q.get('id'), 'pid:', q.get('passage_id'), 'has:', bool(q.get('passage')))
