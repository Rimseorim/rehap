"""
팔꿈치·손목 직접 테스트 주입 스크립트
팔꿈치: Cozen's → Reverse Cozen's 체인 (cause-a 외측 / b 내측 / c 이두건)
손목:   신전 가동성 → TFCC Stress 체인 (cause-a 가동성 / b 신전근 / c TFCC)
"""
import json, os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─── 팔꿈치 ─────────────────────────────────────────────────────────────────
ELBOW_PURPOSES = {
    "pullup":           ("풀업 시 팔꿈치 바깥쪽(가쪽) 통증을 재현합니다. 역수그립 당기기 동작이 손목 신전근에 반복 부하를 줘 외측상과염이 잘 생깁니다.",
                         "풀업 시 팔꿈치 안쪽 통증을 재현합니다. 오버핸드 당기기 동작이 손목 굴곡근과 원회내근에 부하를 줘 내측상과염이 발생합니다."),
    "kipping":          ("키핑 시 팔꿈치 바깥쪽 통증을 재현합니다. 동적 당기기·스윙에서 손목 신전근 반복 수축이 외측 상과에 부하를 줍니다.",
                         "키핑 시 팔꿈치 안쪽 통증을 재현합니다. 스윙 동작에서 손목 굴곡근·전완 회내근에 누적 부하가 생깁니다."),
    "row":              ("로우 시 팔꿈치 바깥쪽 통증을 재현합니다. 수평 당기기 동작에서 손목 신전근이 팔꿈치를 안정시키며 반복 과부하됩니다.",
                         "로우 시 팔꿈치 안쪽 통증을 재현합니다. 당기는 동작에서 손목 굴곡근이 과부하되면 내측상과에 통증이 생깁니다."),
    "press-vertical":   ("오버헤드 프레스 시 팔꿈치 바깥쪽 통증을 재현합니다. 손목 신전 상태로 밀어 올리는 동작이 외측상과에 부하를 줍니다.",
                         "오버헤드 프레스 시 팔꿈치 안쪽 통증을 재현합니다. 밀어 올리는 동작에서 굴곡근 긴장이 내측상과에 집중될 수 있습니다."),
    "press-horizontal": ("벤치프레스 시 팔꿈치 바깥쪽 통증을 재현합니다. 손목을 신전한 채 눌러 내리는 동작이 신전근 기시부(외측상과)에 부하를 줍니다.",
                         "벤치프레스 시 팔꿈치 안쪽 통증을 재현합니다. 바벨을 가슴 쪽으로 내릴 때 굴곡근·회내근 수축이 내측상과에 부하를 줍니다."),
}

def make_elbow_tests(movement_id):
    p_lateral, p_medial = ELBOW_PURPOSES[movement_id]
    return [
        {
            "id": "test-elbow-lateral",
            "name": "코젠(Cozen's) 검사 — 팔꿈치 바깥쪽",
            "purpose": p_lateral,
            "steps": [
                "팔꿈치를 펴고 팔을 앞으로 뻗으세요",
                "손목을 위로 꺾은 자세(손등 방향)를 유지하세요",
                "반대 손으로 손등을 가볍게 눌러 저항을 주세요 (손목 신전에 저항)"
            ],
            "note": "팔꿈치 바깥쪽(가쪽 위관절융기) 통증이 있으면 양성입니다. 양쪽을 비교하세요.",
            "pass_text": "저항 중 팔꿈치 바깥쪽에 통증이 없어요",
            "fail_text": "저항 중 팔꿈치 바깥쪽이 찌릿하거나 아파요",
            "pass_next": "test:test-elbow-medial",
            "fail_next": "cause:cause-a",
            "video_url": ""
        },
        {
            "id": "test-elbow-medial",
            "name": "역 코젠(Reverse Cozen's) 검사 — 팔꿈치 안쪽",
            "purpose": p_medial,
            "steps": [
                "팔꿈치를 펴고 팔을 앞으로 뻗으세요",
                "손목을 아래로 꺾은 자세(손바닥 방향)를 유지하세요",
                "반대 손으로 손바닥을 가볍게 밀어 저항을 주세요 (손목 굴곡에 저항)"
            ],
            "note": "팔꿈치 안쪽(내측 위관절융기) 통증이 있으면 양성입니다. 양쪽을 비교하세요.",
            "pass_text": "저항 중 팔꿈치 안쪽에 통증이 없어요",
            "fail_text": "저항 중 팔꿈치 안쪽이 찌릿하거나 아파요",
            "pass_next": "cause:cause-c",
            "fail_next": "cause:cause-b",
            "video_url": ""
        }
    ]

# ─── 손목 ─────────────────────────────────────────────────────────────────
WRIST_PURPOSES_MOB = {
    "deadlift":         "데드리프트 오버핸드 그립 시 손목이 충분히 신전(뒤로 꺾이는)되는지 확인합니다. 신전 범위가 부족하면 그립 과부하로 이어집니다.",
    "kipping":          "키핑·바 동작 시 손목이 충분히 신전되는지 확인합니다. 범위 부족 시 손목 전면에 과부하가 집중됩니다.",
    "pullup":           "풀업 오버핸드 그립 시 손목이 충분히 신전되는지 확인합니다. 신전 범위 제한은 손목 전면 통증의 주요 원인입니다.",
    "row":              "로우 그립 시 손목이 충분히 신전되는지 확인합니다. 신전 범위 부족 시 손목 앞쪽에 과부하가 생깁니다.",
    "press-vertical":   "오버헤드 프레스 그립 시 손목이 충분히 신전되는지 확인합니다. 신전 가동범위 제한이 손목 통증의 1차 원인입니다.",
    "press-horizontal": "벤치프레스 그립 시 손목이 충분히 신전되는지 확인합니다. 신전 부족 시 손목이 꺾인 채 부하를 받아 통증이 생깁니다.",
}
WRIST_PURPOSES_TFCC = {
    "deadlift":         "새끼손가락 쪽(척측) 손목에 압박을 주어 TFCC(삼각섬유연골) 손상 여부를 확인합니다. 데드리프트 그립에서 척측 과부하가 잦습니다.",
    "kipping":          "새끼손가락 쪽(척측) 손목에 압박을 주어 TFCC 손상 여부를 확인합니다. 바 동작 중 손목 척측에 반복 부하가 집중됩니다.",
    "pullup":           "새끼손가락 쪽(척측) 손목에 압박을 주어 TFCC 손상 여부를 확인합니다. 풀업 그립 시 손목 척측이 과부하될 수 있습니다.",
    "row":              "새끼손가락 쪽(척측) 손목에 압박을 주어 TFCC 손상 여부를 확인합니다. 당기는 동작에서 손목 척측에 부하가 집중됩니다.",
    "press-vertical":   "새끼손가락 쪽(척측) 손목에 압박을 주어 TFCC 손상 여부를 확인합니다. 오버헤드 자세에서 손목 척측 과부하가 발생할 수 있습니다.",
    "press-horizontal": "새끼손가락 쪽(척측) 손목에 압박을 주어 TFCC 손상 여부를 확인합니다. 바벨 그립 시 손목 척측이 반복 압박됩니다.",
}

def make_wrist_tests(movement_id):
    return [
        {
            "id": "test-wrist-ext-mob",
            "name": "손목 신전 가동성 검사",
            "purpose": WRIST_PURPOSES_MOB[movement_id],
            "steps": [
                "양 손바닥을 맞대고 기도하는 자세를 만드세요",
                "손바닥을 붙인 채로 손목을 아래로 내려 손가락이 바닥을 향하게 하세요",
                "손목이 90도(손가락이 완전히 아래)까지 통증 없이 내려가는지 확인하세요"
            ],
            "note": "손목을 억지로 꺾지 마세요. 통증이 느껴지는 각도를 기억해두세요.",
            "pass_text": "90도까지 통증 없이 내려가요",
            "fail_text": "내려가는 중 통증이 있거나 90도까지 안 내려가요",
            "pass_next": "test:test-wrist-tfcc",
            "fail_next": "cause:cause-a",
            "video_url": ""
        },
        {
            "id": "test-wrist-tfcc",
            "name": "TFCC 압박 검사 — 새끼손가락 쪽 통증",
            "purpose": WRIST_PURPOSES_TFCC[movement_id],
            "steps": [
                "팔을 앞으로 뻗고 손바닥이 위를 향하게 하세요",
                "손목을 새끼손가락 방향(척측)으로 비틀어 꺾으세요",
                "반대 손 엄지로 손목 새끼손가락 쪽 뼈 아래를 가볍게 눌러보세요"
            ],
            "note": "새끼손가락 쪽 손목에서 찌릿하거나 욱신거리면 양성입니다.",
            "pass_text": "새끼손가락 쪽에 통증이 없어요",
            "fail_text": "새끼손가락 쪽 손목이 찌릿하거나 아파요",
            "pass_next": "cause:cause-b",
            "fail_next": "cause:cause-c",
            "video_url": ""
        }
    ]

# ─── 주입 ─────────────────────────────────────────────────────────────────
ELBOW_MOVEMENTS = ["pullup", "kipping", "row", "press-vertical", "press-horizontal"]
WRIST_MOVEMENTS = ["deadlift", "kipping", "pullup", "row", "press-vertical", "press-horizontal"]

def inject(movement_id, site_id, tests):
    path = os.path.join(base, f"data/movements/{movement_id}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    updated = False
    for site in data.get("pain_sites", []):
        if not isinstance(site, dict): continue
        if site.get("id") == site_id:
            if site.get("tests", []) == [] or site.get("tests") is None:
                site["tests"] = tests
                updated = True
                print(f"[OK] {movement_id}/{site_id} → {len(tests)}개 주입")
            else:
                print(f"[SKIP] {movement_id}/{site_id} — 이미 테스트 있음")
    if updated:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

for m in ELBOW_MOVEMENTS:
    inject(m, "elbow", make_elbow_tests(m))

for m in WRIST_MOVEMENTS:
    inject(m, "wrist", make_wrist_tests(m))

print("완료")
