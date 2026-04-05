"""
English passage pool for practice tryout generation.
Each entry: passage_text (3 paragraphs separated by double newline), questions list.
"""

POOL = [

# ── PASSAGE 01 ── AI in Healthcare ──────────────────────────────────────────
{
"passage_id": "eng_pool_01",
"passage_text": (
    "Artificial intelligence (AI) is increasingly being integrated into modern healthcare. "
    "Researchers now use AI algorithms to analyze medical imaging data, enabling faster and more accurate diagnoses of conditions such as cancer and cardiovascular disease. "
    "Pharmaceutical companies are also leveraging AI to (a) ________ the drug discovery process, significantly reducing the time needed to bring new treatments to market.\n\n"
    "One celebrated application is early cancer detection, where AI systems trained on thousands of scans have identified tumors that human radiologists occasionally miss. "
    "Predictive analytics can also forecast which patients are at high risk of hospital readmission, allowing doctors to intervene before problems escalate. "
    "These capabilities are fundamentally transforming clinical decision-making and patient care.\n\n"
    "Despite its promise, AI in healthcare carries significant risks. Many training datasets do not represent diverse populations, producing biased predictions that can harm underrepresented groups. "
    "Accountability also remains unresolved: when an AI system errs critically, it is unclear who bears legal responsibility. "
    "Experts therefore argue that human oversight must remain central to any AI-assisted medical decision."
),
"questions": [
    {
        "id": "ep01_q1", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "Which of the following is the best title for the text?",
        "options": [
            {"letter": "A", "text": "How AI Is Replacing Human Doctors"},
            {"letter": "B", "text": "The Promise and Risks of AI in Healthcare"},
            {"letter": "C", "text": "A History of Medical Imaging Technology"},
            {"letter": "D", "text": "Why Drug Discovery Takes So Long"},
            {"letter": "E", "text": "Legal Challenges Facing Modern Medicine"},
        ],
        "correct_answer": "B",
        "explanation": "The passage covers both AI's benefits (paragraphs 1–2) and its risks (paragraph 3), making 'Promise and Risks' the only title broad enough to represent all three paragraphs.",
    },
    {
        "id": "ep01_q2", "subject": "English", "topic": "Grammar and Tenses",
        "question_text": "Fill in blank (a): 'Pharmaceutical companies are leveraging AI to (a) ________ the drug discovery process...'",
        "options": [
            {"letter": "A", "text": "accelerate"},
            {"letter": "B", "text": "accelerating"},
            {"letter": "C", "text": "accelerated"},
            {"letter": "D", "text": "has accelerated"},
            {"letter": "E", "text": "to accelerate"},
        ],
        "correct_answer": "A",
        "explanation": "The structure 'to (blank) the process' requires the base infinitive form. 'Accelerate' is the correct base form here.",
    },
    {
        "id": "ep01_q3", "subject": "English", "topic": "Paragraph Cohesion and Structure",
        "question_text": "What is the relationship between paragraph 2 and paragraph 3?",
        "options": [
            {"letter": "A", "text": "Paragraph 3 gives additional examples supporting paragraph 2"},
            {"letter": "B", "text": "Paragraph 3 presents the risks that counterbalance the benefits in paragraph 2"},
            {"letter": "C", "text": "Paragraph 3 contradicts every claim made in paragraph 2"},
            {"letter": "D", "text": "Paragraph 3 introduces an entirely unrelated topic"},
            {"letter": "E", "text": "Paragraph 3 is a summary of paragraph 2"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 2 highlights positive applications (early detection, readmission prediction). Paragraph 3 then introduces downsides—bias and accountability gaps—creating a benefit-vs-risk contrast.",
    },
    {
        "id": "ep01_q4", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "What can be inferred from paragraph 1?",
        "options": [
            {"letter": "A", "text": "AI has fully replaced radiologists in all hospitals"},
            {"letter": "B", "text": "AI is applied to both diagnosis and pharmaceutical research"},
            {"letter": "C", "text": "Drug discovery now takes no time due to AI"},
            {"letter": "D", "text": "AI is only useful for cancer treatment"},
            {"letter": "E", "text": "Medical imaging is no longer performed by humans"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 1 explicitly mentions AI in medical imaging (diagnosis) and AI in pharmaceutical drug discovery (research), confirming both applications.",
    },
    {
        "id": "ep01_q5", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "The tone of the passage is best described as...",
        "options": [
            {"letter": "A", "text": "Alarmist"},
            {"letter": "B", "text": "Dismissive"},
            {"letter": "C", "text": "Enthusiastically promotional"},
            {"letter": "D", "text": "Balanced and analytical"},
            {"letter": "E", "text": "Humorous"},
        ],
        "correct_answer": "D",
        "explanation": "The author presents both benefits (paragraphs 1–2) and risks (paragraph 3) in objective, measured language — characteristic of a balanced, analytical tone.",
    },
]
},

# ── PASSAGE 02 ── Coastal Cities & Rising Seas ───────────────────────────────
{
"passage_id": "eng_pool_02",
"passage_text": (
    "Rising sea levels driven by climate change pose an existential threat to major coastal cities worldwide. "
    "Projections indicate that by 2100 roughly 800 million people could live in zones at severe risk of flooding. "
    "Governments and urban planners are therefore working urgently to adapt infrastructure before the situation becomes unmanageable.\n\n"
    "Several cities have (a) ________ innovative strategies to reduce their flood risk. "
    "Rotterdam has built water plazas that serve as public spaces in dry weather and flood reservoirs when needed. "
    "Jakarta is accelerating plans to relocate its national capital to higher inland ground, recognizing that engineering alone cannot save the sinking city. "
    "Meanwhile, elevated highways and reinforced sea walls are being constructed across vulnerable coastlines.\n\n"
    "Critics argue, however, that these engineering responses treat symptoms rather than root causes. "
    "Without aggressive global reductions in greenhouse gas emissions, sea-level rise may eventually overwhelm even the most ambitious flood-control projects. "
    "Experts therefore advocate combining local adaptation with decisive international climate policy — only this dual approach can ensure cities remain livable for future generations."
),
"questions": [
    {
        "id": "ep02_q1", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "The most appropriate title for the passage is...",
        "options": [
            {"letter": "A", "text": "Why Jakarta Is Moving Its Capital"},
            {"letter": "B", "text": "Engineering Solutions to Natural Disasters"},
            {"letter": "C", "text": "Coastal Cities Racing to Adapt to Rising Seas"},
            {"letter": "D", "text": "The Economic Cost of Climate Change"},
            {"letter": "E", "text": "How Rotterdam Builds Flood Barriers"},
        ],
        "correct_answer": "C",
        "explanation": "The passage spans multiple cities' flood responses (paragraph 2) and critiques their limits (paragraph 3), making the broader framing 'Coastal Cities Racing to Adapt' most accurate.",
    },
    {
        "id": "ep02_q2", "subject": "English", "topic": "Grammar and Tenses",
        "question_text": "Fill in blank (a): 'Several cities have (a) ________ innovative strategies to reduce their flood risk.'",
        "options": [
            {"letter": "A", "text": "adopting"},
            {"letter": "B", "text": "adopted"},
            {"letter": "C", "text": "adopt"},
            {"letter": "D", "text": "will adopt"},
            {"letter": "E", "text": "had adopt"},
        ],
        "correct_answer": "B",
        "explanation": "'Have + past participle' forms the present perfect tense. 'Adopted' is the past participle of 'adopt', making 'have adopted' the grammatically correct form.",
    },
    {
        "id": "ep02_q3", "subject": "English", "topic": "Paragraph Cohesion and Structure",
        "question_text": "What is the relationship between paragraph 2 and paragraph 3?",
        "options": [
            {"letter": "A", "text": "Paragraph 3 extends the list of engineering solutions in paragraph 2"},
            {"letter": "B", "text": "Paragraph 3 critiques the solutions in paragraph 2 as insufficient on their own"},
            {"letter": "C", "text": "Paragraph 3 explains why the cities in paragraph 2 were built"},
            {"letter": "D", "text": "Paragraph 3 contradicts the statistics mentioned in paragraph 2"},
            {"letter": "E", "text": "Paragraph 3 introduces flooding problems not mentioned in paragraph 2"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 2 describes adaptation measures (sea walls, relocation). Paragraph 3 then argues these are insufficient without global emission reductions — a critique of the solutions in paragraph 2.",
    },
    {
        "id": "ep02_q4", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "What can be inferred from paragraph 1?",
        "options": [
            {"letter": "A", "text": "Only a few cities are threatened by sea-level rise"},
            {"letter": "B", "text": "The threat of flooding is imminent and widespread"},
            {"letter": "C", "text": "Governments have already solved the flooding problem"},
            {"letter": "D", "text": "800 million people have already been displaced"},
            {"letter": "E", "text": "Climate change affects only inland regions"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 1 states that 800 million people could be at risk by 2100 and that governments are working 'urgently' — both details imply the threat is large-scale and pressing.",
    },
    {
        "id": "ep02_q5", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "The writer's purpose in this passage is most likely to...",
        "options": [
            {"letter": "A", "text": "Criticize engineers for proposing flood barriers"},
            {"letter": "B", "text": "Persuade readers to migrate away from coastal areas"},
            {"letter": "C", "text": "Explain both the adaptation efforts and their limitations"},
            {"letter": "D", "text": "Describe the history of sea walls"},
            {"letter": "E", "text": "Argue that climate change is exaggerated"},
        ],
        "correct_answer": "C",
        "explanation": "The passage describes what cities are doing (paragraph 2) and then explains why those efforts may not be enough (paragraph 3), showing a dual informative-analytical purpose.",
    },
]
},

# ── PASSAGE 03 ── Mental Health & Social Media ───────────────────────────────
{
"passage_id": "eng_pool_03",
"passage_text": (
    "The widespread use of social media platforms has sparked growing concern among psychologists and public health researchers. "
    "Studies increasingly link excessive social media use to elevated rates of anxiety, depression, and loneliness, particularly among teenagers. "
    "While correlation does not confirm causation, the volume and consistency of these findings have prompted serious calls for policy action.\n\n"
    "Platforms themselves have been slow to act, often citing user autonomy and the complexity of moderating vast amounts of content. "
    "However, some companies have introduced features such as screen-time reminders, comment filters, and restrictions on recommending certain content to minors. "
    "Critics argue these measures are superficial and that the core business model — which rewards engagement above all else — remains unchanged.\n\n"
    "Experts propose a multi-pronged response. Parents and schools are encouraged to teach digital literacy, helping young people critically evaluate what they consume online. "
    "Regulators in several countries are exploring legislation that would impose stricter transparency requirements on algorithmic recommendation systems. "
    "The consensus is that protecting mental health in the digital age requires cooperation among individuals, platforms, and governments."
),
"questions": [
    {
        "id": "ep03_q1", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "Which of the following best expresses the main idea of the passage?",
        "options": [
            {"letter": "A", "text": "Social media is the sole cause of teenage depression"},
            {"letter": "B", "text": "Platforms have successfully resolved mental health concerns"},
            {"letter": "C", "text": "Addressing social media's mental health impact requires action from multiple parties"},
            {"letter": "D", "text": "Teenagers should be banned from using all social media"},
            {"letter": "E", "text": "Digital literacy programs are ineffective"},
        ],
        "correct_answer": "C",
        "explanation": "Paragraph 3 explicitly states that protecting mental health 'requires cooperation among individuals, platforms, and governments,' which is the central thesis across all three paragraphs.",
    },
    {
        "id": "ep03_q2", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "What can be inferred from paragraph 2?",
        "options": [
            {"letter": "A", "text": "Social media companies have fully committed to protecting user mental health"},
            {"letter": "B", "text": "The existing platform measures are considered largely inadequate by critics"},
            {"letter": "C", "text": "User autonomy is no longer a concern for platforms"},
            {"letter": "D", "text": "Comment filters have eliminated online harassment"},
            {"letter": "E", "text": "All platforms have updated their business models"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 2 notes that platforms have introduced some features but 'critics argue these measures are superficial' and the core business model is unchanged — implying the measures are seen as inadequate.",
    },
    {
        "id": "ep03_q3", "subject": "English", "topic": "Paragraph Cohesion and Structure",
        "question_text": "The relationship between paragraph 1 and paragraph 2 is best described as...",
        "options": [
            {"letter": "A", "text": "Paragraph 2 provides the cause of the problem identified in paragraph 1"},
            {"letter": "B", "text": "Paragraph 2 describes the industry's partial and criticized response to the concern raised in paragraph 1"},
            {"letter": "C", "text": "Paragraph 2 contradicts the research findings of paragraph 1"},
            {"letter": "D", "text": "Paragraph 2 repeats the same information as paragraph 1"},
            {"letter": "E", "text": "Paragraph 2 introduces an unrelated topic"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 1 establishes the mental health concern. Paragraph 2 then describes what platforms have done in response — but notes that critics find those responses insufficient.",
    },
    {
        "id": "ep03_q4", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "The text is most likely addressed to...",
        "options": [
            {"letter": "A", "text": "Social media software engineers"},
            {"letter": "B", "text": "An informed general audience interested in current social issues"},
            {"letter": "C", "text": "Professional clinical psychologists only"},
            {"letter": "D", "text": "Government regulators exclusively"},
            {"letter": "E", "text": "Teenagers experiencing anxiety"},
        ],
        "correct_answer": "B",
        "explanation": "The passage uses accessible language and covers social, policy, and individual angles — hallmarks of writing aimed at an educated general audience rather than a narrow professional group.",
    },
    {
        "id": "ep03_q5", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "The author's attitude toward social media platforms in paragraph 2 is...",
        "options": [
            {"letter": "A", "text": "Fully supportive"},
            {"letter": "B", "text": "Mildly critical with recognition of some effort"},
            {"letter": "C", "text": "Completely indifferent"},
            {"letter": "D", "text": "Enthusiastically praising"},
            {"letter": "E", "text": "Purely optimistic"},
        ],
        "correct_answer": "B",
        "explanation": "The author acknowledges platforms have introduced some features, but immediately notes these are criticized as superficial — a mildly critical stance that recognizes partial effort.",
    },
]
},

# ── PASSAGE 04 ── The Gig Economy ────────────────────────────────────────────
{
"passage_id": "eng_pool_04",
"passage_text": (
    "The gig economy — characterized by short-term contracts and freelance work rather than permanent employment — has grown dramatically over the past decade. "
    "Platforms such as ride-sharing apps, delivery services, and freelance marketplaces have made it easier than ever to (a) ________ work on a flexible, project-by-project basis. "
    "Today, an estimated 25 percent of workers in many developed countries derive at least part of their income from gig work.\n\n"
    "Proponents argue the gig model offers workers unprecedented flexibility and freedom. Individuals can set their own hours, work from multiple platforms simultaneously, and pursue passion projects alongside income-generating tasks. "
    "For businesses, the model lowers overhead costs and allows rapid scaling of workforce in response to demand fluctuations.\n\n"
    "Critics, however, highlight serious structural problems. Gig workers are typically classified as independent contractors, denying them access to benefits such as health insurance, paid leave, and retirement savings plans. "
    "Income volatility also makes financial planning difficult, particularly for those who rely solely on gig earnings. "
    "Several governments are now debating legislation to reclassify gig workers and mandate (b) ________ protections."
),
"questions": [
    {
        "id": "ep04_q1", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "Which of the following best describes the main topic of the passage?",
        "options": [
            {"letter": "A", "text": "The history of labor unions"},
            {"letter": "B", "text": "The growth, benefits, and problems of the gig economy"},
            {"letter": "C", "text": "How ride-sharing apps work technically"},
            {"letter": "D", "text": "Government policies on employment law"},
            {"letter": "E", "text": "The decline of traditional office jobs"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 1 establishes the gig economy's growth, paragraph 2 covers its benefits, and paragraph 3 addresses its problems — the passage as a whole examines all three dimensions.",
    },
    {
        "id": "ep04_q2", "subject": "English", "topic": "Vocabulary in Context",
        "question_text": "Fill in blank (a): 'Platforms...have made it easier than ever to (a) ________ work on a flexible, project-by-project basis.'",
        "options": [
            {"letter": "A", "text": "secure"},
            {"letter": "B", "text": "secured"},
            {"letter": "C", "text": "securing"},
            {"letter": "D", "text": "secures"},
            {"letter": "E", "text": "have secured"},
        ],
        "correct_answer": "A",
        "explanation": "The phrase 'easier than ever to (blank) work' requires the base infinitive form. 'Secure' (meaning 'to obtain') is the grammatically correct base form here.",
    },
    {
        "id": "ep04_q3", "subject": "English", "topic": "Paragraph Cohesion and Structure",
        "question_text": "What is the relationship between paragraph 2 and paragraph 3?",
        "options": [
            {"letter": "A", "text": "Paragraph 3 provides the historical background for paragraph 2"},
            {"letter": "B", "text": "Paragraph 3 presents the drawbacks that contrast with the benefits described in paragraph 2"},
            {"letter": "C", "text": "Paragraph 3 gives more examples of the flexibility mentioned in paragraph 2"},
            {"letter": "D", "text": "Paragraph 3 introduces a completely different subject"},
            {"letter": "E", "text": "Paragraph 3 is a restatement of paragraph 2 in simpler terms"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 2 describes the advantages (flexibility, low overhead). Paragraph 3 then pivots to the downsides (no benefits, income instability) — a classic benefit-vs-drawback contrast.",
    },
    {
        "id": "ep04_q4", "subject": "English", "topic": "Grammar and Tenses",
        "question_text": "Fill in blank (b): 'Several governments are now debating legislation to reclassify gig workers and mandate (b) ________ protections.'",
        "options": [
            {"letter": "A", "text": "basic"},
            {"letter": "B", "text": "basically"},
            {"letter": "C", "text": "the basic"},
            {"letter": "D", "text": "more basic"},
            {"letter": "E", "text": "as basic"},
        ],
        "correct_answer": "A",
        "explanation": "'Mandate (blank) protections' requires an adjective to modify 'protections'. 'Basic' is the correct attributive adjective here, meaning fundamental or minimum protections.",
    },
    {
        "id": "ep04_q5", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "According to the passage, which group MOST benefits from the flexibility of the gig model?",
        "options": [
            {"letter": "A", "text": "Government regulators"},
            {"letter": "B", "text": "Both individual workers and businesses"},
            {"letter": "C", "text": "Only large technology corporations"},
            {"letter": "D", "text": "Retired workers seeking part-time income"},
            {"letter": "E", "text": "Traditional salaried employees"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 2 explicitly states that workers gain flexibility and freedom, while businesses benefit from lower costs and workforce scalability — both groups are identified as beneficiaries.",
    },
]
},

# ── PASSAGE 05 ── Sleep Science ──────────────────────────────────────────────
{
"passage_id": "eng_pool_05",
"passage_text": (
    "Modern research has revealed that sleep is far more than a passive state of rest — it is a complex, active process essential to physical and cognitive health. "
    "During deep sleep, the brain clears metabolic waste through a system known as the glymphatic network, reducing the risk of neurodegenerative diseases. "
    "Simultaneously, the body repairs tissue, consolidates memories, and regulates hormones that control appetite and stress.\n\n"
    "Despite this evidence, chronic sleep deprivation has become a public health crisis in many industrialized nations. "
    "Adults are recommended to sleep between seven and nine hours per night, yet surveys consistently show that large proportions of the working population sleep fewer than six hours. "
    "Shift work, screen exposure before bedtime, and high-stress workplaces all (a) ________ to this widespread deficit.\n\n"
    "The consequences extend beyond personal fatigue. Studies link insufficient sleep to increased rates of cardiovascular disease, obesity, and impaired immune function. "
    "Economically, sleep deprivation costs countries billions of dollars annually through reduced productivity and heightened healthcare demands. "
    "Public health authorities are now calling for workplace policies that treat adequate sleep as a genuine occupational health priority."
),
"questions": [
    {
        "id": "ep05_q1", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "The best title for the passage is...",
        "options": [
            {"letter": "A", "text": "Dreams and Their Psychological Meaning"},
            {"letter": "B", "text": "Sleep Deprivation Is a Modern Crisis With Serious Consequences"},
            {"letter": "C", "text": "How to Fall Asleep Faster"},
            {"letter": "D", "text": "The History of Neuroscience"},
            {"letter": "E", "text": "Workplace Stress and Its Causes"},
        ],
        "correct_answer": "B",
        "explanation": "The passage moves from why sleep matters (paragraph 1), to why we are not getting enough (paragraph 2), to what happens as a result (paragraph 3) — the progression fits 'crisis with serious consequences'.",
    },
    {
        "id": "ep05_q2", "subject": "English", "topic": "Grammar and Tenses",
        "question_text": "Fill in blank (a): 'Shift work, screen exposure...and high-stress workplaces all (a) ________ to this widespread deficit.'",
        "options": [
            {"letter": "A", "text": "contributes"},
            {"letter": "B", "text": "contribute"},
            {"letter": "C", "text": "contributed"},
            {"letter": "D", "text": "contributing"},
            {"letter": "E", "text": "has contributed"},
        ],
        "correct_answer": "B",
        "explanation": "The subject is plural ('Shift work, screen exposure, and high-stress workplaces all...'), requiring the plural verb form 'contribute' without the -s ending.",
    },
    {
        "id": "ep05_q3", "subject": "English", "topic": "Paragraph Cohesion and Structure",
        "question_text": "What is the relationship between paragraph 1 and paragraph 2?",
        "options": [
            {"letter": "A", "text": "Paragraph 2 provides scientific evidence for the claims in paragraph 1"},
            {"letter": "B", "text": "Paragraph 2 argues that the benefits described in paragraph 1 are unproven"},
            {"letter": "C", "text": "Paragraph 2 shows that despite the importance of sleep established in paragraph 1, many people are not getting enough"},
            {"letter": "D", "text": "Paragraph 2 introduces an unrelated topic about workplace stress"},
            {"letter": "E", "text": "Paragraph 2 summarizes paragraph 1 in simpler terms"},
        ],
        "correct_answer": "C",
        "explanation": "Paragraph 1 establishes how vital sleep is. Paragraph 2 then presents the paradox: despite this importance, chronic sleep deprivation is widespread — a contrast between ideal and reality.",
    },
    {
        "id": "ep05_q4", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "According to paragraph 3, which of the following is a consequence of insufficient sleep?",
        "options": [
            {"letter": "A", "text": "Faster memory consolidation"},
            {"letter": "B", "text": "Reduced rates of cardiovascular disease"},
            {"letter": "C", "text": "Economic costs through lower productivity"},
            {"letter": "D", "text": "Improved immune function"},
            {"letter": "E", "text": "Increased workplace efficiency"},
        ],
        "correct_answer": "C",
        "explanation": "Paragraph 3 explicitly states that sleep deprivation 'costs countries billions of dollars annually through reduced productivity and heightened healthcare demands.'",
    },
    {
        "id": "ep05_q5", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "The author's attitude toward the issue of sleep deprivation is...",
        "options": [
            {"letter": "A", "text": "Indifferent — sleep habits are a purely personal choice"},
            {"letter": "B", "text": "Concerned — sleep deprivation is a serious health and economic problem"},
            {"letter": "C", "text": "Optimistic — technology will solve the sleep crisis soon"},
            {"letter": "D", "text": "Dismissive — the research on sleep is unreliable"},
            {"letter": "E", "text": "Humorous — the topic is treated lightly"},
        ],
        "correct_answer": "B",
        "explanation": "The passage uses language like 'public health crisis', 'costs countries billions', and 'genuine occupational health priority' — all indicating serious concern about the issue.",
    },
]
},

# ── PASSAGE 06 ── Renewable Energy Transition ────────────────────────────────
{
"passage_id": "eng_pool_06",
"passage_text": (
    "The global transition from fossil fuels to renewable energy sources represents one of the most sweeping economic and technological shifts of our era. "
    "Solar and wind power have achieved price parity with — and in many regions now undercut — conventional electricity generation. "
    "Governments worldwide are setting ambitious targets: several major economies have pledged to reach net-zero carbon emissions by 2050.\n\n"
    "The benefits extend beyond reducing pollution. Renewable energy projects create substantial local employment, particularly in manufacturing, installation, and maintenance. "
    "Countries that previously depended on costly fuel imports can (a) ________ energy independence by harnessing domestic solar or wind resources, strengthening both economic resilience and national security.\n\n"
    "Nevertheless, the transition poses genuine challenges. Renewable sources are inherently variable — the sun does not always shine and the wind does not always blow — creating reliability concerns for energy grids. "
    "Massive investment in battery storage, smart grids, and intercontinental transmission lines will be required. "
    "Communities reliant on coal mining and fossil-fuel industries also face painful economic disruption unless robust retraining and support programs accompany the energy shift."
),
"questions": [
    {
        "id": "ep06_q1", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "The best title for the passage is...",
        "options": [
            {"letter": "A", "text": "Why Solar Panels Are Cheaper Than Ever"},
            {"letter": "B", "text": "The Renewable Energy Transition: Opportunities and Challenges"},
            {"letter": "C", "text": "How Wind Turbines Are Built"},
            {"letter": "D", "text": "Net-Zero Emissions Policies Explained"},
            {"letter": "E", "text": "The Decline of the Coal Industry"},
        ],
        "correct_answer": "B",
        "explanation": "The passage covers the scale of the transition (paragraph 1), its benefits (paragraph 2), and its challenges (paragraph 3) — 'Opportunities and Challenges' captures this full scope.",
    },
    {
        "id": "ep06_q2", "subject": "English", "topic": "Grammar and Tenses",
        "question_text": "Fill in blank (a): 'Countries...can (a) ________ energy independence by harnessing domestic solar or wind resources...'",
        "options": [
            {"letter": "A", "text": "achieved"},
            {"letter": "B", "text": "achieving"},
            {"letter": "C", "text": "achieve"},
            {"letter": "D", "text": "achieves"},
            {"letter": "E", "text": "to achieve"},
        ],
        "correct_answer": "C",
        "explanation": "'Can + base verb' is the correct modal construction. 'Achieve' (base form) is required after the modal verb 'can'.",
    },
    {
        "id": "ep06_q3", "subject": "English", "topic": "Paragraph Cohesion and Structure",
        "question_text": "What is the relationship between paragraph 2 and paragraph 3?",
        "options": [
            {"letter": "A", "text": "Paragraph 3 provides more economic benefits to complement paragraph 2"},
            {"letter": "B", "text": "Paragraph 3 presents the challenges that must be addressed alongside the benefits in paragraph 2"},
            {"letter": "C", "text": "Paragraph 3 contradicts the energy pricing data in paragraph 2"},
            {"letter": "D", "text": "Paragraph 3 repeats the same ideas as paragraph 2"},
            {"letter": "E", "text": "Paragraph 3 focuses on a different country than paragraph 2"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 2 highlights benefits (jobs, energy independence). Paragraph 3 introduces the real challenges (grid reliability, storage, community disruption) — a benefit-challenge relationship.",
    },
    {
        "id": "ep06_q4", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "What can be inferred from paragraph 1?",
        "options": [
            {"letter": "A", "text": "Renewable energy is still far more expensive than fossil fuels"},
            {"letter": "B", "text": "Only a few small countries have set climate targets"},
            {"letter": "C", "text": "Renewable energy has become cost-competitive and is supported at the highest policy levels"},
            {"letter": "D", "text": "Most governments oppose the shift to renewables"},
            {"letter": "E", "text": "Net-zero targets have already been achieved"},
        ],
        "correct_answer": "C",
        "explanation": "Paragraph 1 states renewables have achieved price parity (cost-competitive) and that major economies are pledging net-zero by 2050 (high-level policy support).",
    },
    {
        "id": "ep06_q5", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "According to paragraph 3, which of the following is NOT mentioned as a challenge of the energy transition?",
        "options": [
            {"letter": "A", "text": "Variability of renewable energy sources"},
            {"letter": "B", "text": "Need for grid modernization and battery storage"},
            {"letter": "C", "text": "Declining public interest in renewable energy"},
            {"letter": "D", "text": "Economic disruption for fossil-fuel communities"},
            {"letter": "E", "text": "Reliability concerns for energy grids"},
        ],
        "correct_answer": "C",
        "explanation": "Paragraph 3 mentions variability (A), battery/grid investment (B), economic disruption for coal communities (D), and grid reliability (E). Declining public interest is never mentioned.",
    },
]
},

# ── PASSAGE 07 ── Space Exploration's New Era ────────────────────────────────
{
"passage_id": "eng_pool_07",
"passage_text": (
    "The landscape of space exploration has changed dramatically in the past two decades, driven by the emergence of private companies alongside traditional government space agencies. "
    "Firms such as SpaceX and Blue Origin have developed reusable rocket technology that has cut launch costs by an order of magnitude. "
    "This cost reduction has (a) ________ a new era of ambition: lunar bases, Mars missions, and commercial space stations are no longer confined to science fiction.\n\n"
    "The democratization of space access brings tangible near-term benefits. Thousands of small satellites now provide high-resolution Earth observation data used for agriculture, disaster response, and climate monitoring. "
    "In addition, satellite internet constellations aim to deliver broadband connectivity to the billions of people who still lack reliable access, potentially transforming education and economic opportunity in remote areas.\n\n"
    "Critics, however, raise important concerns. The rapid proliferation of satellites is contributing to orbital debris, increasing the risk of collisions that could render specific orbital shells unusable for generations — a scenario known as Kessler Syndrome. "
    "Astronomers also report that dense satellite constellations are disrupting ground-based telescope observations. "
    "Managing these trade-offs will require international coordination and binding agreements on responsible use of orbital space."
),
"questions": [
    {
        "id": "ep07_q1", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "The best title for this passage is...",
        "options": [
            {"letter": "A", "text": "SpaceX and the Race to Mars"},
            {"letter": "B", "text": "The New Era of Space Exploration: Opportunities and Risks"},
            {"letter": "C", "text": "How Reusable Rockets Are Built"},
            {"letter": "D", "text": "The History of Government Space Programs"},
            {"letter": "E", "text": "Orbital Debris: A Growing Crisis"},
        ],
        "correct_answer": "B",
        "explanation": "The passage covers new space capabilities (paragraph 1), their benefits (paragraph 2), and associated risks (paragraph 3) — 'Opportunities and Risks' accurately captures this scope.",
    },
    {
        "id": "ep07_q2", "subject": "English", "topic": "Grammar and Tenses",
        "question_text": "Fill in blank (a): 'This cost reduction has (a) ________ a new era of ambition...'",
        "options": [
            {"letter": "A", "text": "ushering"},
            {"letter": "B", "text": "usher"},
            {"letter": "C", "text": "ushered in"},
            {"letter": "D", "text": "was ushering"},
            {"letter": "E", "text": "ushers"},
        ],
        "correct_answer": "C",
        "explanation": "'Has + past participle' forms the present perfect tense. 'Ushered in' is the past participle phrase meaning 'brought about/introduced', making 'has ushered in' the correct form.",
    },
    {
        "id": "ep07_q3", "subject": "English", "topic": "Paragraph Cohesion and Structure",
        "question_text": "What is the relationship between paragraph 2 and paragraph 3?",
        "options": [
            {"letter": "A", "text": "Paragraph 3 provides technical details about the satellites mentioned in paragraph 2"},
            {"letter": "B", "text": "Paragraph 3 raises the environmental and practical concerns that accompany the benefits in paragraph 2"},
            {"letter": "C", "text": "Paragraph 3 argues that the benefits described in paragraph 2 are fictional"},
            {"letter": "D", "text": "Paragraph 3 introduces a separate topic about telescope design"},
            {"letter": "E", "text": "Paragraph 3 summarizes the cost savings in paragraph 2"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 2 describes satellite benefits (Earth observation, internet access). Paragraph 3 then raises the downsides (orbital debris, telescope disruption) — a benefit-vs-risk contrast.",
    },
    {
        "id": "ep07_q4", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "According to paragraph 2, which of the following is a near-term benefit of cheaper space access?",
        "options": [
            {"letter": "A", "text": "Human settlements on Mars"},
            {"letter": "B", "text": "Satellite internet for remote communities"},
            {"letter": "C", "text": "Solving the orbital debris problem"},
            {"letter": "D", "text": "Replacing government space agencies"},
            {"letter": "E", "text": "Eliminating the need for ground-based telescopes"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 2 explicitly mentions 'satellite internet constellations aim to deliver broadband connectivity...to remote areas' as a near-term, tangible benefit.",
    },
    {
        "id": "ep07_q5", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "'Kessler Syndrome' as described in paragraph 3 refers to...",
        "options": [
            {"letter": "A", "text": "A disease affecting astronauts in orbit"},
            {"letter": "B", "text": "A treaty governing satellite communications"},
            {"letter": "C", "text": "A scenario where orbital debris makes certain orbital zones permanently unusable"},
            {"letter": "D", "text": "A type of reusable rocket engine"},
            {"letter": "E", "text": "The process of deorbiting old satellites safely"},
        ],
        "correct_answer": "C",
        "explanation": "Paragraph 3 defines Kessler Syndrome directly: collisions could 'render specific orbital shells unusable for generations' — exactly option C.",
    },
]
},

# ── PASSAGE 08 ── Language Extinction ───────────────────────────────────────
{
"passage_id": "eng_pool_08",
"passage_text": (
    "Thousands of the world's languages are facing extinction at an unprecedented rate. "
    "Linguists estimate that roughly half of the approximately 7,000 languages spoken today will disappear by the end of this century, with one language falling silent every two weeks. "
    "When a language dies, it carries with it an irreplaceable body of knowledge: unique ecological observations, oral histories, and conceptual frameworks found nowhere else.\n\n"
    "The causes are intertwined. Economic pressures push speakers of minority languages to adopt dominant tongues in order to access education and employment. "
    "Urbanization separates communities from the land-based contexts in which their languages flourished. "
    "Meanwhile, mass media and the internet (a) ________ the global dominance of a handful of languages, particularly English and Mandarin, accelerating the marginalisation of smaller ones.\n\n"
    "Efforts to preserve endangered languages are gaining momentum. Immersion schools and bilingual education programs have achieved notable success with languages such as Welsh and Maori. "
    "Digital archiving projects are recording spoken grammars and vocabularies before their last speakers pass away. "
    "Scholars argue, however, that true revitalization requires not just documentation but the creation of vibrant communities of speakers who use the language in everyday life."
),
"questions": [
    {
        "id": "ep08_q1", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "The best title for this passage is...",
        "options": [
            {"letter": "A", "text": "The Dominance of English in Global Communication"},
            {"letter": "B", "text": "Language Extinction: Causes, Consequences, and Conservation"},
            {"letter": "C", "text": "How to Learn a New Language Quickly"},
            {"letter": "D", "text": "The Role of Technology in Modern Communication"},
            {"letter": "E", "text": "Welsh and Maori Language Revival Programs"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 1 discusses the consequences of language loss, paragraph 2 the causes, and paragraph 3 the conservation efforts — 'Causes, Consequences, and Conservation' maps precisely to this structure.",
    },
    {
        "id": "ep08_q2", "subject": "English", "topic": "Grammar and Tenses",
        "question_text": "Fill in blank (a): '...mass media and the internet (a) ________ the global dominance of a handful of languages...'",
        "options": [
            {"letter": "A", "text": "reinforcing"},
            {"letter": "B", "text": "reinforces"},
            {"letter": "C", "text": "reinforce"},
            {"letter": "D", "text": "reinforced"},
            {"letter": "E", "text": "has reinforced"},
        ],
        "correct_answer": "C",
        "explanation": "The compound subject 'mass media and the internet' is plural, requiring the base form 'reinforce' (not reinforces). Present simple is used for ongoing truths.",
    },
    {
        "id": "ep08_q3", "subject": "English", "topic": "Paragraph Cohesion and Structure",
        "question_text": "What is the relationship between paragraph 2 and paragraph 3?",
        "options": [
            {"letter": "A", "text": "Paragraph 3 deepens the economic problems described in paragraph 2"},
            {"letter": "B", "text": "Paragraph 3 presents the solutions being developed to address the causes identified in paragraph 2"},
            {"letter": "C", "text": "Paragraph 3 contradicts the claim that languages are becoming extinct"},
            {"letter": "D", "text": "Paragraph 3 introduces the economic argument against language preservation"},
            {"letter": "E", "text": "Paragraph 3 explains why mass media is harmful"},
        ],
        "correct_answer": "B",
        "explanation": "Paragraph 2 identifies the causes of language death (economic pressure, urbanization, media). Paragraph 3 then describes the preservation efforts — a problem-to-solution structure.",
    },
    {
        "id": "ep08_q4", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "What can be inferred from paragraph 1?",
        "options": [
            {"letter": "A", "text": "The loss of a language has no significant cultural impact"},
            {"letter": "B", "text": "Language extinction only affects spoken communication, not written culture"},
            {"letter": "C", "text": "Each language encodes unique knowledge that cannot be fully recovered once lost"},
            {"letter": "D", "text": "All 7,000 languages will survive into the next century"},
            {"letter": "E", "text": "Linguists are unconcerned about the pace of language loss"},
        ],
        "correct_answer": "C",
        "explanation": "Paragraph 1 states that when a language dies, it carries 'an irreplaceable body of knowledge...found nowhere else' — directly implying that unique knowledge is lost permanently.",
    },
    {
        "id": "ep08_q5", "subject": "English", "topic": "Reading Comprehension",
        "question_text": "According to paragraph 3, what do scholars consider necessary for genuine language revitalization?",
        "options": [
            {"letter": "A", "text": "Only digital recordings of grammar and vocabulary"},
            {"letter": "B", "text": "Financial investment from international organizations"},
            {"letter": "C", "text": "Active living communities of everyday speakers"},
            {"letter": "D", "text": "Government mandates making minority languages official"},
            {"letter": "E", "text": "Reducing the influence of English and Mandarin globally"},
        ],
        "correct_answer": "C",
        "explanation": "Paragraph 3 concludes that 'true revitalization requires...the creation of vibrant communities of speakers who use the language in everyday life' — option C.",
    },
]
},

]  # end POOL first 8 passages
