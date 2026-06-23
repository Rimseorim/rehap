import json

with open('data/phase-exercises.json', encoding='utf-8') as f:
    d = json.load(f)

lu = next(m for m in d['movements'] if m['id'] == 'lunge')
ankle = next(ps for ps in lu['pain_sites'] if ps['id'] == 'ankle')

# 공통 Phase A 동작 정의
def make_banded_talar_distraction():
    return {
        "type": "스트레칭",
        "name": "밴드 거골 후방 견인 스트레칭",
        "equipment": "저항 밴드",
        "target_area": "발목 관절, 거골",
        "why": "거골을 후방으로 당겨 전방 관절 충돌 공간을 확보합니다. 런지 하강 시 발목 배측굴곡 제한을 직접 해결합니다.",
        "sets": "양측 30초 · 3세트",
        "how": [
            "저항 밴드를 복숭아뼈 바로 위에 걸고 반대쪽에 고정하세요",
            "밴드가 팽팽하게 당겨지는 방향으로 한 발을 앞으로 내딛으세요",
            "발뒤꿈치를 바닥에 유지하며 무릎을 앞으로 밀어 발목을 굽히세요",
            "30초 유지 후 발목을 부드럽게 앞뒤로 10회 펌핑합니다. 양측 교대"
        ],
        "video_url": "TBD"
    }

def make_calf_toes_stretch():
    return {
        "type": "스트레칭",
        "name": "Calf and Toes Stretch",
        "equipment": "없음",
        "target_area": "비복근, 가자미근, 족저근막",
        "why": "족저근막과 종아리를 동시에 이완합니다. 배측굴곡 제한 완화에 기여합니다.",
        "sets": "양측 각 40초 · 2세트",
        "how": [
            "무릎을 꿇고 앉되 발가락을 꺾어 세우세요",
            "체중을 뒤꿈치 쪽으로 지긋이 실어 발바닥 전면을 늘립니다",
            "40초 유지 · 양측 교대"
        ],
        "video_url": "TBD"
    }

def make_wall_ankle_mobility(cue_variant=""):
    return {
        "type": "활성화",
        "name": "월 앵클 모빌리티 (Wall Ankle Mobility)",
        "equipment": "없음 (벽 활용)",
        "target_area": "전경골근, 발목 관절",
        "why": "배측굴곡 ROM을 능동적으로 훈련합니다. 런지 하강 시 뒤꿈치가 뜨지 않도록 가동범위를 확보합니다.",
        "sets": "양측 각 10회 · 3세트",
        "cue": cue_variant if cue_variant else "뒤꿈치를 바닥에 고정한 채 무릎을 새끼발가락 방향으로 유지하세요.",
        "how": [
            "벽 앞에 서서 발끝을 벽에서 5cm 떨어뜨리세요",
            "발뒤꿈치를 바닥에 붙인 채 무릎을 벽 쪽으로 밀어보세요",
            "무릎이 닿으면 발을 1cm 더 뒤로 물리고 반복합니다",
            "양발 각각 10회"
        ],
        "video_url": "TBD"
    }

def make_ankle_circles(cue_variant=""):
    return {
        "type": "활성화",
        "name": "Ankle Circles",
        "equipment": "없음",
        "target_area": "전경골근, 비복근, 가자미근, 발목 관절낭",
        "why": "발목 전 방향 관절 유연성을 유지합니다.",
        "sets": "양방향 각 10회 · 2세트",
        "cue": cue_variant if cue_variant else "발목 관절만 움직이며 천천히 회전하세요.",
        "how": [
            "발목을 공중에 띄운 상태에서 천천히 원을 그리세요",
            "시계 방향 10회, 반시계 방향 10회 · 양발 교대"
        ],
        "video_url": "TBD"
    }

def make_open_half_kneeling():
    return {
        "type": "스트레칭",
        "name": "Open Half Kneeling Shift",
        "equipment": "없음",
        "target_area": "내전근, 고관절 관절낭, 발목 관절",
        "why": "런지 자세에서 발목 배측굴곡을 유도합니다. 고관절과 발목을 동시에 가동시킵니다.",
        "sets": "양측 각 30초 · 2세트",
        "cue": "체중을 이동할 때 상체가 앞으로 숙여지지 않도록 척추 중립을 수직으로 유지하세요.",
        "how": [
            "한쪽 무릎을 꿇은 상태에서 반대쪽 다리를 옆으로 열어 딛으세요",
            "체중을 디딘 발 방향으로 수평 이동시키세요",
            "30초 · 양측 교대"
        ],
        "video_url": "TBD"
    }

def make_calf_stretch():
    return {
        "type": "스트레칭",
        "name": "Calf Stretch (비복근)",
        "equipment": "없음 (벽 활용)",
        "target_area": "비복근, 가자미근",
        "why": "비복근을 이완합니다. 배측굴곡 ROM 확보에 필수적입니다.",
        "sets": "양측 각 40초 · 2세트",
        "cue": "뒤꿈치를 바닥에 완전히 붙이세요. 발끝은 정면을 향하게 유지하세요.",
        "how": [
            "벽 앞에 서서 스트레칭할 다리를 뒤로 멀리 보내세요",
            "뒤꿈치를 바닥에 붙인 채 앞쪽 무릎을 구부리세요",
            "40초 유지 · 양측 교대"
        ],
        "video_url": "TBD"
    }

def make_ankle_dorsiflexion():
    return {
        "type": "활성화",
        "name": "Ankle Dorsiflexion",
        "equipment": "없음",
        "target_area": "전경골근",
        "why": "전경골근을 활성화합니다. 런지 시 발목 배측굴곡 패턴을 지지합니다.",
        "sets": "양측 각 15회 · 3세트",
        "cue": "발목 관절만 움직이며 발끝을 정강이 방향으로 최대한 높이 들어 올리세요.",
        "how": [
            "벽에 등을 기대고 서세요",
            "발끝을 정강이 방향으로 최대한 들어 올리세요",
            "15회 · 양측 교대"
        ],
        "video_url": "TBD"
    }

def make_single_leg_balance(cue_variant=""):
    return {
        "type": "활성화",
        "name": "Single Leg Balance",
        "equipment": "없음",
        "target_area": "지면 수용기, 비골근, 후경골근, 발목 심부 안정화",
        "why": "발목 심부 안정화와 고유감각을 훈련합니다.",
        "sets": "양측 각 30초 · 2세트",
        "cue": cue_variant if cue_variant else "세 곳(엄지·새끼발가락·뒤꿈치)이 고르게 바닥을 누르도록 유지하세요.",
        "how": [
            "한 발로 서서 30초 버티세요",
            "양측 교대"
        ],
        "video_url": "TBD"
    }

def make_ankle_eversion():
    return {
        "type": "스트레칭",
        "name": "Ankle Eversion (비골근 활성화)",
        "equipment": "저항 밴드",
        "target_area": "장비골근, 단비골근",
        "why": "비골근(외번근)을 활성화합니다. 외측 불안정의 주원인인 비골근 약화를 직접 해결합니다.",
        "sets": "양측 각 15회 · 3세트",
        "cue": "허벅지 전체가 돌아가지 않도록 하고 발목 관절만 바깥으로 밀어내세요.",
        "how": [
            "바닥에 다리를 곧게 펴고 앉아 밴드를 발 앞부분에 걸으세요",
            "발목을 바깥쪽으로 밀어내면서 비골근을 수축시키세요",
            "천천히 돌아오며 15회 · 양측 교대"
        ],
        "video_url": "TBD"
    }

def make_band_dorsiflexion():
    return {
        "type": "활성화",
        "name": "Band Dorsiflexion",
        "equipment": "저항 밴드",
        "target_area": "전경골근",
        "why": "전경골근을 강화합니다. 발목 전방 안정화에 기여합니다.",
        "sets": "양측 각 15회 · 3세트",
        "cue": "발목 관절 중심의 굴곡을 유도하며 발끝을 정강이 방향으로 당기세요.",
        "how": [
            "밴드를 발등에 묶고 저항을 만드세요",
            "발끝을 정강이 방향으로 당기며 15회 · 양측 교대"
        ],
        "video_url": "TBD"
    }

def make_towel_pickup():
    return {
        "type": "활성화",
        "name": "Towel Pick Up",
        "equipment": "없음 (수건 활용)",
        "target_area": "발바닥 내재근, 장지굴근",
        "why": "발바닥 내재근을 활성화합니다. 발바닥 지지 기반 강화로 발목 안정성에 기여합니다.",
        "sets": "3분 · 2세트",
        "cue": "발가락 힘만으로 수건을 말아 당기세요.",
        "how": [
            "의자에 앉아 바닥에 수건을 펼치세요",
            "발가락의 힘만으로 수건을 말아 당기세요",
            "3분 · 양발 교대"
        ],
        "video_url": "TBD"
    }

def make_foam_roller_calf():
    return {
        "type": "스트레칭",
        "name": "폼롤러 종아리 패시브 릴리즈",
        "equipment": "폼롤러",
        "target_area": "비복근, 가자미근",
        "why": "과부하된 아킬레스건에 능동 신장 없이 종아리를 부드럽게 이완합니다.",
        "sets": "양측 각 60초 · 2세트",
        "cue": "뭉친 곳에서 10~15초 멈췄다가 천천히 이동하세요.",
        "how": [
            "폼롤러 위에 종아리를 올리고 반대쪽 발로 체중을 조절하세요",
            "종아리 아래부터 무릎 아래까지 천천히 롤링하세요",
            "뭉친 곳에서 10~15초 멈추세요",
            "60초 · 양측 교대"
        ],
        "video_url": "TBD"
    }

# ── cause-a: 가동성 부족 (발목 배측굴곡 제한) ───────────────────────────
ca = next(c for c in ankle['causes'] if c['id'] == 'cause-a')
ca_a = make_banded_talar_distraction()
ca_a["set"] = "a"; ca_a["order"] = 1
ca_b = make_calf_toes_stretch()
ca_b["set"] = "a"; ca_b["order"] = 2
ca_c = make_wall_ankle_mobility()
ca_c["set"] = "a"; ca_c["order"] = 3
ca_d = make_ankle_circles("발목을 앞쪽으로 부드럽게 돌려 배측굴곡 범위를 늘려보세요.")
ca_d["set"] = "a"; ca_d["order"] = 4

ca_e = make_open_half_kneeling()
ca_e["set"] = "a_b"; ca_e["order"] = 1
ca_f = make_calf_stretch()
ca_f["set"] = "a_b"; ca_f["order"] = 2
ca_f["cue"] = "뒤꿈치를 바닥에 붙이고 종아리가 당기는 느낌을 찾으세요. 발목 배측굴곡 회복을 위한 핵심 스트레칭입니다."
ca_g = make_ankle_dorsiflexion()
ca_g["set"] = "a_b"; ca_g["order"] = 3
ca_h = make_single_leg_balance()
ca_h["set"] = "a_b"; ca_h["order"] = 4

ca['route']['stages'][0]['phase_a'] = [ca_a, ca_b, ca_c, ca_d, ca_e, ca_f, ca_g, ca_h]
ca['route']['stages'][0]['phase_a_b'] = []
ca['route']['stages'][0]['phase_b'] = [
    {
        "order": 1, "type": "런지",
        "name": "힐 엘리베이티드 런지 + TRX 어시스트",
        "equipment": "플레이트 또는 웨지, TRX 또는 기둥",
        "target_area": "대퇴사두근, 대둔근, 발목",
        "why": "힐을 높여 배측굴곡 요구를 줄이고 TRX로 균형을 보조합니다. 가장 쉬운 조건에서 런지 패턴을 확인합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "앞발 뒤꿈치 아래에 플레이트를 받치고 TRX를 가볍게 잡으세요. 발목 앞쪽에 편안하게 유지되는 게 정상이에요.",
        "how": [
            "앞발 뒤꿈치 아래에 플레이트를 받치세요",
            "TRX나 기둥을 양손으로 가볍게 잡으세요",
            "런지 자세로 내려가세요",
            "10회 · 양측 교대"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    },
    {
        "order": 2, "type": "런지",
        "name": "어시스트 런지 (힐 없이, TRX 유지)",
        "equipment": "TRX 또는 기둥",
        "target_area": "대퇴사두근, 대둔근, 발목",
        "why": "힐 받침을 제거해 Full ROM에 도전하되 TRX 보조는 유지합니다. 관절 각도만 변수로 제어합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "TRX를 가볍게 잡고 앞발 뒤꿈치가 바닥에 닿은 채로 깊이 내려가세요. 발목 앞쪽 느낌을 확인하세요.",
        "how": [
            "TRX나 기둥을 양손으로 가볍게 잡으세요",
            "플레이트 없이 앞발 뒤꿈치를 바닥에 유지하며 깊이 내려가세요",
            "10회 · 양측 교대"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    },
    {
        "order": 3, "type": "런지",
        "name": "맨몸 런지",
        "equipment": "없음",
        "target_area": "대퇴사두근, 대둔근, 발목",
        "why": "TRX 보조 없이 자체적으로 배측굴곡 ROM을 유지하며 런지 가능한지 확인합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "앞발 뒤꿈치가 바닥에 닿은 채로 내려가세요. 발목 앞쪽이 편안하게 유지되는지 확인하세요.",
        "how": [
            "한 발을 앞으로 내밀어 런지 자세를 잡으세요",
            "앞발 뒤꿈치가 바닥에 닿은 채로 내려가세요",
            "10회 · 양측 교대"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    },
    {
        "order": 4, "type": "런지",
        "name": "덤벨 런지",
        "equipment": "덤벨",
        "target_area": "대퇴사두근, 대둔근, 발목, 코어",
        "why": "ROM과 자세가 확보된 상태에서 부하를 추가합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "본인이 10회 이상 무리 없이 들 수 있는 가벼운 무게를 준비해 주세요. 이번 단계의 핵심은 무거운 무게가 아니라 부하가 더해져도 발목 앞쪽이 괜찮은지 확인하는 것입니다.",
        "how": [
            "덤벨을 양손에 들고 런지하세요",
            "앞발 뒤꿈치가 바닥에 닿은 채로 내려가세요",
            "10회 · 양측 교대"
        ],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    }
]

# ── cause-a-mild: 가동성 부족 경미 ─────────────────────────────────────
ca_mild = next(c for c in ankle['causes'] if c['id'] == 'cause-a-mild')
am_a = make_banded_talar_distraction()
am_a["set"] = "a"; am_a["order"] = 1
am_b = make_calf_stretch()
am_b["set"] = "a"; am_b["order"] = 2
am_b["cue"] = "뒤꿈치를 바닥에 붙이고 종아리가 가볍게 당기는 느낌을 찾으세요. 경미한 제한 해소를 위한 유지 스트레칭입니다."
am_c = make_wall_ankle_mobility()
am_c["set"] = "a"; am_c["order"] = 3
am_d = make_ankle_circles("발목 배측굴곡 방향으로 충분히 돌려 가동범위를 확인하세요.")
am_d["set"] = "a"; am_d["order"] = 4

am_e = make_open_half_kneeling()
am_e["set"] = "a_b"; am_e["order"] = 1
am_f = make_calf_toes_stretch()
am_f["set"] = "a_b"; am_f["order"] = 2
am_g = make_ankle_dorsiflexion()
am_g["set"] = "a_b"; am_g["order"] = 3
am_h = make_single_leg_balance()
am_h["set"] = "a_b"; am_h["order"] = 4

ca_mild['route']['stages'][0]['phase_a'] = [am_a, am_b, am_c, am_d, am_e, am_f, am_g, am_h]
ca_mild['route']['stages'][0]['phase_a_b'] = []
ca_mild['route']['stages'][0]['phase_b'] = [
    {
        "order": 1, "type": "런지",
        "name": "맨몸 런지 (가동성 확인)",
        "equipment": "없음",
        "target_area": "대퇴사두근, 대둔근, 발목",
        "why": "경미한 제한이므로 힐 받침 없이 바로 Full ROM 런지에서 발목 반응을 확인합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "앞발 뒤꿈치가 바닥에 닿은 채로 내려가세요. 발목 앞쪽이 편안하게 유지되는지 확인하세요.",
        "how": ["런지 자세로 내려가며 발목 앞쪽 반응을 확인하세요", "10회 · 양측 교대"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    },
    {
        "order": 2, "type": "런지",
        "name": "고블릿 런지",
        "equipment": "덤벨 또는 케틀벨",
        "target_area": "대퇴사두근, 대둔근, 발목",
        "why": "패턴이 확인됐다면 경부하로 발목 반응을 확인합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "본인이 10회 이상 무리 없이 들 수 있는 가벼운 무게를 준비해 주세요. 이번 단계의 핵심은 무거운 무게가 아니라 부하가 더해져도 발목 앞쪽이 괜찮은지 확인하는 것입니다.",
        "how": ["덤벨이나 케틀벨을 가슴 앞에 잡고 런지하세요", "10회 · 양측 교대"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    },
    {
        "order": 3, "type": "런지",
        "name": "덤벨 런지",
        "equipment": "덤벨",
        "target_area": "대퇴사두근, 대둔근, 발목, 코어",
        "why": "무게를 늘려 발목이 더 큰 부하에서도 안정적인지 확인합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "본인이 10회 이상 무리 없이 들 수 있는 가벼운 무게를 준비해 주세요. 이번 단계의 핵심은 무거운 무게가 아니라 발목이 어떻게 반응하는지 확인하는 것입니다.",
        "how": ["덤벨을 양손에 들고 런지하세요", "10회 · 양측 교대"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    },
    {
        "order": 4, "type": "런지",
        "name": "워킹 런지",
        "equipment": "없음 (또는 덤벨)",
        "target_area": "대퇴사두근, 대둔근, 발목, 코어",
        "why": "이동 패턴을 추가해 발목이 다양한 조건에서도 안정적인지 최종 검증합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "앞으로 걸어가며 런지하세요. 발목 앞쪽 반응이 이상하면 속도를 줄이세요.",
        "how": ["앞으로 걸어가며 런지 동작을 반복하세요", "10회 · 3세트"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    }
]

# ── cause-b: 불안정성 (외측 인대) ──────────────────────────────────────
cb = next(c for c in ankle['causes'] if c['id'] == 'cause-b')
cb_a = make_calf_stretch()
cb_a["set"] = "a"; cb_a["order"] = 1
cb_b = make_ankle_eversion()
cb_b["set"] = "a"; cb_b["order"] = 2
cb_c = make_single_leg_balance("발목을 천천히 돌리며 흔들리지 않게 균형을 잡으세요.")
cb_c["set"] = "a"; cb_c["order"] = 3
cb_d = make_ankle_circles("발목을 천천히 돌리며 바깥쪽이 안정적으로 유지되는지 확인하세요.")
cb_d["set"] = "a"; cb_d["order"] = 4

cb_e = make_open_half_kneeling()
cb_e["set"] = "a_b"; cb_e["order"] = 1
cb_f = make_calf_toes_stretch()
cb_f["set"] = "a_b"; cb_f["order"] = 2
cb_g = make_band_dorsiflexion()
cb_g["set"] = "a_b"; cb_g["order"] = 3
cb_h = make_towel_pickup()
cb_h["set"] = "a_b"; cb_h["order"] = 4

cb['route']['stages'][0]['phase_a'] = [cb_a, cb_b, cb_c, cb_d, cb_e, cb_f, cb_g, cb_h]
cb['route']['stages'][0]['phase_a_b'] = []
cb['route']['stages'][0]['phase_b'] = [
    {
        "order": 1, "type": "런지",
        "name": "벽 잡고 런지 (양손 지지)",
        "equipment": "없음 (벽 활용)",
        "target_area": "대퇴사두근, 대둔근, 발목 외측 인대",
        "why": "벽을 양손으로 잡아 전신 지지를 최대로 제공합니다. 발목 안정성을 외부에서 확보한 상태에서 런지 패턴을 확인합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "벽을 양손으로 잡고 런지하세요. 앞발 발목이 바깥으로 꺾이지 않는지 확인하세요.",
        "how": ["벽 앞에 서서 양손으로 벽을 짚으세요", "런지 자세로 내려가세요", "발목이 바깥으로 꺾이지 않는지 확인하세요", "10회 · 양측 교대"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    },
    {
        "order": 2, "type": "런지",
        "name": "벽 잡고 런지 (한손 지지)",
        "equipment": "없음 (벽 활용)",
        "target_area": "대퇴사두근, 대둔근, 발목 외측 인대",
        "why": "지지를 절반으로 줄여 발목이 더 능동적으로 안정을 잡아야 하는 조건을 만듭니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "한 손만 벽을 잡고 런지하세요. 발목이 안정적으로 유지되는지 확인하세요.",
        "how": ["한 손으로 벽을 잡고 런지하세요", "발목 안정성을 확인하세요", "10회 · 양측 교대"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    },
    {
        "order": 3, "type": "런지",
        "name": "맨몸 런지",
        "equipment": "없음",
        "target_area": "대퇴사두근, 대둔근, 발목 외측 인대",
        "why": "보조 없이 발목이 스스로 안정을 유지하며 런지 가능한지 확인합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "보조 없이 런지하세요. 발목이 흔들리면 속도를 줄이고 집중하세요.",
        "how": ["런지 자세로 내려가세요", "발목 안정성을 확인하세요", "10회 · 양측 교대"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    },
    {
        "order": 4, "type": "런지",
        "name": "덤벨 런지",
        "equipment": "덤벨",
        "target_area": "대퇴사두근, 대둔근, 발목 외측 인대, 코어",
        "why": "부하가 더해져도 발목 안정성이 유지되는지 최종 검증합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "본인이 10회 이상 무리 없이 들 수 있는 가벼운 무게를 준비해 주세요. 이번 단계의 핵심은 무거운 무게가 아니라 부하가 더해져도 발목이 안정적으로 유지되는지 확인하는 것입니다.",
        "how": ["덤벨을 양손에 들고 런지하세요", "발목 안정성을 확인하세요", "10회 · 양측 교대"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 통증 없이 수행"
    }
]

# ── cause-c: 과부하 (아킬레스건) ────────────────────────────────────────
cc = next(c for c in ankle['causes'] if c['id'] == 'cause-c')
cc['recovery_note'] = "이 루틴은 회복이 목적입니다. 단계를 서두르다 오히려 다시 아플 수 있어요."
cc['priority_note'] = "런지 세션은 48시간 이상 간격을 두세요. 런지 보폭도 단계별로 점진적으로 늘리세요."

cc_a = make_foam_roller_calf()
cc_a["set"] = "a"; cc_a["order"] = 1
cc_b = make_calf_toes_stretch()
cc_b["set"] = "a"; cc_b["order"] = 2
cc_c = make_ankle_circles("통증 없는 범위에서 천천히 부드럽게 회전하세요.")
cc_c["set"] = "a"; cc_c["order"] = 3
cc_d = make_towel_pickup()
cc_d["set"] = "a"; cc_d["order"] = 4

cc_e = make_open_half_kneeling()
cc_e["set"] = "a_b"; cc_e["order"] = 1
cc_f = make_ankle_eversion()
cc_f["set"] = "a_b"; cc_f["order"] = 2
cc_g = make_band_dorsiflexion()
cc_g["set"] = "a_b"; cc_g["order"] = 3
cc_h = make_single_leg_balance()
cc_h["set"] = "a_b"; cc_h["order"] = 4

cc['route']['stages'][0]['phase_a'] = [cc_a, cc_b, cc_c, cc_d, cc_e, cc_f, cc_g, cc_h]
cc['route']['stages'][0]['phase_a_b'] = []
cc['route']['stages'][0]['phase_b'] = [
    {
        "order": 1, "type": "런지",
        "name": "힐 엘리베이티드 런지 (아킬레스건 부하 감소)",
        "equipment": "플레이트 또는 웨지",
        "target_area": "대퇴사두근, 대둔근, 아킬레스건",
        "why": "뒤꿈치를 높여 아킬레스건 배측굴곡 부하를 줄인 상태에서 런지 패턴을 먼저 확인합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "앞발 뒤꿈치 아래에 플레이트를 받쳐 런지하세요. 아킬레스건에 편안하게 유지되는 게 정상이에요.",
        "how": ["앞발 뒤꿈치 아래에 플레이트를 받치세요", "런지 자세로 내려가세요", "아킬레스건 반응을 확인하세요", "10회 · 양측 교대"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 수행 + 다음날 통증 악화 없음"
    },
    {
        "order": 2, "type": "런지",
        "name": "맨몸 런지 (정상 발 위치)",
        "equipment": "없음",
        "target_area": "대퇴사두근, 대둔근, 아킬레스건",
        "why": "힐 받침 없이 정상 런지에서 아킬레스건 반응을 확인합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "앞발 뒤꿈치가 바닥에 닿은 채로 런지하세요. 아킬레스건 반응을 확인하세요.",
        "how": ["런지 자세로 내려가세요", "아킬레스건 반응을 확인하세요", "10회 · 양측 교대"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 수행 + 다음날 통증 악화 없음"
    },
    {
        "order": 3, "type": "런지",
        "name": "고블릿 런지",
        "equipment": "덤벨 또는 케틀벨",
        "target_area": "대퇴사두근, 대둔근, 아킬레스건",
        "why": "패턴이 안정됐다면 경부하로 아킬레스건 반응을 확인합니다.",
        "sets": "10회 · 3세트 (양측 교대)",
        "cue": "본인이 10회 이상 무리 없이 들 수 있는 가벼운 무게를 준비해 주세요. 이번 단계의 핵심은 무거운 무게가 아니라 아킬레스건이 어떻게 반응하는지 확인하는 것입니다.",
        "how": ["덤벨이나 케틀벨을 가슴 앞에 잡고 런지하세요", "10회 · 양측 교대"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 수행 + 다음날 통증 악화 없음"
    },
    {
        "order": 4, "type": "런지",
        "name": "덤벨 런지 (무게 점진)",
        "equipment": "덤벨",
        "target_area": "대퇴사두근, 대둔근, 아킬레스건, 코어",
        "why": "아킬레스건이 회복된 것을 확인했으니 부상 전 수준으로 무게를 천천히 되돌립니다.",
        "sets": "10회 · 3세트 (양측 교대), 주차별 점진",
        "cue": "세트수는 그대로 두고 무게만 올리세요. 아킬레스건 반응이 이상하면 바로 이전 무게로 돌아가세요.",
        "how": ["덤벨을 양손에 들고 런지하세요", "아킬레스건 반응을 확인하세요", "10회 · 양측 교대"],
        "video_url": "TBD",
        "progression_note": "진급 기준: 2회 연속 세션 수행 + 다음날 통증 악화 없음"
    }
]

with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('완료: 런지/발목 cause-a, a-mild, b, c Phase A+B 추가됨')
