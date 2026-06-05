"""
어깨 직접 테스트 주입 스크립트
각 동작의 통증 패턴에 맞춘 1~2개 테스트
"""
import json

# 동작별 어깨 테스트 정의
TESTS = {
    "squat": [
        {
            "id": "test-shoulder-arc",
            "name": "통증 호弧(Painful Arc) 검사",
            "purpose": "팔을 옆으로 올릴 때 60~120도 구간에서 찝히는 통증이 있는지 확인합니다. 이 구간 통증은 어깨 충돌의 핵심 신호입니다.",
            "steps": [
                "팔을 완전히 내린 상태에서 시작하세요",
                "팔꿈치를 편 채 천천히 옆으로 들어 올리세요",
                "60~120도 구간(어깨 높이 전후)에서 통증이 있는지 확인하세요"
            ],
            "note": "양쪽 모두 해보세요. 아픈 쪽을 집중 확인합니다.",
            "pass_text": "60~120도 구간을 통증 없이 지나가요",
            "fail_text": "올리는 중 60~120도 구간에서 찝히거나 아파요",
            "pass_next": "cause:cause-case1",
            "fail_next": "cause:cause-dp",
            "video_url": ""
        },
        {
            "id": "test-shoulder-ext-rot",
            "name": "어깨 외회전 가동성 검사",
            "purpose": "팔꿈치를 90도로 구부린 채 외회전이 충분히 되는지 확인합니다. 백스쿼트 랙 포지션에서 어깨가 찝히는 주요 원인입니다.",
            "steps": [
                "팔꿈치를 90도로 구부리고 어깨 높이로 드세요",
                "팔꿈치 위치를 고정한 채 손을 천장 방향으로 돌리세요",
                "통증 없이 손이 어깨와 나란한 높이까지 올라가는지 확인하세요"
            ],
            "note": "억지로 올리지 마세요. 통증이 오기 직전 범위만 확인합니다.",
            "pass_text": "손이 어깨 수평 이상으로 올라가고 찝힘이 없어요",
            "fail_text": "손이 잘 안 올라가거나 찝히는 느낌이 있어요",
            "pass_next": "cause:cause-case4",
            "fail_next": "cause:cause-case3",
            "video_url": ""
        }
    ],
    "deadlift": [
        {
            "id": "test-shoulder-arc",
            "name": "통증 호弧(Painful Arc) 검사",
            "purpose": "팔을 옆으로 올릴 때 60~120도 구간에서 찝히는 통증이 있는지 확인합니다. 이 구간 통증은 어깨 충돌의 핵심 신호입니다.",
            "steps": [
                "팔을 완전히 내린 상태에서 시작하세요",
                "팔꿈치를 편 채 천천히 옆으로 들어 올리세요",
                "60~120도 구간(어깨 높이 전후)에서 통증이 있는지 확인하세요"
            ],
            "note": "양쪽 모두 해보세요. 아픈 쪽을 집중 확인합니다.",
            "pass_text": "60~120도 구간을 통증 없이 지나가요",
            "fail_text": "올리는 중 60~120도 구간에서 찝히거나 아파요",
            "pass_next": "cause:cause-case1",
            "fail_next": "cause:cause-dp",
            "video_url": ""
        },
        {
            "id": "test-shoulder-int-rot",
            "name": "어깨 내회전 저항 검사",
            "purpose": "데드리프트 오버핸드 그립 자세에서 가해지는 내회전 부하를 재현합니다. 회전근개 강도와 통증 여부를 확인합니다.",
            "steps": [
                "팔꿈치를 90도로 구부리고 옆구리에 붙이세요",
                "반대 손으로 손목 안쪽을 가볍게 잡아 저항을 주세요",
                "저항을 이기며 손을 배 쪽으로 돌리세요 (내회전)"
            ],
            "note": "양쪽을 비교하세요. 한쪽만 약하거나 통증이 있으면 양성입니다.",
            "pass_text": "저항을 이기며 통증 없이 내회전이 돼요",
            "fail_text": "내회전 시 통증이 있거나 힘이 많이 빠져요",
            "pass_next": "cause:cause-case1",
            "fail_next": "cause:cause-dp",
            "video_url": ""
        }
    ],
    "pullup": [
        {
            "id": "test-shoulder-flex",
            "name": "능동 어깨 굴곡 검사",
            "purpose": "팔을 머리 위로 완전히 들 수 있는지 확인합니다. 풀업 시작 자세(데드 행) 진입에 필요한 기본 가동범위입니다.",
            "steps": [
                "양팔을 앞으로 뻗고 시작하세요",
                "팔꿈치를 편 채 천천히 머리 위로 들어 올리세요",
                "통증 없이 귀 옆까지 올라가는지 확인하세요"
            ],
            "note": "허리가 과도하게 젖혀지지 않도록 주의하세요.",
            "pass_text": "통증 없이 귀 옆(180도)까지 올라가요",
            "fail_text": "올리는 중 통증이 있거나 귀 옆까지 안 올라가요",
            "pass_next": "cause:cause-case4",
            "fail_next": "cause:cause-case1",
            "video_url": ""
        },
        {
            "id": "test-shoulder-hang",
            "name": "데드 행(Dead Hang) 부하 검사",
            "purpose": "바에 매달린 상태에서 어깨가 통증 없이 부하를 버티는지 확인합니다. 풀업 전 기본 어깨 안정성 검사입니다.",
            "steps": [
                "철봉이나 링에 오버핸드 그립으로 매달리세요",
                "어깨를 귀 쪽으로 올리지 말고 자연스럽게 늘어뜨리세요",
                "10~15초 유지하며 통증 여부를 확인하세요"
            ],
            "note": "발을 바닥에 살짝 딛어 체중을 일부 지지해도 됩니다.",
            "pass_text": "15초 매달리는 동안 통증이 없어요",
            "fail_text": "매달리는 즉시 또는 도중 어깨가 아파요",
            "pass_next": "cause:cause-case2",
            "fail_next": "cause:cause-dp",
            "video_url": ""
        }
    ],
    "kipping": [
        {
            "id": "test-shoulder-flex",
            "name": "능동 어깨 굴곡 검사",
            "purpose": "팔을 머리 위로 완전히 들 수 있는지 확인합니다. 키핑의 전방 스윙 국면에서 필요한 기본 가동범위입니다.",
            "steps": [
                "양팔을 앞으로 뻗고 시작하세요",
                "팔꿈치를 편 채 천천히 머리 위로 들어 올리세요",
                "통증 없이 귀 옆까지 올라가는지 확인하세요"
            ],
            "note": "허리가 과도하게 젖혀지지 않도록 주의하세요.",
            "pass_text": "통증 없이 귀 옆(180도)까지 올라가요",
            "fail_text": "올리는 중 통증이 있거나 귀 옆까지 안 올라가요",
            "pass_next": "cause:cause-case4",
            "fail_next": "cause:cause-case1",
            "video_url": ""
        },
        {
            "id": "test-shoulder-ext",
            "name": "어깨 후방 신전 가동성 검사",
            "purpose": "팔을 몸 뒤로 뻗을 때 통증이 없는지 확인합니다. 키핑 후방 스윙 국면에서 어깨 과신전이 필요합니다.",
            "steps": [
                "허리를 세우고 양팔을 옆에 내려두세요",
                "팔꿈치를 편 채 양팔을 등 뒤쪽으로 최대한 들어 올리세요",
                "통증 없이 들어 올릴 수 있는 높이를 확인하세요"
            ],
            "note": "상체가 앞으로 숙여지지 않도록 허리를 세우세요.",
            "pass_text": "등 뒤로 팔이 올라갈 때 통증이 없어요",
            "fail_text": "등 뒤로 올릴 때 어깨가 아프거나 많이 제한돼요",
            "pass_next": "cause:cause-case2",
            "fail_next": "cause:cause-case3",
            "video_url": ""
        }
    ],
    "row": [
        {
            "id": "test-shoulder-arc",
            "name": "통증 호弧(Painful Arc) 검사",
            "purpose": "팔을 옆으로 올릴 때 60~120도 구간에서 찝히는 통증이 있는지 확인합니다. 로우 동작 중 어깨 충돌 여부를 선별합니다.",
            "steps": [
                "팔을 완전히 내린 상태에서 시작하세요",
                "팔꿈치를 편 채 천천히 옆으로 들어 올리세요",
                "60~120도 구간(어깨 높이 전후)에서 통증이 있는지 확인하세요"
            ],
            "note": "양쪽 모두 해보세요. 아픈 쪽을 집중 확인합니다.",
            "pass_text": "60~120도 구간을 통증 없이 지나가요",
            "fail_text": "올리는 중 60~120도 구간에서 찝히거나 아파요",
            "pass_next": "cause:cause-case1",
            "fail_next": "cause:cause-dp",
            "video_url": ""
        },
        {
            "id": "test-shoulder-h-abd",
            "name": "수평 외전 저항 검사",
            "purpose": "팔을 수평으로 벌릴 때 저항을 버티는 능력을 확인합니다. 로우에서 어깨를 뒤로 당기는 후방 회전근개와 후삼각근 기능입니다.",
            "steps": [
                "팔을 앞으로 뻗어 어깨 높이로 수평을 유지하세요",
                "반대 손으로 팔꿈치 안쪽에 가볍게 저항을 주세요",
                "저항을 이기며 팔을 옆으로 벌려보세요"
            ],
            "note": "저항의 강도와 통증 여부를 양쪽 비교하세요.",
            "pass_text": "저항을 이기며 통증 없이 팔을 벌릴 수 있어요",
            "fail_text": "힘이 많이 빠지거나 통증이 있어요",
            "pass_next": "cause:cause-case2",
            "fail_next": "cause:cause-dp",
            "video_url": ""
        }
    ],
    "press-vertical": [
        {
            "id": "test-shoulder-flex",
            "name": "능동 어깨 굴곡 검사",
            "purpose": "팔을 머리 위로 완전히 들 수 있는지 확인합니다. 오버헤드 프레스의 최종 자세(팔꿈치 펴고 바 머리 위)에 필요한 기본 가동범위입니다.",
            "steps": [
                "양팔을 앞으로 뻗고 시작하세요",
                "팔꿈치를 편 채 천천히 머리 위로 들어 올리세요",
                "통증 없이 귀 옆까지 올라가는지 확인하세요"
            ],
            "note": "허리가 과도하게 젖혀지지 않도록 주의하세요.",
            "pass_text": "통증 없이 귀 옆(180도)까지 올라가요",
            "fail_text": "올리는 중 통증이 있거나 귀 옆까지 안 올라가요",
            "pass_next": "cause:cause-case4",
            "fail_next": "cause:cause-case1",
            "video_url": ""
        },
        {
            "id": "test-shoulder-empty-can",
            "name": "빈 캔(Empty Can) 검사",
            "purpose": "어깨를 45도 벌리고 엄지를 아래로 향한 채 올릴 때 통증과 근력을 확인합니다. 오버헤드 동작의 핵심인 극상근(회전근개) 기능 검사입니다.",
            "steps": [
                "팔을 45도 비스듬히 벌려 어깨 높이로 유지하세요",
                "엄지손가락을 바닥 방향으로 돌리세요 (빈 캔 기울이는 동작)",
                "반대 손으로 팔목에 가볍게 저항을 주며 버텨보세요"
            ],
            "note": "양쪽을 비교하세요. 힘이 빠지거나 통증이 있으면 양성입니다.",
            "pass_text": "저항을 이기며 통증 없이 자세를 유지해요",
            "fail_text": "저항에 팔이 밀리거나 어깨가 아파요",
            "pass_next": "cause:cause-case2",
            "fail_next": "cause:cause-dp",
            "video_url": ""
        }
    ],
    "press-horizontal": [
        {
            "id": "test-shoulder-arc",
            "name": "통증 호弧(Painful Arc) 검사",
            "purpose": "팔을 옆으로 올릴 때 60~120도 구간에서 찝히는 통증이 있는지 확인합니다. 수평 프레스 하강 시 어깨 충돌 여부를 선별합니다.",
            "steps": [
                "팔을 완전히 내린 상태에서 시작하세요",
                "팔꿈치를 편 채 천천히 옆으로 들어 올리세요",
                "60~120도 구간(어깨 높이 전후)에서 통증이 있는지 확인하세요"
            ],
            "note": "양쪽 모두 해보세요. 아픈 쪽을 집중 확인합니다.",
            "pass_text": "60~120도 구간을 통증 없이 지나가요",
            "fail_text": "올리는 중 60~120도 구간에서 찝히거나 아파요",
            "pass_next": "cause:cause-case1",
            "fail_next": "cause:cause-dp",
            "video_url": ""
        },
        {
            "id": "test-shoulder-h-add",
            "name": "수평 내전 저항 검사",
            "purpose": "팔을 수평으로 앞쪽으로 모을 때 저항을 버티는 능력을 확인합니다. 벤치프레스의 가슴 수축 국면에서 필요한 어깨 전방 안정성입니다.",
            "steps": [
                "팔을 옆으로 수평으로 벌리세요",
                "반대 손을 팔꿈치 바깥쪽에 대고 저항을 주세요",
                "저항을 이기며 팔을 앞으로 모아보세요"
            ],
            "note": "팔꿈치는 약간 구부려도 됩니다. 통증 위치를 정확히 확인하세요.",
            "pass_text": "저항을 이기며 통증 없이 팔을 모을 수 있어요",
            "fail_text": "힘이 많이 빠지거나 어깨 앞쪽이 아파요",
            "pass_next": "cause:cause-case2",
            "fail_next": "cause:cause-dp",
            "video_url": ""
        }
    ]
}

MOVEMENT_FILES = {
    "squat": "data/movements/squat.json",
    "deadlift": "data/movements/deadlift.json",
    "pullup": "data/movements/pullup.json",
    "kipping": "data/movements/kipping.json",
    "row": "data/movements/row.json",
    "press-vertical": "data/movements/press-vertical.json",
    "press-horizontal": "data/movements/press-horizontal.json",
}

import sys
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for movement_id, rel_path in MOVEMENT_FILES.items():
    path = os.path.join(base, rel_path)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    updated = False
    for site in data.get("pain_sites", []):
        if site.get("id") == "shoulder":
            if site.get("tests") == [] or site.get("tests") is None:
                site["tests"] = TESTS[movement_id]
                updated = True
                print(f"[OK] {movement_id}/shoulder → {len(TESTS[movement_id])}개 주입")
            else:
                print(f"[SKIP] {movement_id}/shoulder — 이미 테스트 있음")

    if updated:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print("완료")
