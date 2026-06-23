import json

with open('data/phase-exercises.json', encoding='utf-8') as f:
    d = json.load(f)

# ── 공통 짝수날 운동 ────────────────────────────────────────────────────

def 종아리스트레칭_가자미근():
    return {"set":"a_b","type":"스트레칭","name":"종아리 스트레칭 (가자미근)",
            "equipment":"없음 (벽 활용)","target_area":"가자미근",
            "why":"가자미근을 집중 이완합니다. 무릎을 구부려 비복근을 이완하고 가자미근만 늘립니다.",
            "sets":"양측 각 40초 · 2세트",
            "cue":"뒤쪽 무릎을 살짝 구부린 채 뒤꿈치를 바닥에 붙이세요. 정강이 아래쪽이 당기는 느낌이 정상입니다.",
            "how":["벽에 양손을 짚고 스트레칭할 다리를 뒤로 보내세요",
                   "뒤쪽 무릎을 살짝 구부린 채 뒤꿈치를 바닥에 붙이세요",
                   "40초 유지 · 양측 교대"],"video_url":"TBD"}

def 오픈하프닐링시프트():
    return {"set":"a_b","type":"스트레칭","name":"오픈 하프닐링 시프트",
            "equipment":"없음","target_area":"내전근, 고관절 관절낭, 발목 관절",
            "why":"고관절 관절낭과 내전근을 이완합니다. 발목 배측굴곡 제한에서 고관절과 발목을 복합적으로 준비합니다.",
            "sets":"양측 각 30초 · 2세트",
            "cue":"체중을 이동할 때 상체가 앞으로 숙여지지 않도록 척추 중립을 수직으로 유지하세요.",
            "how":["한쪽 무릎을 꿇은 상태에서 반대쪽 다리를 옆으로 열어 딛으세요",
                   "체중을 디딘 발 방향으로 수평 이동시키세요","30초 · 양측 교대"],"video_url":"TBD"}

def 한발균형서기():
    return {"set":"a_b","type":"활성화","name":"한 발 균형 서기",
            "equipment":"없음","target_area":"지면 수용기, 비복근, 후경골근, 발목 심부 안정화",
            "why":"발목 고유감각과 심부 안정화를 훈련합니다. 배측굴곡 가동성 회복 후 기능적 안정성을 확보합니다.",
            "sets":"양측 각 30초 · 2세트",
            "cue":"엄지발가락·새끼발가락·뒤꿈치 세 곳이 고르게 바닥을 누르도록 유지하세요.",
            "how":["한 발로 서서 30초 버티세요","양측 교대"],"video_url":"TBD"}

def 발목배측굴곡운동():
    return {"set":"a_b","type":"활성화","name":"발목 배측굴곡 운동",
            "equipment":"없음","target_area":"전경골근",
            "why":"전경골근을 능동적으로 강화합니다. 스쿼트 하강 시 배측굴곡 패턴을 지지합니다.",
            "sets":"양측 각 15회 · 3세트",
            "cue":"발목 관절만 움직이며 발끝을 정강이 방향으로 최대한 높이 들어 올리세요.",
            "how":["벽에 등을 기대고 서세요","발끝을 정강이 방향으로 최대한 들어 올리세요",
                   "15회 · 양측 교대"],"video_url":"TBD"}

def 하프닐링고관절굴곡근스트레칭():
    return {"set":"a_b","type":"스트레칭","name":"하프닐링 고관절 굴곡근 스트레칭",
            "equipment":"없음","target_area":"장요근, 대퇴직근",
            "why":"고관절 굴곡근을 이완합니다. 굴곡근이 단축되면 골반 전방경사가 생겨 슬개대퇴 부하가 증가합니다.",
            "sets":"양측 각 60초 · 2세트",
            "cue":"앞쪽 다리에 체중을 실으며 뒤쪽 허벅지 앞이 당기는 느낌을 찾으세요. 허리가 젖혀지지 않도록 복부를 살짝 조이세요.",
            "how":["한쪽 무릎을 바닥에 대고 반대쪽 다리를 앞으로 내밀어 런지 자세를 취하세요",
                   "상체를 세우며 뒤쪽 허벅지 앞이 당기는 느낌을 유지하세요",
                   "60초 · 양측 교대"],"video_url":"TBD"}

def 코치스트레칭():
    return {"set":"a_b","type":"스트레칭","name":"코치 스트레칭 (Couch Stretch)",
            "equipment":"없음 (벽 또는 소파 활용)","target_area":"장요근, 대퇴직근",
            "why":"장요근을 직접 이완합니다. 고관절 굴곡근 단축이 무릎과 슬개골에 추가 부담을 줄 수 있습니다.",
            "sets":"양측 각 60초 · 2세트",
            "cue":"앞쪽 다리에 체중을 실으며 뒤쪽 허벅지 앞이 당기는 느낌을 찾으세요.",
            "how":["한쪽 무릎을 벽 앞에 대고 발을 벽에 붙이세요",
                   "반대쪽 다리를 앞으로 내밀어 런지 자세를 취하세요",
                   "상체를 세우며 60초 · 양측 교대"],"video_url":"TBD"}

def 글루트브릿지():
    return {"set":"a_b","type":"활성화","name":"글루트 브릿지",
            "equipment":"없음","target_area":"대둔근, 햄스트링",
            "why":"대둔근을 활성화합니다. 외전근의 길항 패턴을 강화해 무릎 안정성을 지지합니다.",
            "sets":"15회 · 3세트",
            "cue":"최고점에서 엉덩이를 2초 쥐어짜세요. 허리가 아니라 엉덩이로 올라가는 느낌이 정상입니다.",
            "how":["바닥에 누워 무릎을 세우세요","엉덩이를 들어 무릎·골반·어깨가 일직선이 되게 하세요",
                   "최고점에서 2초 유지 후 천천히 내립니다","15회 · 3세트"],"video_url":"TBD"}

def 버드독():
    return {"set":"a_b","type":"활성화","name":"버드 독",
            "equipment":"없음","target_area":"척추기립근, 다열근, 대둔근",
            "why":"심부 안정근을 활성화합니다. 골반 안정성을 높여 무릎 부하를 줄입니다.",
            "sets":"좌우 교대 10회 · 3세트",
            "cue":"골반이 옆으로 기울지 않도록 속도보다 안정성에 집중합니다.",
            "how":["네발기기 자세에서 척추를 중립으로 맞추세요",
                   "한쪽 팔과 반대쪽 다리를 몸통과 수평이 되도록 뻗어줍니다",
                   "2~3초 유지 후 돌아옵니다","10회 · 양측 교대"],"video_url":"TBD"}

def 햄스트링스트레칭():
    return {"set":"a_b","type":"스트레칭","name":"햄스트링 스트레칭",
            "equipment":"없음","target_area":"햄스트링",
            "why":"햄스트링을 이완합니다. 햄스트링 긴장이 슬개골에 간접적 부담을 줄 수 있습니다.",
            "sets":"양측 각 40초 · 2세트",
            "cue":"등을 말지 마세요. 척추 중립을 유지한 채 골반만 접어 내려가세요.",
            "how":["바닥에 한쪽 다리를 펴고 앉거나 서서 발을 낮은 곳에 올리세요",
                   "척추를 곧게 세우고 상체를 앞으로 지긋이 숙여주세요",
                   "허벅지 뒤쪽이 당기는 느낌 유지 40초 · 양측 교대"],"video_url":"TBD"}

def 폼롤러IT밴드():
    return {"set":"a_b","type":"스트레칭","name":"폼롤러 IT밴드 이완",
            "equipment":"폼롤러","target_area":"IT밴드, 외측 허벅지",
            "why":"외측 허벅지와 IT밴드를 이완합니다. 슬개골 외측 당김을 줄입니다.",
            "sets":"양측 각 60초 · 2세트",
            "cue":"뭉친 곳에서 10~15초 멈췄다가 천천히 이동하세요.",
            "how":["옆으로 누워 폼롤러를 외측 허벅지 아래에 두세요",
                   "외측 허벅지를 따라 천천히 롤링하세요","뭉친 곳에서 멈추세요",
                   "60초 · 양측 교대"],"video_url":"TBD"}

def 클램셸():
    return {"set":"a_b","type":"활성화","name":"클램셸",
            "equipment":"없음","target_area":"중둔근 후부 섬유, 고관절 심부 외회전근",
            "why":"중둔근을 활성화합니다. 무릎 내측 쏠림을 방지하는 핵심 근육입니다.",
            "sets":"양측 각 15회 · 3세트",
            "cue":"발은 붙인 채 무릎만 조개처럼 열어주세요. 골반이 뒤로 돌아가지 않도록 주의하세요.",
            "how":["옆으로 누워 무릎을 90도로 구부리고 양 뒤꿈치를 붙이세요",
                   "골반을 고정한 채 위쪽 무릎을 천천히 열어주세요","15회 · 양측 교대"],"video_url":"TBD"}

def 사이드라잉힙어브덕션():
    return {"set":"a_b","type":"활성화","name":"사이드라잉 힙 어브덕션",
            "equipment":"없음","target_area":"중둔근, 대퇴근막장근",
            "why":"중둔근을 강화합니다. 무릎 안정성과 직결된 핵심 외전근입니다.",
            "sets":"양측 각 15회 · 3세트",
            "cue":"뒤꿈치가 몸통보다 약간 뒤를 향하게 한 상태에서 대각선 후상방으로 들어 올리세요.",
            "how":["옆으로 바르게 누워 아래쪽 다리는 구부려 중심을 잡으세요",
                   "위쪽 다리는 무릎을 완전히 펴고 뒤꿈치를 약간 뒤로 향하게 하세요",
                   "대각선 후상방으로 들어 올리세요","15회 · 양측 교대"],"video_url":"TBD"}

# ── 짝수날 세트 정의 ─────────────────────────────────────────────────

# 발목 가동성 짝수날: 종아리(가자미근) + 오픈하프닐링 → 한발균형 + 발목배측굴곡
def ankle_mobility_even():
    a = 종아리스트레칭_가자미근(); a["order"] = 1
    b = 오픈하프닐링시프트(); b["order"] = 2
    c = 한발균형서기(); c["order"] = 3
    d_ex = 발목배측굴곡운동(); d_ex["order"] = 4
    return [a, b, c, d_ex]

# 고관절 외전근 약화 짝수날: 하프닐링굴곡근 + 코치 → 글루트브릿지 + 버드독
def hip_abductor_weakness_even():
    a = 하프닐링고관절굴곡근스트레칭(); a["order"] = 1
    b = 코치스트레칭(); b["order"] = 2
    c = 글루트브릿지(); c["order"] = 3
    d_ex = 버드독(); d_ex["order"] = 4
    return [a, b, c, d_ex]

# 신경근/슬개대퇴 짝수날: 햄스트링 + IT밴드 → 클램셸 + 글루트브릿지
def patellofemoral_even():
    a = 햄스트링스트레칭(); a["order"] = 1
    b = 폼롤러IT밴드(); b["order"] = 2
    c = 클램셸(); c["order"] = 3
    d_ex = 글루트브릿지(); d_ex["order"] = 4
    return [a, b, c, d_ex]

# TFL/IT밴드 과긴장 짝수날: 햄스트링 + 코치 → 글루트브릿지 + 버드독
def tfl_overuse_even():
    a = 햄스트링스트레칭(); a["order"] = 1
    b = 코치스트레칭(); b["order"] = 2
    c = 글루트브릿지(); c["order"] = 3
    d_ex = 버드독(); d_ex["order"] = 4
    return [a, b, c, d_ex]

# 특이소견 없음 짝수날: 하프닐링굴곡근 + 햄스트링 → 클램셸 + 사이드라잉
def general_conditioning_even():
    a = 하프닐링고관절굴곡근스트레칭(); a["order"] = 1
    b = 햄스트링스트레칭(); b["order"] = 2
    c = 클램셸(); c["order"] = 3
    d_ex = 사이드라잉힙어브덕션(); d_ex["order"] = 4
    return [a, b, c, d_ex]

# ── 각 cause에 짝수날 추가 ──────────────────────────────────────────────

even_day_map = {
    ('back-squat', 'knee', 'cause-a'): ankle_mobility_even,
    ('back-squat', 'knee', 'cause-b'): hip_abductor_weakness_even,
    ('back-squat', 'knee', 'cause-c'): patellofemoral_even,
    ('back-squat', 'knee', 'cause-d'): general_conditioning_even,
    ('lunge',      'knee', 'cause-a'): ankle_mobility_even,
    ('lunge',      'knee', 'cause-b'): hip_abductor_weakness_even,
    ('lunge',      'knee', 'cause-c'): tfl_overuse_even,
    ('lunge',      'knee', 'cause-d'): patellofemoral_even,
    ('lunge',      'knee', 'cause-e'): general_conditioning_even,
    ('deadlift',   'knee', 'cause-a'): patellofemoral_even,
    ('deadlift',   'knee', 'cause-b'): hip_abductor_weakness_even,
    ('deadlift',   'knee', 'cause-c'): tfl_overuse_even,
    ('deadlift',   'knee', 'cause-d'): general_conditioning_even,
}

count = 0
for mv in d['movements']:
    for ps in mv['pain_sites']:
        for c in ps.get('causes', []):
            key = (mv['id'], ps['id'], c['id'])
            if key in even_day_map:
                pa = c['route']['stages'][0].get('phase_a', [])
                # 기존 a_b 있으면 제거
                pa = [e for e in pa if e.get('set') != 'a_b']
                # 짝수날 추가
                pa += even_day_map[key]()
                c['route']['stages'][0]['phase_a'] = pa
                count += 1

print(f'완료: {count}개 cause 짝수날 추가됨')

with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
