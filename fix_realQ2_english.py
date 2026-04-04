import json

passages_data = [
    {
        "id": "passage_q2_01",
        "title": "AI in Healthcare",
        "text": "Artificial intelligence (AI) is rapidly transforming the healthcare industry, promising more accurate diagnoses and personalized treatments. Machine learning algorithms can now analyze medical images, such as X-rays and MRI scans, with a level of precision that often matches or even exceeds human experts. (a) ________, these systems can detect early signs of diseases like cancer before they become visible to the naked eye.\n\nDespite these advancements, experts warn that AI should not replace doctors but rather serve as a powerful tool to assist them. The human element, including empathy, ethical considerations, and complex decision-making, remains irreplaceable in patient care.\n\nWhile the integration of AI in medicine holds great promise, it also raises concerns about data privacy. Training these algorithms requires massive amounts of patient data, sparking debates about consent and the security of sensitive medical records.",
        "questions": [
            {
                "topic": "Reading Comprehension",
                "question_text": "What is the primary theme of the passage?",
                "options": [
                    {"letter": "A", "text": "The replacement of doctors by AI"},
                    {"letter": "B", "text": "The benefits and challenges of AI in healthcare"},
                    {"letter": "C", "text": "The history of medical imaging technology"},
                    {"letter": "D", "text": "Data privacy laws in hospitals"},
                    {"letter": "E", "text": "The cost of implementing new healthcare technologies"}
                ],
                "correct_answer": "B",
                "explanation": "The passage discusses both the positive impacts of AI (accurate diagnoses) and the challenges (data privacy, ethical concerns), making B the correct answer."
            },
            {
                "topic": "Vocabulary in Context",
                "question_text": "Fill in the blank space (a) ________ with the most appropriate transition.",
                "options": [
                    {"letter": "A", "text": "However"},
                    {"letter": "B", "text": "In contrast"},
                    {"letter": "C", "text": "Furthermore"},
                    {"letter": "D", "text": "Nevertheless"},
                    {"letter": "E", "text": "Otherwise"}
                ],
                "correct_answer": "C",
                "explanation": "'Furthermore' is used to add to the point already made. Here it adds an extra benefit of AI analyzing medical images."
            },
            {
                "topic": "Reading Comprehension",
                "question_text": "According to the passage, why is the human element in medicine irreplaceable?",
                "options": [
                    {"letter": "A", "text": "Because patients refuse to be diagnosed by machines"},
                    {"letter": "B", "text": "Because AI cannot analyze MRI scans efficiently"},
                    {"letter": "C", "text": "Because medical imaging requires manual calibration"},
                    {"letter": "D", "text": "Because it involves empathy and complex decision-making"},
                    {"letter": "E", "text": "Because doctors must manually input patient data"}
                ],
                "correct_answer": "D",
                "explanation": "The second paragraph explicitly states that 'The human element, including empathy, ethical considerations, and complex decision-making, remains irreplaceable...'"
            },
            {
                "topic": "Paragraph Cohesion and Structure",
                "question_text": "The relationship between paragraph 1 and paragraph 3 is best described as:",
                "options": [
                    {"letter": "A", "text": "Paragraph 3 completely contradicts paragraph 1"},
                    {"letter": "B", "text": "Paragraph 3 outlines a negative implication of the technology introduced in paragraph 1"},
                    {"letter": "C", "text": "Paragraph 3 summarizes the findings of paragraph 1"},
                    {"letter": "D", "text": "Paragraph 3 provides specific examples of the success mentioned in paragraph 1"},
                    {"letter": "E", "text": "Paragraph 3 is irrelevant to paragraph 1"}
                ],
                "correct_answer": "B",
                "explanation": "Paragraph 1 introduces the benefits of AI. Paragraph 3 discusses the data privacy concerns that arise from these technologies, acting as a caveat or implication."
            }
        ]
    },
    {
        "id": "passage_q2_02",
        "title": "Deep Sea Exploration",
        "text": "The deep ocean remains one of the most mysterious and unexplored frontiers on Earth. Due to extreme pressure, freezing temperatures, and absolute darkness, human exploration of the abyssal zones has been highly restricted. However, recent developments in autonomous underwater vehicles (AUVs) have allowed marine biologists to study these harsh environments safely.\n\nThese robotic submersibles have uncovered entirely new ecosystems near hydrothermal vents. Here, completely independent of sunlight, life thrives on chemical energy through a process known as chemosynthesis. Giant tube worms and blind crabs are among the bizarre species that call these deep-sea chimneys home.\n\nDiscovering these ecosystems has profound implications for biology. It forces scientists to reconsider the conditions necessary for life. If organisms can flourish in such extreme terrestrial environments, the likelihood of finding extraterrestrial life on icy moons, like Jupiter's Europa, dramatically increases.",
        "questions": [
            {
                "topic": "Reading Comprehension",
                "question_text": "What enables life to exist near hydrothermal vents?",
                "options": [
                    {"letter": "A", "text": "Photosynthesis from filtered sunlight"},
                    {"letter": "B", "text": "Geothermal heat trapped by ocean currents"},
                    {"letter": "C", "text": "Chemical energy via chemosynthesis"},
                    {"letter": "D", "text": "Nutrients dropped by surface-dwelling animals"},
                    {"letter": "E", "text": "Oxygen pockets trapped in underwater caves"}
                ],
                "correct_answer": "C",
                "explanation": "Paragraph 2 explicitly states that life thrives there 'on chemical energy through a process known as chemosynthesis.'"
            },
            {
                "topic": "Grammar and Tenses",
                "question_text": "In the sentence 'human exploration of the abyssal zones has been highly restricted', the verb tense used is:",
                "options": [
                    {"letter": "A", "text": "Simple Past"},
                    {"letter": "B", "text": "Present Continuous"},
                    {"letter": "C", "text": "Present Perfect Passive"},
                    {"letter": "D", "text": "Past Perfect Passive"},
                    {"letter": "E", "text": "Future Perfect"}
                ],
                "correct_answer": "C",
                "explanation": "'has been restricted' comprises 'has' (present tense auxiliary), 'been' (past participle of be), and 'restricted' (past participle), forming the Present Perfect in the passive voice."
            },
            {
                "topic": "Reading Comprehension",
                "question_text": "Why does deep-sea exploration increase the likelihood of finding extraterrestrial life?",
                "options": [
                    {"letter": "A", "text": "Because AUV technology is also used in space exploration"},
                    {"letter": "B", "text": "Because it proves that life can exist without sunlight in extreme environments"},
                    {"letter": "C", "text": "Because deep-sea marine life originated from meteorites"},
                    {"letter": "D", "text": "Because oceans on Earth and Europa share the exact same chemical makeup"},
                    {"letter": "E", "text": "Because tube worms can survive in the vacuum of space"}
                ],
                "correct_answer": "B",
                "explanation": "Paragraph 3 notes that if organisms can flourish without sunlight in extreme conditions, it increases the likelihood of extraterrestrial life on icy moons."
            }
        ]
    },
    {
        "id": "passage_q2_03",
        "title": "The Psychology of Habits",
        "text": "Habits form the invisible architecture of daily life. Research indicates that approximately 40 percent of our daily actions are automatically driven by habit rather than conscious decision-making. The neurological loop at the core of all habits consists of three parts: a cue, a routine, and a reward.\n\nUnderstanding this loop is key to breaking bad habits. Merely relying on willpower is rarely effective long-term. Instead, psychologists suggest identifying the underlying cue that triggers the behavior and the reward it provides. By keeping the cue and reward the same but altering the routine, individuals can successfully rewire their behavior.\n\nFor instance, if stress (the cue) leads to unhealthy snacking (the routine) to gain temporary relief (the reward), one could substitute the snacking with an alternative stress-relieving activity, such as deep breathing or walking. Eventually, this new routine overrides the old habit.",
        "questions": [
            {
                "topic": "Reading Comprehension",
                "question_text": "Which of the following is NOT a component of the habit loop mentioned in the text?",
                "options": [
                    {"letter": "A", "text": "A cue"},
                    {"letter": "B", "text": "A routine"},
                    {"letter": "C", "text": "A reward"},
                    {"letter": "D", "text": "A punishment"},
                    {"letter": "E", "text": "These are all components"}
                ],
                "correct_answer": "D",
                "explanation": "The text lists three parts: a cue, a routine, and a reward. Punishment is not mentioned as part of the loop."
            },
            {
                "topic": "Reading Comprehension",
                "question_text": "According to psychologists referenced in the text, what is the best way to change a bad habit?",
                "options": [
                    {"letter": "A", "text": "Avoid all cues entirely"},
                    {"letter": "B", "text": "Rely heavily on strong willpower"},
                    {"letter": "C", "text": "Alter the reward while keeping the routine consistent"},
                    {"letter": "D", "text": "Substitute the routine while maintaining the same cue and reward"},
                    {"letter": "E", "text": "Suppress the desire for the reward"}
                ],
                "correct_answer": "D",
                "explanation": "The text advises 'keeping the cue and reward the same but altering the routine'."
            },
            {
                "topic": "Vocabulary in Context",
                "question_text": "The word 'overrides' in the last sentence is closest in meaning to:",
                "options": [
                    {"letter": "A", "text": "Supports"},
                    {"letter": "B", "text": "Replaces"},
                    {"letter": "C", "text": "Complicates"},
                    {"letter": "D", "text": "Highlights"},
                    {"letter": "E", "text": "Ignores"}
                ],
                "correct_answer": "B",
                "explanation": "In this context, when a new routine 'overrides' the old one, it takes its place or supersedes it, making 'Replaces' the best fit."
            }
        ]
    },
    {
        "id": "passage_q2_04",
        "title": "Renewable Energy Economics",
        "text": "For decades, the high cost of implementation hindered the widespread adoption of renewable energy sources such as solar and wind power. However, economies of scale and tremendous advancements in engineering have fundamentally shifted the global energy landscape. Over the last ten years, the cost of generating electricity from solar panels has plummeted by nearly 80 percent.\n\nToday, in many parts of the world, building new renewable energy plants is actually cheaper than maintaining existing coal or gas-fired power stations. This economic tipping point is forcing utility companies to reevaluate their long-term infrastructure investments. Investors are increasingly diverting capital away from fossil fuels.\n\nDespite this momentum, transitioning to a fully renewable grid poses logistical hurdles. The intermittent nature of wind and solar requires robust energy storage solutions, such as massive lithium-ion battery farms, to ensure consistent power supply during calm or cloudy days.",
        "questions": [
            {
                "topic": "Reading Comprehension",
                "question_text": "What has been the primary driver in reducing the cost of solar energy over the last decade?",
                "options": [
                    {"letter": "A", "text": "Strict environmental regulations"},
                    {"letter": "B", "text": "Subsidies provided by international banks"},
                    {"letter": "C", "text": "Economies of scale and advancements in engineering"},
                    {"letter": "D", "text": "The depletion of global coal reserves"},
                    {"letter": "E", "text": "Decreased global demand for electricity"}
                ],
                "correct_answer": "C",
                "explanation": "Paragraph 1 states that 'economies of scale and tremendous advancements in engineering have fundamentally shifted the global energy landscape'."
            },
            {
                "topic": "Paragraph Cohesion and Structure",
                "question_text": "The phrase 'This economic tipping point' in paragraph 2 refers directly to:",
                "options": [
                    {"letter": "A", "text": "The 80 percent drop in solar energy costs"},
                    {"letter": "B", "text": "The fact that new renewables are now cheaper than maintaining existing fossil fuel plants"},
                    {"letter": "C", "text": "The decrease in capital investments"},
                    {"letter": "D", "text": "The logistical hurdles of energy storage"},
                    {"letter": "E", "text": "The rising prices of natural gas"}
                ],
                "correct_answer": "B",
                "explanation": "The immediately preceding sentence explains that building new renewable plants is cheaper than maintaining old fossil fuel plants, identifying the specific 'tipping point'."
            },
            {
                "topic": "Reading Comprehension",
                "question_text": "According to the passage, why are robust energy storage solutions necessary?",
                "options": [
                    {"letter": "A", "text": "To increase the efficiency of coal-fired stations"},
                    {"letter": "B", "text": "To reduce the physical footprint of solar panels"},
                    {"letter": "C", "text": "To power electric utility vehicles"},
                    {"letter": "D", "text": "To compensate for the intermittent nature of solar and wind power"},
                    {"letter": "E", "text": "To lower the manufacturing cost of lithium-ion batteries"}
                ],
                "correct_answer": "D",
                "explanation": "The text states that energy storage is required 'to ensure consistent power supply during calm or cloudy days' due to the 'intermittent nature of wind and solar'."
            }
        ]
    },
    {
        "id": "passage_q2_05",
        "title": "Ancient Roman Architecture",
        "text": "The durability of Ancient Roman architecture is a source of fascination for modern engineers. While many modern concrete structures show signs of significant degradation within a century, iconic Roman buildings like the Pantheon have stood intact for over two millennia. The secret to this longevity lies primarily in the unique recipe of Roman concrete, known as opus caementicium.\n\nUnlike modern concrete, which often relies on Portland cement, the Romans mixed volcanic ash, quicklime, and seawater. This mixture induced a chemical reaction called a pozzolanic reaction. When microscopic cracks formed in the material, rainwater seeping in would react with the unreacted lime to create new crystals, effectively self-healing the fractures.\n\nUnderstanding and replicating these ancient techniques holds immense potential for the future. By incorporating similar self-healing properties into modern construction materials, the building industry could drastically reduce maintenance costs and lower the environmental impact of frequent concrete replacement.",
        "questions": [
            {
                "topic": "Reading Comprehension",
                "question_text": "What is the main topic of the passage?",
                "options": [
                    {"letter": "A", "text": "The decline of the Roman Empire"},
                    {"letter": "B", "text": "The environmental impact of modern construction"},
                    {"letter": "C", "text": "The history of the Pantheon in Rome"},
                    {"letter": "D", "text": "The composition and durability of Roman concrete"},
                    {"letter": "E", "text": "A comparison between Greek and Roman architecture"}
                ],
                "correct_answer": "D",
                "explanation": "The passage primarily discusses how the unique recipe of Roman concrete allows structures to last for millennia."
            },
            {
                "topic": "Vocabulary in Context",
                "question_text": "Based on the passage, what does the term 'self-healing' imply regarding Roman concrete?",
                "options": [
                    {"letter": "A", "text": "It requires frequent manual repair by engineers"},
                    {"letter": "B", "text": "It actively repels rainwater entirely"},
                    {"letter": "C", "text": "It can naturally patch its own microscopic fractures over time"},
                    {"letter": "D", "text": "It becomes softer when exposed to the elements"},
                    {"letter": "E", "text": "It purifies seawater as it passes through the walls"}
                ],
                "correct_answer": "C",
                "explanation": "The text explains that returning rainwater reacts with lime to 'create new crystals, effectively self-healing the fractures.'"
            },
            {
                "topic": "Grammar and Tenses",
                "question_text": "In the sentence 'While many modern concrete structures show signs of significant degradation within a century, iconic Roman buildings like the Pantheon have stood intact for over two millennia', what purpose does the word 'While' serve?",
                "options": [
                    {"letter": "A", "text": "To indicate a sequence of events"},
                    {"letter": "B", "text": "To introduce a direct contradiction or contrast between two subjects"},
                    {"letter": "C", "text": "To show cause and effect"},
                    {"letter": "D", "text": "To illustrate a condition that must be met"},
                    {"letter": "E", "text": "To define an exact period of time"}
                ],
                "correct_answer": "B",
                "explanation": "'While' acts as a subordinating conjunction introducing a contrast between the short lifespan of modern concrete and the extreme longevity of Roman buildings."
            },
            {
                "topic": "Reading Comprehension",
                "question_text": "How could applying Roman concrete techniques benefit modern society?",
                "options": [
                    {"letter": "A", "text": "By increasing the speed of construction projects"},
                    {"letter": "B", "text": "By completely eliminating the need for architectural design"},
                    {"letter": "C", "text": "By reducing maintenance costs and environmental impact"},
                    {"letter": "D", "text": "By making buildings highly resistant to severe earthquakes"},
                    {"letter": "E", "text": "By lowering the price of volcanic ash"}
                ],
                "correct_answer": "C",
                "explanation": "Paragraph 3 explicitly states that using these techniques 'could drastically reduce maintenance costs and lower the environmental impact'."
            }
        ]
    },
    {
        "id": "passage_q2_06",
        "title": "Space Debris Problem",
        "text": "Since the launch of Sputnik in 1957, humanity has sent thousands of satellites into orbit. While these technological marvels have revolutionized global communication and navigation, they have also created a hazardous byproduct: space debris. Millions of fragments, ranging from defunct satellites to tiny paint flecks, currently circle the Earth at immense speeds.\n\nThe danger of this orbital litter is severe. Because objects in low Earth orbit travel at roughly 17,500 miles per hour, even a collision with a bolt size piece of debris can cause catastrophic damage to active spacecraft. This risk is compounded by the Kessler Syndrome, a theoretical scenario where a single collision creates a cascade of debris, triggering further collisions until orbit becomes unusable.\n\nSeveral space agencies are currently designing initiatives to clean up the orbit. Proposed solutions include deploying large magnetic nets, utilizing robotic arms to capture dead satellites, and using lasers to push fragments into the atmosphere where they will safely burn up. Addressing the space debris issue is crucial for the future viability of space exploration.",
        "questions": [
            {
                "topic": "Reading Comprehension",
                "question_text": "What is the primary danger associated with space debris according to the text?",
                "options": [
                    {"letter": "A", "text": "It blocks communication signals from active satellites"},
                    {"letter": "B", "text": "It travels at high speeds and can cause catastrophic damage"},
                    {"letter": "C", "text": "It frequently re-enters the atmosphere, endangering populated areas"},
                    {"letter": "D", "text": "It increases the cost of launching new satellites"},
                    {"letter": "E", "text": "It reflects sunlight, altering Earth's climate"}
                ],
                "correct_answer": "B",
                "explanation": "Paragraph 2 notes that because debris travels 'at roughly 17,500 miles per hour, even a collision with a bolt size piece... can cause catastrophic damage'."
            },
            {
                "topic": "Vocabulary in Context",
                "question_text": "What does the term 'Kessler Syndrome' refer to?",
                "options": [
                    {"letter": "A", "text": "A physical illness experienced by astronauts in zero gravity"},
                    {"letter": "B", "text": "The malfunction of navigation equipment caused by solar radiation"},
                    {"letter": "C", "text": "A cascade of collisions where one impact creates debris that triggers further impacts"},
                    {"letter": "D", "text": "The process of a satellite safely burning up in the atmosphere"},
                    {"letter": "E", "text": "The political failure to implement space cleanup initiatives"}
                ],
                "correct_answer": "C",
                "explanation": "Paragraph 2 defines the Kessler Syndrome as 'a cascade of debris, triggering further collisions until orbit becomes unusable'."
            },
            {
                "topic": "Reading Comprehension",
                "question_text": "Which of the following is NOT mentioned as a proposed solution to clean up space debris?",
                "options": [
                    {"letter": "A", "text": "Deploying large magnetic nets"},
                    {"letter": "B", "text": "Using robotic arms to capture dead satellites"},
                    {"letter": "C", "text": "Launching black hole simulators to absorb fragments"},
                    {"letter": "D", "text": "Using lasers to push fragments into the atmosphere"},
                    {"letter": "E", "text": "All of these are mentioned"}
                ],
                "correct_answer": "C",
                "explanation": "Paragraph 3 lists magnetic nets, robotic arms, and lasers. Black hole simulators are not mentioned."
            }
        ]
    }
]

def update_realQ2():
    with open('realQ2.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Remove old English questions
    filtered = [q for q in data if q.get('subject') != 'English']
    
    # Generate new English section flat
    english_questions = []
    eng_id = 1
    for p in passages_data:
        passage_id = p["id"]
        passage_text = p["text"]
        for q in p["questions"]:
            q_obj = {
                "id": f"english_{eng_id:02d}",
                "passage_id": passage_id,
                "passage": passage_text,
                "subject": "English",
                "topic": q["topic"],
                "question_text": q["question_text"],
                "options": q["options"],
                "correct_answer": q["correct_answer"],
                "explanation": q["explanation"]
            }
            english_questions.append(q_obj)
            eng_id += 1
            
    # Combine back
    # English questions go after the first 20 Basic Math questions
    final_data = filtered[:20] + english_questions + filtered[20:]
    
    with open('realQ2.json', 'w', encoding='utf-8') as f:
        json.dump(final_data, f, indent=2, ensure_ascii=False)
        
    print("realQ2.json updated successfully with grouped passages.")

if __name__ == '__main__':
    update_realQ2()
