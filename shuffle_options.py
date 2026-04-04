import json
import glob
import os
import random

def shuffle_options_in_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data.get('questions', [])
    modified = False

    for q in questions:
        if 'options' in q and 'correct_answer' in q:
            # find text for correct answer
            correct_opt = next((o for o in q['options'] if o['letter'] == q['correct_answer']), None)
            if not correct_opt:
                continue
            
            correct_text = correct_opt['text']
            
            # extract all option texts and shuffle them
            opts_text = [o['text'] for o in q['options']]
            random.shuffle(opts_text)
            
            letters = ["A", "B", "C", "D", "E"]
            for i, opt in enumerate(q['options']):
                opt['text'] = opts_text[i]
                if opts_text[i] == correct_text:
                    q['correct_answer'] = letters[i]
            
            modified = True

    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Shuffled options in: {path}")

files = glob.glob(r'quiz-app/src/PracticeQuestions/**/*.json', recursive=True)
for f in files:
    shuffle_options_in_file(f)
