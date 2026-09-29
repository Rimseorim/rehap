import json

PHASE_PATH = 'data/phase-exercises.json'
INDEX_PATH = 'index.html'

PHASE_B = [
    {
        "order": 1, "type": "수평프레스",
        "name": "인클라인 푸시업 플러스", "equipment": "벽 또는 높은 벤치",
        "target_area": "대흉근, 전거근, 삼두근",
        "why": "눕지 않고 서서 또는 높은 곳을 짚고 미는 패턴을 먼저 확인합니다. 팔꿈치를 옆으로 벌리지 않으면 어깨가 옆으로 벌어지는 자세를 피하고, 마지막에 날개뼈를 앞으로 더 밀어 겨드랑이 옆 근육(전거근)을 씁니다.",
        "sets": "12회 · 3세트",
        "cue": "팔꿈치를 옆으로 펼치지 말고, 몸통과 45도쯤 각도를 유지하며 내리세요. 다 민 뒤 날개뼈를 앞으로 살짝 더 밀어내세요. 허리가 꺾이지 않게 배에 힘을 주세요.",
        "how": [
            "벽이나 높은 벤치에 손을 어깨 너비보다 약간 넓게 짚으세요",
            "팔꿈치를 옆으로 펼치지 말고 몸통과 45도쯤 각도를 유지한 채 가슴을 낮췄다가 미세요",
            "다 민 뒤 날개뼈를 앞으로 살짝 더 밀어내세요",
            "12회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 Phase A로 복귀."
    },
    {
        "order": 2, "type": "수평프레스",
        "name": "덤벨 플로어 프레스", "equipment": "가벼운 덤벨",
        "target_area": "대흉근, 전면 삼각근, 삼두근",
        "why": "바닥에 누워 하면 팔꿈치가 바닥에 닿아 더 깊이 내려가지 않으므로, 어깨가 뒤로 과하게 젖혀지는 것을 자동으로 막습니다. 손바닥이 마주 보는 중립 그립은 어깨 위 공간을 덜 좁힙니다. 통증 구간을 통제된 속도로 지나가는 훈련입니다.",
        "sets": "10회 · 3세트",
        "cue": "손바닥이 마주 보게 잡고, 팔꿈치는 몸통에서 45도쯤 벌려 바닥에 살짝 닿게 하세요. 내릴 때는 툭 떨어뜨리지 말고 2~3초 동안 천천히 버티며 내리세요. 밀어 올릴 때도 어깨를 앞으로 내밀지 말고, 날개뼈가 바닥에서 떨어지지 않게 하세요. 찌릿한 높이가 있으면 그 직전에서 멈추세요.",
        "how": [
            "바닥에 누워 무릎을 세우고 덤벨을 가슴 옆에 손바닥이 마주 보게 잡으세요",
            "팔꿈치를 몸통에서 45도쯤 벌린 채 덤벨을 위로 미세요",
            "2~3초 동안 천천히 내려 팔꿈치가 바닥에 살짝 닿게 하세요",
            "10회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 구간 통과 시도가 3회 이상 실패하면 1단계로 복귀."
    },
    {
        "order": 3, "type": "수평프레스",
        "name": "덤벨 벤치프레스", "equipment": "가벼운 덤벨, 벤치",
        "target_area": "대흉근, 전면 삼각근, 삼두근",
        "why": "벤치 위에서 바닥 없이 깊이를 스스로 통제합니다. 통증 없이 플로어 프레스가 가능해졌으니, 벤치 자세에서 범위를 조금씩 넓힙니다.",
        "sets": "10회 · 3세트",
        "cue": "10회 이상 무리 없이 드는 가벼운 무게를 고르세요. 손바닥이 마주 보게 잡으세요. 덤벨이 가슴 옆선 아래로 내려가지 않게 하고, 팔꿈치는 몸통에서 45도쯤 벌리세요. 내릴 때는 2~3초 동안 천천히 버티며 내리세요. 밀어 올릴 때도 어깨를 앞으로 내밀지 말고, 모아 둔 날개뼈가 벤치에서 떨어지지 않게 하세요.",
        "how": [
            "벤치에 누워 날개뼈를 모아 아래로 살짝 내리세요",
            "덤벨을 가슴 옆에 손바닥이 마주 보게 잡고 위로 미세요",
            "2~3초 동안 천천히 내리되 가슴 옆선 아래로는 내리지 마세요",
            "10회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 2단계로 복귀."
    },
    {
        "order": 4, "type": "수평프레스",
        "name": "바벨 벤치프레스", "equipment": "바벨, 벤치, 세이프티 바(또는 보조자)",
        "target_area": "대흉근, 전면 삼각근, 삼두근",
        "why": "실제 훈련 도구로 전환합니다. 바는 양손이 고정돼 팔꿈치가 벌어지기 쉬워서, 부상 전 무게의 30~40%에서 시작합니다.",
        "sets": "5회 · 3세트, 부상 전 무게의 30~40%에서 시작",
        "cue": "바를 잡는 너비는 바를 내렸을 때 팔뚝이 바닥과 수직이 되는 너비로 하세요. 바는 쇄골(빗장뼈) 쪽이 아니라 가슴뼈(흉골) 아래쪽, 명치 바로 위에 닿게 하세요. 팔꿈치는 몸통에서 45도쯤 벌리고, 밀어 올릴 때도 모아 둔 날개뼈가 벤치에서 떨어지지 않게 하세요. 바를 내릴 때는 2~3초 동안 천천히 버티며 내리세요. 통증 없이 2회 연속 세션과 다음날 악화가 없으면 무게를 주차별 5~10%씩 올려 부상 전 무게로 돌아가세요.",
        "how": [
            "벤치에 누워 날개뼈를 모아 아래로 살짝 내리고 엉덩이는 벤치에 붙이세요",
            "팔뚝이 바닥과 수직이 되는 너비로 빈 바나 가벼운 바를 잡으세요",
            "바를 가슴뼈 아래쪽, 명치 바로 위로 2~3초 동안 천천히 내리세요",
            "몸통에서 45도쯤 벌린 팔꿈치로 바를 위로 미세요",
            "5회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행 + 다음날 통증 악화 없음. 탈출 경로: 통증 재현 시 3단계로 복귀하고 무게 증가를 1주 더 미루세요."
    }
]

MOVEMENT_ID = 'horizontal-press'
BUNDLED_ID = 'press-horizontal'


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
