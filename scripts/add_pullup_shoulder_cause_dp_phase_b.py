import json

PHASE_PATH = 'data/phase-exercises.json'
INDEX_PATH = 'index.html'

PHASE_B = [
    {
        "order": 1, "type": "풀업",
        "name": "스탠딩 로우", "equipment": "낮은 바 또는 링",
        "target_area": "광배근, 중부승모근, 능형근",
        "why": "머리 위로 팔을 올리지 않고 당기는 패턴(등 옆 근육(광배근)과 날개뼈 모으기)을 먼저 확인합니다. 바를 낮게 설정해 몸을 기울이면 팔이 통증 구간(가슴 높이 이하) 밖에 머문 채로 풀업의 당기는 감각을 훈련할 수 있습니다.",
        "sets": "10회 · 3세트",
        "cue": "몸을 뒤로 기울이고 발은 바닥에 댄 채 가슴을 바 쪽으로 당기세요. 팔꿈치가 어깨보다 높이 올라가지 않게 하세요.",
        "how": [
            "낮은 바나 링을 어깨너비로 잡고 발은 바닥에 댄 채 몸을 뒤로 기울이세요",
            "가슴을 바 쪽으로 당기며 팔꿈치가 어깨 높이를 넘지 않게 하세요",
            "10회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 Phase A로 복귀."
    },
    {
        "order": 2, "type": "풀업",
        "name": "밴드 보조 액티브 행", "equipment": "강한 보조 밴드",
        "target_area": "하부승모근, 전거근, 광배근, 회전근개",
        "why": "완전히 힘을 뺀 매달리기는 체중 때문에 팔뼈 윗부분이 위로 밀려 올라가, 어깨 위 뼈(견봉) 아래 공간이 좁아집니다. 특히 팔을 끝까지 뻗은 맨 위 구간에서 충돌 위험이 가장 큽니다. 날개뼈 아래쪽 근육(하부 승모근)과 겨드랑이 옆 근육(전거근)을 살짝 써서 날개뼈를 내린 채(액티브 행) 밴드로 체중을 받치면, 같은 각도에서도 눌림이 줄어듭니다.",
        "sets": "20~30초 매달리기 · 3세트",
        "cue": "팔에 힘을 완전히 빼지 마세요. 귀와 어깨가 멀어지도록 날개뼈를 아래로 살짝 내린 채 밴드에 의지해 매달리세요. 찌릿한 지점 직전에서 잠시 멈췄다가 천천히 통과하세요.",
        "how": [
            "강한 보조 밴드를 바에 걸고 한쪽 발이나 무릎을 밴드에 대세요",
            "날개뼈를 아래로 살짝 내린 채(귀와 어깨 사이 공간 유지) 팔을 천천히 뻗어 매달리는 자세로 들어가세요",
            "찌릿한 지점 직전에서 잠시 멈췄다가 천천히 통과하세요",
            "20~30초 유지 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 구간 통과 시도가 3회 이상 실패하면 1단계로 복귀."
    },
    {
        "order": 3, "type": "풀업",
        "name": "밴드 보조 스트릭 풀업", "equipment": "약한 보조 밴드",
        "target_area": "광배근, 대원근, 이두근, 하부승모근",
        "why": "보조를 줄여 실제 풀업 동작을 다시 시작합니다. 반동 없는 스트릭 형태로 제한해 어깨가 앞으로 말리는 보상 없이 수행합니다.",
        "sets": "5회 · 3세트",
        "cue": "가능하면 중립 그립이나 언더핸드(친업) 그립으로 잡으세요. 어깨를 바깥으로 돌려 어깨 위 공간을 덜 좁힙니다. 반동 없이 당기고, 턱이 바 위로 올라갈 때 어깨를 귀 쪽으로 으쓱하지 마세요. 어깨 반응이 이상하면 2단계로 돌아가세요.",
        "how": [
            "약한 보조 밴드를 걸고, 가능하면 중립 그립이나 언더핸드(친업) 그립으로 바를 잡으세요. 발이나 무릎을 밴드에 대세요",
            "반동 없이 몸을 수직으로 당겨 올리세요",
            "턱이 바 위로 올라가면 천천히 내려오세요",
            "5회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 2단계로 복귀."
    },
    {
        "order": 4, "type": "풀업",
        "name": "볼륨 점진 복귀", "equipment": "철봉 (밴드 또는 맨몸)",
        "target_area": "광배근, 대원근, 이두근, 하부승모근, 전거근",
        "why": "어깨가 통증 없이 당기는 동작을 되찾았으니, 볼륨(횟수×세트)을 부상 전 수준으로 천천히 되돌립니다.",
        "sets": "부상 전 볼륨의 50%에서 시작, 주차별 1~2세트씩 증가",
        "cue": "보조 수준은 그대로 두고 세트 수만 올리세요. 가능하면 중립 그립이나 언더핸드(친업) 그립을 유지하세요. 통증이 없을 때만 다음 주에 늘리세요.",
        "how": [
            "3단계와 같은 보조 수준과 그립을 유지하세요",
            "부상 전 볼륨의 절반부터 시작하세요",
            "통증 없이 1주 유지되면 세트 수를 1~2세트씩 늘리세요"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행 + 다음날 통증 악화 없음. 탈출 경로: 볼륨 증가 후 통증이 재현되면 이전 볼륨으로 되돌리고 1주 더 유지하세요."
    }
]


def find_stage(root_movement):
    ps = next(p for p in root_movement['pain_sites'] if p['id'] == 'shoulder')
    c = next(x for x in ps['causes'] if x['id'] == 'cause-dp')
    return c['route']['stages'][0]


# 1) data/phase-exercises.json
with open(PHASE_PATH, encoding='utf-8') as f:
    d = json.load(f)
mv = next(m for m in d['movements'] if m['id'] == 'pullup')
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
st_b = find_stage(bundled['pullup'])
assert not st_b.get('phase_b'), 'index.html phase_b가 비어있지 않음, 중단'
st_b['phase_b'] = PHASE_B
new_raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
html = html[:start] + new_raw + html[start + length:]
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

# 검증
with open(PHASE_PATH, encoding='utf-8') as f:
    d2 = json.load(f)
n1 = len(find_stage(next(m for m in d2['movements'] if m['id'] == 'pullup'))['phase_b'])
with open(INDEX_PATH, encoding='utf-8') as f:
    h2 = f.read()
s2 = h2.index('BUNDLED = ') + len('BUNDLED = ')
b2, _ = json.JSONDecoder().raw_decode(h2[s2:])
n2 = len(find_stage(b2['pullup'])['phase_b'])
print(f'{"OK" if n1 == 4 and n2 == 4 else "ERR"} pullup/shoulder/cause-dp phase_b data={n1} index={n2}')
