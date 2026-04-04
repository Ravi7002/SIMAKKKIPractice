import json

def flatten_realQ(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    new_data = []
    modified = False
    for item in data:
        if 'passages' in item and 'questions' in item:
            modified = True
            passages = {p['id']: p['text'] for p in item['passages']}
            for q in item['questions']:
                pid = q.get('passage_id')
                if pid and pid in passages:
                    q['passage'] = passages[pid]
                new_data.append(q)
        else:
            new_data.append(item)
            
    if modified:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2, ensure_ascii=False)
        print(f"Flattened {filename}")
    else:
        print(f"No nested structure found in {filename}")

flatten_realQ('realQ1.json')
# Also do realQ2 just in case
try:
    flatten_realQ('realQ2.json')
except:
    pass
