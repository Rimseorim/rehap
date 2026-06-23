import json

with open('data/phase-exercises.json', encoding='utf-8') as f:
    d = json.load(f)

lu = next(m for m in d['movements'] if m['id'] == 'lunge')
hip = next(ps for ps in lu['pain_sites'] if ps['id'] == 'hip')

def make_9090(why="고관절 외회전근과 내회전근 복합 가동성을 확보합니다."):
    return {"type":"스트레칭","name":"90/90 Stretch","equipment":"없음",
            "target_area":"고관절 외회전근, 심부이상근, 내회전근","why":why,
            "sets":"양측 각 60초 · 2세트",
            "cue":"앞다리는 90도 외회전, 뒷다리는 90도 내회전으로 정렬한 뒤 척추를 편 상태로 상체를 앞으로 숙여주세요.",
            "how":["바닥에 앉아 앞다리는 90도 외회전, 뒷다리는 90도 내회전 형태로 정렬하세요",
                   "척추를 편 상태로 상체를 앞으로 숙여주세요","60초 유지 · 양측 교대"],"video_url":"TBD"}

def make_hip_flexor_rock_back():
    return {"type":"스트레칭","name":"Hip Flexor Rock Back","equipment":"없음",
            "target_area":"장요근, 둔근, 고관절 관절낭",
            "why":"고관절 굴곡 가동범위를 확보합니다. 런지 하강 시 고관절이 충분히 열릴 수 있는 범위를 만듭니다.",
            "sets":"10회 · 3세트",
            "cue":"엉덩이를 뒤꿈치 쪽으로 천천히 밀어내며 고관절 굴곡 가동 범위를 확보하세요. 허리가 말리지 않는 범위까지만 내려가세요.",
            "how":["네발기기 자세에서 시작하세요","척추 정렬을 유지한 채 엉덩이를 뒤꿈치 쪽으로 천천히 밀어내세요",
                   "고관절 굴곡 가동 범위를 확보한 후 돌아옵니다","10회 · 3세트"],"video_url":"TBD"}

def make_clamshell(cue="발은 붙인 채 무릎만 조개처럼 열어주세요. 골반이 뒤로 돌아가지 않도록 주의하세요."):
    return {"type":"활성화","name":"Clamshell","equipment":"없음",
            "target_area":"중둔근 후부 섬유, 고관절 심부 외회전근",
            "why":"중둔근 후부와 고관절 심부 외회전근을 활성화합니다.",
            "sets":"양측 각 15회 · 3세트","cue":cue,
            "how":["옆으로 누워 무릎을 90도로 구부리고 양 뒤꿈치를 붙이세요",
                   "골반을 고정한 채 위쪽 무릎을 천천히 열어주세요","15회 · 양측 교대"],"video_url":"TBD"}

def make_side_lying_hip_abduction(why="중둔근을 강화합니다. 연구에 따르면 약 80% MVIC를 달성하는 핵심 중둔근 훈련 동작입니다."):
    return {"type":"활성화","name":"Side-lying Hip Abduction","equipment":"없음",
            "target_area":"중둔근, 대퇴근막장근","why":why,
            "sets":"양측 각 15회 · 3세트",
            "cue":"뒤꿈치가 몸통보다 약간 뒤를 향하게 한 상태에서 대각선 후상방으로 들어 올리세요.",
            "how":["옆으로 바르게 누워 아래쪽 다리는 구부려 중심을 잡으세요",
                   "위쪽 다리는 무릎을 완전히 펴고 뒤꿈치를 약간 뒤로 향하게 하세요",
                   "다리를 대각선 후상방으로 들어 올리세요","15회 · 양측 교대"],"video_url":"TBD"}

def make_deep_squat_rotation():
    return {"type":"스트레칭","name":"Deep Squat Rotation","equipment":"없음",
            "target_area":"흉추, 고관절 외회전근, 발목 가자미근",
            "why":"흉추와 고관절 외회전 복합 가동성을 확보합니다.",
            "sets":"양측 각 10회 · 2세트",
            "cue":"딥 스쿼트 자세를 유지한 채 반대 팔을 천장으로 크게 회전하세요.",
            "how":["딥 스쿼트 자세에서 한 손으로 바닥을 지지하세요",
                   "반대 팔을 천장 방향으로 크게 회전하세요","10회 · 양측 교대"],"video_url":"TBD"}

def make_open_half_kneeling():
    return {"type":"스트레칭","name":"Open Half Kneeling Shift","equipment":"없음",
            "target_area":"내전근, 고관절 관절낭, 발목 관절",
            "why":"내전근과 고관절 관절낭을 이완합니다.",
            "sets":"양측 각 30초 · 2세트",
            "cue":"체중을 이동할 때 상체가 앞으로 숙여지지 않도록 척추 중립을 수직으로 유지하세요.",
            "how":["한쪽 무릎을 꿇은 상태에서 반대쪽 다리를 옆으로 열어 딛으세요",
                   "체중을 디딘 발 방향으로 수평 이동시키세요","30초 · 양측 교대"],"video_url":"TBD"}

def make_glute_bridge():
    return {"type":"활성화","name":"Glute Bridge","equipment":"없음",
            "target_area":"대둔근, 햄스트링","why":"대둔근을 활성화합니다.",
            "sets":"15회 · 3세트",
            "cue":"최고점에서 엉덩이를 2초 쥐어짜세요. 허리가 아니라 엉덩이로 올라가는 느낌이 정상입니다.",
            "how":["바닥에 누워 무릎을 세우세요","엉덩이를 들어 올리세요",
                   "최고점에서 2초 유지 후 천천히 내립니다","15회 · 3세트"],"video_url":"TBD"}

def make_bird_dog():
    return {"type":"활성화","name":"Bird Dog","equipment":"없음",
            "target_area":"척추기립근, 다열근, 대둔근","why":"심부 안정근을 활성화합니다.",
            "sets":"좌우 교대 10회 · 3세트",
            "cue":"골반이 옆으로 기울지 않도록 속도보다 안정성에 집중합니다.",
            "how":["네발기기 자세에서 척추를 중립으로 맞추세요",
                   "한쪽 팔과 반대쪽 다리를 뻗어줍니다","2~3초 유지 후 돌아옵니다",
                   "10회 · 양측 교대"],"video_url":"TBD"}

def make_foam_roller_iliopsoas():
    return {"type":"스트레칭","name":"폼롤러 장요근 릴리즈","equipment":"폼롤러",
            "target_area":"장요근",
            "why":"과부하된 장요근에 능동 신장 없이 패시브 이완합니다.",
            "sets":"양측 각 60초 · 2세트","cue":"뭉친 곳에서 10~15초 멈췄다가 천천히 이동하세요.",
            "how":["폼롤러를 골반 앞쪽(장요근 위치)에 대고 엎드리세요",
                   "천천히 체중을 실으며 압박하세요","뭉친 곳에서 멈추세요",
                   "60초 · 양측 교대"],"video_url":"TBD"}

def make_foam_roller_quad():
    return {"type":"스트레칭","name":"폼롤러 대퇴직근 릴리즈","equipment":"폼롤러",
            "target_area":"대퇴직근",
            "why":"과부하된 대퇴직근에 능동 신장 없이 패시브 이완합니다.",
            "sets":"양측 각 60초 · 2세트",
            "cue":"엎드려 폼롤러를 허벅지 앞쪽에 올리고 천천히 롤링하세요.",
            "how":["엎드려 폼롤러를 허벅지 앞쪽에 올리세요","천천히 롤링하세요",
                   "뭉친 곳에서 멈추세요","60초 · 양측 교대"],"video_url":"TBD"}

def make_dead_bug():
    return {"type":"활성화","name":"Dead Bug","equipment":"없음",
            "target_area":"복직근, 복사근, 장요근",
            "why":"코어 안정화를 훈련합니다. 굴곡근 과긴장의 보상 패턴(허리 과신전)을 방지합니다.",
            "sets":"좌우 교대 10회 · 3세트",
            "cue":"허리가 바닥에서 뜨지 않게 내내 눌러줍니다.",
            "how":["바닥에 누워 팔을 천장으로 뻗고 무릎을 90도로 들어 올리세요",
                   "허리를 바닥에 밀착시킨 채 반대쪽 팔다리를 뻗었다 돌아오세요",
                   "10회 · 양측 교대"],"video_url":"TBD"}

def make_hamstring_stretch():
    return {"type":"스트레칭","name":"Hamstring Stretch","equipment":"없음",
            "target_area":"햄스트링","why":"햄스트링을 이완합니다. 고관절 신전 제한을 보완합니다.",
            "sets":"양측 각 40초 · 2세트",
            "cue":"등을 말지 마세요. 척추 중립을 유지한 채 골반만 접어 내려가세요.",
            "how":["바닥에 한쪽 다리를 펴고 앉거나 서서 발을 낮은 곳에 올리세요",
                   "척추를 곧게 세우고 상체를 앞으로 지긋이 숙여주세요",
                   "허벅지 뒤쪽이 당기는 느낌을 유지하며 40초","양측 교대"],"video_url":"TBD"}

# ── cause-a: 가동성 부족 (고관절 외회전 제한) ──────────────────────────
ca = next(c for c in hip['causes'] if c['id'] == 'cause-a')
a1 = make_9090(); a1["set"]="a"; a1["order"]=1
a2 = make_hip_flexor_rock_back(); a2["set"]="a"; a2["order"]=2
a3 = make_clamshell(); a3["set"]="a"; a3["order"]=3
a4 = make_side_lying_hip_abduction(); a4["set"]="a"; a4["order"]=4
a5 = make_deep_squat_rotation(); a5["set"]="a_b"; a5["order"]=1
a6 = make_open_half_kneeling(); a6["set"]="a_b"; a6["order"]=2
a7 = make_glute_bridge(); a7["set"]="a_b"; a7["order"]=3
a8 = make_bird_dog(); a8["set"]="a_b"; a8["order"]=4
ca['route']['stages'][0]['phase_a'] = [a1,a2,a3,a4,a5,a6,a7,a8]
ca['route']['stages'][0]['phase_a_b'] = []
ca['route']['stages'][0]['phase_b'] = [
    {"order":1,"type":"런지","name":"TRX 어시스트 런지 (발끝 바깥 스탠스)","equipment":"TRX 또는 기둥",
     "target_area":"대퇴사두근, 대둔근, 고관절",
     "why":"발끝을 더 바깥으로 향해 외회전 부담을 줄이고 TRX로 균형을 보조합니다. 가장 쉬운 조건에서 시작합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"발끝을 45도 바깥으로 향하고 TRX를 가볍게 잡으세요. 고관절 바깥쪽에 편안하게 유지되는 게 정상이에요.",
     "how":["TRX나 기둥을 양손으로 가볍게 잡으세요","발끝을 45도 바깥으로 향하고 런지하세요",
            "고관절 바깥쪽 반응을 확인하세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"},
    {"order":2,"type":"런지","name":"TRX 어시스트 런지 (정상 스탠스)","equipment":"TRX 또는 기둥",
     "target_area":"대퇴사두근, 대둔근, 고관절",
     "why":"발끝 각도를 정상화해 관절 각도만 변수로 제어합니다. TRX 보조는 유지합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"TRX를 가볍게 잡고 정상 스탠스로 런지하세요. 고관절 바깥쪽이 편안하게 유지되는지 확인하세요.",
     "how":["TRX를 잡고 정상 스탠스로 런지하세요","고관절 바깥쪽 반응을 확인하세요",
            "10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"},
    {"order":3,"type":"런지","name":"맨몸 런지","equipment":"없음",
     "target_area":"대퇴사두근, 대둔근, 고관절",
     "why":"TRX 보조 없이 자체적으로 고관절 외회전을 유지하며 런지 가능한지 확인합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"보조 없이 런지하세요. 고관절 바깥쪽이 편안하게 유지되는지 확인하세요.",
     "how":["런지 자세로 내려가세요","고관절 반응을 확인하세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"},
    {"order":4,"type":"런지","name":"덤벨 런지","equipment":"덤벨",
     "target_area":"대퇴사두근, 대둔근, 고관절, 코어",
     "why":"ROM과 자세가 확보된 상태에서 부하를 추가합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"본인이 10회 이상 무리 없이 들 수 있는 가벼운 무게를 준비해 주세요. 이번 단계의 핵심은 무거운 무게가 아니라 부하가 더해져도 고관절 바깥쪽이 괜찮은지 확인하는 것입니다.",
     "how":["덤벨을 양손에 들고 런지하세요","고관절 반응을 확인하세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"}
]

# ── cause-b: 과부하 (고관절 굴곡근 긴장) ────────────────────────────────
cb = next(c for c in hip['causes'] if c['id'] == 'cause-b')
cb['recovery_note'] = "이 루틴은 회복이 목적입니다. 단계를 서두르다 오히려 다시 아플 수 있어요."
cb['priority_note'] = "런지 세션은 48시간 이상 간격을 두세요. 런지 보폭도 단계별로 점진 확대하세요."
b1 = make_foam_roller_iliopsoas(); b1["set"]="a"; b1["order"]=1
b2 = make_foam_roller_quad(); b2["set"]="a"; b2["order"]=2
b3 = make_glute_bridge(); b3["set"]="a"; b3["order"]=3
b4 = make_dead_bug(); b4["set"]="a"; b4["order"]=4
b5 = make_hip_flexor_rock_back(); b5["set"]="a_b"; b5["order"]=1
b6 = make_open_half_kneeling(); b6["set"]="a_b"; b6["order"]=2
b7 = make_bird_dog(); b7["set"]="a_b"; b7["order"]=3
b8 = make_side_lying_hip_abduction("중둔근 강화. 고관절 굴곡근 과부하 케이스에서 길항근 강화로 부하 분산."); b8["set"]="a_b"; b8["order"]=4
cb['route']['stages'][0]['phase_a'] = [b1,b2,b3,b4,b5,b6,b7,b8]
cb['route']['stages'][0]['phase_a_b'] = []
cb['route']['stages'][0]['phase_b'] = [
    {"order":1,"type":"런지","name":"맨몸 런지 (무부하 패턴 확인)","equipment":"없음",
     "target_area":"대퇴사두근, 대둔근, 고관절 굴곡근",
     "why":"부하 없이 굴곡근 반응을 먼저 확인합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"런지하며 사타구니 앞쪽 반응을 확인하세요. 편안하게 유지되는 게 정상이에요.",
     "how":["런지 자세로 내려가세요","사타구니 앞쪽 반응을 확인하세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 수행 + 다음날 통증 악화 없음"},
    {"order":2,"type":"런지","name":"고블릿 런지 (경부하)","equipment":"덤벨 또는 케틀벨",
     "target_area":"대퇴사두근, 대둔근, 고관절 굴곡근",
     "why":"무부하에서 통증이 없었다면 경부하로 굴곡근 반응을 확인합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"본인이 10회 이상 무리 없이 들 수 있는 가벼운 무게를 준비해 주세요. 이번 단계의 핵심은 무거운 무게가 아니라 사타구니 앞쪽이 어떻게 반응하는지 확인하는 것입니다.",
     "how":["덤벨이나 케틀벨을 가슴 앞에 잡고 런지하세요","사타구니 앞쪽 반응을 확인하세요",
            "10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 수행 + 다음날 통증 악화 없음"},
    {"order":3,"type":"런지","name":"덤벨 런지 (중부하)","equipment":"덤벨",
     "target_area":"대퇴사두근, 대둔근, 고관절 굴곡근",
     "why":"실제 부하로 굴곡근이 견딜 수 있는지 확인합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"사타구니 앞쪽 반응이 이상하면 무게를 낮추세요.",
     "how":["부상 직전 무게의 50~60%로 덤벨을 들고 런지하세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 수행 + 다음날 통증 악화 없음"},
    {"order":4,"type":"런지","name":"덤벨 런지 (무게 점진)","equipment":"덤벨",
     "target_area":"대퇴사두근, 대둔근, 고관절 굴곡근",
     "why":"굴곡근이 회복됐으니 부상 전 수준으로 무게를 천천히 되돌립니다.",
     "sets":"10회 · 3세트 (양측 교대), 주차별 점진",
     "cue":"세트수는 그대로 두고 무게만 올리세요. 사타구니 앞쪽 반응이 이상하면 바로 이전 무게로 돌아가세요.",
     "how":["이전 단계에서 점진적으로 무게를 올리세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 수행 + 다음날 통증 악화 없음"}
]

# ── cause-c: 복합 (중둔근 약화 + 이상근 보상) ───────────────────────────
cc = next(c for c in hip['causes'] if c['id'] == 'cause-c')
c1 = make_9090("이상근과 고관절 심부 외회전근을 이완합니다. 이상근 과긴장을 직접 해소합니다.")
c1["set"]="a"; c1["order"]=1
c2 = make_hip_flexor_rock_back(); c2["set"]="a"; c2["order"]=2
c3 = make_clamshell("발은 붙인 채 무릎만 열어주세요. 이상근 대신 중둔근으로 무릎을 여는 느낌을 찾으세요.")
c3["set"]="a"; c3["order"]=3
c4 = make_glute_bridge(); c4["set"]="a"; c4["order"]=4
c5 = make_open_half_kneeling(); c5["set"]="a_b"; c5["order"]=1
c6 = make_hip_flexor_rock_back()
c6["set"]="a_b"; c6["order"]=2
c6["name"] = "Hip Flexor Rock Back (짝수날)"
c7 = make_side_lying_hip_abduction("중둔근을 강화합니다. 약 80% MVIC를 달성하는 핵심 훈련 동작입니다.")
c7["set"]="a_b"; c7["order"]=3
c8 = make_bird_dog(); c8["set"]="a_b"; c8["order"]=4
cc['route']['stages'][0]['phase_a'] = [c1,c2,c3,c4,c5,c6,c7,c8]
cc['route']['stages'][0]['phase_a_b'] = []
cc['route']['stages'][0]['phase_b'] = [
    {"order":1,"type":"런지","name":"보조가 강한 밴드 맨몸 런지 (무릎 위)","equipment":"보조가 강한 저항 밴드",
     "target_area":"중둔근, 대둔근",
     "why":"저항 밴드로 중둔근을 최대 활성화합니다. 무게 없이 밴드 저항만 변수로 제어합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"밴드가 안으로 당기는 힘에 저항하며 무릎을 발끝 방향으로 유지하세요. 밴드를 이기는 느낌이 정상입니다.",
     "how":["보조가 강한 밴드를 양쪽 무릎 위에 걸치세요","런지 자세로 내려가세요",
            "밴드 저항에 맞서 무릎이 발끝 방향을 유지하도록 하세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"},
    {"order":2,"type":"런지","name":"맨몸 런지 (밴드 없이)","equipment":"없음",
     "target_area":"중둔근, 대퇴사두근, 대둔근",
     "why":"밴드 없이도 중둔근이 자가적으로 무릎 정렬을 유지하는지 확인합니다. 밴드 제거만 변수.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"보조 없이 런지하세요. 무릎이 발끝 방향을 유지하는지 확인하세요.",
     "how":["런지 자세로 내려가세요","무릎 정렬을 확인하세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"},
    {"order":3,"type":"런지","name":"고블릿 런지","equipment":"덤벨 또는 케틀벨",
     "target_area":"중둔근, 대퇴사두근, 대둔근",
     "why":"자가 정렬이 확인됐다면 경부하를 추가해 중둔근이 부하 아래서도 유지되는지 확인합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"본인이 10회 이상 무리 없이 들 수 있는 가벼운 무게를 준비해 주세요. 이번 단계의 핵심은 무거운 무게가 아니라 부하가 더해져도 무릎이 발끝 방향을 유지하는지 확인하는 것입니다.",
     "how":["덤벨이나 케틀벨을 가슴 앞에 잡고 런지하세요","무릎 정렬을 확인하세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"},
    {"order":4,"type":"런지","name":"덤벨 런지","equipment":"덤벨",
     "target_area":"중둔근, 대퇴사두근, 대둔근, 코어",
     "why":"무게를 늘려 중둔근이 더 큰 부하에서도 무릎 정렬을 유지하는지 최종 검증합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"본인이 10회 이상 무리 없이 들 수 있는 가벼운 무게를 준비해 주세요. 이번 단계의 핵심은 무거운 무게가 아니라 부하가 더해져도 무릎이 안으로 쏠리지 않는지 확인하는 것입니다.",
     "how":["덤벨을 양손에 들고 런지하세요","무릎 정렬을 확인하세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"}
]

# ── cause-d: 특이소견 없음 ──────────────────────────────────────────────
cd = next(c for c in hip['causes'] if c['id'] == 'cause-d')
d1 = make_hip_flexor_rock_back(); d1["set"]="a"; d1["order"]=1
d2 = make_open_half_kneeling(); d2["set"]="a"; d2["order"]=2
d3 = make_glute_bridge(); d3["set"]="a"; d3["order"]=3
d4 = make_clamshell(); d4["set"]="a"; d4["order"]=4
d5 = make_deep_squat_rotation(); d5["set"]="a_b"; d5["order"]=1
d6 = make_hamstring_stretch(); d6["set"]="a_b"; d6["order"]=2
d7 = make_side_lying_hip_abduction(); d7["set"]="a_b"; d7["order"]=3
d8 = make_bird_dog(); d8["set"]="a_b"; d8["order"]=4
cd['route']['stages'][0]['phase_a'] = [d1,d2,d3,d4,d5,d6,d7,d8]
cd['route']['stages'][0]['phase_a_b'] = []
cd['route']['stages'][0]['phase_b'] = [
    {"order":1,"type":"런지","name":"벽 잡고 런지 (양손)","equipment":"없음 (벽 활용)",
     "target_area":"대퇴사두근, 대둔근, 고관절",
     "why":"지지를 최대화해 가장 부담 없는 조건에서 통증 반응을 먼저 확인합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"벽을 양손으로 잡고 런지하세요. 고관절에 어떤 느낌인지 확인하세요. 편안한 느낌이 정상입니다.",
     "how":["벽을 양손으로 잡으세요","런지 자세로 내려가세요","고관절 반응을 확인하세요",
            "10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"},
    {"order":2,"type":"런지","name":"맨몸 런지","equipment":"없음",
     "target_area":"대퇴사두근, 대둔근, 고관절",
     "why":"보조 없이 고관절 반응을 확인합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"보조 없이 런지하세요. 고관절이 편안하게 유지되는지 확인하세요.",
     "how":["런지 자세로 내려가세요","고관절 반응을 확인하세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"},
    {"order":3,"type":"런지","name":"고블릿 런지","equipment":"덤벨 또는 케틀벨",
     "target_area":"대퇴사두근, 대둔근, 코어",
     "why":"패턴이 안정됐다면 경부하로 고관절 반응을 확인합니다.",
     "sets":"10회 · 3세트 (양측 교대)",
     "cue":"본인이 10회 이상 무리 없이 들 수 있는 가벼운 무게를 준비해 주세요. 이번 단계의 핵심은 무거운 무게가 아니라 고관절이 어떻게 반응하는지 확인하는 것입니다.",
     "how":["덤벨이나 케틀벨을 가슴 앞에 잡고 런지하세요","고관절 반응을 확인하세요",
            "10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"},
    {"order":4,"type":"런지","name":"덤벨 런지 (무게 점진)","equipment":"덤벨",
     "target_area":"대퇴사두근, 대둔근, 코어",
     "why":"실제 부하에서 고관절 반응을 최종 확인합니다.",
     "sets":"10회 · 3세트 (양측 교대), 주차별 점진",
     "cue":"세트수는 그대로 두고 무게만 올리세요. 고관절 반응이 이상하면 바로 이전 무게로 돌아가세요.",
     "how":["덤벨을 양손에 들고 런지하세요","고관절 반응을 확인하세요","10회 · 양측 교대"],"video_url":"TBD",
     "progression_note":"진급 기준: 2회 연속 세션 통증 없이 수행"}
]

with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('완료: 런지/고관절 cause-a~d Phase A+B 추가됨')
