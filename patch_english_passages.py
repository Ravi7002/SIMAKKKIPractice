import json
import glob
import os

passage_mapping = {
    "Reading Comprehension (Long Passage)": "In contemporary discussions on education reform, the importance of holistic development often takes center stage. While specialized knowledge and technical proficiencies are undeniably vital in advancing modern industry, educators increasingly emphasize that soft skills such as emotional intelligence, cross-cultural understanding, and adaptive thinking form the true bedrock of sustained personal and professional success. Recent longitudinal studies tracking the career trajectories of graduates demonstrate that those who engage in diverse extracurricular environments out-perform their peers in leadership and crisis management roles. However, skeptics argue that reducing academic rigor in favor of holistic initiatives might compromise technical execution in high-stakes environments.",
    "Reading Comprehension (Short Passage)": "During the mid-20th century, rapid industrialization fundamentally altered urban demographics. Factory centers expanded, drawing populations from rural agrarian townships into densely packed metropolitan areas. This demographic shift caused unprecedented stress on infrastructure, leading to the rapid deployment of public sanitation and housing reforms that shaped modern city planning.",
    "Vocabulary in Context": "The scientist was incredibly fastidious when observing the cultures in the petri dishes. Every minor change in color, no matter how ephemeral, was catalogued with meticulous care."
}

def patch_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    qs = data if isinstance(data, list) else data.get('questions', [])
    updated = False
    
    for q in qs:
        # If it's English, check topic and attach passage if missing
        if q.get('subject') == 'English' and not q.get('passage'):
            topic = q.get('topic')
            if topic in passage_mapping:
                q['passage'] = passage_mapping[topic]
                updated = True
                
    if updated:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Patched {path}")

# Patch realQ1, realQ2
if os.path.exists('realQ1.json'): patch_file('realQ1.json')
if os.path.exists('realQ2.json'): patch_file('realQ2.json')

# Patch all PracticeQuestions
for f in glob.glob('quiz-app/src/PracticeQuestions/**/*.json', recursive=True):
    patch_file(f)

# Patch Generated Tryouts
for f in glob.glob('quiz-app/src/GeneratedTryouts/*.json'):
    patch_file(f)
