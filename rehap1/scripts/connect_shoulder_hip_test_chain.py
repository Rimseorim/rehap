"""
어깨·고관절 질문 흐름 테스트 체인 연결

어깨: q3/q4는 Lumbar Lock·Apley's Scratch 물리검사 형식이라 유지.
      통증 확인 경로(cause-dp 행선지)만 test:test-shoulder-arc 로 연결.
      - cause-dp 로 가는 choices → test:test-shoulder-arc

고관절: 팔꿈치·손목과 동일하게 전체 연결.
        squat·lunge: c1/c2/c3 → test:test-hip-fadir
        deadlift:    c1/c2/c3 → test:test-hip-hamstring
"""
import json, os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SHOULDER_MOVEMENTS = [
    "squat", "deadlift", "pullup", "kipping",
    "row", "press-vertical", "press-horizontal"
]
HIP_SQUAT_LUNGE = ["squat", "lunge"]
HIP_DEADLIFT    = ["deadlift"]

def connect_shoulder(movement_id):
    path = os.path.join(base, f"data/movements/{movement_id}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    changed = False
    for site in data.get("pain_sites", []):
        if not isinstance(site, dict) or site.get("id") != "shoulder":
            continue
        first_test = site["tests"][0]["id"]  # 동작별 첫 테스트 ID

        for q in site.get("questions", []):
            for choice in q.get("choices", []):
                if choice.get("next") == "cause:cause-dp":
                    choice["next"] = f"test:{first_test}"
                    changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] {movement_id}/shoulder → cause-dp 경로를 test:{first_test} 로 연결")
    else:
        print(f"[SKIP] {movement_id}/shoulder — cause-dp 경로 없음")

def connect_hip_all(movement_id, first_test_id):
    path = os.path.join(base, f"data/movements/{movement_id}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    changed = False
    for site in data.get("pain_sites", []):
        if not isinstance(site, dict) or site.get("id") != "hip":
            continue
        for q in site.get("questions", []):
            for choice in q.get("choices", []):
                if choice.get("next", "").startswith("cause:"):
                    choice["next"] = f"test:{first_test_id}"
                    changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] {movement_id}/hip → 전체 cause 경로를 test:{first_test_id} 로 연결")
    else:
        print(f"[SKIP] {movement_id}/hip — 변경 없음")

for m in SHOULDER_MOVEMENTS:
    connect_shoulder(m)

for m in HIP_SQUAT_LUNGE:
    connect_hip_all(m, "test-hip-fadir")

for m in HIP_DEADLIFT:
    connect_hip_all(m, "test-hip-hamstring")

print("완료")
