import json
import re

INDEX_PATH = "index.html"
PHASE_PATH = "data/phase-exercises.json"

MOVEMENT_ID_MAP = {
    "back-squat": "squat",
    "lunge": "lunge",
    "deadlift": "deadlift",
    "pullup": "pullup",
    "vertical-press": "press-vertical",
    "horizontal-press": "press-horizontal",
    "row": "row",
    "kipping": "kipping",
}

with open(PHASE_PATH, encoding="utf-8") as f:
    phase_data = json.load(f)

with open(INDEX_PATH, encoding="utf-8") as f:
    html = f.read()

m = re.search(r"const BUNDLED\s*=\s*(\{[\s\S]*?\});", html)
if not m:
    raise SystemExit("BUNDLED constant not found")
bundled_raw = m.group(1)
bundled = json.loads(bundled_raw)

merged = 0
skipped = []

for mv_p in phase_data["movements"]:
    bundled_mv_id = MOVEMENT_ID_MAP.get(mv_p["id"])
    if not bundled_mv_id or bundled_mv_id not in bundled:
        skipped.append(f"movement not found: {mv_p['id']}")
        continue
    mv_b = bundled[bundled_mv_id]

    for ps_p in mv_p["pain_sites"]:
        ps_b = next((p for p in mv_b["pain_sites"] if p["id"] == ps_p["id"]), None)
        if ps_b is None:
            skipped.append(f"{mv_p['id']}/{ps_p['id']}: pain_site not found")
            continue

        for cause_p in ps_p["causes"]:
            cause_b = next((c for c in ps_b["causes"] if c["id"] == cause_p["id"]), None)
            if cause_b is None:
                skipped.append(f"{mv_p['id']}/{ps_p['id']}/{cause_p['id']}: cause not found")
                continue

            stage1_p = cause_p["route"]["stages"][0]
            stage1_b = cause_b["route"]["stages"][0]

            phase_a = stage1_p.get("phase_a") or []
            phase_b = stage1_p.get("phase_b") or []
            if not phase_a and not phase_b:
                skipped.append(f"{mv_p['id']}/{ps_p['id']}/{cause_p['id']}: empty phase_a/phase_b")
                continue

            stage1_b["phase_a"] = phase_a
            stage1_b["phase_b"] = phase_b
            stage1_b.pop("exercises", None)
            recovery_note = stage1_p.get("recovery_note")
            if recovery_note:
                stage1_b["recovery_note"] = recovery_note
            merged += 1

new_bundled_raw = json.dumps(bundled, ensure_ascii=False, separators=(",", ":"))
html = html[:m.start(1)] + new_bundled_raw + html[m.end(1):]

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print(f"병합 완료: {merged}건")
print(f"스킵: {len(skipped)}건")
for s in skipped:
    print(" -", s)
