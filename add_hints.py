import json
import glob
import re

def split_to_steps(text, topic):
    if not isinstance(text, str):
        return [f"Review the concept of {topic}."]
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    if not sentences: return [f"Review the concept of {topic}."]
    return sentences

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    questions = data.get('questions', []) if isinstance(data, dict) else data
    if not isinstance(questions, list):
        return
        
    for q in questions:
        if not isinstance(q, dict): continue
        exp = q.get('explanation', '')
        topic = q.get('topic', 'this topic')
        
        # Make each hint personal and derived ONLY from the explanation.
        hints = split_to_steps(exp, topic)
        q['hints'] = hints

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Added hints to {path}")

import os
target_dirs = [
    'quiz-app/src/GeneratedTryouts',
    'quiz-app/src/PracticeQuestions'
]

files_to_process = []
for d in target_dirs:
    for root, _, files in os.walk(d):
        for file in files:
            if file.endswith('.json'):
                files_to_process.append(os.path.join(root, file))

for f in files_to_process:
    process_file(f)
