import json
import os

def clean_and_group(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    passages = []
    questions = []
    
    # Extract unique passages
    seen_passage_ids = set()
    
    for q in data:
        # Remove hints as requested
        if 'hints' in q:
            del q['hints']
            
        p_id = q.get('passage_id')
        p_text = q.get('passage')
        
        if p_id and p_text:
            if p_id not in seen_passage_ids:
                passages.append({
                    "id": p_id,
                    "text": p_text
                })
                seen_passage_ids.add(p_id)
            
            # Remove redundant passage text from the question object itself
            # to make it look like the realQ1/realQ2 format (ref by ID)
            del q['passage']
        
        questions.append(q)

    # Reconstruct in the "grouped" format similar to realQ1
    # This structure has a 'passages' list and a 'questions' list
    output = {
        "passages": passages,
        "questions": questions
    }

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

# Clean all 4 exported files
folder = 'Tryout_JSON_Files'
for i in range(1, 5):
    fname = os.path.join(folder, f'Tryout_{i}.json')
    if os.path.exists(fname):
        clean_and_group(fname)
        print(f"Cleaned and grouped {fname}")
