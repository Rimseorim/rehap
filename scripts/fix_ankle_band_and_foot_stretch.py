import json

PHASE_PATH = 'data/phase-exercises.json'
INDEX_PATH = 'index.html'

BAND = '밴드 거골 후방 견인 스트레칭'
FOOT_OLD = '종아리·발바닥 복합 스트레칭'
FOOT_NEW = '발바닥·발가락 스트레칭'

BAND_OLD_FORMS = ['복숭아뼈 바로 위(발목 앞쪽)에 걸고', '복숭아뼈 바로 위에 걸고']
BAND_NEW = '발목 앞쪽 접히는 부위(복숭아뼈 높이)에 걸고'

LUNGE_ANKLE_A_BAND_CUE = '밴드를 발목 앞쪽 접히는 부위에 걸고 뒤에서 당기게 하세요. 뒤꿈치를 바닥에 붙인 채 무릎을 둘째 발가락 방향으로 앞으로 미세요. 발목 앞쪽이 콕 집히는 통증이 있으면 범위를 줄이세요. 종아리가 당기는 느낌은 괜찮습니다.'

FOOT_CUE_BASE = '발가락을 꺾어 세운 채 체중을 뒤꿈치 쪽으로 천천히 실으세요. 발바닥과 발가락 아래가 당기는 정도에서 멈추세요. 저리거나 찌르는 느낌은 피하세요.'
FOOT_CUE = {
    'cause-a': FOOT_CUE_BASE,
    'cause-b': FOOT_CUE_BASE + ' 발목 바깥쪽이 불안하거나 아프면 체중을 줄이세요.',
    'cause-c': FOOT_CUE_BASE + ' 발뒤꿈치가 찌르듯 아프면 체중을 줄이세요.',
}
FOOT_WHY_A = '발바닥(족저근막)과 발가락 아래를 늘려 발 앞쪽의 뻣뻣함을 풀어 줍니다.'
FOOT_WHY_BC = FOOT_WHY_A + ' 종아리·아킬레스건에는 직접 부담이 적은 이완입니다.'
SQUAT_WHY = {
    'cause-c': '족저근막(발바닥)을 이완합니다. 홀수날 Calf Stretch와 다른 타겟으로 차별화됩니다.',
    'cause-d': '족저근막(발바닥)을 이완합니다. 홀수날 Calf Stretch와 다른 타겟입니다.',
}

ID_NORM = {'back-squat': 'squat', 'vertical-press': 'press-vertical', 'horizontal-press': 'press-horizontal'}

log = []


def replace_in(text, olds, new):
    for o in olds:
        if o in text:
            return text.replace(o, new), True
    return text, False


def apply(mv_id, ps_id, cause):
    stage = cause['route']['stages'][0]
    cid = cause['id']
    for key in ('phase_a', 'phase_b'):
        for e in stage.get(key) or []:
            # 밴드 위치 통일 (사실관계 → 모든 인스턴스)
            if e['name'] == BAND:
                how = []
                for h in e['how']:
                    h2, ch = replace_in(h, BAND_OLD_FORMS, BAND_NEW)
                    if ch:
                        log.append(f'band how {mv_id}/{ps_id}/{cid}')
                    how.append(h2)
                e['how'] = how
                cue = e.get('cue') or ''
                if mv_id == 'lunge' and ps_id == 'ankle' and cid == 'cause-a':
                    e['cue'] = LUNGE_ANKLE_A_BAND_CUE
                    log.append(f'band cue(new) {mv_id}/{ps_id}/{cid}')
                else:
                    c2, ch = replace_in(cue, BAND_OLD_FORMS, BAND_NEW)
                    if ch:
                        e['cue'] = c2
                        log.append(f'band cue {mv_id}/{ps_id}/{cid}')
            # 발바닥 스트레칭: 이름 정정 (squat/ankle/cause-a는 종아리 단계가 있어 유지)
            if e['name'] == FOOT_OLD and not (mv_id == 'squat' and ps_id == 'ankle' and cid == 'cause-a'):
                e['name'] = FOOT_NEW
                log.append(f'foot rename {mv_id}/{ps_id}/{cid}')
                if mv_id == 'lunge' and ps_id == 'ankle':
                    assert not (e.get('cue') or '').strip()
                    e['cue'] = FOOT_CUE[cid]
                    e['why'] = FOOT_WHY_A if cid == 'cause-a' else FOOT_WHY_BC
                    log.append(f'foot cue+why {mv_id}/{ps_id}/{cid}')
                if mv_id == 'squat' and ps_id == 'ankle' and cid in SQUAT_WHY:
                    e['why'] = SQUAT_WHY[cid]
                    log.append(f'foot why {mv_id}/{ps_id}/{cid}')


def walk_data(d):
    for m in d['movements']:
        mv_id = ID_NORM.get(m['id'], m['id'])
        for ps in m['pain_sites']:
            for c in ps['causes']:
                apply(mv_id, ps['id'], c)


def walk_bundled(b):
    for mv_id, m in b.items():
        if mv_id == 'manifest':
            continue
        for ps in m['pain_sites']:
            for c in ps['causes']:
                apply(mv_id, ps['id'], c)


# 1) data/phase-exercises.json
with open(PHASE_PATH, encoding='utf-8') as f:
    d = json.load(f)
walk_data(d)
data_log = list(log)
log.clear()
with open(PHASE_PATH, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

# 2) index.html BUNDLED
with open(INDEX_PATH, encoding='utf-8') as f:
    html = f.read()
start = html.index('BUNDLED = ') + len('BUNDLED = ')
bundled, length = json.JSONDecoder().raw_decode(html[start:])
walk_bundled(bundled)
new_raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
html = html[:start] + new_raw + html[start + length:]
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print('data 변경', len(data_log), '/ index 변경', len(log))
if sorted(data_log) != sorted(log):
    print('WARN: data와 index 변경 목록이 다름')
for x in sorted(log):
    print(' -', x)
