import json
import glob
import re

def split_to_steps(text, topic, subject):
    base_hints = []
    
    sub = str(subject).lower()
    top = str(topic).lower()

    if 'english' in sub:
        base_hints.append(f"Consider the main rules of {topic} in an English reading context.")
        base_hints.append("Eliminate options that clearly contain grammatical or structural errors.")
    elif 'math' in sub or 'quant' in sub or 'quantitative' in sub:
        base_hints.append(f"Identify the mathematical formula or principle required for {topic}.")
        base_hints.append("Set up the equation carefully before jumping to calculations.")
    elif 'logic' in sub:
        base_hints.append(f"Break down the logical conditions provided in this {topic} problem.")
        base_hints.append("Map out the sequence or deduction steps systematically.")
    else:
        base_hints.append(f"Focus strictly on the concepts of {topic}.")
        base_hints.append("Analyze the given information step-by-step.")

    if not isinstance(text, str) or not text.strip():
        return base_hints + ["Review your learning material for this specific topic."]
        
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    return base_hints + sentences

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
        subject = q.get('subject', 'this subject')
        
        # Make each hint personal and derived ONLY from the explanation.
        hints = split_to_steps(exp, topic, subject)
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
