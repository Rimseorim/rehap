import json

with open('data/phase-exercises.json', encoding='utf-8') as f:
    d = json.load(f)

# cause-dp 보호 루틴 5개 (set:"a" 단일 세션, 홀수/짝수 구분 없음)
dp_exercises = [
    {
        "set":"a","order":1,"type":"스트레칭",
        "name":"펜듈럼 운동 (Pendulum Exercise)","equipment":"없음 (테이블 또는 의자 활용)",
        "target_area":"어깨 관절낭, 회전근개 전체",
        "why":"중력을 이용한 수동적 어깨 관절 가동 운동입니다. 관절낭을 전방향으로 부드럽게 이완해 염증 조절과 관절 공간 확보에 도움을 줍니다.",
        "sets":"각 방향 20~30초 · 2세트",
        "cue":"어깨 근육을 사용하지 말고 상체의 반동으로 팔이 수동적으로 흔들리게 하세요. 팔에 힘을 완전히 빼는 것이 핵심입니다.",
        "how":["테이블에 한 손을 짚고 상체를 숙이세요",
               "힘을 완전히 뺀 팔을 중력에 맡겨 시계추처럼 부드럽게 전후좌우로 흔들어주세요",
               "각 방향 20~30초"],"video_url":"TBD"
    },
    {
        "set":"a","order":2,"type":"활성화",
        "name":"월 프레스 (Wall Press, 등척성)","equipment":"없음 (벽 활용)",
        "target_area":"회전근개, 삼각근, 견갑 주변 안정근",
        "why":"통증 없는 범위 내 등척성 수축으로 최소한의 근육 활성화를 유지합니다. 오버헤드 없이 어깨를 보호하면서 안정성을 유지하는 핵심 운동입니다.",
        "sets":"10초 유지 · 5세트",
        "cue":"팔꿈치를 90도로 구부려 전완을 벽에 대고 지긋이 미세요. 통증이 생기면 즉시 멈추세요.",
        "how":["벽을 마주 보고 서서 팔꿈치를 90도로 구부려 전완을 벽에 붙이세요",
               "벽을 향해 지긋이 밀어내며 10초 유지하세요",
               "통증 없는 범위 내에서만 수행하세요","10초 · 5세트"],"video_url":"TBD"
    },
    {
        "set":"a","order":3,"type":"활성화",
        "name":"아이소메트릭 밴드 홀드 (내/외회전)","equipment":"약한 저항 밴드",
        "target_area":"극하근, 소원근, 견갑하근 (회전근개)",
        "why":"통증 없는 범위 내에서 회전근개를 등척성으로 활성화합니다. 최소한의 부하로 건 조직에 자극을 주어 혈류를 유지합니다.",
        "sets":"각 방향 10초 · 3세트",
        "cue":"통증이 생기는 즉시 멈추세요. 버티는 것이 목적이며 움직임이 없어야 합니다.",
        "how":["약한 밴드를 기둥에 걸고 팔꿈치를 90도로 구부려 옆구리에 붙이세요",
               "내회전(몸 쪽으로) 방향으로 10초 버티세요",
               "외회전(몸 바깥으로) 방향으로 10초 버티세요",
               "통증 없는 범위 내에서만 · 양측 교대"],"video_url":"TBD"
    },
    {
        "set":"a","order":4,"type":"활성화",
        "name":"바텀업 케틀벨 홀드","equipment":"가벼운 케틀벨",
        "target_area":"회전근개, 전완 굴곡근, 견갑 주변 안정근",
        "why":"케틀벨을 거꾸로 들어 반사적 안정화를 유도합니다. 무게 중심이 불안정해 신경근 반응이 자동으로 활성화됩니다. 통증 없는 저부하 범위에서만 수행합니다.",
        "sets":"20~30초 · 3세트",
        "cue":"케틀벨이 흔들리지 않도록 코어와 어깨를 함께 잡아주세요. 팔꿈치는 90도를 유지하세요.",
        "how":["가벼운 케틀벨을 거꾸로 (손잡이가 아래) 쥐고 팔꿈치를 90도로 구부리세요",
               "케틀벨이 쓰러지지 않도록 안정적으로 유지하세요",
               "20~30초 · 3세트 · 통증 없는 범위 내"],"video_url":"TBD"
    },
    {
        "set":"a","order":5,"type":"활성화",
        "name":"크로스오버 시머트리 활성화","equipment":"약한 저항 밴드",
        "target_area":"회전근개, 삼각근, 견갑 주변 근육군",
        "why":"약한 밴드 장력으로 어깨 주변 혈류를 증가시킵니다. 통증이 시작되기 전까지만 수행하며, 염증 조절과 가벼운 근 활성화를 동시에 얻습니다.",
        "sets":"15~20회 · 3세트",
        "cue":"통증이 생기기 전 범위에서 멈추세요. 가장 약한 밴드를 사용하고 불편함이 없어야 합니다.",
        "how":["약한 밴드를 대각선 방향으로 당겨 통증 없는 범위 내에서 어깨를 움직이세요",
               "통증이 시작되기 전에 멈추세요",
               "15~20회 · 3세트"],"video_url":"TBD"
    }
]

intro_message = "현재 단계에서는 어깨를 머리 위로 올리는 모든 오버헤드 동작을 즉시 중단하세요. 본 5가지 보호 루틴은 통증 완화와 최소한의 안정성 유지를 위해 매일 일관되게 수행합니다. 통증이 소실되면 원인 재검사를 통해 해당 원인 case로 이동하세요."

target_movements = [
    'back-squat','deadlift','pullup',
    'vertical-press','horizontal-press','row','kipping'
]

count = 0
for mv in d['movements']:
    if mv['id'] not in target_movements:
        continue
    for ps in mv['pain_sites']:
        if ps['id'] != 'shoulder':
            continue
        for c in ps.get('causes', []):
            if c['id'] == 'cause-dp':
                c['intro_message'] = intro_message
                c['route']['stages'][0]['phase_a'] = dp_exercises
                c['route']['stages'][0]['phase_a_b'] = []
                c['route']['stages'][0]['phase_b'] = []
                count += 1

print(f'완료: {count}개 동작에 cause-dp 추가됨')

with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

# 검증
with open('data/phase-exercises.json', encoding='utf-8') as f:
    d2 = json.load(f)

for mv in d2['movements']:
    if mv['id'] not in target_movements:
        continue
    for ps in mv['pain_sites']:
        if ps['id'] != 'shoulder':
            continue
        for c in ps.get('causes', []):
            if c['id'] == 'cause-dp':
                pa = c['route']['stages'][0].get('phase_a', [])
                print(f'{mv["id"]}/shoulder/cause-dp: phase_a {len(pa)}개, intro_message 있음: {"intro_message" in c}')
