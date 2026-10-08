"""정본(index.html 의 BUNDLED)을 읽고 쓰는 단일 창구.

서비스가 실제로 쓰는 데이터는 index.html 안의 BUNDLED 하나다. 스크립트는 직접 파싱하지 말고 이 모듈로 읽고 쓴다.
data/phase-exercises.json, docs/pt_review_전체동작.md, 검수판은 모두 정본에서 나온 사본이며,
정본과 맞는지는 scripts/check_seams.py 로 확인한다.

사용 예:
    from rehab_data import load_bundled, save_bundled, exercises
    b, ctx = load_bundled()
    for mv, ps, cause, stage, phase, ex in exercises(b):
        ...
    save_bundled(b, ctx)
"""
import json
import subprocess

INDEX = 'index.html'
PHASE = 'data/phase-exercises.json'
MARK = 'BUNDLED = '
# 화면에 나오지 않는 필드 / 이름처럼 쓰이는 필드 (문구 일괄 수정 때 건드리지 않는다)
SKIP = {'id', 'next', 'pass_next', 'fail_next', 'video_url', 'target_area', 'entry_question'}
NAME_LIKE = {'name', 'title', 'tag', 'sets', 'set', 'equipment'}
PHASE_KEYS = ('exercises', 'phase_a', 'phase_b')


def load_bundled(path=INDEX, rev=None):
    """(bundled, ctx) 를 돌려준다. rev 를 주면 그 커밋의 index.html 을 읽는다(읽기 전용)."""
    if rev:
        html = subprocess.run(['git', 'show', f'{rev}:{path}'], capture_output=True).stdout.decode('utf-8')
    else:
        html = open(path, encoding='utf-8').read()
    start = html.index(MARK) + len(MARK)
    bundled, length = json.JSONDecoder().raw_decode(html[start:])
    return bundled, {'path': path, 'html': html, 'start': start, 'length': length, 'rev': rev}


def dump_bundled(bundled):
    return json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))


def roundtrip_ok(bundled, ctx):
    """고치지 않은 정본을 다시 직렬화했을 때 원문과 같은가 (같아야 변경분만 diff 에 나온다)."""
    return dump_bundled(bundled) == ctx['html'][ctx['start']:ctx['start'] + ctx['length']]


def save_bundled(bundled, ctx):
    if ctx.get('rev'):
        raise ValueError('과거 커밋에서 읽은 정본은 저장할 수 없다')
    html, start, length = ctx['html'], ctx['start'], ctx['length']
    open(ctx['path'], 'w', encoding='utf-8').write(html[:start] + dump_bundled(bundled) + html[start + length:])


def load_phase(path=PHASE):
    return json.load(open(path, encoding='utf-8'))


def save_phase(phase, path=PHASE):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(phase, f, ensure_ascii=False, indent=2)
        f.write('\n')


PHASE_NOTE = ('Phase A: 매일 계속 (홀수/짝수 날 번갈아, 8개), Phase B: 하루 한 동작씩 (sequence, 4-5개). '
              '이 파일은 index.html 의 BUNDLED(정본)에서 생성한다. 직접 고치지 말고 scripts/export_phase_exercises.py 를 실행한다.')


def export_phase(b):
    """정본에서 data/phase-exercises.json 의 내용(원인별 Phase A/B 운동)을 만든다."""
    movs = []
    for mv in movements(b):
        sites = []
        for ps in mv['pain_sites']:
            cs = []
            for c in ps.get('causes', []):
                cause = {k: c[k] for k in ('id', 'label', 'tag', 'name', 'description', 'priority_note') if k in c}
                cause['route'] = {'stages': [
                    {k: st[k] for k in ('id', 'name', 'phase_a', 'phase_b', 'recovery_note') if k in st}
                    for st in c.get('route', {}).get('stages', []) if 'phase_a' in st or 'phase_b' in st]}
                cs.append(cause)
            sites.append({'id': ps['id'], 'name': ps['name'], 'causes': cs})
        movs.append({'id': mv['id'], 'name': mv['name'], 'pain_sites': sites})
    return {'_schema': 'Phase A/B Exercise Database', '_note': PHASE_NOTE, 'movements': movs}


def movements(b):
    for mf in b['manifest']:
        yield b[mf['id']] | {'id': mf['id']}


def pain_sites(b):
    for mv in movements(b):
        for ps in mv['pain_sites']:
            yield mv, ps


def causes(b):
    for mv, ps in pain_sites(b):
        for c in ps.get('causes', []):
            yield mv, ps, c


def tests(b):
    for mv, ps in pain_sites(b):
        for t in ps.get('tests', []):
            yield mv, ps, t


def exercises(b):
    """(동작, 부위, 원인, 단계, 단계 안 묶음 이름, 운동) 을 차례로 준다."""
    for mv, ps, c in causes(b):
        for st in c.get('route', {}).get('stages', []):
            for key in PHASE_KEYS:
                for ex in st.get(key) or []:
                    yield mv, ps, c, st, key, ex


def text_fields(obj, key=None):
    """화면에 나오는 본문 문자열을 (필드 이름, 문자열) 로 준다. 이름류·내부 필드는 뺀다."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from text_fields(v, k)
    elif isinstance(obj, list):
        for v in obj:
            yield from text_fields(v, key)
    elif isinstance(obj, str) and key not in SKIP and key not in NAME_LIKE:
        yield key, obj


def flow(ps):
    """한 통증 부위의 감별 흐름. 화면 코드(index.html 의 selectChoice·selectTestResult·goRetest)와 같은 규칙이다.

    돌려주는 값: 도달 가능한 노드 집합('q:..', 'test:..', 'cause:..'), 가리키는 곳이 없는 연결 목록,
    원인별 재검사로 뽑히는 검사 id 사전.
    """
    nodes = {}
    for q in ps.get('questions', []):
        nodes['q:' + q['id']] = [c.get('next') for c in q.get('choices', [])]
    for t in ps.get('tests', []):
        nodes['test:' + t['id']] = [t.get('pass_next'), t.get('fail_next'), (t.get('extra_choice') or {}).get('next')]
    cause_ids = {'cause:' + c['id'] for c in ps.get('causes', [])}
    dangling = [(src, n) for src, outs in nodes.items() for n in outs
                if isinstance(n, str) and not n.startswith('danger') and n not in nodes and n not in cause_ids]
    entry = 'q:' + str(ps.get('entry_question'))
    seen, todo = set(), [entry] if entry in nodes else []
    while todo:
        x = todo.pop()
        if x in seen:
            continue
        seen.add(x)
        todo += [n for n in nodes.get(x, []) if isinstance(n, str) and (n in nodes or n in cause_ids)]
    # goRetest: 전용 재검사(통과·실패 모두 그 원인)가 있으면 그것, 없으면 그 원인으로 실패(fail_next)하는 첫 검사,
    # 그것도 없으면 통과(pass_next)로 닿는 첫 검사를 재검사로 쓴다.
    retest = {}
    for c in cause_ids:
        tl = ps.get('tests', [])
        pick = (next((t for t in tl if t.get('fail_next') == c and t.get('pass_next') == c), None)
                or next((t for t in tl if t.get('fail_next') == c), None)
                or next((t for t in tl if t.get('pass_next') == c), None))
        if pick:
            retest[c] = 'test:' + pick['id']
    return seen, dangling, retest
