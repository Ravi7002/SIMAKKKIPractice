import json
import os

def normalize(s):
    # Remove extension if any
    if s.endswith(".json"):
        s = s[:-5]
    # Replace common symbols
    s = s.replace("_", " ").replace("&", "and")
    # Remove punctuation for matching
    import re
    s = re.sub(r'[.,()]', '', s)
    return " ".join(s.lower().split())

def analyze():
    # Load real questions
    real_files = ["realQ1.json", "realQ2.json"]
    real_topics = {} # subject -> set of topics

    for f in real_files:
        if os.path.exists(f):
            with open(f, "r", encoding="utf-8") as file:
                questions = json.load(file)
                for q in questions:
                    subj = q.get("subject", "Unknown")
                    topo = q.get("topic", "Unknown")
                    if subj not in real_topics:
                        real_topics[subj] = set()
                    real_topics[subj].add(topo)

    # Load current practice topics
    practice_base = "PracticeQuestions"
    practice_topics = {} # subject -> list of topics (filenames)
    
    if os.path.exists(practice_base):
        for subj_dir in os.listdir(practice_base):
            subj_path = os.path.join(practice_base, subj_dir)
            if os.path.isdir(subj_path):
                # Subject directory names are often underscores (e.g. Basic_Mathematics)
                # We should match these with real_topics subjects
                subj_name = subj_dir.replace("_", " ")
                practice_topics[subj_name] = []
                for f in os.listdir(subj_path):
                    if f.endswith(".json"):
                        topic_name = f[:-5].replace("_", " ")
                        practice_topics[subj_name].append(topic_name)

    # Build report
    report = {
        "summary": "Analysis of topics found in realQ1 and realQ2 vs current PracticeQuestions",
        "sections": {}
    }

    all_subjects = set(real_topics.keys()) | set(practice_topics.keys())

    for subj in all_subjects:
        real = sorted(list(real_topics.get(subj, [])))
        curr = sorted(practice_topics.get(subj, []))
        
        # Check relevance
        relevant = []
        missing_in_practice = []
        for rt in real:
            # Simple match: normalize both and compare
            n_rt = normalize(rt)
            found = False
            for ct in curr:
                if normalize(ct) == n_rt:
                    found = True
                    break
            if found:
                relevant.append(rt)
            else:
                missing_in_practice.append(rt)

        extra_in_practice = []
        for ct in curr:
            n_ct = normalize(ct)
            found = False
            for rt in real:
                if normalize(rt) == n_ct:
                    found = True
                    break
            if not found:
                extra_in_practice.append(ct)

        report["sections"][subj] = {
            "real_test_topics": real,
            "current_practice_topics": curr,
            "missing_in_practice": missing_in_practice,
            "extra_in_practice": extra_in_practice,
            "relevance_summary": f"{len(relevant)}/{len(real)} real topics covered."
        }

    # Save report
    output_path = os.path.join("RealTryoutAnalysis", "topic_analysis.json")
    os.makedirs("RealTryoutAnalysis", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as out:
        json.dump(report, out, indent=4)
    
    print(f"Analysis complete. Saved to {output_path}")

if __name__ == "__main__":
    analyze()
