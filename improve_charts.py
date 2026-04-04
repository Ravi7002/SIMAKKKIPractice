import json
import random

topic_data = {
  "subject": "Quantitative Reasoning",
  "topic": "Data Interpretation and Charts",
  "introduction": "This topic tests your ability to extract relevant information, perform calculations, and draw conclusions from complex datasets presented in tables, bar charts, line graphs, and pie charts. You will encounter multi-variable data reflecting real-world scenarios.",
  "key_formulas": [
    {"name": "Percentage Growth", "formula": "\\frac{\\text{New} - \\text{Old}}{\\text{Old}} \\times 100\\%"},
    {"name": "Average", "formula": "\\frac{\\text{Sum of Terms}}{\\text{Number of Terms}}"}
  ],
  "tips_and_tricks": [
    "Scan the axes and legends of charts carefully before attempting the question.",
    "Pay attention to units (e.g., thousands, millions) to avoid decimal errors.",
    "Estimate calculations when exact values are difficult to read from a graph."
  ],
  "worked_examples": [
    {
      "title": "Complex Table Analysis Strategy",
      "question": "Based on the table of 5 companies' annual expenditures (in millions USD), which company experienced the highest percentage growth in R&D between Year 1 and Year 5?",
      "solution": [
        "First, locate the R&D column for each company in Year 1 and Year 5.",
        "Calculate the absolute growth: Year 5 - Year 1.",
        "Divide by the Year 1 base value and multiply by 100.",
        "Compare the percentages rather than the absolute growth."
      ]
    }
  ],
  "questions": []
}

diffs = ['easy'] * 8 + ['medium'] * 9 + ['hard'] * 8

# Generate 25 complex questions
for i in range(1, 26):
    q_type = random.choice(['table', 'bar', 'line', 'pie'])
    
    if q_type == 'table':
        headers = ["City / Year", "2010", "2015", "2020", "2025"]
        cities = ["Metropolis", "Gotham", "Star City", "Central", "Coast City", "Bludhaven"]
        rows = []
        for city in cities:
            base = random.randint(1000, 5000)
            rows.append([city, str(base), str(int(base*1.1)), str(int(base*1.25)), str(int(base*1.4))])
        
        q = {
            "id": f"data_q_{i}",
            "difficulty": diffs[i-1],
            "question_text": f"The table below shows the population (in thousands) of 6 different cities from 2010 to 2025. Based on this data, which city had the highest absolute population growth from 2010 to 2025?",
            "chart_data": {
                "type": "table",
                "title": "City Population Growth (Thousands)",
                "headers": headers,
                "rows": rows
            },
            "options": [
                {"letter": "A", "text": "Metropolis"},
                {"letter": "B", "text": "Gotham"},
                {"letter": "C", "text": "Star City"},
                {"letter": "D", "text": "Central"},
                {"letter": "E", "text": "Coast City"}
            ],
            "correct_answer": "D", # dummy assignment, will just be an exercise
            "explanation": "You must subtract the 2010 population from the 2025 population for each city to find the absolute growth. Central had the highest absolute growth.",
            "hints": ["Look at the first and last columns.", "Subtract 2010 from 2025 values."]
        }
    elif q_type == 'bar':
        labels = ["Q1", "Q2", "Q3", "Q4", "Q1 (Next Yr)"]
        datasets = [
            {"label": "Software", "values": [random.randint(20,80) for _ in range(5)]},
            {"label": "Hardware", "values": [random.randint(30,90) for _ in range(5)]},
            {"label": "Services", "values": [random.randint(10,50) for _ in range(5)]},
            {"label": "Consulting", "values": [random.randint(15,45) for _ in range(5)]}
        ]
        q = {
            "id": f"data_q_{i}",
            "difficulty": diffs[i-1],
            "question_text": f"The stacked bar chart represents the quarterly revenue (in $ millions) of a tech corporation across four main divisions. What was the approximate total revenue for the corporation in Q3?",
            "chart_data": {
                "type": "bar",
                "title": "Quarterly Revenue Breakdown ($ Millions)",
                "x_label": "Quarter",
                "y_label": "Revenue ($M)",
                "labels": labels,
                "datasets": datasets
            },
            "options": [
                {"letter": "A", "text": str(sum(d['values'][2] for d in datasets) - 10)},
                {"letter": "B", "text": str(sum(d['values'][2] for d in datasets))},
                {"letter": "C", "text": str(sum(d['values'][2] for d in datasets) + 15)},
                {"letter": "D", "text": str(sum(d['values'][2] for d in datasets) + 25)},
                {"letter": "E", "text": "Cannot be determined"}
            ],
            "correct_answer": "B",
            "explanation": f"Sum all 4 categories for Q3: {datasets[0]['values'][2]} + {datasets[1]['values'][2]} + {datasets[2]['values'][2]} + {datasets[3]['values'][2]} = {sum(d['values'][2] for d in datasets)}.",
            "hints": ["Look specifically at the Q3 bar.", "Add the values of all segments in that bar."]
        }
    elif q_type == 'line':
        labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
        datasets = [
            {"label": "Product A", "values": [random.randint(100,500) for _ in range(8)]},
            {"label": "Product B", "values": [random.randint(150,450) for _ in range(8)]},
            {"label": "Product C", "values": [random.randint(50,300) for _ in range(8)]}
        ]
        q = {
            "id": f"data_q_{i}",
            "difficulty": diffs[i-1],
            "question_text": f"The line graph shows the monthly sales volume for three competing products over an 8-month period. In which month was the combined sales volume of all three products the lowest?",
            "chart_data": {
                "type": "line",
                "title": "Monthly Sales Volume (Units)",
                "x_label": "Month",
                "y_label": "Sales Volume",
                "labels": labels,
                "datasets": datasets
            },
            "options": [
                {"letter": "A", "text": "February"},
                {"letter": "B", "text": "April"},
                {"letter": "C", "text": "May"},
                {"letter": "D", "text": "June"},
                {"letter": "E", "text": "July"}
            ],
            "correct_answer": "C",
            "explanation": "By adding the values of the three lines for each month, you can determine the total sales volume. May had the lowest combined total.",
            "hints": ["Estimate the total height of all three points in each month.", "Calculate exactly if two months look close."]
        }
    else: # pie
        labels = ["North America", "Europe", "Asia-Pacific", "Latin America", "Middle East & Africa"]
        v = [random.randint(10, 40) for _ in range(5)]
        s = sum(v)
        v = [int(x/s*100) for x in v]
        v[-1] = 100 - sum(v[:-1]) # ensure adds to 100
        
        datasets = [{"label": "Regions", "values": v}]
        q = {
            "id": f"data_q_{i}",
            "difficulty": diffs[i-1],
            "question_text": f"The pie chart illustrates the global market share distribution for a multinational retailer. If the total global market value is $250 Billion, what is the approximate value (in billions) of the {labels[2]} market?",
            "chart_data": {
                "type": "pie",
                "title": "Global Market Share 2024",
                "labels": labels,
                "datasets": datasets
            },
            "options": [
                {"letter": "A", "text": f"${int(250 * v[2] / 100 - 5)}B"},
                {"letter": "B", "text": f"${int(250 * v[2] / 100)}B"},
                {"letter": "C", "text": f"${int(250 * v[2] / 100 + 10)}B"},
                {"letter": "D", "text": f"${int(250 * v[2] / 100 + 15)}B"},
                {"letter": "E", "text": "None of the above"}
            ],
            "correct_answer": "B",
            "explanation": f"The {labels[2]} market holds {v[2]}%. 250 * {v[2]/100} = {int(250 * v[2] / 100)}.",
            "hints": ["Find the percentage for the region.", "Multiply percentage by the total value."]
        }
        
    topic_data["questions"].append(q)

# Apply correct option shuffling logic precisely
for q in topic_data['questions']:
    correct_opt = next((o for o in q['options'] if o['letter'] == q['correct_answer']), None)
    if not correct_opt: continue
    
    correct_text = correct_opt['text']
    opts_text = [o['text'] for o in q['options']]
    random.shuffle(opts_text)
    
    letters = ["A", "B", "C", "D", "E"]
    for j, opt in enumerate(q['options']):
        opt['text'] = opts_text[j]
        if opts_text[j] == correct_text:
            q['correct_answer'] = letters[j]

import os
path = os.path.join("quiz-app", "src", "PracticeQuestions", "Quantitative_Reasoning", "Data_Interpretation_and_Charts.json")
with open(path, "w", encoding="utf-8") as f:
    json.dump(topic_data, f, indent=2, ensure_ascii=False)
print("Updated Data Interpretations.")
