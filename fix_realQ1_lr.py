import json

with open('realQ1.json', 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8-sig')

# Fix the broken JSON
data = json.loads(content.rstrip() + '\n}\n]')
print(f"Parsed OK: {len(data)} top-level items")

# Flatten any nested {passages, questions} blocks
new_data = []
for item in data:
    if isinstance(item, dict) and 'passages' in item and 'questions' in item:
        passages = {p['id']: p['text'] for p in item['passages']}
        for q in item['questions']:
            pid = q.get('passage_id')
            if pid and pid in passages and not q.get('passage'):
                q['passage'] = passages[pid]
            new_data.append(q)
        print(f"  Flattened nested block: {len(item['questions'])} questions, {len(passages)} passages")
    else:
        new_data.append(item)

# Report
print(f"\nTotal questions after flatten: {len(new_data)}")
subjects = {}
for q in new_data:
    s = q.get('subject', 'Unknown')
    subjects[s] = subjects.get(s, 0) + 1
for s, n in subjects.items():
    print(f"  {s}: {n}")

lr = [q for q in new_data if q.get('subject') == 'Logical Reasoning']
print(f"\nLogical Reasoning ({len(lr)}):")
for q in lr:
    print(f"  {q.get('id')} | passage_id: {q.get('passage_id')} | has_passage: {bool(q.get('passage'))}")

# Save
with open('realQ1.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, indent=2, ensure_ascii=False)
print("\nSaved realQ1.json ✓")
