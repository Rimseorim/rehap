"""[실행 금지] data/phase-exercises.json으로 index.html의 모든 원인 운동(Phase A/B)을 덮어쓴다.

index.html에서 직접 고친 내용(꼬리표 삭제, 쉬운 말 표기, 내부 메모 제거 등)이 전부 사라진다.
2026-09-25 커밋 bd87c7b에서 실행돼 약 70개 원인의 수정분이 되돌려졌고, 2026-09-29에 복구했다.

새 운동을 넣을 때는 이 스크립트 대신, 해당 원인만 data/phase-exercises.json과 index.html
양쪽에 넣는 스크립트(예: add_deadlift_shoulder_cause_dp_phase_b.py)를 쓴다.
정말 전체 덮어쓰기가 필요하면 먼저 data 파일을 index.html과 동기화한 뒤 --force-overwrite-all 을 붙인다.
"""
import json
import re
import sys

if "--force-overwrite-all" not in sys.argv:
    sys.exit("중단: 이 스크립트는 index.html의 직접 수정분을 전부 덮어씁니다. 파일 상단 설명을 읽으세요.")

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
