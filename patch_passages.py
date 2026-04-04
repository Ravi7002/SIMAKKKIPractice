"""
Restructures English questions in realQ1.json and realQ2.json to use passage groups.
A passage group = { passage_id, passage_text, questions: [...] }
The flat list gets split: passage questions are grouped under their passage,
standalone questions (grammar/vocab/structure) stay as-is with passage: null.

Also updates the English practice questions folder to add proper passage groups.
"""
import json
import os

# ─── Rich English passages ──────────────────────────────────────────────────
PASSAGES = {
    "passage_1": {
        "title": "The Rise of Remote Work",
        "text": """The COVID-19 pandemic accelerated a workplace transformation that had been quietly building for years: the shift to remote work. Almost overnight, millions of employees transitioned from shared offices to home workspaces, forcing companies to rapidly adopt digital collaboration tools and rethink fundamental assumptions about productivity and management.

Proponents of remote work argue that eliminating daily commutes returns precious hours to workers, reduces stress, and allows for a better work-life balance. Studies from Stanford University suggest that remote workers are roughly 13% more productive than their in-office counterparts, partly because they take shorter breaks and call in sick less frequently. Furthermore, companies can access global talent pools rather than limiting their search radius to commuting distance from a physical office.

Critics, however, raise compelling concerns. The boundaries between professional and personal life can dissolve, leading to longer working hours and burnout. Junior employees may struggle without informal mentorship opportunities that arise naturally in shared physical spaces. Additionally, spontaneous collaboration—the kind that often sparks innovation—is harder to replicate through a video screen. A 2023 Microsoft survey found that while productivity metrics often remained stable, many workers reported feeling less connected to their company's culture and mission.

Organizations navigating this tension have largely settled on hybrid models as a compromise: employees spend part of the week in the office and part working remotely. This approach attempts to capture the focused productivity of remote work while preserving the collaborative energy of in-person interaction. Whether this equilibrium proves stable in the long run, or whether the pendulum swings back toward mandatory in-office attendance, remains one of the defining organizational questions of the decade."""
    },
    "passage_2": {
        "title": "Ocean Acidification and Marine Ecosystems",
        "text": """Since the Industrial Revolution, the world's oceans have absorbed approximately 30% of all carbon dioxide (CO₂) emitted by human activity. While this has slowed the rate of atmospheric warming, it has triggered a parallel crisis largely invisible to public awareness: ocean acidification. When CO₂ dissolves in seawater, it forms carbonic acid, which gradually lowers the ocean's pH. Surface ocean pH has already dropped from a pre-industrial level of 8.2 to approximately 8.1—a change that, on the logarithmic pH scale, represents a 26% increase in acidity.

The ecological consequences are profound. Marine organisms that build shells or skeletons from calcium carbonate—including oysters, mussels, sea urchins, and corals—find it increasingly difficult to calcify in more acidic waters. Research published in the journal Nature has demonstrated that oyster larvae in the Pacific Northwest have suffered massive die-offs linked directly to acidification. Coral reefs, already stressed by rising water temperatures, face a compounded threat: not only does bleaching occur when symbiotic algae are expelled due to heat stress, but acidic water also weakens the coral's calcium carbonate structure, making recovery from bleaching events less likely.

The consequences extend beyond marine invertebrates. Pteropods—tiny free-swimming sea snails that serve as a critical food source for salmon, herring, and even some whale species—have been documented dissolving in waters already acidified near Antarctica. Disruptions at such a foundational level of the marine food web send cascading effects upward through entire ocean ecosystems.

Addressing ocean acidification requires reducing global carbon emissions at a scale and pace that current international commitments have not yet achieved. In the interim, some researchers explore more localized interventions, such as adding alkaline minerals to coastal waters to neutralize acidity, but these approaches remain experimental and ecologically controversial."""
    },
    "passage_3": {
        "title": "The Architecture of Memory",
        "text": """Human memory is not a fixed recording of the past but a dynamic, reconstructive process—one that is far more susceptible to distortion than most people realize. Each time we recall a memory, we do not simply retrieve a stored copy; we actively rebuild it using fragments of the original experience interwoven with our current knowledge, expectations, and emotional state. This reconstructive nature means that memories can change subtly every time they are accessed.

The neuroscience of memory distinguishes between several systems. Declarative memory encompasses facts and events that can be consciously recalled, subdivided into semantic memory (general world knowledge) and episodic memory (autobiographical events). Non-declarative memory, by contrast, operates largely below conscious awareness and includes procedural skills like riding a bicycle. These systems rely on different brain structures: the hippocampus plays a pivotal role in forming new episodic memories, while the cerebellum is central to procedural learning.

Psychologist Elizabeth Loftus spent decades demonstrating how easily false memories can be implanted. In her seminal "lost in the mall" study, approximately 25% of participants came to "remember" a childhood event of being lost in a shopping mall that had never actually occurred, simply after it was described to them by a family member. Her work has had profound implications for the legal system, raising serious questions about the reliability of eyewitness testimony.

These insights challenge the intuitive sense that remembering is passive and neutral. Memory, it turns out, is always a creative act—shaped by who we are at the moment of recall as much as by who we were at the moment of experience."""
    }
}

# ─── Map English topics to passage IDs ──────────────────────────────────────
TOPIC_TO_PASSAGE = {
    "Reading Comprehension (Long Passage)": None,   # will assign dynamically
    "Reading Comprehension (Short Passage)": None,
}

def rebuild_english_group(questions, passage_id, passage):
    """
    Takes a flat list of English reading-comp questions for one passage
    and attaches the passage to each of them (they keep their individual structure
    so they still work in flat-list mode, but passage_id groups them).
    """
    for q in questions:
        q["passage_id"] = passage_id
        q["passage"] = passage["text"]
        q["passage_title"] = passage["title"]
    return questions

# ─── Patch realQ1 & realQ2 ──────────────────────────────────────────────────
for fname, passage_cycle in [("realQ1.json", ["passage_1","passage_2"]),
                               ("realQ2.json", ["passage_2","passage_3"])]:
    with open(fname, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Find English reading-comp questions and group them by topic
    groups = {}
    for q in data:
        if q.get("subject") == "English" and "Reading Comprehension" in q.get("topic",""):
            topic = q["topic"]
            groups.setdefault(topic, []).append(q)

    # Assign passages to grouped questions
    passage_keys = list(passage_cycle)
    for idx, (topic, qs) in enumerate(groups.items()):
        pid = passage_keys[idx % len(passage_keys)]
        rebuild_english_group(qs, pid, PASSAGES[pid])

    with open(fname, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Patched {fname}: {sum(len(v) for v in groups.values())} reading-comp questions grouped")

# ─── Patch English PracticeQuestions folder ────────────────────────────────
import glob
for fpath in glob.glob("quiz-app/src/PracticeQuestions/English/**/*.json", recursive=True):
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)

    topic = data.get("topic","")
    qs = data.get("questions", [])

    if "Reading Comprehension" in topic:
        # pick a passage for this topic file
        if "Long" in topic:      pid = "passage_1"
        elif "Short" in topic:   pid = "passage_2"
        else:                    pid = "passage_3"

        passage = PASSAGES[pid]
        data["passage_id"]    = pid
        data["passage_text"]  = passage["text"]
        data["passage_title"] = passage["title"]
        for q in qs:
            q["passage_id"]    = pid
            q["passage"]       = passage["text"]
            q["passage_title"] = passage["title"]
        data["questions"] = qs
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Patched {fpath}")

# ─── Patch Generated Tryouts ─────────────────────────────────────────────────
for fpath in glob.glob("quiz-app/src/GeneratedTryouts/*.json"):
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)

    groups = {}
    for q in data:
        if q.get("subject") == "English" and "Reading Comprehension" in q.get("topic",""):
            topic = q["topic"]
            groups.setdefault(topic, []).append(q)

    for idx, (topic, qs) in enumerate(groups.items()):
        pid = ["passage_1","passage_2","passage_3"][idx % 3]
        rebuild_english_group(qs, pid, PASSAGES[pid])

    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Patched tryout: {fpath}")

print("Done.")
