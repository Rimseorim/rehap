import json

PHASE_PATH = 'data/phase-exercises.json'
INDEX_PATH = 'index.html'

PHASE_B = [
    {
        "order": 1, "type": "로우",
        "name": "서서 밴드 로우", "equipment": "저항 밴드(허리 높이에 고정)",
        "target_area": "광배근, 중부승모근, 능형근",
        "why": "상체를 숙이지 않고 서서 당기는 패턴을 먼저 확인합니다. 밴드를 허리 높이에 걸면 팔이 앞쪽 낮은 각도에 머물러 통증 구간 밖에서 등 근육을 쓸 수 있습니다.",
        "sets": "12회 · 3세트",
        "cue": "팔꿈치를 몸통 가까이 붙여 당기고, 몸통 옆선까지만 오면 멈추세요. 몸 뒤로 젖히지 마세요. 어깨를 귀 쪽으로 으쓱하지 마세요.",
        "how": [
            "밴드를 허리 높이에 걸고 양손으로 잡고 서세요",
            "날개뼈를 아래로 살짝 내린 채 팔꿈치를 몸통 옆으로 당기세요",
            "몸통 옆선까지만 당기고 천천히 되돌리세요",
            "12회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 Phase A로 복귀."
    },
    {
        "order": 2, "type": "로우",
        "name": "힌지 자세 밴드 로우", "equipment": "저항 밴드",
        "target_area": "광배근, 중부승모근, 후면 삼각근, 햄스트링",
        "why": "실제 로우 자세(엉덩이 접기, 힌지)로 넘어갑니다. 상체를 숙일수록 팔이 통증 구간으로 올라가므로, 아픈 깊이 전까지만 숙입니다. 자세를 완전히 멈춘 뒤 당기기만 따로 해서 반동 없이 통제합니다.",
        "sets": "10회 · 3세트",
        "cue": "상체를 어깨가 아프기 전 깊이까지만 숙이세요. 자세를 멈춘 뒤에만 당기고, 몸으로 반동을 주지 마세요. 팔꿈치는 몸통 옆선까지만 당기고 몸 뒤로 젖히지 마세요.",
        "how": [
            "밴드를 낮은 곳에 걸고 무릎을 살짝 굽혀 엉덩이를 뒤로 빼며 상체를 숙이세요(어깨가 아프기 전 깊이까지)",
            "자세를 완전히 멈추세요",
            "팔꿈치를 몸통 옆선까지 당겼다 천천히 되돌리세요",
            "10회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 1단계로 복귀."
    },
    {
        "order": 3, "type": "로우",
        "name": "덤벨 로우", "equipment": "가벼운 덤벨, 벤치 또는 박스",
        "target_area": "광배근, 중부승모근, 후면 삼각근",
        "why": "손에 무게를 쥐고 부하를 처음 얹습니다. 한 손을 벤치에 짚어 몸통을 받치면 허리와 균형 부담이 줄어 어깨 반응에만 집중할 수 있습니다. 손바닥이 마주 보는 중립 그립은 어깨 위 공간을 덜 좁힙니다.",
        "sets": "10회 · 3세트(양쪽)",
        "cue": "10회 이상 무리 없이 드는 가벼운 무게를 고르세요. 손바닥이 몸통을 마주 보게 잡으세요(중립 그립). 팔꿈치는 몸통 옆선까지만 당기고 몸 뒤로 젖히지 마세요. 아픈 높이가 있으면 벤치를 높이거나 상체를 더 세우세요.",
        "how": [
            "한 손과 한쪽 무릎을 벤치에 짚고, 다른 손에 덤벨을 손바닥이 몸통을 마주 보게 잡으세요",
            "날개뼈를 아래로 살짝 내리고 팔꿈치를 몸통 옆선까지 당기세요",
            "천천히 내리세요",
            "10회 · 3세트(양쪽)"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 2단계로 복귀."
    },
    {
        "order": 4, "type": "로우",
        "name": "바벨 로우", "equipment": "바벨",
        "target_area": "광배근, 중부승모근, 후면 삼각근, 척추기립근",
        "why": "실제 훈련 도구로 전환합니다. 양손이 동시에 당겨져 어깨 부담이 커질 수 있어, 부상 전 무게의 30~40%에서 시작해 주차별로 올립니다.",
        "sets": "5회 · 3세트, 부상 전 무게의 30~40%에서 시작",
        "cue": "바를 허벅지 가까이 붙여 아랫배 쪽으로 당기세요. 팔꿈치는 몸통에서 벌리지 말고 옆선까지만 당기세요. 어깨가 아픈 깊이 전까지만 숙이고, 어깨를 으쓱하지 마세요. 통증 없이 2회 연속 세션과 다음날 악화가 없으면 무게를 주차별 10%씩 올려 부상 전 무게로 돌아가세요.",
        "how": [
            "빈 바나 가벼운 바를 잡고 어깨가 아프기 전 깊이까지 힌지 자세로 숙이세요",
            "바를 허벅지 가까이 붙여 아랫배 쪽으로 당기고 팔꿈치는 몸통 옆선까지만 당기세요",
            "천천히 내리세요",
            "5회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행 + 다음날 통증 악화 없음. 탈출 경로: 통증 재현 시 3단계로 복귀하고 무게 증가를 1주 더 미루세요."
    }
]

MOVEMENT_ID = 'row'


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
st_b = find_stage(bundled[MOVEMENT_ID])
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
n2 = len(find_stage(b2[MOVEMENT_ID])['phase_b'])
print(f'{"OK" if n1 == 4 and n2 == 4 else "ERR"} {MOVEMENT_ID}/shoulder/cause-dp phase_b data={n1} index={n2}')
