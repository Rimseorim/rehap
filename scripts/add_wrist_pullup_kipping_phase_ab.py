import json

with open('data/phase-exercises.json', encoding='utf-8') as f:
    d = json.load(f)

# ── 공통 Phase A 동작 ──────────────────────────────────────────────────

def 밴드견인손목신전():
    return {"type":"스트레칭","name":"밴드 견인 손목 신전","equipment":"저항 밴드",
            "target_area":"손목 관절낭, 손목 굴곡근 건",
            "why":"밴드가 손목 관절을 후방으로 당겨 관절 공간을 확보합니다. 철봉 그립 자세에서 손목 신전 가동범위를 효과적으로 확보합니다.",
            "sets":"양측 각 30초 · 3세트",
            "cue":"밴드가 손목을 뒤로 당기는 느낌을 유지하며 체중을 앞으로 천천히 이동하세요. 손바닥은 바닥에서 뜨지 않게 밀착시키세요.",
            "how":["네발기기 자세에서 밴드를 손목 주름 바로 아래에 걸고 기둥에 고정하세요",
                   "체중을 앞으로 천천히 이동시키며 손목이 자연스럽게 신전되도록 하세요",
                   "30초 유지 · 양측 교대"],"video_url":"TBD"}

def 손목굴곡신전스트레칭():
    return {"type":"스트레칭","name":"손목 굴곡·신전 스트레칭","equipment":"없음",
            "target_area":"전완 굴곡근군, 전완 신전근군",
            "why":"전완 앞뒤 근육을 부드럽게 이완합니다. 철봉 그립 전 손목 주변 긴장을 해소합니다.",
            "sets":"양측 각 30초 · 2세트",
            "cue":"팔을 앞으로 뻗고 반대쪽 손으로 손바닥과 손등을 몸쪽으로 번갈아 당겨주세요. 팔꿈치가 구부러지지 않도록 유지하세요.",
            "how":["팔을 앞으로 곧게 뻗으세요","반대쪽 손으로 손바닥을 몸쪽으로 당겨 신전근을 30초 늘리세요",
                   "손등을 몸쪽으로 당겨 굴곡근을 30초 늘리세요","양측 교대"],"video_url":"TBD"}

def 손목관절가동성운동():
    return {"type":"활성화","name":"손목 관절 가동성 운동 (CARs)","equipment":"없음",
            "target_area":"손목 관절낭, 전완 굴곡·신전근 전체",
            "why":"손목 관절이 그릴 수 있는 최대 가동범위를 능동적으로 훈련합니다. 철봉 그립 자세에서 손목 관절 준비에 효과적입니다.",
            "sets":"양방향 각 5회 · 2세트",
            "cue":"전완은 완전히 고정하고 손목만 천천히 가장 큰 원을 그리세요.",
            "how":["팔꿈치를 90도로 구부려 옆구리에 붙이세요","반대쪽 손으로 전완을 단단히 고정하세요",
                   "손목만 이용해 가능한 가장 큰 원을 천천히 그리세요",
                   "안쪽에서 바깥쪽으로 5회, 반대 방향으로 5회 · 양측 교대"],"video_url":"TBD"}

def 손목신전강화(why="손목 신전근을 강화합니다. 철봉 그립 자세에서 손목이 꺾이지 않도록 지지합니다."):
    return {"type":"활성화","name":"손목 신전 강화","equipment":"없음 또는 가벼운 덤벨",
            "target_area":"요측수근신근, 척측수근신근","why":why,
            "sets":"양측 각 15회 · 3세트",
            "cue":"전완을 테이블에 올리고 손목은 모서리 밖으로 내보내세요. 손등을 하늘 방향으로 천천히 들어 올리세요.",
            "how":["의자나 테이블에 전완을 올리고 손목은 모서리 밖으로 내보내세요",
                   "손바닥이 바닥을 향하게 두세요","손등을 하늘 방향으로 천천히 들어 올리세요",
                   "천천히 내리며 15회 · 양측 교대"],"video_url":"TBD"}

def 손목가동성스트레칭():
    return {"type":"스트레칭","name":"손목 가동성 스트레칭 (네발기기)","equipment":"없음",
            "target_area":"손목 관절낭, 전완 굴곡·신전근 전체",
            "why":"네발기기 자세에서 체중을 이용해 손목 전 방향 가동범위를 열어줍니다.",
            "sets":"30초 · 2세트",
            "cue":"손바닥이 바닥에서 뜨지 않도록 유지하며 체중을 앞뒤로 천천히 이동하세요.",
            "how":["네발기기 자세에서 손가락 방향을 앞·옆·뒤로 각각 바꿔가며 배치하세요",
                   "체중을 앞뒤좌우로 천천히 이동하며 손목을 부드럽게 늘려주세요","각 방향 30초"],"video_url":"TBD"}

def 전완회내회외스트레칭():
    return {"type":"스트레칭","name":"전완 회내·회외 스트레칭","equipment":"없음",
            "target_area":"회내근, 회외근, 요척관절낭",
            "why":"전완 회전 가동성을 확보합니다. 철봉 그립 변형 시 전완 회전이 손목 부담에 영향을 줍니다.",
            "sets":"양방향 각 10회 · 2세트",
            "cue":"팔꿈치를 옆구리에 붙이고 손바닥이 위아래를 완전히 바라보도록 번갈아 회전하세요.",
            "how":["팔꿈치를 90도로 구부려 옆구리에 붙이세요",
                   "손바닥이 완전히 하늘을 향하도록 회외시키세요",
                   "손바닥이 완전히 바닥을 향하도록 회내시키세요",
                   "각 끝점에서 1~2초 유지 · 10회 반복 · 양측 교대"],"video_url":"TBD"}

def 등척성손목유지():
    return {"type":"활성화","name":"등척성 손목 유지","equipment":"없음",
            "target_area":"전완 굴곡·신전근 전체, 손목 심부 안정화 근육군",
            "why":"손목 주변 근육을 등척성으로 강화합니다. 철봉 그립 시 손목을 중립으로 잠그는 능력을 훈련합니다.",
            "sets":"방향당 5~10초 · 3세트",
            "cue":"손목을 중립으로 유지한 채 반대쪽 손이 미는 저항에 단 1mm도 움직이지 않고 버티세요.",
            "how":["팔꿈치를 90도로 구부려 옆구리에 붙이세요",
                   "반대쪽 손으로 주먹을 위·아래·좌·우 방향으로 강하게 미세요",
                   "손목은 움직이지 않고 5~10초 버티세요","양측 교대"],"video_url":"TBD"}

def 그립강화():
    return {"type":"활성화","name":"그립 강화","equipment":"소프트볼 또는 타월",
            "target_area":"지굴근군, 손목 굴곡근",
            "why":"풀업·키핑에 필요한 그립 지구력을 강화합니다.",
            "sets":"20회 · 3세트",
            "cue":"손바닥 전체로 꽉 쥐었다가 천천히 놓으세요. 손가락 끝만 쥐지 않도록 주의하세요.",
            "how":["소프트볼이나 타월을 손에 쥐세요",
                   "손바닥 전체의 압력으로 꽉 쥐었다가 천천히 놓으세요",
                   "20회 · 3세트 · 양손 교대"],"video_url":"TBD"}

def 전완폼롤러릴리즈(why="과부하된 전완 근육을 패시브 릴리즈합니다. 능동 신장 금지 규칙 적용."):
    return {"type":"스트레칭","name":"전완 폼롤러 릴리즈","equipment":"폼롤러 또는 마사지볼",
            "target_area":"전완 신전근군 또는 굴곡근군","why":why,
            "sets":"양측 각 60초 · 2세트",
            "cue":"뭉친 곳에서 10~15초 멈췄다가 천천히 이동하세요. 강한 통증이 느껴지면 압박 강도를 줄이세요.",
            "how":["테이블 위에 폼롤러를 올리고 전완을 올리세요",
                   "반대쪽 손으로 체중을 지긋이 실어 압박하세요",
                   "손목부터 팔꿈치 직전까지 천천히 롤링하세요",
                   "뭉친 곳에서 10~15초 멈추세요","60초 · 양측 교대"],"video_url":"TBD"}

def 손목원형돌리기():
    return {"type":"스트레칭","name":"손목 원형 돌리기","equipment":"없음",
            "target_area":"수근관절 주변 인대 및 가동 근육군",
            "why":"손목 전 방향 가동성을 유지합니다. 능동 신장 없이 관절 가동성을 유지합니다.",
            "sets":"양방향 각 10회 · 2세트",
            "cue":"전완은 고정하고 손목만 천천히 가능한 가장 큰 원을 그리세요.",
            "how":["주먹을 가볍게 쥐고 전완을 고정하세요",
                   "손목 관절이 그릴 수 있는 가장 큰 가동범위로 원을 그리세요",
                   "시계방향 10회, 반시계방향 10회 · 양측 교대"],"video_url":"TBD"}

def 손가락신전():
    return {"type":"활성화","name":"손가락 신전 (밴드 저항)","equipment":"저항 밴드",
            "target_area":"손가락 지신근, 전완 외측 근육군",
            "why":"손가락 신전근(길항근)을 강화합니다. 굴곡근 과부하 케이스에서 균형을 회복합니다.",
            "sets":"15회 · 3세트",
            "cue":"손목은 중립을 유지하고 손가락만 밴드 저항을 이겨내며 활짝 펴세요.",
            "how":["다섯 손가락 끝에 밴드를 팽팽하게 걸으세요",
                   "손목 중립을 유지한 채 손가락을 사방으로 활짝 펴세요",
                   "최대로 편 위치에서 2초 유지 후 천천히 모으세요",
                   "15회 · 양측 교대"],"video_url":"TBD"}

def 손목굴곡강화():
    return {"type":"활성화","name":"손목 굴곡 강화","equipment":"없음 또는 가벼운 덤벨",
            "target_area":"전완 굴곡근군",
            "why":"신전근 건병증 케이스에서 굴곡근(길항근)을 강화해 전완 근육 균형을 회복합니다.",
            "sets":"양측 각 15회 · 3세트",
            "cue":"전완을 테이블에 올리고 손바닥이 위를 향하게 두세요. 손바닥을 위쪽으로 천천히 말아 올리세요.",
            "how":["의자나 테이블에 전완을 올리고 손바닥이 위를 향하게 두세요",
                   "손바닥을 위쪽으로 천천히 말아 올리세요",
                   "천천히 내리며 15회 · 양측 교대"],"video_url":"TBD"}

# ── Phase B 공통 빌더 ─────────────────────────────────────────────────

def make_pullup_phase_b(cause_tag, include_eccentric=False):
    """
    cause_tag: '과부하' or '가동성' or '특이소견'
    include_eccentric: cause-b에서 편심성 운동 선행 여부
    변수: 강도(1→3) + 볼륨(3→4)
    """
    prog_note_overload = "진급 기준: 2회 연속 세션 수행 + 다음날 통증 악화 없음"
    prog_note_normal = "진급 기준: 2회 연속 세션 통증 없이 수행"
    note = prog_note_overload if cause_tag == '과부하' else prog_note_normal

    steps = []
    order = 1

    if include_eccentric:
        steps.append({
            "order": order, "type": "재활",
            "name": "손목 신전근 편심성 운동 (3~5초 버티기)",
            "equipment": "가벼운 덤벨",
            "target_area": "요측수근신근, 척측수근신근",
            "why": "편심성 부하가 건 조직 리모델링을 촉진합니다. 통증 0~3점(NRS) 이하에서만 수행하고 내릴 때 3~5초 버팁니다.",
            "sets": "15회 · 3세트 (하루 2~3회)",
            "cue": "올릴 때는 반대쪽 손의 도움을 받아도 됩니다. 내릴 때만 천천히 3~5초에 걸쳐 버티며 내려가세요. 통증이 4점 이상이면 즉시 중단하세요.",
            "how": ["전완을 테이블에 올리고 손목은 모서리 밖으로 내보내세요",
                    "반대쪽 손의 도움으로 손목을 최대 신전 위치로 올리세요",
                    "반대쪽 손을 떼고 3~5초에 걸쳐 천천히 내려가세요","15회 · 3세트"],
            "video_url": "TBD", "progression_note": note
        })
        order += 1

    steps += [
        {
            "order": order, "type": "풀업 준비",
            "name": "데드 행 (매달리기만)",
            "equipment": "철봉",
            "target_area": "전완, 손목",
            "why": "철봉에 매달려 그립 자세와 손목 반응을 먼저 확인합니다. 당기는 동작 없이 부하를 최소화합니다.",
            "sets": "20~30초 · 3세트",
            "cue": "철봉을 잡고 편안하게 매달리세요. 손목에 어떤 느낌인지 확인하세요. 편안한 느낌이 정상입니다.",
            "how": ["철봉을 오버핸드 그립으로 잡으세요",
                    "발을 바닥에서 떼지 않아도 됩니다 (중량 조절 가능)",
                    "20~30초 매달리며 손목 반응을 확인하세요","3세트"],
            "video_url": "TBD", "progression_note": note
        },
        {
            "order": order + 1, "type": "풀업",
            "name": "밴드 어시스트 풀업 (보조가 강한 밴드)",
            "equipment": "철봉, 보조가 강한 밴드",
            "target_area": "광배근, 이두근, 전완, 손목",
            "why": "강한 보조로 그립 부하를 줄여 손목 반응을 확인합니다.",
            "sets": "5회 · 3세트",
            "cue": "밴드에 발이나 무릎을 걸고 풀업하세요. 손목에 이상이 생기면 즉시 멈추세요.",
            "how": ["보조가 강한 밴드를 철봉에 걸고 발이나 무릎을 걸으세요",
                    "풀업을 수행하며 손목 반응을 확인하세요","5회 · 3세트"],
            "video_url": "TBD", "progression_note": note
        },
        {
            "order": order + 2, "type": "풀업",
            "name": "밴드 어시스트 풀업 (보조가 약한 밴드)",
            "equipment": "철봉, 보조가 약한 밴드",
            "target_area": "광배근, 이두근, 전완, 손목",
            "why": "보조를 줄여 그립 부하를 높입니다. 손목이 더 큰 부하에서도 안정적인지 확인합니다.",
            "sets": "5회 · 3세트",
            "cue": "보조가 약한 밴드로 풀업하세요. 손목에 이상이 생기면 강한 밴드로 돌아가세요.",
            "how": ["보조가 약한 밴드를 철봉에 걸고 풀업하세요",
                    "손목 반응을 확인하세요","5회 · 3세트"],
            "video_url": "TBD", "progression_note": note
        },
        {
            "order": order + 3, "type": "풀업",
            "name": "부상 전 수준에서 볼륨 점진 복귀",
            "equipment": "철봉 (밴드 또는 맨몸)",
            "target_area": "광배근, 이두근, 전완, 손목",
            "why": "3단계와 동일한 보조 수준을 유지하며 세트수·횟수만 점진 증가합니다. 맨몸 풀업이 가능한 사람은 맨몸으로, 밴드가 본인 최고 수준인 사람은 약한 밴드로 볼륨을 올립니다.",
            "sets": "부상 전 볼륨의 50%에서 시작, 주차별 10~20% 증가",
            "cue": "3단계와 동일한 방식을 유지하세요. 보조 수준은 바꾸지 말고 세트수나 횟수만 조금씩 늘리세요.",
            "how": ["3단계와 동일한 보조 수준(밴드 또는 맨몸)을 유지하세요",
                    "부상 전 볼륨의 50%에서 시작해 주차별로 10~20%씩 늘리세요",
                    "손목에 이상이 생기면 볼륨을 줄이세요"],
            "video_url": "TBD", "progression_note": note
        }
    ]
    return steps

def make_kipping_phase_b(cause_tag, include_eccentric=False):
    """키핑은 동적 부하 특성상 스윙 단계 포함"""
    prog_note_overload = "진급 기준: 2회 연속 세션 수행 + 다음날 통증 악화 없음"
    prog_note_normal = "진급 기준: 2회 연속 세션 통증 없이 수행"
    note = prog_note_overload if cause_tag == '과부하' else prog_note_normal

    steps = []
    order = 1

    if include_eccentric:
        steps.append({
            "order": order, "type": "재활",
            "name": "손목 신전근 편심성 운동 (3~5초 버티기)",
            "equipment": "가벼운 덤벨",
            "target_area": "요측수근신근, 척측수근신근",
            "why": "편심성 부하가 건 조직 리모델링을 촉진합니다. 통증 0~3점(NRS) 이하에서만 수행합니다.",
            "sets": "15회 · 3세트",
            "cue": "올릴 때는 반대쪽 손의 도움을 받아도 됩니다. 내릴 때만 3~5초 버티세요.",
            "how": ["전완을 테이블에 올리고 손목은 모서리 밖으로 내보내세요",
                    "반대쪽 손으로 올린 뒤 혼자 3~5초 버티며 내려가세요","15회 · 3세트"],
            "video_url": "TBD", "progression_note": note
        })
        order += 1

    steps += [
        {
            "order": order, "type": "준비",
            "name": "데드 행 (매달리기만)",
            "equipment": "철봉",
            "target_area": "전완, 손목",
            "why": "철봉에 매달려 그립 자세와 손목 반응을 먼저 확인합니다.",
            "sets": "20~30초 · 3세트",
            "cue": "철봉을 잡고 편안하게 매달리세요. 손목에 어떤 느낌인지 확인하세요.",
            "how": ["철봉을 오버핸드 그립으로 잡으세요","20~30초 매달리며 손목 반응을 확인하세요","3세트"],
            "video_url": "TBD", "progression_note": note
        },
        {
            "order": order + 1, "type": "키핑 준비",
            "name": "소범위 스윙 (허로우·아치 패턴 확인)",
            "equipment": "철봉",
            "target_area": "광배근, 코어, 전완, 손목",
            "why": "키핑에 필요한 스윙 동작에서 손목이 동적 부하에 반응하는지 확인합니다. 소범위로 부하를 최소화합니다.",
            "sets": "10회 · 3세트",
            "cue": "작게 흔들며 손목 반응을 확인하세요. 손목에 이상이 있으면 스윙 범위를 줄이세요.",
            "how": ["철봉에 매달려 작게 앞뒤로 흔드세요","허로우(hollow)와 아치(arch) 패턴을 소범위로 연습하세요",
                    "손목 반응을 확인하세요","10회 · 3세트"],
            "video_url": "TBD", "progression_note": note
        },
        {
            "order": order + 2, "type": "키핑",
            "name": "밴드 어시스트 키핑 풀업",
            "equipment": "철봉, 보조가 강한 밴드",
            "target_area": "광배근, 이두근, 코어, 전완, 손목",
            "why": "보조를 사용해 키핑 풀업 동작에서 손목 부하를 줄입니다.",
            "sets": "5회 · 3세트",
            "cue": "밴드 보조로 키핑 풀업을 수행하세요. 손목 반응을 확인하세요.",
            "how": ["보조가 강한 밴드를 걸고 키핑 풀업을 수행하세요",
                    "손목 반응을 확인하세요","5회 · 3세트"],
            "video_url": "TBD", "progression_note": note
        },
        {
            "order": order + 3, "type": "키핑",
            "name": "부상 전 수준에서 볼륨 점진 복귀",
            "equipment": "철봉 (밴드 또는 맨몸)",
            "target_area": "광배근, 이두근, 코어, 전완, 손목",
            "why": "3단계와 동일한 보조 수준을 유지하며 세트수·횟수만 점진 증가합니다.",
            "sets": "부상 전 볼륨의 50%에서 시작, 주차별 10~20% 증가",
            "cue": "3단계와 동일한 방식을 유지하세요. 보조 수준은 바꾸지 말고 세트수나 횟수만 조금씩 늘리세요.",
            "how": ["3단계와 동일한 보조 수준을 유지하세요",
                    "부상 전 볼륨의 50%에서 시작해 주차별로 10~20%씩 늘리세요"],
            "video_url": "TBD", "progression_note": note
        }
    ]
    return steps

# ═══════════════════════════════════════════════════════════════════════
# 풀업/손목
# ═══════════════════════════════════════════════════════════════════════

pu = next(m for m in d['movements'] if m['id'] == 'pullup')
pu_wrist = next(ps for ps in pu['pain_sites'] if ps['id'] == 'wrist')

# ── 풀업 cause-a: 가동성 부족 ────────────────────────────────────────
pu_ca = next(c for c in pu_wrist['causes'] if c['id'] == 'cause-a')
pa1 = 밴드견인손목신전(); pa1["set"]="a"; pa1["order"]=1
pa2 = 손목굴곡신전스트레칭(); pa2["set"]="a"; pa2["order"]=2
pa3 = 손목신전강화(); pa3["set"]="a"; pa3["order"]=3
pa4 = 손목관절가동성운동(); pa4["set"]="a"; pa4["order"]=4
pa5 = 손목가동성스트레칭(); pa5["set"]="a_b"; pa5["order"]=1
pa6 = 전완회내회외스트레칭(); pa6["set"]="a_b"; pa6["order"]=2
pa7 = 등척성손목유지(); pa7["set"]="a_b"; pa7["order"]=3
pa8 = 그립강화(); pa8["set"]="a_b"; pa8["order"]=4
pu_ca['route']['stages'][0]['phase_a'] = [pa1,pa2,pa3,pa4,pa5,pa6,pa7,pa8]
pu_ca['route']['stages'][0]['phase_a_b'] = []
pu_ca['route']['stages'][0]['phase_b'] = make_pullup_phase_b('가동성')

# ── 풀업 cause-b: 신전근 건병증 ─────────────────────────────────────
pu_cb = next(c for c in pu_wrist['causes'] if c['id'] == 'cause-b')
pu_cb['priority_note'] = "전완 신전근(팔꿈치 바깥쪽 아래 근육 무리)에 대한 강한 능동 스트레칭을 절대 금지합니다. 폼롤러나 마사지볼을 이용한 허혈성 압박 및 부드러운 롤링(릴리즈)만 허용합니다."
pu_cb['recovery_note'] = "이 루틴은 회복이 목적입니다. 편심성 운동 시 통증 0~3점(NRS) 이하에서만 수행하고, 내릴 때 3~5초간 천천히 버티세요."
pb1 = 전완폼롤러릴리즈("전완 신전근 쪽 패시브 릴리즈. 능동 신장 절대 금지."); pb1["set"]="a"; pb1["order"]=1
pb2 = 손목원형돌리기(); pb2["set"]="a"; pb2["order"]=2
pb3 = 그립강화(); pb3["set"]="a"; pb3["order"]=3
pb4 = 등척성손목유지(); pb4["set"]="a"; pb4["order"]=4
pb5 = 전완회내회외스트레칭(); pb5["set"]="a_b"; pb5["order"]=1
pb6 = 손목가동성스트레칭(); pb6["set"]="a_b"; pb6["order"]=2
pb7 = 손목굴곡강화(); pb7["set"]="a_b"; pb7["order"]=3
pb8 = 손가락신전(); pb8["set"]="a_b"; pb8["order"]=4
pu_cb['route']['stages'][0]['phase_a'] = [pb1,pb2,pb3,pb4,pb5,pb6,pb7,pb8]
pu_cb['route']['stages'][0]['phase_a_b'] = []
pu_cb['route']['stages'][0]['phase_b'] = make_pullup_phase_b('과부하', include_eccentric=True)

# ── 풀업 cause-c: 굴곡근·TFCC ───────────────────────────────────────
pu_cc = next(c for c in pu_wrist['causes'] if c['id'] == 'cause-c')
pu_cc['priority_note'] = "손목 굴곡근에 대한 강한 능동 스트레칭을 절대 금지합니다. 폼롤러나 마사지볼 패시브 릴리즈만 허용합니다."
pu_cc['recovery_note'] = "이 루틴은 회복이 목적입니다. 새끼손가락 쪽 통증이 올라오면 즉시 부하를 줄이세요."
pc1 = 전완폼롤러릴리즈("전완 굴곡근 쪽 패시브 릴리즈. 굴곡근 능동 신장 절대 금지."); pc1["set"]="a"; pc1["order"]=1
pc2 = 손목원형돌리기(); pc2["set"]="a"; pc2["order"]=2
pc3 = 손가락신전(); pc3["set"]="a"; pc3["order"]=3
pc3["why"] = "손가락 신전근(길항근) 활성화. 굴곡근 과부하 균형 회복."
pc4 = 손목신전강화("손목 신전근(길항근) 강화. 굴곡근 부하를 분산합니다."); pc4["set"]="a"; pc4["order"]=4
pc5 = 전완회내회외스트레칭(); pc5["set"]="a_b"; pc5["order"]=1
pc6 = 손목가동성스트레칭(); pc6["set"]="a_b"; pc6["order"]=2
pc7 = 등척성손목유지(); pc7["set"]="a_b"; pc7["order"]=3
pc8 = 그립강화(); pc8["set"]="a_b"; pc8["order"]=4
pu_cc['route']['stages'][0]['phase_a'] = [pc1,pc2,pc3,pc4,pc5,pc6,pc7,pc8]
pu_cc['route']['stages'][0]['phase_a_b'] = []
pu_cc['route']['stages'][0]['phase_b'] = make_pullup_phase_b('과부하')

# ── 풀업 cause-d: 특이소견 없음 ─────────────────────────────────────
pu_cd = next(c for c in pu_wrist['causes'] if c['id'] == 'cause-d')
pd1 = 손목굴곡신전스트레칭(); pd1["set"]="a"; pd1["order"]=1
pd2 = 손목가동성스트레칭(); pd2["set"]="a"; pd2["order"]=2
pd3 = 등척성손목유지(); pd3["set"]="a"; pd3["order"]=3
pd4 = 손목원형돌리기(); pd4["set"]="a"; pd4["order"]=4
pd5 = 밴드견인손목신전(); pd5["set"]="a_b"; pd5["order"]=1
pd6 = 전완회내회외스트레칭(); pd6["set"]="a_b"; pd6["order"]=2
pd7 = 손목신전강화(); pd7["set"]="a_b"; pd7["order"]=3
pd8 = 그립강화(); pd8["set"]="a_b"; pd8["order"]=4
pu_cd['route']['stages'][0]['phase_a'] = [pd1,pd2,pd3,pd4,pd5,pd6,pd7,pd8]
pu_cd['route']['stages'][0]['phase_a_b'] = []
pu_cd['route']['stages'][0]['phase_b'] = make_pullup_phase_b('특이소견')

# ═══════════════════════════════════════════════════════════════════════
# 키핑/손목 (cause-b, c, d — cause-a는 이미 있음)
# ═══════════════════════════════════════════════════════════════════════

kp = next(m for m in d['movements'] if m['id'] == 'kipping')
kp_wrist = next(ps for ps in kp['pain_sites'] if ps['id'] == 'wrist')

# ── 키핑 cause-b: 신전근 건병증 ─────────────────────────────────────
kp_cb = next(c for c in kp_wrist['causes'] if c['id'] == 'cause-b')
kp_cb['priority_note'] = "전완 신전근에 대한 강한 능동 스트레칭을 절대 금지합니다. 폼롤러나 마사지볼 패시브 릴리즈만 허용합니다."
kp_cb['recovery_note'] = "이 루틴은 회복이 목적입니다. 편심성 운동 시 통증 0~3점(NRS) 이하에서만 수행하고, 내릴 때 3~5초간 천천히 버티세요."
kb1 = 전완폼롤러릴리즈("전완 신전근 쪽 패시브 릴리즈."); kb1["set"]="a"; kb1["order"]=1
kb2 = 손목원형돌리기(); kb2["set"]="a"; kb2["order"]=2
kb3 = 그립강화(); kb3["set"]="a"; kb3["order"]=3
kb4 = 등척성손목유지(); kb4["set"]="a"; kb4["order"]=4
kb5 = 전완회내회외스트레칭(); kb5["set"]="a_b"; kb5["order"]=1
kb6 = 손목가동성스트레칭(); kb6["set"]="a_b"; kb6["order"]=2
kb7 = 손목굴곡강화(); kb7["set"]="a_b"; kb7["order"]=3
kb8 = 손가락신전(); kb8["set"]="a_b"; kb8["order"]=4
kp_cb['route']['stages'][0]['phase_a'] = [kb1,kb2,kb3,kb4,kb5,kb6,kb7,kb8]
kp_cb['route']['stages'][0]['phase_a_b'] = []
kp_cb['route']['stages'][0]['phase_b'] = make_kipping_phase_b('과부하', include_eccentric=True)

# ── 키핑 cause-c: 굴곡근·TFCC ───────────────────────────────────────
kp_cc = next(c for c in kp_wrist['causes'] if c['id'] == 'cause-c')
kp_cc['priority_note'] = "손목 굴곡근에 대한 강한 능동 스트레칭을 절대 금지합니다. 폼롤러나 마사지볼 패시브 릴리즈만 허용합니다."
kp_cc['recovery_note'] = "이 루틴은 회복이 목적입니다. 새끼손가락 쪽 통증이 올라오면 즉시 부하를 줄이세요."
kc1 = 전완폼롤러릴리즈("전완 굴곡근 쪽 패시브 릴리즈."); kc1["set"]="a"; kc1["order"]=1
kc2 = 손목원형돌리기(); kc2["set"]="a"; kc2["order"]=2
kc3 = 손가락신전(); kc3["set"]="a"; kc3["order"]=3
kc4 = 손목신전강화("길항근(신전근) 강화로 굴곡근 부하 분산."); kc4["set"]="a"; kc4["order"]=4
kc5 = 전완회내회외스트레칭(); kc5["set"]="a_b"; kc5["order"]=1
kc6 = 손목가동성스트레칭(); kc6["set"]="a_b"; kc6["order"]=2
kc7 = 등척성손목유지(); kc7["set"]="a_b"; kc7["order"]=3
kc8 = 그립강화(); kc8["set"]="a_b"; kc8["order"]=4
kp_cc['route']['stages'][0]['phase_a'] = [kc1,kc2,kc3,kc4,kc5,kc6,kc7,kc8]
kp_cc['route']['stages'][0]['phase_a_b'] = []
kp_cc['route']['stages'][0]['phase_b'] = make_kipping_phase_b('과부하')

# ── 키핑 cause-d: 특이소견 없음 ─────────────────────────────────────
kp_cd = next(c for c in kp_wrist['causes'] if c['id'] == 'cause-d')
kd1 = 손목굴곡신전스트레칭(); kd1["set"]="a"; kd1["order"]=1
kd2 = 손목가동성스트레칭(); kd2["set"]="a"; kd2["order"]=2
kd3 = 등척성손목유지(); kd3["set"]="a"; kd3["order"]=3
kd4 = 손목원형돌리기(); kd4["set"]="a"; kd4["order"]=4
kd5 = 밴드견인손목신전(); kd5["set"]="a_b"; kd5["order"]=1
kd6 = 전완회내회외스트레칭(); kd6["set"]="a_b"; kd6["order"]=2
kd7 = 손목신전강화(); kd7["set"]="a_b"; kd7["order"]=3
kd8 = 그립강화(); kd8["set"]="a_b"; kd8["order"]=4
kp_cd['route']['stages'][0]['phase_a'] = [kd1,kd2,kd3,kd4,kd5,kd6,kd7,kd8]
kp_cd['route']['stages'][0]['phase_a_b'] = []
kp_cd['route']['stages'][0]['phase_b'] = make_kipping_phase_b('특이소견')

# ── 키핑 cause-a Phase A 추가 (phase_b는 이미 있음) ─────────────────
kp_ca = next(c for c in kp_wrist['causes'] if c['id'] == 'cause-a')
if not kp_ca['route']['stages'][0].get('phase_a'):
    ka1 = 밴드견인손목신전(); ka1["set"]="a"; ka1["order"]=1
    ka2 = 손목굴곡신전스트레칭(); ka2["set"]="a"; ka2["order"]=2
    ka3 = 손목신전강화(); ka3["set"]="a"; ka3["order"]=3
    ka4 = 손목관절가동성운동(); ka4["set"]="a"; ka4["order"]=4
    ka5 = 손목가동성스트레칭(); ka5["set"]="a_b"; ka5["order"]=1
    ka6 = 전완회내회외스트레칭(); ka6["set"]="a_b"; ka6["order"]=2
    ka7 = 등척성손목유지(); ka7["set"]="a_b"; ka7["order"]=3
    ka8 = 그립강화(); ka8["set"]="a_b"; ka8["order"]=4
    kp_ca['route']['stages'][0]['phase_a'] = [ka1,ka2,ka3,ka4,ka5,ka6,ka7,ka8]
    kp_ca['route']['stages'][0]['phase_a_b'] = []

with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('완료: 풀업/손목 cause-a~d + 키핑/손목 cause-a~d Phase A+B 추가됨')
