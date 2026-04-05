import json

d = json.load(open('realQ1.json', encoding='utf-8'))
lr = [q for q in d if q.get('subject') == 'Logical Reasoning']
for q in lr:
    pid = q.get('passage_id')
    has = bool(q.get('passage'))
    print(q.get('id'), 'pid:', str(pid), 'has_passage:', str(has))
