import json

PATH = "data/phase-exercises.json"

with open(PATH, encoding="utf-8") as f:
    data = json.load(f)

mv = next(m for m in data["movements"] if m["id"] == "row")
site = next(s for s in mv["pain_sites"] if s["id"] == "shoulder")
cause = next(c for c in site["causes"] if c["id"] == "cause-case1")
stage1 = cause["route"]["stages"][0]

fixed = 0
for it in stage1["phase_b"]:
    if "advancement_criteria" in it:
        it["progression_note"] = it.pop("advancement_criteria")
        fixed += 1

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"advancement_criteria -> progression_note 필드명 수정: {fixed}건")
