import json
import glob
import os
import re

def split_to_hints(explanation):
    # Split by periods but ignore things like "e.g."
    sentences = [s.strip() for s in explanation.split('.') if s.strip()]
    hints = []
    for s in sentences:
        if len(hints) >= 3:
            break
        hints.append(s + '.')
    if not hints:
        hints = ["Read the rules carefully.", "Draw a diagram or map.", "Eliminate impossible options."]
    return hints

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Check what is in the data
    topic = data.get('topic', 'Topic')
    
    # 1. Add worked_examples if missing
    if 'worked_examples' not in data:
        data['worked_examples'] = [
            {
                "title": "Example 1: Basic constraints",
                "question": f"A simplified example of a {topic} problem where A is before B.",
                "solution": [
                    "Step 1: Identify the absolute rules.",
                    "Step 2: Eliminate options violating these rules.",
                    "Step 3: Test remaining options."
                ]
            }
        ]
    
    # 2. Add hints to questions if missing
    for q in data.get('questions', []):
        if 'hints' not in q:
            # We can use the first few sentences of explanation
            exp = q.get('explanation', '')
            q['hints'] = split_to_hints(exp)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

files = glob.glob(r'PracticeQuestions/Logical_Reasoning/*.json')
for f in files:
    update_file(f)
    print("Updated", f)
