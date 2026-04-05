# english_pool_v3.py
# Total 28 unique passages (01-28)
# Each tryout (7 passages) must total 20 questions.
# Tryout 1 (P1-P7), Tryout 2 (P8-P14), Tryout 3 (P15-P21), Tryout 4 (P22-P28)

POOL = [

# ── TRYOUT 1: PASSAGES 01-07 (20 Q Total) ──────────────────────────────────
# P1: Space Junk (3 Q)
{"id": "t1_p1", "text": "Orbiting the Earth is a growing cloud of space debris, ranging from defunct satellites to tiny paint flecks. This 'space junk' travels at speeds up to 28,000 kilometers per hour, making even small pieces dangerous to active spacecraft. International space agencies are now (a) ________ missions to capture and de-orbit the largest pieces of debris to prevent a chain reaction of collisions.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): 'International space agencies are now (a) ________ missions...'", "options": [{"letter":"A","text":"launched"},{"letter":"B","text":"launching"},{"letter":"C","text":"launch"},{"letter":"D","text":"has launched"},{"letter":"E","text":"to launch"}], "correct_answer": "B", "explanation": "The present continuous 'are now launching' describes an action currently in progress."},
    {"subject": "English", "topic": "Reading", "question_text": "According to the text, why is space junk dangerous?", "options": [{"letter":"A","text":"Because it is made of radioactive material"},{"letter":"B","text":"Because it travels at extremely high speeds"},{"letter":"C","text":"Because it interferes with internet signals"},{"letter":"D","text":"Because it is invisible to radar"},{"letter":"E","text":"Because it is falling to Earth"}], "correct_answer": "B", "explanation": "The text states it travels up to 28,000 km/h, making it dangerous."},
    {"subject": "English", "topic": "Reading", "question_text": "What is the primary goal of the de-orbiting missions?", "options": [{"letter":"A","text":"To salvage gold from old satellites"},{"letter":"B","text":"To clean the atmosphere of CO2"},{"letter":"C","text":"To prevent a chain reaction of collisions"},{"letter":"D","text":"To build new space stations"},{"letter":"E","text":"To study the effects of high-speed paint flecks"}], "correct_answer": "C", "explanation": "The text states missions aim to 'capture and de-orbit... to prevent a chain reaction of collisions'."}
 ]},

# P2: Coral Bleaching (3 Q)
{"id": "t1_p2", "text": "Coral reefs are often called the rainforests of the sea because of their immense biodiversity. However, rising ocean temperatures have led to widespread coral bleaching. When water is too warm, corals expel the algae living in their tissues, causing them to turn completely white. (1) This process weakens the coral and makes them more susceptible to disease. (2) Many people enjoy scuba diving in tropical waters. (3) Sustainable tourism and carbon reduction are essential for reef survival.",
 "questions": [
    {"subject": "English", "topic": "Cohesion", "question_text": "Which sentence is irrelevant to the paragraph?", "options": [{"letter":"A","text":"Sentence 1"},{"letter":"B","text":"Sentence 2"},{"letter":"C","text":"Both 1 and 2"},{"letter":"D","text":"Sentence 3"},{"letter":"E","text":"None"}], "correct_answer": "B", "explanation": "Sentence 2 is about scuba diving, while the rest are about coral bleaching and survival."},
    {"subject": "English", "topic": "Reading", "question_text": "Under what condition does coral bleaching occur?", "options": [{"letter":"A","text":"When the water becomes too salty"},{"letter":"B","text":"When ocean temperatures rise too high"},{"letter":"C","text":"When there is a lack of sunlight"},{"letter":"D","text":"When predatory fish increase"},{"letter":"E","text":"When the tide is low"}], "correct_answer": "B", "explanation": "The text explicitly mentions rising ocean temperatures as the cause."},
    {"subject": "English", "topic": "Vocabulary", "question_text": "In the text, the word 'expel' is closest in meaning to...", "options": [{"letter":"A","text":"absorb"},{"letter":"B","text":"protect"},{"letter":"C","text":"release"},{"letter":"D","text":"consume"},{"letter":"E","text":"invite"}], "correct_answer": "C", "explanation": "Corals 'expel' (release/force out) the algae tissues when stressed."}
 ]},

# P3: Remote Work Evolution (3 Q)
{"id": "t1_p3", "text": "The conceptualization of 'the office' has fundamentally shifted. Before 2020, remote work was a perk for a minority. Today, it is a structural reality for millions. While some firms demand a full return to headquarters, others have embraced 'hybrid' models. This flexibility (a) ________ employees to better balance professional duties with personal health, though it can lead to feelings of isolation if not managed carefully.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): 'This flexibility (a) ________ employees to better balance...'", "options": [{"letter":"A","text":"allow"},{"letter":"B","text":"allowing"},{"letter":"C","text":"allows"},{"letter":"D","text":"allowed"},{"letter":"E","text":"to allow"}], "correct_answer": "C", "explanation": "Singular subject 'flexibility' requires the singular verb 'allows'."},
    {"subject": "English", "topic": "Reading", "question_text": "What is mentioned as a potential downside of remote work?", "options": [{"letter":"A","text":"Increased commuting time"},{"letter":"B","text":"Lower productivity"},{"letter":"C","text":"Feelings of isolation"},{"letter":"D","text":"Higher office costs"},{"letter":"E","text":"Lack of professional duties"}], "correct_answer": "C", "explanation": "The text mentions it 'can lead to feelings of isolation'."},
    {"subject": "English", "topic": "Reading", "question_text": "How has the status of remote work changed since before 2020?", "options": [{"letter":"A","text":"It has become completely illegal"},{"letter":"B","text":"It moved from a rare perk to a structural reality"},{"letter":"C","text":"It transitioned from a requirement to an optional choice"},{"letter":"D","text":"It was replaced entirely by hybrid models"},{"letter":"E","text":"It is no longer considered beneficial for employees"}], "correct_answer": "B", "explanation": "The text states: 'Before 2020, remote work was a perk for a minority. Today, it is a structural reality for millions.'"}
 ]},

# P4: Vertical Farming (3 Q)
{"id": "t1_p4", "text": "As the global population nears 10 billion, the demand for food is (a) ________. Vertical farming offers a solution by growing crops in stacked layers, often in controlled indoor environments. This method uses 95% less water than traditional farming and eliminates the need for chemical pesticides. However, the high energy cost of artificial lighting remains a significant hurdle for large-scale adoption.",
 "questions": [
    {"subject": "English", "topic": "Vocabulary", "question_text": "Fill in blank (a): 'the demand for food is (a) ________.'", "options": [{"letter":"A","text":"stagnating"},{"letter":"B","text":"decreasing"},{"letter":"C","text":"soaring"},{"letter":"D","text":"fluctuating"},{"letter":"E","text":"vanishing"}], "correct_answer": "C", "explanation": "'Soaring' (rising rapidly) fits the context of 10 billion people."},
    {"subject": "English", "topic": "Reading", "question_text": "What is one environmental benefit of vertical farming mentioned?", "options": [{"letter":"A","text":"It uses no electricity"},{"letter":"B","text":"It uses significantly less water"},{"letter":"C","text":"It provides habitat for wildlife"},{"letter":"D","text":"It is cheaper than traditional farming"},{"letter":"E","text":"It encourages soil erosion"}], "correct_answer": "B", "explanation": "The text states it uses 95% less water than traditional farming."},
    {"subject": "English", "topic": "Reading", "question_text": "What is the main drawback to large-scale vertical farming adoption?", "options": [{"letter":"A","text":"A lack of viable crops"},{"letter":"B","text":"The 95% water reduction"},{"letter":"C","text":"The high energy cost of artificial lighting"},{"letter":"D","text":"Opposition from traditional farmers"},{"letter":"E","text":"Insufficient global demand for food"}], "correct_answer": "C", "explanation": "The text identifies 'high energy cost of artificial lighting' as a 'significant hurdle'."}
 ]},

# P5: The History of Tea (3 Q)
{"id": "t1_p5", "text": "Legend has it that tea was discovered by Emperor Shen Nong in 2737 BC when leaves from a wild tree blew into his pot of boiling water. From its origins in China, tea spread to Japan and eventually to Europe via Dutch traders. Today, it is the most consumed beverage in the world after water. Its (a) ________ is attributed to its diverse flavors and perceived health benefits.",
 "questions": [
    {"subject": "English", "topic": "Vocabulary", "question_text": "Fill in blank (a): 'Its (a) ________ is attributed to its diverse flavors...'", "options": [{"letter":"A","text":"popularity"},{"letter":"B","text":"scarcity"},{"letter":"C","text":"complexity"},{"letter":"D","text":"bitterness"},{"letter":"E","text":"fragility"}], "correct_answer": "A", "explanation": "'Popularity' fits the context of being 'the most consumed beverage'."},
    {"subject": "English", "topic": "Reading", "question_text": "How did tea first reach Europe according to the text?", "options": [{"letter":"A","text":"Through Chinese explorers"},{"letter":"B","text":"By Dutch traders"},{"letter":"C","text":"Via the Silk Road"},{"letter":"D","text":"Through Japanese monks"},{"letter":"E","text":"It was grown in Europe initially"}], "correct_answer": "B", "explanation": "The text states tea spread to Europe 'via Dutch traders'."},
    {"subject": "English", "topic": "Reading", "question_text": "According to the passage, where did tea consumption begin?", "options": [{"letter":"A","text":"Europe"},{"letter":"B","text":"Japan"},{"letter":"C","text":"China"},{"letter":"D","text":"India"},{"letter":"E","text":"The Middle East"}], "correct_answer": "C", "explanation": "The text mentions its discovery by a Chinese emperor and its 'origins in China'."}
 ]},

# P6: Electric Aviation (2 Q)
{"id": "t1_p6", "text": "Aviation contributes roughly 2% of global CO2 emissions. While electric cars are mainstream, electric planes face a massive (a) ________: weight. Jet fuel contains 40 times more energy per kilogram than the best modern batteries. Short-haul electric flights are becoming possible, but long-distance travel still requires liquid fuels or hydrogen alternatives to be viable.",
 "questions": [
    {"subject": "English", "topic": "Vocabulary", "question_text": "Fill in blank (a): 'electric planes face a massive (a) ________: weight.'", "options": [{"letter":"A","text":"advantage"},{"letter":"B","text":"obstacle"},{"letter":"C","text":"incentive"},{"letter":"D","text":"connection"},{"letter":"E","text":"victory"}], "correct_answer": "B", "explanation": "'Obstacle' fits because weight is a problem for electric planes."},
    {"subject": "English", "topic": "Reading", "question_text": "Why is long-distance electric flight currently difficult?", "options": [{"letter":"A","text":"Batteries have low energy density compared to jet fuel"},{"letter":"B","text":"Electric motors are too noisy"},{"letter":"C","text":"There are no charging stations in the sky"},{"letter":"D","text":"Hydrogen is cheaper than batteries"},{"letter":"E","text":"Aircraft are too small"}], "correct_answer": "A", "explanation": "The text explains jet fuel has 40x more energy per kg than batteries."}
 ]},

# P7: Cybersecurity (3 Q)
{"id": "t1_p7", "text": "In the digital age, cybersecurity is no longer optional for businesses. Hackers use sophisticated phishing emails and ransomware to (a) ________ sensitive data. Training employees to recognize suspicious links is the first line of defense. (1) Companies also invest in firewalls and encryption. (2) Most employees prefer to eat lunch at their desks. (3) A single breach can cost millions in damages and lost trust.",
 "questions": [
    {"subject": "English", "topic": "Cohesion", "question_text": "Which sentence is irrelevant to the cybersecurity topic?", "options": [{"letter":"A","text":"Sentence 1"},{"letter":"B","text":"Sentence 2"},{"letter":"C","text":"Sentence 3"},{"letter":"D","text":"None"},{"letter":"E","text":"Sentence 1 and 3"}], "correct_answer": "B", "explanation": "Sentence 2 is about lunch habits, unrelated to cybersecurity."},
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): 'Hackers use...to (a) ________ sensitive data.'", "options": [{"letter":"A","text":"stole"},{"letter":"B","text":"stealing"},{"letter":"C","text":"steal"},{"letter":"D","text":"stolen"},{"letter":"E","text":"to steal"}], "correct_answer": "C", "explanation": "Infinitive 'to steal' is used for purpose."},
    {"subject": "English", "topic": "Reading", "question_text": "What does the text suggest is the 'first line of defense' in cybersecurity?", "options": [{"letter":"A","text":"Expensive firewalls"},{"letter":"B","text":"Encryption of all emails"},{"letter":"C","text":"Employee training to recognize suspicious links"},{"letter":"D","text":"Paying ransomware demands immediately"},{"letter":"E","text":"Deleting all sensitive data from the cloud"}], "correct_answer": "C", "explanation": "The text states: 'Training employees to recognize suspicious links is the first line of defense.'"}
 ]},

# ── TRYOUT 2: PASSAGES 08-14 (20 Q Total) ──────────────────────────────────
# P8: Microplastics (3 Q)
# P9: Renaissance Art (3 Q)
# P10: Electric Eel Biology (3 Q)
# P11: Pompeii Excavation (3 Q)
# P12: Artificial Intelligence (3 Q)
# P13: Graphene (2 Q)
# P14: The Great Wall (3 Q)
# (Same logic for P8-P28... adding more questions per passage to reach 20 per tryout set)

# [Expanding all remaining passages to ensure 20 total per block]

# P8: Microplastics (3 Q)
{"id": "t2_p1", "text": "Microplastics have been found in the deepest parts of the ocean and at the top of Mt. Everest. These tiny particles, defined as being less than 5mm in length, come from the breakdown of larger plastics or are (a) ________ in cosmetic products. They enter the food chain when small organisms ingest them, eventually reaching humans who consume seafood.",
 "questions": [
    {"subject": "English", "topic": "Vocabulary", "question_text": "Fill in blank (a): '...or are (a) ________ in cosmetic products.'", "options": [{"letter":"A","text":"intentional"},{"letter":"B","text":"intentionally added"},{"letter":"C","text":"unintentionally"},{"letter":"D","text":"intention"},{"letter":"E","text":"intend"}], "correct_answer": "B", "explanation": "'Intentionally added' fits the context of microbeads in cosmetics."},
    {"subject": "English", "topic": "Reading", "question_text": "How do microplastics enter the human body according to the text?", "options": [{"letter":"A","text":"Through skin contact"},{"letter":"B","text":"Through inhalation of city air"},{"letter":"C","text":"Through the food chain, specifically seafood"},{"letter":"D","text":"By drinking from plastic bottles only"},{"letter":"E","text":"They do not enter the human body"}], "correct_answer": "C", "explanation": "The text says they reach humans who consume seafood."},
    {"subject": "English", "topic": "Reading", "question_text": "What is the maximum length of a particle to be classified as a 'microplastic' in this text?", "options": [{"letter":"A","text":"5 millimeters"},{"letter":"B","text":"5 centimeters"},{"letter":"C","text":"1 millimeter"},{"letter":"D","text":"0.5 millimeters"},{"letter":"E","text":"The text does not say"}], "correct_answer": "A", "explanation": "The text defines them as 'less than 5mm in length'."}
 ]},

# P9: Renaissance Art (3 Q)
{"id": "t2_p2", "text": "The Renaissance was a period of 'rebirth' in European culture, moving away from medieval styles toward realism. Artists such as Leonardo da Vinci (a) ________ techniques like chiaroscuro to create the illusion of three-dimensional depth. This era emphasized humanism, focusing on human potential and achievements rather than purely religious subjects.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): 'Artists... (a) ________ techniques...'", "options": [{"letter":"A","text":"pioneer"},{"letter":"B","text":"pioneering"},{"letter":"C","text":"pioneered"},{"letter":"D","text":"has pioneered"},{"letter":"E","text":"pioneers"}], "correct_answer": "C", "explanation": "Past tense 'pioneered' is needed for a historical period."},
    {"subject": "English", "topic": "Reading", "question_text": "What was a central focus of the Renaissance according to the text?", "options": [{"letter":"A","text":"Abstract geometry"},{"letter":"B","text":"Humanism and realism"},{"letter":"C","text":"Medieval tradition"},{"letter":"D","text":"Purely religious subject matter"},{"letter":"E","text":"Digital manipulation"}], "correct_answer": "B", "explanation": "The text mentions moving toward 'realism' and emphasizing 'humanism'."},
    {"subject": "English", "topic": "Vocabulary", "question_text": "What is the purpose of the 'chiaroscuro' technique mentioned in the text?", "options": [{"letter":"A","text":"To mix paints effectively"},{"letter":"B","text":"To create the illusion of 3D depth"},{"letter":"C","text":"To preserve the canvas from mold"},{"letter":"D","text":"To paint religious symbols accurately"},{"letter":"E","text":"To hide imperfections in the painting"}], "correct_answer": "B", "explanation": "The text says it was used 'to create the illusion of three-dimensional depth'."}
 ]},

# P10: Electric Eel Biology (3 Q)
{"id": "t2_p3", "text": "The electric eel is not actually an eel, but a type of knifefish. It can (a) ________ shocks of up to 600 volts to stun prey or deter predators. These shocks come from specialized cells called electroocytes. Scientists are studying these cells to develop better bio-inspired batteries for medical implants.",
 "questions": [
    {"subject": "English", "topic": "Vocabulary", "question_text": "Fill in blank (a): 'It can (a) ________ shocks...'", "options": [{"letter":"A","text":"generate"},{"letter":"B","text":"received"},{"letter":"C","text":"absorbed"},{"letter":"D","text":"refuse"},{"letter":"E","text":"insulate"}], "correct_answer": "A", "explanation": "'Generate' shocks is the appropriate verb for an electric eel."},
    {"subject": "English", "topic": "Reading", "question_text": "Why are scientists studying the electric eel according to the text?", "options": [{"letter":"A","text":"To find a cure for electric shocks"},{"letter":"B","text":"To develop bio-inspired batteries for medical use"},{"letter":"C","text":"To learn how to swim faster"},{"letter":"D","text":"To categorize it as a true eel"},{"letter":"E","text":"To protect it from extinction"}], "correct_answer": "B", "explanation": "The text states they are studying cells to develop 'bio-inspired batteries'."},
    {"subject": "English", "topic": "Reading", "question_text": "Which of the following is true according to the passage?", "options": [{"letter":"A","text":"The electric eel is a true eel"},{"letter":"B","text":"The electric eel can generate up to 600 volts"},{"letter":"C","text":"Shocks are used only for communication"},{"letter":"D","text":"The specialized cells are located in the heart"},{"letter":"E","text":"Eels are currently used to power hospitals"}], "correct_answer": "B", "explanation": "The text explicitly says it can generate 'shocks of up to 600 volts'."}
 ]},

# P11: Pompeii Excavation (3 Q)
{"id": "t2_p4", "text": "The eruption of Mt. Vesuvius in 79 AD buried the city of Pompeii under a thick layer of volcanic ash. This (a) ________ preserved the city, freezing a moment in time for future archaeologists. Today, excavations reveal detailed glimpses into daily Roman life, from bakeries to public baths. However, the site now faces the challenge of erosion and 'over-tourism'.",
 "questions": [
    {"subject": "English", "topic": "Vocabulary", "question_text": "Fill in blank (a): 'This (a) ________ preserved the city...'", "options": [{"letter":"A","text":"unintentionally"},{"letter":"B","text":"willingly"},{"letter":"C","text":"destructively"},{"letter":"D","text":"rarely"},{"letter":"E","text":"partially"}], "correct_answer": "A", "explanation": "The preservation was an accidental (unintentional) result of the disaster."},
    {"subject": "English", "topic": "Reading", "question_text": "What is one challenge Pompeii faces today?", "options": [{"letter":"A","text":"Another imminent eruption"},{"letter":"B","text":"A lack of interest from tourists"},{"letter":"C","text":"Erosion and over-tourism"},{"letter":"D","text":"The ash is too hard to dig"},{"letter":"E","text":"Archaeologists are banned"}], "correct_answer": "C", "explanation": "The text mentions 'erosion and over-tourism' as challenges."},
    {"subject": "English", "topic": "Reading", "question_text": "What provided the preservation of Pompeii according to the passage?", "options": [{"letter":"A","text":"Strong modern chemicals"},{"letter":"B","text":"A thick layer of volcanic ash"},{"letter":"C","text":"A massive flood"},{"letter":"D","text":"Ancient stone walls"},{"letter":"E","text":"The dry desert heat"}], "correct_answer": "B", "explanation": "The text says ash 'buried the city... and preserved' it."}
 ]},

# P12: Artificial Intelligence (3 Q)
{"id": "t2_p5", "text": "Machine learning is a subset of AI where computers learn from data (a) ________ being explicitly programmed. By identifying patterns in massive datasets, these systems can name objects in photos or predict stock market trends. While AI offers efficiency, philosophers worry about the 'black box' problem — we don't always know *why* an AI made a specific decision.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): '...computers learn from data (a) ________ being explicitly programmed.'", "options": [{"letter":"A","text":"with"},{"letter":"B","text":"without"},{"letter":"C","text":"instead"},{"letter":"D","text":"by"},{"letter":"E","text":"unless"}], "correct_answer": "B", "explanation": "'Without' being programmed is the definition of machine learning context here."},
    {"subject": "English", "topic": "Reading", "question_text": "What is the 'black box' problem mentioned in the text?", "options": [{"letter":"A","text":"AI being too expensive"},{"letter":"B","text":"The lack of transparency in AI decision-making"},{"letter":"C","text":"AI running out of data"},{"letter":"D","text":"Computers being literally black in color"},{"letter":"E","text":"AI failing to identify photos"}], "correct_answer": "B", "explanation": "The text states 'we don't always know *why* an AI made a specific decision'."},
    {"subject": "English", "topic": "Vocabulary", "question_text": "The word 'explicitly' in the text is closest in meaning to...", "options": [{"letter":"A","text":"vaguely"},{"letter":"B","text":"publicly"},{"letter":"C","text":"unnecessarily"},{"letter":"D","text":"directly and clearly"},{"letter":"E","text":"quickly"}], "correct_answer": "D", "explanation": "Explicitly means in a direct, clear manner."}
 ]},

# P13: Graphene (2 Q)
{"id": "t2_p6", "text": "Graphene is a single layer of carbon atoms arranged in a hexagonal lattice. It is 200 times stronger than steel, yet incredibly flexible and lightweight. It also conducts electricity better than copper. (1) These properties make it ideal for flexible electronics and faster batteries. (2) Copper is a reddish-brown metal. (3) Despite its potential, mass-producing high-quality graphene at a low cost remains difficult.",
 "questions": [
    {"subject": "English", "topic": "Cohesion", "question_text": "Which sentence is irrelevant to the graphene topic?", "options": [{"letter":"A","text":"Sentence 1"},{"letter":"B","text":"Sentence 2"},{"letter":"C","text":"Sentence 3"},{"letter":"D","text":"None"},{"letter":"E","text":"Sentence 1 and 3"}], "correct_answer": "B", "explanation": "Sentence 2 is a generic fact about copper, while the rest are about graphene."},
    {"subject": "English", "topic": "Reading", "question_text": "What is one mentioned property of graphene?", "options": [{"letter":"A","text":"It is weaker than steel"},{"letter":"B","text":"It is a poor conductor"},{"letter":"C","text":"It is 200 times stronger than steel"},{"letter":"D","text":"It is very heavy"},{"letter":"E","text":"It is brittle and easily broken"}], "correct_answer": "C", "explanation": "The text says it is 200 times stronger than steel."}
 ]},

# P14: The Great Wall (3 Q)
{"id": "t2_p7", "text": "The Great Wall of China is not a single continuous wall, but a series of fortifications built across different dynasties. Most of the existing wall was (a) ________ during the Ming Dynasty. It stretches for over 21,000 kilometers, serving as a defense against northern invasions and a means of controlling Silk Road trade.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): 'Most of the existing wall was (a) ________ during the Ming Dynasty.'", "options": [{"letter":"A","text":"construct"},{"letter":"B","text":"constructing"},{"letter":"C","text":"constructed"},{"letter":"D","text":"has constructed"},{"letter":"E","text":"constructs"}], "correct_answer": "C", "explanation": "Passive voice 'was constructed' is correct."},
    {"subject": "English", "topic": "Reading", "question_text": "Beside defense, what was another purpose of the Great Wall?", "options": [{"letter":"A","text":"To provide a marathon track"},{"letter":"B","text":"To control Silk Road trade"},{"letter":"C","text":"To act as a dam for rivers"},{"letter":"D","text":"To keep animals from migrating"},{"letter":"E","text":"To observe the stars"}], "correct_answer": "B", "explanation": "The text mentioned it served as a 'means of controlling Silk Road trade'."},
    {"subject": "English", "topic": "Reading", "question_text": "According to the text, is the Great Wall one long solid wall?", "options": [{"letter":"A","text":"Yes, it is one continuous structure"},{"letter":"B","text":"No, it is a series of fortifications"},{"letter":"C","text":"It was before the Ming Dynasty"},{"letter":"D","text":"It only became one after 1900"},{"letter":"E","text":"The text does not provide this information"}], "correct_answer": "B", "explanation": "The text says it is 'not a single continuous wall, but a series of fortifications'."}
 ]},

# ── TRYOUT 3: PASSAGES 15-21 (20 Q Total) ──────────────────────────────────
# P15: Hydrothermal Vents (3 Q)
# P16: Printing Press (3 Q)
# P17: Self-Driving Cars (3 Q)
# P18: Library of Alexandria (3 Q)
# P19: IoT (3 Q)
# P20: Origami (2 Q)
# P21: Giant Squid (3 Q)

# P15: Deep Sea Hydrothermal Vents (3 Q)
{"id": "t3_p1", "text": "Deep on the ocean floor, hydrothermal vents spew superheated, mineral-rich water. Surprisingly, these dark environments (a) ________ unique ecosystems that do not rely on sunlight. Instead of photosynthesis, bacteria use a process called chemosynthesis to create energy from chemicals. This discovery has changed our understanding of where life can exist on other planets.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): '...these dark environments (a) ________ unique ecosystems...'", "options": [{"letter":"A","text":"host"},{"letter":"B","text":"hosts"},{"letter":"C","text":"hosting"},{"letter":"D","text":"hosted"},{"letter":"E","text":"has hosted"}], "correct_answer": "A", "explanation": "Plural subject 'environments' takes plural verb 'host'."},
    {"subject": "English", "topic": "Reading", "question_text": "What process do bacteria near hydrothermal vents use to create energy?", "options": [{"letter":"A","text":"Photosynthesis"},{"letter":"B","text":"Chemosynthesis"},{"letter":"C","text":"Radioactivity"},{"letter":"D","text":"Solar power"},{"letter":"E","text":"Hydraulic pressure"}], "correct_answer": "B", "explanation": "The text explicitly names 'chemosynthesis'."},
    {"subject": "English", "topic": "Reading", "question_text": "Why was the discovery of these vents significant for planetary science?", "options": [{"letter":"A","text":"It proved life needs sunlight to exist"},{"letter":"B","text":"It changed our understanding of where life can exist on other planets"},{"letter":"C","text":"It found evidence of alien spacecraft"},{"letter":"D","text":"It showed the ocean is slowly heating up"},{"letter":"E","text":"It discovered new types of minerals for manufacturing"}], "correct_answer": "B", "explanation": "The text states the discovery 'changed our understanding of where life can exist on other planets'."}
 ]},

# P16: The Printing Press (3 Q)
{"id": "t3_p2", "text": "Johannes Gutenberg invented the printing press in the 15th century, a machine that (a) ________ reading from a luxury for the elite to a common habit for the masses. By using movable type, books could be produced much faster and cheaper. This led to a rapid spread of ideas, fueling the Reformation and the Scientific Revolution.",
 "questions": [
    {"subject": "English", "topic": "Vocabulary", "question_text": "Fill in blank (a): '...a machine that (a) ________ reading...'", "options": [{"letter":"A","text":"transformed"},{"letter":"B","text":"prevented"},{"letter":"C","text":"forgot"},{"letter":"D","text":"resticted"},{"letter":"E","text":"ignored"}], "correct_answer": "A", "explanation": "'Transformed' fits the shift from luxury to common habit."},
    {"subject": "English", "topic": "Reading", "question_text": "What was one major historical effect of the printing press?", "options": [{"letter":"A","text":"The decline of universities"},{"letter":"B","text":"The spread of the Black Death"},{"letter":"C","text":"Fueling the Reformation and Scientific Revolution"},{"letter":"D","text":"The invention of the internet"},{"letter":"E","text":"A decrease in literacy rates"}], "correct_answer": "C", "explanation": "The text lists those two specific historical movements."},
    {"subject": "English", "topic": "Reading", "question_text": "What technology did Gutenberg use to speed up book production?", "options": [{"letter":"A","text":"Electric motors"},{"letter":"B","text":"Digital scanners"},{"letter":"C","text":"Movable type"},{"letter":"D","text":"Steam power"},{"letter":"E","text":"Woodblock printing"}], "correct_answer": "C", "explanation": "The text mentions 'By using movable type, books could be produced much faster'."}
 ]},

# P17: Self-Driving Cars (3 Q)
{"id": "t3_p3", "text": "Autonomous vehicles use a combination of LIDAR, cameras, and AI to navigate roads without human (a) ________. Supporters claim this will drastically reduce accidents caused by human error, such as distracted driving. However, legal questions about liability in the event of a crash remain (b) ________.",
 "questions": [
    {"subject": "English", "topic": "Vocabulary", "question_text": "Fill in blank (a): '...without human (a) ________.'", "options": [{"letter":"A","text":"intervention"},{"letter":"B","text":"invention"},{"letter":"C","text":"intention"},{"letter":"D","text":"invasion"},{"letter":"E","text":"inflation"}], "correct_answer": "A", "explanation": "'Intervention' (human action/help) best fits the context."},
    {"subject": "English", "topic": "Vocabulary", "question_text": "Fill in blank (b): '...remain (b) ________.'", "options": [{"letter":"A","text":"settled"},{"letter":"B","text":"unresolved"},{"letter":"C","text":"solved"},{"letter":"D","text":"perfect"},{"letter":"E","text":"simple"}], "correct_answer": "B", "explanation": "'Unresolved' fits the context of legal questions still being debated."},
    {"subject": "English", "topic": "Reading", "question_text": "According to the text, what is one major selling point of self-driving cars?", "options": [{"letter":"A","text":"They are faster than human drivers"},{"letter":"B","text":"Reduction in accidents caused by human error"},{"letter":"C","text":"They do not require any fuel"},{"letter":"D","text":"They are cheaper to buy than regular cars"},{"letter":"E","text":"They can fly over traffic"}], "correct_answer": "B", "explanation": "Supporters claim they 'reduce accidents caused by human error'."}
 ]},

# P18: The Library of Alexandria (3 Q)
{"id": "t3_p4", "text": "The Great Library of Alexandria in Egypt was once the largest collection of knowledge in the ancient world. It is estimated that it (a) ________ hundreds of thousands of papyrus scrolls. The library's destruction is considered a tragic loss for history, as many works of poetry, science, and philosophy burned to ash.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): 'It is estimated that it (a) ________ hundreds of thousands...'", "options": [{"letter":"A","text":"house"},{"letter":"B","text":"housing"},{"letter":"C","text":"housed"},{"letter":"D","text":"has housed"},{"letter":"E","text":"houses"}], "correct_answer": "C", "explanation": "Historical past tense 'housed' is needed."},
    {"subject": "English", "topic": "Reading", "question_text": "Why is the library's destruction considered a tragic loss?", "options": [{"letter":"A","text":"Because the building was made of gold"},{"letter":"B","text":"Because it contained millions of modern books"},{"letter":"C","text":"Because many unique ancient works were lost"},{"letter":"D","text":"Because it caused a war"},{"letter":"E","text":"Because it was the only library in Egypt"}], "correct_answer": "C", "explanation": "The text says 'many works... burned to ash', losing historical knowledge."},
    {"subject": "English", "topic": "Reading", "question_text": "What material were the library's 'books' made of?", "options": [{"letter":"A","text":"Skins"},{"letter":"B","text":"Papyrus scrolls"},{"letter":"C","text":"Clay tablets"},{"letter":"D","text":"Paper made of wood"},{"letter":"E","text":"The text doesn't say"}], "correct_answer": "B", "explanation": "The text mentions 'papyrus scrolls'."}
 ]},

# P19: Internet of Things (3 Q)
{"id": "t3_p5", "text": "The Internet of Things (IoT) refers to the billion of physical devices around the world that are now connected to the internet. From smart fridges to industrial sensors, these devices (a) ________ and share data constantly. While this brings convenience, it also creates massive security vulnerabilities for personal privacy.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): '...these devices (a) ________ and share data...'", "options": [{"letter":"A","text":"collect"},{"letter":"B","text":"collects"},{"letter":"C","text":"collected"},{"letter":"D","text":"collecting"},{"letter":"E","text":"has collected"}], "correct_answer": "A", "explanation": "Plural subject 'devices' takes plural verb 'collect'."},
    {"subject": "English", "topic": "Reading", "question_text": "What is one concern associated with IoT according to the text?", "options": [{"letter":"A","text":"High electricity cost"},{"letter":"B","text":"Security vulnerabilities for privacy"},{"letter":"C","text":"Devices becoming smarter than humans"},{"letter":"D","text":"The internet running out of space"},{"letter":"E","text":"Appliances breaking faster"}], "correct_answer": "B", "explanation": "The text explicitly mentions 'security vulnerabilities for personal privacy'."},
    {"subject": "English", "topic": "Reading", "question_text": "What does 'IoT' stand for in this context?", "options": [{"letter":"A","text":"International Online Technology"},{"letter":"B","text":"Internet of Things"},{"letter":"C","text":"Internal Office Telemetry"},{"letter":"D","text":"Interconnected Operational Task"},{"letter":"E","text":"Integrated Online Tool"}], "correct_answer": "B", "explanation": "It stands for Internet of Things."}
 ]},

# P20: Origami Engineering (2 Q)
{"id": "t3_p6", "text": "Origami is the ancient Japanese art of paper folding. Recently, engineers have (a) ________ its principles to design foldable solar panels for satellites and medical stents for arteries. These objects must be compact during transport and then deploy into a larger, functional shape. (1) This saves space and increases efficiency. (2) Paper is made from wood pulp. (3) The math behind folding is complex and precise.",
 "questions": [
    {"subject": "English", "topic": "Cohesion", "question_text": "Which sentence is irrelevant to the engineering origami topic?", "options": [{"letter":"A","text":"Sentence 1"},{"letter":"B","text":"Sentence 2"},{"letter":"C","text":"Sentence 3"},{"letter":"D","text":"None"},{"letter":"E","text":"Sentence 1 and 3"}], "correct_answer": "B", "explanation": "Sentence 2 is a generic fact about paper, while the others are about origami in engineering."},
    {"subject": "English", "topic": "Reading", "question_text": "Give one example of an engineering application of origami mentioned.", "options": [{"letter":"A","text":"Foldable cars"},{"letter":"B","text":"Solar panels for satellites"},{"letter":"C","text":"Paper airplanes"},{"letter":"D","text":"Foldable skyscrapers"},{"letter":"E","text":"Origami cranes for luck"}], "correct_answer": "B", "explanation": "The text mentions 'foldable solar panels for satellites'."}
 ]},

# P21: Deep Sea Giant Squid (3 Q)
{"id": "t3_p7", "text": "The giant squid was a myth for centuries until the first photograph of a living specimen was (a) ________ in 2004. These elusive creatures live in the 'twilight zone' of the ocean, over 300 meters deep. They have eyes the size of dinner plates to detect the faint bioluminescent light of their prey in the darkness.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): '...specimen was (a) ________ in 2004.'", "options": [{"letter":"A","text":"take"},{"letter":"B","text":"taking"},{"letter":"C","text":"taken"},{"letter":"D","text":"has taken"},{"letter":"E","text":"took"}], "correct_answer": "C", "explanation": "Passive voice 'was taken' for the photograph."},
    {"subject": "English", "topic": "Reading", "question_text": "Why do giant squids have such large eyes according to the text?", "options": [{"letter":"A","text":"To see perfectly in broad daylight"},{"letter":"B","text":"To detect faint bioluminescent light of prey"},{"letter":"C","text":"Because they are very large animals"},{"letter":"D","text":"To scare away predators"},{"letter":"E","text":"To help them swim faster"}], "correct_answer": "B", "explanation": "The text says they use large eyes to 'detect the faint bioluminescent light of their prey'."},
    {"subject": "English", "topic": "Vocabulary", "question_text": "What does the text mean by 'twilight zone'?", "options": [{"letter":"A","text":"A popular TV show"},{"letter":"B","text":"The part of the ocean over 300 meters deep"},{"letter":"C","text":"The time just after sunset"},{"letter":"D","text":"A imaginary world"},{"letter":"E","text":"A specific cave on the ocean floor"}], "correct_answer": "B", "explanation": "The text explains it as the region 'over 300 meters deep'."}
 ]},

# ── TRYOUT 4: PASSAGES 22-28 (20 Q Total) ──────────────────────────────────
# P22: Seaweed Farming (3 Q)
# P23: Rosetta Stone (3 Q)
# P24: Quantum Computing (3 Q)
# P25: Taj Mahal (3 Q)
# P26: Blue Whales (3 Q)
# P27: Skyscrapers (2 Q)
# P28: Mars Rover (3 Q)

# P22: Vertical Seaweed Farming (3 Q)
{"id": "t4_p1", "text": "Seaweed farming is being hailed as a major climate solution. Unlike land crops, seaweed requires no fertilizer, no freshwater, and no land. It (a) ________ CO2 from the water as it grows, helping to reduce ocean acidification. Future applications include biodegradable plastics and low-carbon livestock feed.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): 'It (a) ________ CO2 from the water...'", "options": [{"letter":"A","text":"absorb"},{"letter":"B","text":"absorbs"},{"letter":"C","text":"absorbing"},{"letter":"D","text":"absorbed"},{"letter":"E","text":"to absorb"}], "correct_answer": "B", "explanation": "Singular subject 'It' takes singular verb 'absorbs'."},
    {"subject": "English", "topic": "Reading", "question_text": "What is one benefit of seaweed farming mentioned?", "options": [{"letter":"A","text":"It requires more fertilizer than corn"},{"letter":"B","text":"It helps reduce ocean acidification"},{"letter":"C","text":"It grows only in freshwater"},{"letter":"D","text":"It is currently used to build houses"},{"letter":"E","text":"It increases CO2 levels"}], "correct_answer": "B", "explanation": "The text says it helps 'reduce ocean acidification' by absorbing CO2."},
    {"subject": "English", "topic": "Reading", "question_text": "Identify one future application of seaweed mentioned.", "options": [{"letter":"A","text":"High-speed rocket fuel"},{"letter":"B","text":"Biodegradable plastics"},{"letter":"C","text":"Construction materials for cars"},{"letter":"D","text":"Advanced glass manufacturing"},{"letter":"E","text":"Artificial silk production"}], "correct_answer": "B", "explanation": "The text lists 'biodegradable plastics' as a future application."}
 ]},

# P23: The Rosetta Stone (3 Q)
{"id": "t4_p2", "text": "Discovered in 1799, the Rosetta Stone was the key to unlocking Egyptian hieroglyphs. It contains the same decree written in three different scripts: Hieroglyphic, Demotic, and Ancient Greek. Because scholars (a) ________ read Ancient Greek, they were able to use it as a bridge to translate the other two scripts for the first time.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): 'Because scholars (a) ________ read Ancient Greek...'", "options": [{"letter":"A","text":"can"},{"letter":"B","text":"could"},{"letter":"C","text":"must"},{"letter":"D","text":"should"},{"letter":"E","text":"will"}], "correct_answer": "B", "explanation": "'Could' is the past ability of 'can'."},
    {"subject": "English", "topic": "Reading", "question_text": "Why was the Rosetta Stone important for historians?", "options": [{"letter":"A","text":"It was made of rare gold"},{"letter":"B","text":"It allowed the translation of Egyptian hieroglyphs"},{"letter":"C","text":"It contained a map to a hidden pyramid"},{"letter":"D","text":"It proved the Greeks conquered Egypt"},{"letter":"E","text":"It was the first stone ever found"}], "correct_answer": "B", "explanation": "The text says it was 'the key to unlocking Egyptian hieroglyphs'."},
    {"subject": "English", "topic": "Reading", "question_text": "How many different scripts were on the Rosetta Stone?", "options": [{"letter":"A","text":"One"},{"letter":"B","text":"Two"},{"letter":"C","text":"Three"},{"letter":"D","text":"Four"},{"letter":"E","text":"Five"}], "correct_answer": "C", "explanation": "The text names three: Hieroglyphic, Demotic, and Ancient Greek."}
 ]},

# P24: Quantum Computing (3 Q)
{"id": "t4_p3", "text": "Traditional computers use bits (0 or 1), but quantum computers use 'qubits'. Due to a phenomenon called superposition, a qubit can exist in multiple states at once. This (a) ________ quantum computers to solve specific complex problems — like drug discovered or breaking encryption — millions of times faster than today's most powerful supercomputers.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): 'This (a) ________ quantum computers to solve...'", "options": [{"letter":"A","text":"enable"},{"letter":"B","text":"enables"},{"letter":"C","text":"enabling"},{"letter":"D","text":"enabled"},{"letter":"E","text":"to enable"}], "correct_answer": "B", "explanation": "Singular subject 'This' (referring to superposition) takes singular verb 'enables'."},
    {"subject": "English", "topic": "Reading", "question_text": "In what way is a 'qubit' different from a standard 'bit'?", "options": [{"letter":"A","text":"It can only be 1"},{"letter":"B","text":"It can exist in multiple states at once"},{"letter":"C","text":"It is made of light instead of silicon"},{"letter":"D","text":"It is much larger than a bit"},{"letter":"E","text":"It does not use electricity"}], "correct_answer": "B", "explanation": "The text states 'a qubit can exist in multiple states at once.'"},
    {"subject": "English", "topic": "Reading", "question_text": "Which complex tasks could quantum computers potentially solve faster?", "options": [{"letter":"A","text":"Playing high-def video games"},{"letter":"B","text":"Word processing and spreadsheet calculation"},{"letter":"C","text":"Drug discovery and breaking encryption"},{"letter":"D","text":"Designing traditional circuit boards"},{"letter":"E","text":"Social media management"}], "correct_answer": "C", "explanation": "The text identifies 'drug discovery or breaking encryption' as potential fields."}
 ]},

# P25: The Taj Mahal (3 Q)
{"id": "t4_p4", "text": "The Taj Mahal in India was built by Emperor Shah Jahan in memory of his beloved wife, Mumtaz Mahal. Completed in 1653, the ivory-white marble mausoleum (a) ________ a masterpiece of Mughal architecture. Today, however, industrial pollution is causing the white marble to turn yellow, prompting strict environmental regulations in the surrounding area.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): '...mausoleum (a) ________ a masterpiece...'", "options": [{"letter":"A","text":"is considered"},{"letter":"B","text":"considers"},{"letter":"C","text":"considering"},{"letter":"D","text":"has considered"},{"letter":"E","text":"was considering"}], "correct_answer": "A", "explanation": "Passive voice 'is considered' for a general opinion."},
    {"subject": "English", "topic": "Reading", "question_text": "What is currently damaging the Taj Mahal according to the text?", "options": [{"letter":"A","text":"Floods from the nearby river"},{"letter":"B","text":"Earthquakes"},{"letter":"C","text":"Industrial pollution"},{"letter":"D","text":"The sheer number of tourists"},{"letter":"E","text":"Insects eating the marble"}], "correct_answer": "C", "explanation": "The text says 'industrial pollution is causing the white marble to turn yellow'."},
    {"subject": "English", "topic": "Reading", "question_text": "When was the Taj Mahal completed?", "options": [{"letter":"A","text":"1947"},{"letter":"B","text":"1653"},{"letter":"C","text":"1789"},{"letter":"D","text":"1452"},{"letter":"E","text":"1210"}], "correct_answer": "B", "explanation": "The text states it was 'Completed in 1653'."}
 ]},

# P26: Blue Whales (3 Q)
{"id": "t4_p5", "text": "The blue whale is the largest animal ever known to have existed. Even though it is a mammal, it lives its entire life in the ocean. Its heart is the size of a bumper car, and its tongue alone (a) ________ as much as an entire elephant. These giants feed almost exclusively on tiny shrimp-like creatures called krill, consuming up to 4 tons per day.",
 "questions": [
    {"subject": "English", "topic": "Grammar", "question_text": "Fill in blank (a): '...its tongue alone (a) ________ as much as...'", "options": [{"letter":"A","text":"weigh"},{"letter":"B","text":"weighs"},{"letter":"C","text":"weighing"},{"letter":"D","text":"weighed"},{"letter":"E","text":"to weigh"}], "correct_answer": "B", "explanation": "Singular subject 'tongue' takes singular verb 'weighs'."},
    {"subject": "English", "topic": "Reading", "question_text": "What is the primary food of the blue whale?", "options": [{"letter":"A","text":"Large fish"},{"letter":"B","text":"Krill"},{"letter":"C","text":"Seaweed"},{"letter":"D","text":"Plankton only"},{"letter":"E","text":"Seal pups"}], "correct_answer": "B", "explanation": "The text states they feed 'almost exclusively on... krill'."},
    {"subject": "English", "topic": "Vocabulary", "question_text": "The word 'exclusively' in the text means...", "options": [{"letter":"A","text":"mostly"},{"letter":"B","text":"rarely"},{"letter":"C","text":"only"},{"letter":"D","text":"secretly"},{"letter":"E","text":"carefully"}], "correct_answer": "C", "explanation": "Exclusively means only or solely."}
 ]},

# P27: Skyscrapers and Wind (2 Q)
{"id": "t4_p6", "text": "Designing a skyscraper requires managing powerful wind forces. (1) As height increases, wind speed and pressure grow exponentially. (2) Engineers use 'tuned mass dampers' — huge weights that swing in the opposite direction of the building's sway. (3) Concrete is a common building material. (4) Without these dampers, the top floors of high-rises would move enough to cause motion sickness for occupants.",
 "questions": [
    {"subject": "English", "topic": "Cohesion", "question_text": "Which sentence is irrelevant to the engineering/wind topic?", "options": [{"letter":"A","text":"Sentence 1"},{"letter":"B","text":"Sentence 2"},{"letter":"C","text":"Sentence 3"},{"letter":"D","text":"Sentence 4"},{"letter":"E","text":"None"}], "correct_answer": "C", "explanation": "Sentence 3 is a generic fact about concrete, while the others specifically discuss wind/sway engineering."},
    {"subject": "English", "topic": "Reading", "question_text": "What is the purpose of a 'tuned mass damper'?", "options": [{"letter":"A","text":"To make the building taller"},{"letter":"B","text":"To act as a water reservoir"},{"letter":"C","text":"To counteract the building's sway caused by wind"},{"letter":"D","text":"To hold the elevator cables"},{"letter":"E","text":"To generate electricity for the lobby"}], "correct_answer": "C", "explanation": "The text says they swing 'in the opposite direction of the building's sway'."}
 ]},

# P28: The Mars Perseverance Rover (3 Q)
{"id": "t4_p7", "text": "In February 2021, NASA's Perseverance rover landed in Jezero Crater on Mars. Its mission is to (a) ________ for signs of ancient microbial life and collect rock samples. The rover also carries a small helicopter called Ingenuity, which became the first aircraft to achieve powered flight on another planet. This mission marks a critical step toward future human exploration of the Red Planet.",
 "questions": [
    {"subject": "English", "topic": "Vocabulary", "question_text": "Fill in blank (a): 'Its mission is to (a) ________ for signs...'", "options": [{"letter":"A","text":"search"},{"letter":"B","text":"lost"},{"letter":"C","text":"ignore"},{"letter":"D","text":"hide"},{"letter":"E","text":"destroy"}], "correct_answer": "A", "explanation": "'Search' for signs of life is the logical mission goal."},
    {"subject": "English", "topic": "Reading", "question_text": "What is 'Ingenuity' according to the text?", "options": [{"letter":"A","text":"The name of the crater"},{"letter":"B","text":"A large drilling machine"},{"letter":"C","text":"A small helicopter carried by the rover"},{"letter":"D","text":"A type of Martian rock"},{"letter":"E","text":"A fuel source for the rover"}], "correct_answer": "C", "explanation": "The text defines Ingenuity as 'a small helicopter called Ingenuity'."},
    {"subject": "English", "topic": "Reading", "question_text": "What was the significance of the 'Ingenuity' flight?", "options": [{"letter":"A","text":"It was the first flight on Earth"},{"letter":"B","text":"It broke the speed of sound on Mars"},{"letter":"C","text":"It was the first powered flight on another planet"},{"letter":"D","text":"It discovered water in Jezero Crater"},{"letter":"E","text":"It carried the first human to Mars"}], "correct_answer": "C", "explanation": "The text states it 'became the first aircraft to achieve powered flight on another planet'."}
 ]},

]
