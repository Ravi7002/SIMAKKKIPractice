import json
import glob
import os
import random

def split_to_hints(explanation):
    sentences = [s.strip() for s in explanation.replace('\n', ' ').split('.') if s.strip()]
    hints = []
    for s in sentences:
        if len(hints) >= 3: break
        hints.append(s + '.')
    if not hints:
        hints = ["Read the question carefully.", "Calculate the necessary values.", "Choose the correct option."]
    return hints

def add_charts_to_data_interpretation(questions):
    for q in questions:
        if 'chart_data' not in q:
            text = q.get('question_text', '').lower()
            if 'pie' in text or 'budget' in text:
                q['chart_data'] = {
                    "type": "pie", "title": "Distribution", "labels": ["Category A", "Category B", "Category C"],
                    "datasets": [{"label": "Amount", "values": [40, 20, 40]}]
                }
            elif 'bar' in text:
                q['chart_data'] = {
                    "type": "bar", "title": "Sales", "labels": ["Prod A", "Prod B", "Prod C"],
                    "datasets": [{"label": "Units", "values": [150, 250, 100]}]
                }
            elif 'table' in text:
                q['chart_data'] = {
                    "type": "table", "title": "Survey Data", "headers": ["Group", "Members", "Seniors%"],
                    "rows": [["Club A", "120", "20%"], ["Club B", "80", "50%"]]
                }
            elif 'investment' in text or 'steady' in text:
                q['chart_data'] = {
                    "type": "line", "title": "Stock Values", "labels": ["Yr 0", "Yr 1", "Yr 2", "Yr 3"],
                    "datasets": [{"label": "Stock X", "values": [100, 250, 150, 187.5]}, {"label": "Stock Y", "values": [100, 125, 150, 187.5]}]
                }
            elif 'poll' in text:
                q['chart_data'] = {
                    "type": "bar", "title": "Policy Support", "labels": ["Policy A", "Policy B"],
                    "datasets": [{"label": "Support %", "values": [70, 80]}]
                }
            else:
                 q['chart_data'] = {
                    "type": "bar", "title": "Variable Comparison", "labels": ["Var 1", "Var 2"],
                    "datasets": [{"label": "Metric", "values": [random.randint(10,50), random.randint(10,50)]}]
                }

def generate_math_q(topic, diff, idx):
    # Generates a valid math question based on topic with random numbers
    id_str = f"{topic[:3].lower()}_{diff}_{idx}"
    letters = ["A", "B", "C", "D", "E"]
    
    if topic == "Algebraic Manipulation":
        a = random.randint(2, 6)
        b = random.randint(1, 5)
        ans = (a*a) - (b*b)
        q_text = f"Simplify and evaluate: ({a}x - {b})({a}x + {b}) when x = 1"
        expl = f"Difference of squares: ({a}x - {b})({a}x + {b}) = {a*a}x² - {b*b}. If x=1, it is {a*a} - {b*b} = {ans}."
        opts = [ans, ans+1, ans-1, ans+2, ans-2]
    
    elif topic == "Coordinate Geometry":
        x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
        x2, y2 = x1 + random.randint(1, 5), y1 + random.randint(1, 5)
        ans = (x2-x1)**2 + (y2-y1)**2
        q_text = f"What is the squared distance between the points ({x1}, {y1}) and ({x2}, {y2})?"
        expl = f"Distance squared = (x2-x1)² + (y2-y1)² = ({x2}-{x1})² + ({y2}-{y1})² = {ans}."
        opts = [ans, ans+1, ans-1, ans+4, ans-4]
    
    elif topic == "Data Interpretation and Charts":
        total = random.choice([200, 300, 400, 500])
        perc = random.randint(2, 8) * 10
        ans = int(total * (perc/100))
        q_text = f"A pie chart shows {perc}% of a {total} budget went to Housing. How much was allocated to Housing?"
        expl = f"{perc}% of {total} = ({perc}/100) * {total} = {ans}."
        opts = [ans, ans+10, ans-10, ans+20, ans-20]
        
    elif topic == "Geometry":
        l, w, h = random.randint(2, 5), random.randint(2, 5), random.randint(2, 5)
        ans = l * w * h
        q_text = f"Find the volume of a rectangular prism with length {l}, width {w}, and height {h}."
        expl = f"Volume = l * w * h = {l} * {w} * {h} = {ans}."
        opts = [ans, ans+2, ans-2, ans+4, ans-4]
        
    elif topic == "Matrix Algebra":
        k = random.randint(2, 5)
        x, y = random.randint(1, 4), random.randint(1, 4)
        ans = k * x + k * y
        q_text = f"If A = [{k} 0; 0 {k}] and B = [{x}; {y}], what is the sum of the elements in the matrix AB?"
        expl = f"AB = [{k*x}; {k*y}]. Sum = {k*x} + {k*y} = {ans}."
        opts = [ans, ans+k, ans-k, ans+1, ans-1]
        
    elif topic == "Pattern Recognition and Puzzles":
        start = random.randint(2, 10)
        mult = random.randint(2, 4)
        ans = start * (mult ** 3)
        q_text = f"Find the next number in the pattern: {start}, {start*mult}, {start*(mult**2)}, ..."
        expl = f"Each number is multiplied by {mult}. Next is {start*(mult**2)} * {mult} = {ans}."
        opts = [ans, ans+mult, ans-mult, ans+10, ans-10]
        
    elif topic == "Systems of Linear Equations":
        x, y = random.randint(1, 5), random.randint(1, 5)
        s1 = x + y
        s2 = x - y
        ans = x * y
        q_text = f"If x + y = {s1} and x - y = {s2}, find the product xy."
        expl = f"Adding equations: 2x = {s1+s2} -> x = {x}. Subtracting: 2y = {s1-s2} -> y = {y}. Product = {x * y} = {ans}."
        opts = [ans, ans+1, ans-1, ans+2, ans-2]
        
    elif topic == "Word Problems":
        r1, r2 = random.randint(2, 5), random.randint(2, 5)
        ans = (r1 * 3) + (r2 * 3)
        q_text = f"Worker A finishes {r1} tasks per hour. Worker B finishes {r2} tasks per hour. How many tasks do they finish together in 3 hours?"
        expl = f"Combined rate = {r1} + {r2} = {r1+r2} tasks/hr. In 3 hours: 3 * {r1+r2} = {ans}."
        opts = [ans, ans+3, ans-3, ans+2, ans-2]
        
    else:
        ans = random.randint(10, 100)
        q_text = f"Solve for x: x - {ans} = 0"
        expl = f"x = {ans}."
        opts = [ans, ans+1, ans-1, ans+2, ans-2]

    # Add chart data for data interpretation generated questions
    chart_data = None
    if topic == "Data Interpretation and Charts":
        chart_data = {
            "type": "pie", "title": "Budget Breakdown", "labels": ["Housing", "Other"],
            "datasets": [{"label": "Amount", "values": [perc, 100-perc]}]
        }

    random.shuffle(opts)
    correct_idx = opts.index(ans)
    
    options = []
    for i, o in enumerate(opts):
        options.append({"letter": letters[i], "text": str(o)})
        
    q = {
        "id": id_str,
        "subject": "Quantitative Reasoning",
        "topic": topic,
        "difficulty": diff,
        "question_text": q_text,
        "options": options,
        "correct_answer": letters[correct_idx],
        "explanation": expl,
        "hints": split_to_hints(expl)
    }
    
    if chart_data:
        q['chart_data'] = chart_data
        
    return q

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    topic = data.get('topic', 'Topic')
    if 'worked_examples' not in data:
        data['worked_examples'] = [{
            "title": f"Example for {topic}",
            "question": f"A sample real-exam structure for {topic}.",
            "solution": ["Step 1: Read carefully.", "Step 2: Apply the correct logical rule.", "Step 3: Solve."]
        }]

    questions = data.get('questions', [])
    
    if topic == "Data Interpretation and Charts":
        add_charts_to_data_interpretation(questions)
        
    # Generate up to 25
    current_count = len(questions)
    diffs = ['easy', 'medium', 'hard']
    
    while len(questions) < 25:
        idx = len(questions) + 1
        diff = random.choice(diffs)
        new_q = generate_math_q(topic, diff, idx)
        questions.append(new_q)
            
    # Add hints to existing
    for q in questions:
        if 'hints' not in q:
            q['hints'] = split_to_hints(q.get('explanation', ''))

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

files = glob.glob(r'PracticeQuestions/Quantitative_Reasoning/*.json')
for f in files:
    update_file(f)
    print("Updated", f)
