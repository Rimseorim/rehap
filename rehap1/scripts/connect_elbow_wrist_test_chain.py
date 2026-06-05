"""
팔꿈치·손목 질문 흐름을 테스트 체인 첫 번째로 연결
- 팔꿈치 c1/c2/c3 → test:test-elbow-lateral (체인 시작)
- 손목   c1/c2/c3 → test:test-wrist-ext-mob (체인 시작)
- c4(danger) 유지
"""
import json, os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ELBOW_MOVEMENTS = ["pullup", "kipping", "row", "press-vertical", "press-horizontal"]
WRIST_MOVEMENTS = ["deadlift", "kipping", "pullup", "row", "press-vertical", "press-horizontal"]

def connect(movement_id, site_id, first_test_id):
    path = os.path.join(base, f"data/movements/{movement_id}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    changed = False
    for site in data.get("pain_sites", []):
        if not isinstance(site, dict): continue
        if site.get("id") != site_id: continue

        for q in site.get("questions", []):
            for choice in q.get("choices", []):
                if choice.get("next", "").startswith("cause:"):
                    choice["next"] = f"test:{first_test_id}"
                    changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] {movement_id}/{site_id} → 질문 라우팅을 test:{first_test_id} 로 연결")
    else:
        print(f"[SKIP] {movement_id}/{site_id} — 변경 없음")

for m in ELBOW_MOVEMENTS:
    connect(m, "elbow", "test-elbow-lateral")

for m in WRIST_MOVEMENTS:
    connect(m, "wrist", "test-wrist-ext-mob")

print("완료")
