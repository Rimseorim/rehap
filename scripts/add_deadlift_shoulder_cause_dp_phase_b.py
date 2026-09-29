import json

PHASE_PATH = 'data/phase-exercises.json'
INDEX_PATH = 'index.html'

PHASE_B = [
    {
        "order": 1, "type": "데드리프트",
        "name": "맨몸 힙 힌지", "equipment": "없음",
        "target_area": "햄스트링, 대둔근",
        "why": "어깨를 거의 쓰지 않는 하체 패턴(엉덩이 접기, 힙 힌지)을 먼저 확인합니다. 팔은 힘을 빼고 늘어뜨려 어깨가 통증 구간 밖에 머물게 합니다. 상체를 깊이 숙이면 늘어뜨린 팔이 몸통 기준으로 앞쪽 위로 올라가 통증 구간에 닿을 수 있어서, 통증이 없는 깊이까지만 내려갑니다.",
        "sets": "10회 · 3세트",
        "cue": "팔에 힘은 빼되, 어깨가 바닥 쪽으로 말려 떨어지지 않게 겨드랑이 아래에 살짝 힘을 유지하세요. 어깨가 아픈 깊이 전에서 멈추세요.",
        "how": [
            "발을 어깨 너비로 서고 무릎을 살짝 구부리세요",
            "팔은 자연스럽게 늘어뜨리되, 겨드랑이 아래에 살짝 힘을 유지하세요",
            "엉덩이를 뒤로 빼며 상체를 앞으로 기울이세요. 어깨가 아프기 전 깊이에서 멈추세요",
            "10회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 Phase A로 복귀."
    },
    {
        "order": 2, "type": "데드리프트",
        "name": "밴드 스트레이트암 당기기", "equipment": "약한 저항 밴드",
        "target_area": "광배근, 후면 삼각근, 회전근개",
        "why": "힙 힌지 자세에서 팔을 편 채 밴드를 허벅지 쪽으로 당기며 등 옆 근육(광배근)을 조이는 훈련입니다. 데드리프트에서 이 근육이 어깨를 제자리에 잡아 줍니다. 완전히 멈춘 상태에서 천천히 하므로, 통증이 나는 높이를 정확히 확인하며 통과할 수 있습니다.",
        "sets": "10회 · 3세트",
        "cue": "힙 힌지 자세에서 완전히 멈춘 뒤, 팔을 편 채 밴드를 허벅지 쪽으로 당겨 등 옆을 조이세요. 팔을 뒤로 젖히거나 반동을 쓰지 마세요.",
        "how": [
            "밴드를 앞쪽 높은 곳에 걸고, 양손으로 잡은 채 힙 힌지 자세로 내려가세요",
            "완전히 멈춘 상태에서 팔을 편 채 밴드를 허벅지 쪽으로 천천히 당겨 등 옆을 조이세요",
            "찌릿한 높이가 있으면 그 아래에서 멈추세요",
            "10회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 높이를 3회 이상 넘지 못하면 1단계로 복귀."
    },
    {
        "order": 3, "type": "데드리프트",
        "name": "덤벨 데드리프트", "equipment": "가벼운 덤벨",
        "target_area": "햄스트링, 대둔근, 광배근",
        "why": "손에 무게를 쥐고 힙 힌지에 부하를 처음 얹습니다. 덤벨이 몸에서 멀어지면 어깨가 앞으로 끌려가므로, 등 옆 근육을 조여 몸에 붙여 둡니다.",
        "sets": "10회 · 3세트",
        "cue": "10회 이상 무리 없이 드는 가벼운 무게를 고르세요. 양쪽 겨드랑이에 신문지를 끼운 듯 등 옆을 조인 채, 덤벨이 허벅지를 따라 미끄러지게 내리세요. 손목과 팔 힘으로 끌지 마세요.",
        "how": [
            "가벼운 덤벨을 양손에 들고 허벅지 앞에 두세요",
            "겨드랑이에 신문지를 끼운 듯 등 옆을 조이세요",
            "덤벨을 허벅지에 붙인 채 엉덩이를 뒤로 빼며 내리세요",
            "10회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 2단계로 복귀."
    },
    {
        "order": 4, "type": "데드리프트",
        "name": "빈 바벨 데드리프트", "equipment": "바벨",
        "target_area": "햄스트링, 대둔근, 광배근, 코어",
        "why": "실제 훈련 도구로 전환합니다. 데드리프트는 오버헤드 동작보다 어깨 충돌 위험이 낮습니다. 다만 맨 위에서 어깨를 뒤로 젖히면 어깨 앞쪽에 당기는 부담이 생기므로, 부상 전 무게의 30~40%로 보수적으로 시작합니다.",
        "sets": "5회 · 3세트, 부상 전 무게의 30~40%에서 시작",
        "cue": "맨 위에서는 엉덩이를 조여 상체를 곧게 세운 지점에서 바로 멈추세요. 어깨를 뒤로 넘기거나 상체를 젖히지 마세요.",
        "how": [
            "빈 바벨을 정강이 앞에 두고 힙 힌지 자세를 잡으세요",
            "바를 몸에 붙인 채 들어 올리세요",
            "맨 위에서 엉덩이를 조여 상체를 곧게 세우고 멈추세요. 어깨는 뒤로 넘기지 마세요",
            "5회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행 + 다음날 통증 악화 없음. 탈출 경로: 통증 재현 시 3단계로 복귀하고 무게 증가를 1주 더 미루세요."
    }
]


def find_stage(root_movement):
    ps = next(p for p in root_movement['pain_sites'] if p['id'] == 'shoulder')
    c = next(x for x in ps['causes'] if x['id'] == 'cause-dp')
    return c['route']['stages'][0]


# 1) data/phase-exercises.json
with open(PHASE_PATH, encoding='utf-8') as f:
    d = json.load(f)
mv = next(m for m in d['movements'] if m['id'] == 'deadlift')
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
st_b = find_stage(bundled['deadlift'])
assert not st_b.get('phase_b'), 'index.html phase_b가 비어있지 않음, 중단'
st_b['phase_b'] = PHASE_B
new_raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
html = html[:start] + new_raw + html[start + length:]
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

# 검증
with open(PHASE_PATH, encoding='utf-8') as f:
    d2 = json.load(f)
n1 = len(find_stage(next(m for m in d2['movements'] if m['id'] == 'deadlift'))['phase_b'])
with open(INDEX_PATH, encoding='utf-8') as f:
    h2 = f.read()
s2 = h2.index('BUNDLED = ') + len('BUNDLED = ')
b2, _ = json.JSONDecoder().raw_decode(h2[s2:])
n2 = len(find_stage(b2['deadlift'])['phase_b'])
print(f'{"OK" if n1 == 4 and n2 == 4 else "ERR"} deadlift/shoulder/cause-dp phase_b data={n1} index={n2}')
