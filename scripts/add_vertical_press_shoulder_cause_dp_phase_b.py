import json

PHASE_PATH = 'data/phase-exercises.json'
INDEX_PATH = 'index.html'

PHASE_B = [
    {
        "order": 1, "type": "프레스",
        "name": "서서 밴드 전방 프레스", "equipment": "저항 밴드",
        "target_area": "전면 삼각근, 전거근, 삼두근",
        "why": "머리 위로 올리기 전에 팔이 어깨 높이보다 낮게 머무는 밀기 패턴을 먼저 확인합니다. 어깨가 통증 구간(팔이 어깨 높이 근처로 올라오는 구간) 밖에 있으면서, 날개뼈가 앞으로 밀려나는 감각(전거근)을 익힙니다.",
        "sets": "12회 · 3세트",
        "cue": "팔을 어깨 높이보다 높게 올리지 말고, 가슴 중앙에서 약간 아래쪽 방향으로 뻗으세요. 어깨를 귀에서 멀리 내려 둔 채 시작하고, 갈비뼈가 들리지 않게 배에 힘을 주세요.",
        "how": [
            "밴드를 등 뒤에 걸고 양손으로 가슴 앞에서 잡으세요",
            "어깨를 귀에서 멀리 내려 둔 채 팔을 가슴 중앙에서 약간 아래쪽 방향으로 뻗으세요(어깨 높이보다 낮게)",
            "천천히 되돌리세요",
            "12회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 Phase A로 복귀."
    },
    {
        "order": 2, "type": "프레스",
        "name": "하프 닐링 덤벨 오버헤드 프레스", "equipment": "가벼운 덤벨",
        "target_area": "삼각근, 전거근, 하부승모근, 회전근개",
        "why": "한쪽 무릎을 세운 자세로 몸통을 안정시키고, 통증 직전 높이까지만 올리는 범위 훈련을 합니다. 팔을 몸 정면이 아니라 앞쪽 대각선으로 올리고 손바닥이 마주 보게 잡으면, 어깨 위 공간을 덜 좁힙니다.",
        "sets": "양쪽 각 8회 · 3세트",
        "cue": "손바닥이 마주 보게 잡고, 팔을 몸 정면보다 앞쪽 대각선(약 30도)으로 올리세요. 찌릿한 높이가 있으면 그 직전에서 멈추고, 매주 조금씩만 범위를 늘리세요. 갈비뼈가 들리지 않게 배에 힘을 주세요. 내릴 때는 툭 떨어뜨리지 말고 2~3초 동안 천천히 버티며 어깨 앞으로 내리세요.",
        "how": [
            "한쪽 무릎을 세우고 반대 무릎은 바닥에 대세요",
            "덤벨을 어깨 앞에 손바닥이 마주 보게 잡으세요",
            "팔을 앞쪽 대각선으로 통증 직전 높이까지만 올렸다 내리세요",
            "양쪽 각 8회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 구간 진입 시도가 3회 이상 실패하면 1단계로 복귀."
    },
    {
        "order": 3, "type": "프레스",
        "name": "스탠딩 덤벨 오버헤드 프레스", "equipment": "가벼운 덤벨",
        "target_area": "삼각근, 전거근, 삼두근, 코어",
        "why": "서서 전체 범위로 올립니다. 통증 없이 가능해졌으니 범위를 끝까지 넓혀 실제 프레스 자세를 되찾습니다.",
        "sets": "10회 · 3세트",
        "cue": "10회 이상 무리 없이 드는 가벼운 무게를 고르세요. 손바닥이 마주 보게 잡고 앞쪽 대각선으로 올리세요. 엉덩이를 조여 허리가 젖혀지지 않게 하세요. 아픈 높이가 있으면 그 직전까지만 올리세요. 내릴 때는 툭 떨어뜨리지 말고 2~3초 동안 천천히 버티며 어깨 앞으로 내리세요.",
        "how": [
            "덤벨을 어깨 앞에 손바닥이 마주 보게 잡고 서세요",
            "엉덩이를 조이고 팔을 앞쪽 대각선으로 머리 위까지 올리세요",
            "천천히 내리세요",
            "10회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 2단계로 복귀."
    },
    {
        "order": 4, "type": "프레스",
        "name": "바벨 오버헤드 프레스", "equipment": "바벨",
        "target_area": "삼각근, 전거근, 삼두근, 코어",
        "why": "실제 훈련 도구로 전환합니다. 바벨은 손바닥이 앞을 향하는 그립이라 덤벨보다 어깨를 안쪽으로 돌려, 오버헤드 부담이 가장 큽니다. 부상 전 무게의 30~40%에서 시작합니다(수직 프레스는 다른 동작보다 보수적으로 잡습니다).",
        "sets": "5회 · 3세트, 부상 전 무게의 30~40%에서 시작",
        "cue": "바가 얼굴 앞을 수직으로 지나가게 머리를 살짝 뒤로 빼세요. 엉덩이를 조이고 갈비뼈가 들리지 않게 하세요. 맨 위에서 귀 옆까지 뻗고, 어깨가 아프면 무게를 낮추세요. 바를 내릴 때는 2~3초 동안 천천히 버티며 쇄골 앞으로 내리세요. 통증 없이 2회 연속 세션과 다음날 악화가 없으면 무게를 주차별 5~10%씩 올려 부상 전 무게로 돌아가세요.",
        "how": [
            "어깨너비보다 약간 넓게, 바를 내렸을 때 팔뚝이 바닥과 수직이 되는 너비로 빈 바나 가벼운 바를 잡고 쇄골 앞에 얹으세요",
            "엉덩이를 조이고 머리를 살짝 뒤로 빼며 바를 머리 위로 올리세요",
            "맨 위에서 귀 옆까지 뻗고 천천히 내리세요",
            "5회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행 + 다음날 통증 악화 없음. 탈출 경로: 통증 재현 시 3단계로 복귀하고 무게 증가를 1주 더 미루세요."
    }
]

MOVEMENT_ID = 'vertical-press'
BUNDLED_ID = 'press-vertical'


def find_stage(root_movement):
    ps = next(p for p in root_movement['pain_sites'] if p['id'] == 'shoulder')
    c = next(x for x in ps['causes'] if x['id'] == 'cause-dp')
    return c['route']['stages'][0]


# 1) data/phase-exercises.json
with open(PHASE_PATH, encoding='utf-8') as f:
    d = json.load(f)
mv = next(m for m in d['movements'] if m['id'] == MOVEMENT_ID)
st = find_stage(mv)
assert st.get('phase_b') == [], 'phase_b가 비어있지 않음, 중단'
st['phase_b'] = PHASE_B
with open(PHASE_PATH, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

# 2) index.html BUNDLED (해당 cause만 수정)
with open(INDEX_PATH, encoding='utf-8') as f:
    html = f.read()
start = html.index('BUNDLED = ') + len('BUNDLED = ')
bundled, length = json.JSONDecoder().raw_decode(html[start:])
st_b = find_stage(bundled[BUNDLED_ID])
assert not st_b.get('phase_b'), 'index.html phase_b가 비어있지 않음, 중단'
st_b['phase_b'] = PHASE_B
new_raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
html = html[:start] + new_raw + html[start + length:]
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

# 검증
with open(PHASE_PATH, encoding='utf-8') as f:
    d2 = json.load(f)
n1 = len(find_stage(next(m for m in d2['movements'] if m['id'] == MOVEMENT_ID))['phase_b'])
with open(INDEX_PATH, encoding='utf-8') as f:
    h2 = f.read()
s2 = h2.index('BUNDLED = ') + len('BUNDLED = ')
b2, _ = json.JSONDecoder().raw_decode(h2[s2:])
n2 = len(find_stage(b2[BUNDLED_ID])['phase_b'])
print(f'{"OK" if n1 == 4 and n2 == 4 else "ERR"} {MOVEMENT_ID}/shoulder/cause-dp phase_b data={n1} index={n2}')
