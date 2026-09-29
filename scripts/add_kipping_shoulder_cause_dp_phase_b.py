import json

PHASE_PATH = 'data/phase-exercises.json'
INDEX_PATH = 'index.html'

PHASE_B = [
    {
        "order": 1, "type": "키핑",
        "name": "바닥 아치-할로우 전환", "equipment": "없음(매트)",
        "target_area": "복근, 척추기립근, 대둔근",
        "why": "키핑의 몸통 패턴(아치-할로우)을 팔을 머리 위로 올리지 않고 먼저 익힙니다. 팔을 몸 옆에 두므로 어깨가 통증 구간 밖에 머뭅니다.",
        "sets": "10회 · 3세트",
        "cue": "팔은 몸 옆 바닥에 두고, 허리를 바닥에 붙이는 할로우와 엉덩이·등 뒤쪽에 가볍게 힘이 들어가는 정도의 아치를 천천히 오가세요. 가슴을 과하게 꺾지 말고, 어깨에는 힘을 주지 마세요.",
        "how": [
            "매트에 누워 팔을 몸 옆에 두세요",
            "허리를 바닥에 붙이고 다리와 어깨를 살짝 든 할로우 자세를 만드세요",
            "이어서 엉덩이와 등 뒤쪽에 가볍게 힘을 주는 정도의 아치 자세로 넘어가세요",
            "10회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 Phase A로 복귀."
    },
    {
        "order": 2, "type": "키핑",
        "name": "소범위 키핑 스윙", "equipment": "철봉",
        "target_area": "광배근, 하부승모근, 전거근, 복근",
        "why": "스윙 뒤쪽 끝에서 어깨가 뒤로 밀려 충돌 위험이 커집니다. 힘을 뺀 매달림이 아니라 날개뼈를 내린 액티브 행 상태에서, 당기지 않고 몸통만 작게 흔들어 그 구간을 통제합니다.",
        "sets": "스윙 5~8회 · 3세트",
        "cue": "날개뼈를 아래로 살짝 내린 채(귀와 어깨 사이 공간 유지) 매달리세요. 팔은 굽히지 말고 몸통으로만 아주 작게 흔드세요. 몸이 앞으로 나가는 아치 구간에서 어깨가 앞으로 꺾이거나 찝히지 않도록 진폭을 작게 유지하세요. 체중을 매달리기 부담스러우면 발끝을 바닥에 살짝 대고 시작하세요. 찌릿하면 그 진폭 아래에서 멈추세요.",
        "how": [
            "철봉에 매달려 날개뼈를 아래로 살짝 내린 액티브 행 자세를 잡으세요(필요하면 발끝을 바닥에 대세요)",
            "팔을 편 채 아치-할로우로 작게 흔드세요(당기지 않기)",
            "찌릿한 진폭이 있으면 그보다 작게 하세요",
            "스윙 5~8회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 통증 재현 시 1단계로 복귀."
    },
    {
        "order": 3, "type": "키핑",
        "name": "밴드 보조 키핑 풀업", "equipment": "철봉, 강한 보조 밴드",
        "target_area": "광배근, 대원근, 이두근, 하부승모근",
        "why": "스윙에 당기기를 처음 더합니다. 밴드가 체중 일부를 받아 주므로, 어깨 반응을 확인하며 실제 키핑 풀업 리듬을 되찾습니다.",
        "sets": "5회 · 3세트",
        "cue": "스윙은 2단계와 같은 크기로 시작하고, 몸이 앞으로 나가는 구간에서 어깨가 앞으로 꺾이지 않게 하세요. 스윙 끝에서 이어서 당기세요. 반동을 일부러 키우지 마세요. 턱이 바 위로 올라갈 때 어깨를 귀 쪽으로 으쓱하지 마세요.",
        "how": [
            "강한 보조 밴드를 걸고 액티브 행 자세를 잡으세요",
            "2단계와 같은 크기로 스윙하세요",
            "스윙 끝에서 이어서 몸을 당겨 올리세요",
            "5회 · 3세트"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행. 탈출 경로: 어깨 반응이 이상하면 2단계로 복귀."
    },
    {
        "order": 4, "type": "키핑",
        "name": "볼륨 점진 복귀", "equipment": "철봉 (밴드 또는 맨몸)",
        "target_area": "광배근, 대원근, 이두근, 하부승모근, 전거근",
        "why": "통증 없이 스윙과 당기기가 이어졌으니, 볼륨(횟수×세트)을 부상 전 수준으로 천천히 되돌립니다.",
        "sets": "부상 전 볼륨의 50%에서 시작, 주차별 1~2세트씩 증가",
        "cue": "밴드 보조 수준은 그대로 두고 세트 수만 올리세요. 통증이 없을 때만 다음 주에 늘리세요.",
        "how": [
            "3단계와 같은 보조 수준을 유지하세요",
            "부상 전 볼륨의 절반부터 시작하세요",
            "통증 없이 1주 유지되면 세트 수를 1~2세트씩 늘리세요"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행 + 다음날 통증 악화 없음. 탈출 경로: 볼륨 증가 후 통증이 재현되면 이전 볼륨으로 되돌리고 1주 더 유지하세요."
    }
]

MOVEMENT_ID = 'kipping'


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
