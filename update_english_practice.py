import json
import os
import sys

# Load new pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from english_pool_v4 import POOL

# Map topic to file name
topic_to_file = {
    'grammar': 'Grammar_and_Tenses.json',
    'vocabulary': 'Vocabulary_in_Context.json',
    'structure': 'Paragraph_Cohesion_and_Structure.json',
    'cohesion': 'Paragraph_Cohesion_and_Structure.json',
    'paragraph cohesion': 'Paragraph_Cohesion_and_Structure.json',
    # fallback
    'default': 'Reading_Comprehension.json'
}

# Load the existing files to keep header data
dir_path = 'quiz-app/src/PracticeQuestions/English'
files = {
    'Grammar_and_Tenses.json': [],
    'Vocabulary_in_Context.json': [],
    'Paragraph_Cohesion_and_Structure.json': [],
    'Reading_Comprehension.json': []
}

# Organize questions
for p in POOL:
    for q in p['questions']:
        # attach passage to question
        q['passage'] = p['text']
        q['passage_id'] = p['id']
        t = str(q.get('topic')).lower()
        
        target_file = 'Reading_Comprehension.json'
        for k, v in topic_to_file.items():
            if k in t:
                target_file = v
                break
                
        files[target_file].append(q)

# Update each file
for filename, qs in files.items():
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    data['questions'] = qs
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Updated {filename} with +{len(qs)} questions.")

