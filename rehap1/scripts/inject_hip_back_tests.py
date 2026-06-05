"""
고관절·허리 직접 테스트 주입 스크립트
고관절(squat·lunge): FADIR → Thomas 체인 (cause-a FAI / b 굴곡근 / c 중둔근)
고관절(deadlift):    Seated Hamstring → FADIR 체인 (cause-a 햄스트링 / b FAI / c 굴곡근)
허리(kipping):       서서 과신전 검사 1개 (cause-a 과신전 / b 코어)
허리(pullup):        Hollow Body Hold 1개 (cause-a 광배근 보상 / b 코어)
"""
import json, os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─── 고관절: squat·lunge (같은 cause 구조) ──────────────────────────────────
SQUAT_LUNGE_HIP = {
    "squat": "스쿼트 바닥 자세에서 사타구니·고관절에 찝힘이 생기는 FAI(고관절 임핀지먼트) 여부를 누운 자세로 재현합니다.",
    "lunge": "런지 앞발 착지 시 사타구니·고관절에 찝힘이 생기는 FAI(고관절 임핀지먼트) 여부를 누운 자세로 재현합니다.",
}
SQUAT_LUNGE_THOMAS = {
    "squat": "스쿼트 하강 시 고관절 앞쪽(사타구니 아래)이 당기거나 걸리는 굴곡근 단축 여부를 확인합니다.",
    "lunge": "런지 뒷발 자세에서 고관절 앞쪽이 당기는 굴곡근 단축 여부를 확인합니다.",
}

def make_squat_lunge_hip(movement_id):
    return [
        {
            "id": "test-hip-fadir",
            "name": "FADIR 검사 — 고관절 임핀지먼트",
            "purpose": SQUAT_LUNGE_HIP[movement_id],
            "steps": [
                "바닥에 등을 대고 누우세요",
                "아픈 쪽 무릎을 가슴 쪽으로 당기세요 (고관절 굴곡 90도)",
                "무릎을 반대쪽(안쪽)으로 살짝 당기고, 발끝을 안으로 돌리세요 (내전+내회전)"
            ],
            "note": "사타구니 안쪽에서 찝히거나 아프면 양성입니다. 억지로 누르지 마세요.",
            "pass_text": "사타구니에 찝힘이나 통증이 없어요",
            "fail_text": "사타구니 안쪽이 찝히거나 아파요",
            "pass_next": "test:test-hip-thomas",
            "fail_next": "cause:cause-a",
            "video_url": ""
        },
        {
            "id": "test-hip-thomas",
            "name": "토마스(Thomas) 검사 — 고관절 굴곡근 단축",
            "purpose": SQUAT_LUNGE_THOMAS[movement_id],
            "steps": [
                "침대나 테이블 끝에 앉은 뒤 천천히 등을 대고 누우세요",
                "양 무릎을 가슴으로 당겨 안은 채로 허리가 바닥에 붙게 하세요",
                "한 다리를 천천히 내려놓고 반대 무릎은 계속 잡고 있으세요"
            ],
            "note": "내려놓은 다리가 바닥에서 뜨거나 앞쪽(허벅지 위)이 당기면 양성입니다.",
            "pass_text": "내려놓은 다리가 바닥에 닿고 앞쪽 당김이 없어요",
            "fail_text": "다리가 바닥에서 뜨거나 앞쪽이 많이 당겨요",
            "pass_next": "cause:cause-c",
            "fail_next": "cause:cause-b",
            "video_url": ""
        }
    ]

# ─── 고관절: deadlift (다른 cause 구조) ─────────────────────────────────────
DEADLIFT_HIP = [
    {
        "id": "test-hip-hamstring",
        "name": "앉아서 햄스트링 부하 검사 — 좌골결절 통증",
        "purpose": "데드리프트 힌지 자세에서 엉덩이 아래(좌골결절)에 생기는 햄스트링 기시부 통증을 재현합니다.",
        "steps": [
            "의자 끝에 걸터앉아 아픈 쪽 다리를 앞으로 뻗으세요",
            "발끝을 천장 방향으로 당기며 무릎을 최대한 펴세요",
            "상체를 살짝 앞으로 기울여 엉덩이 아래(좌골)에 통증이 오는지 확인하세요"
        ],
        "note": "엉덩이 아래 깊은 곳이 당기거나 아프면 양성입니다. 허리 통증은 별개입니다.",
        "pass_text": "엉덩이 아래에 통증 없이 다리를 뻗을 수 있어요",
        "fail_text": "엉덩이 아래(좌골) 깊은 곳이 당기거나 아파요",
        "pass_next": "test:test-hip-fadir-dl",
        "fail_next": "cause:cause-a",
        "video_url": ""
    },
    {
        "id": "test-hip-fadir-dl",
        "name": "FADIR 검사 — 고관절 임핀지먼트",
        "purpose": "데드리프트 시작 자세에서 사타구니 안쪽에 찝힘이 생기는 FAI 여부를 누운 자세로 재현합니다.",
        "steps": [
            "바닥에 등을 대고 누우세요",
            "아픈 쪽 무릎을 가슴 쪽으로 당기세요 (고관절 굴곡 90도)",
            "무릎을 반대쪽(안쪽)으로 살짝 당기고, 발끝을 안으로 돌리세요 (내전+내회전)"
        ],
        "note": "사타구니 안쪽에서 찝히거나 아프면 양성입니다.",
        "pass_text": "사타구니에 찝힘이나 통증이 없어요",
        "fail_text": "사타구니 안쪽이 찝히거나 아파요",
        "pass_next": "cause:cause-c",
        "fail_next": "cause:cause-b",
        "video_url": ""
    }
]

# ─── 허리: kipping ───────────────────────────────────────────────────────────
KIPPING_BACK = [
    {
        "id": "test-back-ext",
        "name": "서서 요추 과신전 검사",
        "purpose": "키핑 아치 페이즈에서 요추가 과도하게 젖혀지며 생기는 통증을 서서 재현합니다.",
        "steps": [
            "두 발을 어깨 너비로 벌리고 서세요",
            "양손을 허리 뒤에 대고 상체를 천천히 뒤로 젖히세요",
            "허리 통증이 재현되는지 확인하세요"
        ],
        "note": "뒤로 젖힐 때 아프면 양성입니다. 다리 저림이 동반되면 병원 권유입니다.",
        "pass_text": "뒤로 젖혀도 허리 통증이 없어요",
        "fail_text": "뒤로 젖힐 때 허리가 아파요",
        "pass_next": "cause:cause-b",
        "fail_next": "cause:cause-a",
        "video_url": ""
    }
]

# ─── 허리: pullup ────────────────────────────────────────────────────────────
PULLUP_BACK = [
    {
        "id": "test-back-hollow",
        "name": "할로우 바디(Hollow Body) 유지 검사",
        "purpose": "풀업 매달린 자세에서 코어가 허리를 잡아주는지 확인합니다. 코어 약화 여부와 광배근 보상 패턴을 구별합니다.",
        "steps": [
            "바닥에 등을 대고 누워 허리를 바닥에 붙이세요",
            "양팔을 귀 옆으로 뻗고 양 다리를 약 30도 들어 올리세요",
            "허리가 바닥에서 떨어지지 않고 10초를 버티는지 확인하세요"
        ],
        "note": "허리가 바닥에서 뜨면 즉시 멈추세요. 다리 높이는 낮출수록 어렵습니다.",
        "pass_text": "허리가 바닥에 붙은 채 10초를 버텨요",
        "fail_text": "허리가 바닥에서 뜨거나 10초 버티기가 안 돼요",
        "pass_next": "cause:cause-a",
        "fail_next": "cause:cause-b",
        "video_url": ""
    }
]

# ─── 주입 ────────────────────────────────────────────────────────────────────
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

inject("squat",    "hip",        make_squat_lunge_hip("squat"))
inject("lunge",    "hip",        make_squat_lunge_hip("lunge"))
inject("deadlift", "hip",        DEADLIFT_HIP)
inject("kipping",  "lower-back", KIPPING_BACK)
inject("pullup",   "lower-back", PULLUP_BACK)

print("완료")
