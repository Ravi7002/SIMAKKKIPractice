import json, random, re, os, copy, sys, glob

# ─── Load real exam bases ────────────────────────────────────────────────────
with open('realQ1.json', 'r', encoding='utf-8') as f:
    q1 = json.load(f)
with open('realQ2.json', 'r', encoding='utf-8') as f:
    q2 = json.load(f)

bases = [q1, q2]
os.makedirs(os.path.join('quiz-app', 'src', 'GeneratedTryouts'), exist_ok=True)

# ─── Load English passage pools ──────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from english_pool_v4 import POOL as LONG_PASSAGES

# ─── Name banks for LR mutation (4 sets, one per tryout) ─────────────────────
NAME_SETS = [
    # Set 0 (tryout 1) - realQ1 names + realQ2 Indonesian names
    {"Alex": "James", "Bella": "Sarah", "Chris": "Kevin", "Diana": "Laura",
     "Ethan": "Ryan", "Fiona": "Megan", "George": "Daniel", "Hannah": "Sophie",
     "Aaron": "Marcus", "Brian": "Steven", "Clara": "Nadia", "Evan": "Felix",
     "Grace": "Ivy", "Henry": "Oscar", "Liam": "Victor", "Noah": "Derek",
     "Olivia": "Priya", "Emma": "Tara", "Ava": "Zara", "Rina": "Yuki",
     "Mira": "Sari", "Adam": "Hugo", "Chloe": "Wendy", "Nina": "Rita",
     "Owen": "Jack", "Paul": "Theo", "Mark": "Leo", "Lina": "Nia",
     # realQ2 names
     "Nasyhah": "Aisha", "Berto": "Faisal", "Doni": "Rahmat", "Elsa": "Wulan",
     "Citra": "Indah", "Alfa": "Gilang", "Bayu": "Rendi", "Devi": "Putri",
     "Farah": "Laila", "Galih": "Andi", "Hendra": "Budi", "Intan": "Siti",
     "Joko": "Agus", "Karina": "Dewi", "Luki": "Eko", "Mega": "Sri",
     "Nita": "Tuti", "Omar": "Hadi", "Putra": "Wawan", "Reza": "Yanto",
     "Siska": "Umi", "Tono": "Bambang", "Usman": "Darto", "Vera": "Fitri",
     "Wina": "Gita", "Yola": "Hesti", "Abigail": "Melinda", "Amru": "Kurnia",
     "Wawan": "Susanto", "Siti": "Ratna",
     "P": "W", "Q": "X", "R": "Y", "S": "Z", "T": "V"},
    # Set 1 (tryout 2)
    {"Alex": "Patrick", "Bella": "Carla", "Chris": "Dominic", "Diana": "Elena",
     "Ethan": "Marco", "Fiona": "Greta", "George": "Hector", "Hannah": "Irene",
     "Aaron": "Boris", "Brian": "Cedric", "Clara": "Daphne", "Evan": "Grant",
     "Grace": "Helen", "Henry": "Ivan", "Liam": "Andre", "Noah": "Bruno",
     "Olivia": "Fatima", "Emma": "Kira", "Ava": "Luna", "Rina": "Sita",
     "Mira": "Dina", "Adam": "Ravi", "Chloe": "Petra", "Nina": "Vera",
     "Owen": "Quinn", "Paul": "Samir", "Mark": "Noel", "Lina": "Freya",
     # realQ2 names
     "Nasyhah": "Zahra", "Berto": "Kemal", "Doni": "Wahyu", "Elsa": "Nuri",
     "Citra": "Ratih", "Alfa": "Surya", "Bayu": "Tegar", "Devi": "Andin",
     "Farah": "Bunga", "Galih": "Dimas", "Hendra": "Fajar", "Intan": "Gani",
     "Joko": "Haris", "Karina": "Isma", "Luki": "Kamal", "Mega": "Lestari",
     "Nita": "Mawar", "Omar": "Nugroho", "Putra": "Ojan", "Reza": "Pandu",
     "Siska": "Qori", "Tono": "Rudi", "Usman": "Soleh", "Vera": "Tasya",
     "Wina": "Ulfa", "Yola": "Vina", "Abigail": "Kartini", "Amru": "Ridho",
     "Wawan": "Prasetyo", "Siti": "Aminah",
     "P": "M", "Q": "N", "R": "K", "S": "L", "T": "J"},
    # Set 2 (tryout 3)
    {"Alex": "Carlos", "Bella": "Yolanda", "Chris": "Raymond", "Diana": "Ingrid",
     "Ethan": "Tobias", "Fiona": "Astrid", "George": "Walter", "Hannah": "Bianca",
     "Aaron": "Stefan", "Brian": "Luther", "Clara": "Hilda", "Evan": "Norman",
     "Grace": "Olga", "Henry": "Klaus", "Liam": "Ernst", "Noah": "Franz",
     "Olivia": "Giselle", "Emma": "Heidi", "Ava": "Margot", "Rina": "Aiko",
     "Mira": "Lena", "Adam": "Fritz", "Chloe": "Anke", "Nina": "Elke",
     "Owen": "Hans", "Paul": "Dieter", "Mark": "Bernd", "Lina": "Ulla",
     # realQ2 names
     "Nasyhah": "Firdaus", "Berto": "Lukman", "Doni": "Irfan", "Elsa": "Nabila",
     "Citra": "Hasna", "Alfa": "Rizki", "Bayu": "Arief", "Devi": "Sinta",
     "Farah": "Jihan", "Galih": "Mukti", "Hendra": "Novan", "Intan": "Prita",
     "Joko": "Rama", "Karina": "Salma", "Luki": "Udin", "Mega": "Vivi",
     "Nita": "Widya", "Omar": "Yusuf", "Putra": "Zaki", "Reza": "Amir",
     "Siska": "Bella", "Tono": "Chandra", "Usman": "Darma", "Vera": "Eka",
     "Wina": "Fani", "Yola": "Gina", "Abigail": "Hanum", "Amru": "Ilham",
     "Wawan": "Jefri", "Siti": "Kiki",
     "P": "F", "Q": "G", "R": "H", "S": "I", "T": "E"},
    # Set 3 (tryout 4)
    {"Alex": "Naomi", "Bella": "Kenji", "Chris": "Haruto", "Diana": "Sakura",
     "Ethan": "Akira", "Fiona": "Yumi", "George": "Toshi", "Hannah": "Mei",
     "Aaron": "Riku", "Brian": "Kai", "Clara": "Suki", "Evan": "Jiro",
     "Grace": "Hana", "Henry": "Shin", "Liam": "Bram", "Noah": "Lars",
     "Olivia": "Elin", "Emma": "Sigrid", "Ava": "Helga", "Rina": "Anita",
     "Mira": "Devi", "Adam": "Arjun", "Chloe": "Priti", "Nina": "Kavita",
     "Owen": "Vijay", "Paul": "Rohit", "Mark": "Sunil", "Lina": "Deepa",
     # realQ2 names
     "Nasyhah": "Astuti", "Berto": "Guntur", "Doni": "Hermawan", "Elsa": "Juliana",
     "Citra": "Lilis", "Alfa": "Mahendra", "Bayu": "Okta", "Devi": "Rini",
     "Farah": "Suci", "Galih": "Tirta", "Hendra": "Utama", "Intan": "Warni",
     "Joko": "Yandri", "Karina": "Zubaida", "Luki": "Bagus", "Mega": "Cantik",
     "Nita": "Desti", "Omar": "Erwin", "Putra": "Firman", "Reza": "Gunawan",
     "Siska": "Hikmah", "Tono": "Iwan", "Usman": "Jaka", "Vera": "Krisna",
     "Wina": "Lusiana", "Yola": "Murni", "Abigail": "Novrida", "Amru": "Prambudi",
     "Wawan": "Rino", "Siti": "Tini",
     "P": "U", "Q": "D", "R": "B", "S": "C", "T": "A"}
]

# Number offsets per tryout (added to numbers in LR questions)
# T1(idx0) uses base rQ2, T2(idx1) uses rQ1, T3(idx2) uses rQ2, T4(idx3) uses rQ1
# Ensure same-base tryouts (0&2, 1&3) have different offsets
NUM_OFFSETS = [2, 5, 8, 11]

# Context word swaps to differentiate even generic LR questions
CONTEXT_SWAPS = [
    # Set 0
    {"workshop": "seminar", "employees": "staff members", "company": "firm",
     "school": "academy", "hotel": "resort", "flight": "train", "meeting": "briefing",
     "City A": "Town X", "City B": "Town Y", "laptop": "workstation",
     "TripGo": "BookNow", "birds": "eagles", "colorful": "spotted",
     "tropical storm": "monsoon", "power outage": "blackout", "Machine learning": "Deep learning",
     "artificial intelligence": "computational intelligence", "Self-driving cars": "Autonomous vehicles",
     "cooling system": "ventilation unit", "registration form": "sign-up sheet",
     "debate team": "quiz team", "competition": "tournament", "panelists": "speakers",
     "conference": "forum", "overtime": "extra shift", "stamina": "endurance",
     "exercise": "train", "university": "college", "Cloud computing": "Edge computing",
     "physical servers": "hardware servers", "moderator": "host",
     "international": "regional", "desk": "table", "programming": "coding",
     "library": "archive center", "mammals": "primates", "warm-blooded": "endothermic",
     "ocean": "deep sea", "nutrition": "dietary", "athletes": "players",
     "weight": "mass", "sugar": "fructose", "B consists": "B includes", "average": "mean",
     "host": "moderator", "guests": "participants", "guest": "participant",
     "Which of the following groups could be selected?": "Identify the team that can be formed from these choices:",
     "Who sits at table A?": "Which individuals are located at table A?",
     "Who sits at table B?": "Which pair is positioned at table B?"},
    # Set 1
    {"workshop": "lecture", "employees": "team members", "company": "corporation",
     "school": "institute", "hotel": "lodge", "flight": "bus", "meeting": "session",
     "City A": "Region P", "City B": "Region Q", "laptop": "desktop",
     "TripGo": "StayEasy", "birds": "parrots", "colorful": "vibrant",
     "tropical storm": "cyclone", "power outage": "electricity failure", "Machine learning": "Neural networks",
     "artificial intelligence": "smart computing", "Self-driving cars": "Robotic vehicles",
     "cooling system": "heat dissipation module", "registration form": "enrollment form",
     "debate team": "speech team", "competition": "contest", "panelists": "presenters",
     "conference": "symposium", "overtime": "additional hours", "stamina": "resilience",
     "exercise": "work out", "university": "polytechnic", "Cloud computing": "Distributed computing",
     "physical servers": "dedicated machines", "moderator": "coordinator",
     "international": "national", "desk": "booth", "programming": "software development",
     "library": "reference hall", "mammals": "amphibians", "warm-blooded": "active-blooded",
     "ocean": "pelagic zone", "nutrition": "calorie", "athletes": "competitors",
     "weight": "heaviness", "sugar": "glucose", "B consists": "B is made of", "average": "midpoint",
     "host": "coordinator", "guests": "attendees", "guest": "attendee",
     "Which of the following groups could be selected?": "Find the combination that satisfies all conditions:",
     "Who sits at table A?": "Who are the occupants of table A?",
     "Who sits at table B?": "Who has been assigned to table B?"},
    # Set 2
    {"workshop": "training", "employees": "workers", "company": "organization",
     "school": "college", "hotel": "inn", "flight": "ferry", "meeting": "assembly",
     "City A": "District M", "City B": "District N", "laptop": "tablet",
     "TripGo": "TravelMate", "birds": "sparrows", "colorful": "bright",
     "tropical storm": "typhoon", "power outage": "electrical disruption", "Machine learning": "Predictive modeling",
     "artificial intelligence": "machine intelligence", "Self-driving cars": "Driverless vehicles",
     "cooling system": "thermal management system", "registration form": "attendance form",
     "debate team": "oratory team", "competition": "championship", "panelists": "discussants",
     "conference": "summit", "overtime": "supplementary duty", "stamina": "vigor",
     "exercise": "practice sports", "university": "academy", "Cloud computing": "Virtual computing",
     "physical servers": "on-premise hardware", "moderator": "facilitator",
     "international": "intercity", "desk": "workstation", "programming": "development",
     "library": "media center", "mammals": "reptiles", "warm-blooded": "stable-temperature",
     "ocean": "open water", "nutrition": "meal", "athletes": "runners",
     "weight": "bulk", "sugar": "carbs", "B consists": "B is composed of", "average": "median-value",
     "host": "facilitator", "guests": "invitees", "guest": "invitee",
     "Which of the following groups could be selected?": "Based on the rules, which group is a possible selection?",
     "Who sits at table A?": "Name the students sitting at table A:",
     "Who sits at table B?": "Determine who is sitting at table B:"},
    # Set 3
    {"workshop": "bootcamp", "employees": "associates", "company": "enterprise",
     "school": "campus", "hotel": "villa", "flight": "shuttle", "meeting": "gathering",
     "City A": "Zone K", "City B": "Zone L", "laptop": "notebook",
     "TripGo": "GoTravel", "birds": "finches", "colorful": "vivid",
     "tropical storm": "severe weather system", "power outage": "grid failure", "Machine learning": "Pattern recognition",
     "artificial intelligence": "cognitive computing", "Self-driving cars": "Self-navigating vehicles",
     "cooling system": "cooling apparatus", "registration form": "confirmation slip",
     "debate team": "argument team", "competition": "rivalry", "panelists": "contributors",
     "conference": "congress", "overtime": "extra work period", "stamina": "fortitude",
     "exercise": "do fitness", "university": "institution", "Cloud computing": "Remote computing",
     "physical servers": "local infrastructure", "moderator": "chairperson",
     "international": "global", "desk": "counter", "programming": "engineering",
     "library": "study center", "mammals": "aquatic animals", "warm-blooded": "heat-regulating",
     "ocean": "marine environment", "nutrition": "energy", "athletes": "pros",
     "weight": "size", "sugar": "sucrose", "B consists": "B comprises", "average": "center-value",
     "host": "announcer", "guests": "presenters", "guest": "presenter",
     "Which of the following groups could be selected?": "Select the list that represents a valid group:",
     "Who sits at table A?": "Who is currently at table A?",
     "Who sits at table B?": "Which individuals are assigned to table B?"}
]


# ─── LR-specific text mutation ───────────────────────────────────────────────
def mutate_lr_text(text, name_map, num_offset, context_map):
    """Mutate Logical Reasoning text by replacing names, numbers, and context words."""
    if not isinstance(text, str):
        return text
    result = text
    # Replace names (longer names first to avoid partial replacements)
    for orig, repl in sorted(name_map.items(), key=lambda x: -len(x[0])):
        if len(orig) > 1:
            result = result.replace(orig, repl)
        else:
            # Single-letter names like P, Q, R, S, T
            result = re.sub(r'\b' + re.escape(orig) + r'\b', repl, result)
    
    # Replace context words (case-sensitive first, then case-insensitive for sentence starts)
    for orig, repl in sorted(context_map.items(), key=lambda x: -len(x[0])):
        result = result.replace(orig, repl)
        # Also handle capitalized versions
        result = result.replace(orig.capitalize(), repl.capitalize())

    # Add sentence starter variations to ensure uniqueness
    if result.startswith("All "):
        starters = ["Every ", "Each ", "Totally all ", "Broadly all "]
        result = starters[num_offset % 4] + result[4:]
    elif result.startswith("If "):
        starters = ["Whenever ", "Provided ", "Supposing ", "When "]
        result = starters[num_offset % 4] + result[3:]
    
    # Shift numbers to make each tryout feel different
    def shift_num(m):
        n = int(m.group(0))
        if n == 0:
            return "0"
        if n < 10:
            return str(n + (num_offset % 3))  # Small shift for small numbers
        if n < 100:
            return str(n + num_offset)
        return str(n + num_offset * 3)
    
    result = re.sub(r'(?<![.,a-zA-Z])\b(\d+)\b(?![.,a-zA-Z])', lambda m: shift_num(m), result)
    return result

def mutate_lr_question(q, tryout_idx):
    """Deep-mutate an entire LR question dict (question_text, options, explanation, passage, hints)."""
    name_map = NAME_SETS[tryout_idx % len(NAME_SETS)]
    num_offset = NUM_OFFSETS[tryout_idx % len(NUM_OFFSETS)]
    context_map = CONTEXT_SWAPS[tryout_idx % len(CONTEXT_SWAPS)]
    
    q_copy = copy.deepcopy(q)
    q_copy['question_text'] = mutate_lr_text(q_copy.get('question_text', ''), name_map, num_offset, context_map)
    q_copy['explanation'] = mutate_lr_text(q_copy.get('explanation', ''), name_map, num_offset, context_map)
    
    if 'passage' in q_copy and q_copy['passage']:
        q_copy['passage'] = mutate_lr_text(q_copy['passage'], name_map, num_offset, context_map)
    
    for opt in q_copy.get('options', []):
        opt['text'] = mutate_lr_text(opt.get('text', ''), name_map, num_offset, context_map)
    
    for idx, hint in enumerate(q_copy.get('hints', [])):
        q_copy['hints'][idx] = mutate_lr_text(hint, name_map, num_offset, context_map)
    
    return q_copy

# ─── General text mutation (for non-LR, non-English) ────────────────────────
def mutate_text(text, skip_numbers=False):
    if not isinstance(text, str): return text
    def rep_num(m):
        start, end = m.start(), m.end()
        if start > 0 and text[start-1] in '.,': return m.group(0)
        if end < len(text) and text[end] in '.,': return m.group(0)
        n = int(m.group(0))
        if n == 0: return "0"
        if n < 10: return str(n + random.randint(1, 2))
        if n < 100: return str(n + random.randint(1, 5))
        return str(n + random.randint(5, 15))
    if not skip_numbers:
        text = re.sub(r'(?<![.,])\b(\d+)\b(?![.,])', lambda m: rep_num(m), text)
    return text

# ─── Auto-hints ──────────────────────────────────────────────────────────────
def generate_hints(q):
    subject = str(q.get('subject', '')).lower()
    topic   = str(q.get('topic', '')).lower()
    q_text  = str(q.get('question_text', '')).lower()
    if 'english' in subject:
        if 'grammar' in topic or 'fill' in q_text:
            return ["Identify the subject and its number (singular or plural).", "Check the tense marker (is, was, have been)."]
        if 'reading' in topic:
            return ["Look for the specific keywords in the passage.", "Eliminate answers that are not mentioned in the text."]
        if 'cohesion' in topic or 'relationship' in q_text or 'paragraph' in q_text:
            return ["Identify the main idea of each paragraph first.", "Check if the second paragraph provides evidence, a contrast, or a solution to the first."]
        return ["Re-read the relevant part of the passage carefully."]
    if 'logical' in subject:
        return ["Draw a diagram or list the conditions systematically.", "If-then statements are keys to the sequence."]
    return ["Identify the core formula needed for this problem."]

# ─── Main generation ─────────────────────────────────────────────────────────
SUBJECT_ORDER = ['Basic Mathematics', 'English', 'Quantitative Reasoning', 'Logical Reasoning']

# Load Practice Pools for Math and Quantitative Reasoning ONLY
practice_pools = {}
for fp in glob.glob('PracticeQuestions/**/*.json', recursive=True):
    with open(fp, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if 'questions' in data:
            s_key = data.get('subject', '').lower().strip()
            for q in data['questions']:
                t_key = q.get('topic', data.get('topic', '')).lower().strip()
                s_key_q = q.get('subject', s_key).lower().strip()
                key = (s_key_q, t_key)
                if key not in practice_pools:
                    practice_pools[key] = []
                practice_pools[key].append(q)

used_q_ids = set()
used_q_texts = set()

for i in range(1, 5): 
    raw_base = copy.deepcopy(bases[i % 2])
    
    # Process non-English (60 Qs total)
    non_english = []
    
    def process_item_for_tryout(item, item_id_suffix):
        """Sample a unique replacement from PracticeQuestions pool (for Math/Quant only)."""
        s_key = item.get('subject', '').lower().strip()
        t_key = item.get('topic', '').lower().strip()
        pool = practice_pools.get((s_key, t_key), [])
        avail = [q for q in pool if q.get('id') not in used_q_ids and q.get('question_text', '')[:80] not in used_q_texts]
        
        # If pool is empty or missing, try fuzzy topic matching within the subject
        if not avail:
            fallback_pool = []
            for (ps, pt), qs in practice_pools.items():
                if ps == s_key:
                    fallback_pool.extend(qs)
            avail = [q for q in fallback_pool if q.get('id') not in used_q_ids and q.get('question_text', '')[:80] not in used_q_texts]
            
        if avail:
            rep_q = copy.deepcopy(random.choice(avail))
            used_q_ids.add(rep_q.get('id'))
            used_q_texts.add(rep_q.get('question_text', '')[:80])
            rep_q['id'] = f"{item.get('id', rep_q.get('id'))}_gen_{item_id_suffix}"
            if 'hints' not in rep_q:
                rep_q['hints'] = generate_hints(rep_q)
            return rep_q
        else:
            q_copy = copy.deepcopy(item)
            q_copy['id'] = f"{item.get('id', 'unk')}_gen_{item_id_suffix}"
            if 'hints' not in q_copy:
                q_copy['hints'] = generate_hints(q_copy)
            return q_copy

    for item in raw_base:
        if isinstance(item, dict) and 'passages' in item and 'questions' in item:
            # This is a passages block — contains Logical Reasoning questions
            pmap = {p['id']: p['text'] for p in item['passages']}
            for q in item['questions']:
                if str(q.get('subject','')).lower() == 'english':
                    continue
                q_copy = copy.deepcopy(q)
                if q_copy.get('passage_id') and not q_copy.get('passage'):
                    q_copy['passage'] = pmap.get(q_copy['passage_id'])
                
                if str(q_copy.get('subject','')).lower() == 'logical reasoning':
                    # KEEP original LR structure, just mutate names/numbers
                    q_mutated = mutate_lr_question(q_copy, i - 1)
                    q_mutated['id'] = f"{q.get('id')}_gen_{i}"
                    if 'hints' not in q_mutated:
                        q_mutated['hints'] = generate_hints(q_mutated)
                    non_english.append(q_mutated)
                else:
                    # Non-LR passage question: use pool sampling
                    non_english.append(process_item_for_tryout(q_copy, i))
                    
        elif isinstance(item, dict) and str(item.get('subject','')).lower() != 'english':
            if str(item.get('subject','')).lower() == 'logical reasoning':
                # KEEP original LR structure, just mutate names/numbers
                q_mutated = mutate_lr_question(item, i - 1)
                q_mutated['id'] = f"{item.get('id')}_gen_{i}"
                if 'hints' not in q_mutated:
                    q_mutated['hints'] = generate_hints(q_mutated)
                non_english.append(q_mutated)
            else:
                # Math/Quantitative: substitute from pool
                non_english.append(process_item_for_tryout(item, i))

    # Process English (Exactly 20 Qs from 7 distinct passages per tryout)
    english_qs = []
    
    # Select 7 distinct passages for this tryout
    start_idx = (i - 1) * 7
    tryout_passages = []
    for j in range(7):
        p_idx = (start_idx + j) % 28 # Rotate through main 28 passages
        if j == 3:
            p_idx = 28 + ((i - 1) % 3)
        tryout_passages.append(copy.deepcopy(LONG_PASSAGES[p_idx]))

    # Flatten questions and assign passage text
    flat_questions = []
    q_counts = [3, 4, 3, 2, 3, 3, 2]
    
    for idx, p in enumerate(tryout_passages):
        count_target = q_counts[idx]
        passage_qs = copy.deepcopy(p['questions'])
        
        while len(passage_qs) > count_target:
            passage_qs.pop()
            
        while len(passage_qs) < count_target:
            passage_qs.append({
                "subject": "English",
                "topic": "Reading Comprehension",
                "question_text": "Which of the following best captures the main theme of the passage?",
                "options": [
                    {"letter": "A", "text": "The specific detail mentioned in paragraph 2"},
                    {"letter": "B", "text": "The historical background mentioned in paragraph 1"},
                    {"letter": "C", "text": "The overall conceptual framework unifying all paragraphs"},
                    {"letter": "D", "text": "The future challenges outlined in paragraph 3"},
                    {"letter": "E", "text": "None of the above accurately describes the main theme"}
                ],
                "correct_answer": "C",
                "explanation": "To capture the main theme, you must select the option that encompasses the overarching narrative of all paragraphs combined, rather than an isolated detail."
            })
            
        for q in passage_qs:
            q['passage'] = p['text']
            q['passage_id'] = p['id']
            flat_questions.append(q)
    
    english_qs = flat_questions

    # Mutate and format English
    for idx, q in enumerate(english_qs):
        base_id = q.get('id', f'eng_{idx+1:02d}')
        q['id'] = f"{base_id}_gen_{i}"
        q['hints'] = generate_hints(q)

    # Combine and Sort
    all_qs = english_qs + non_english
    all_qs.sort(key=lambda q: (SUBJECT_ORDER.index(q.get('subject','')) if q.get('subject','') in SUBJECT_ORDER else 99))

    # Save
    with open(f'quiz-app/src/GeneratedTryouts/tryout_{i}.json', 'w', encoding='utf-8') as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    
    print(f"Tryout {i}: English ({len(english_qs)}), Others ({len(non_english)}), Total ({len(all_qs)})")

# Clean up
for i in range(5, 21):
    path = f'quiz-app/src/GeneratedTryouts/tryout_{i}.json'
    if os.path.exists(path): os.remove(path)

print("\nSuccess: Generated 4 tryouts with exactly 7 distinct passages / 20 English questions each.")
