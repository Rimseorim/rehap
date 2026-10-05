"""정본(index.html BUNDLED)과 그 사본·규칙 사이의 이음새를 점검한다.

사용: python scripts/check_seams.py        (레포 루트에서 실행, [실패]가 하나라도 있으면 종료 코드 1)

[실패] 지금 깨끗하고 앞으로도 깨끗해야 하는 것 — 커밋 전에 고친다
[주의] 이미 어긋나 있어 사람이 방향을 정해야 하는 것 — 숫자가 늘지 않게 본다
"""
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_pt_review_doc import gen  # noqa: E402
from rehab_data import (causes, exercises, export_phase, flow, load_bundled, load_phase,  # noqa: E402
                        pain_sites, roundtrip_ok, tests, text_fields)

DOC = 'docs/pt_review_전체동작.md'
BANNED_CUE = re.compile(r'지 마세요|지 마십시오|지 않게|지 않도록|지 말고|지 맙니다|금지|말 것')
MODE_IN_NAME = re.compile(r'등척성|등장성|편심성|아이소메트릭|익센트릭')
fails, warns = [], []
QUIET = '-q' in sys.argv


def report(ok, label, items=(), warn=False):
    items = list(items)
    if ok:
        if not QUIET:
            print(f'[통과] {label}')
        return
    (warns if warn else fails).append(label)
    head = '[주의]' if warn else '[실패]'
    print(f'{head} {label}: {len(items)}건' + (f' — 예: {"; ".join(map(str, items[:3]))}' if items else ''))


def main():
    b, ctx = load_bundled()
    report(roundtrip_ok(b, ctx), '정본을 다시 직렬화하면 원문과 같다')

    # ---- 감별 흐름 ----
    dangling, no_entry, lost_causes, lost_q, dead_tests = [], [], [], [], []
    for mv, ps in pain_sites(b):
        where = f"{mv['name']}/{ps['name']}"
        seen, dang, retest = flow(ps)
        dangling += [f'{where} {s}→{n}' for s, n in dang]
        if not seen:
            no_entry.append(where)
        lost_causes += [f"{where}/{c['id']}" for c in ps.get('causes', []) if 'cause:' + c['id'] not in seen]
        lost_q += [f"{where}/{q['id']}" for q in ps.get('questions', []) if 'q:' + q['id'] not in seen]
        used = seen | set(retest.values())
        dead_tests += [f"{where}/{t['id']}({t['name']})" for t in ps.get('tests', []) if 'test:' + t['id'] not in used]
    report(not dangling, '모든 연결(next)이 실제 질문·검사·원인을 가리킨다', dangling)
    report(not no_entry, '모든 통증 부위에 시작 질문(entry_question)이 있다', no_entry)
    report(not lost_causes, '모든 원인에 시작 질문에서 도달할 수 있다', lost_causes)
    report(not lost_q, '모든 질문에 시작 질문에서 도달할 수 있다', lost_q, warn=True)
    report(not dead_tests, '모든 검사가 감별 또는 재검사에서 쓰인다', dead_tests, warn=True)

    # ---- 구조 ----
    no_danger = [f"{mv['name']}/{ps['name']}" for mv, ps in pain_sites(b) if not ps.get('danger')]
    report(not no_danger, '모든 통증 부위에 위험신호가 있다', no_danger)
    bad_route = []
    for mv, ps, c in causes(b):
        st = c.get('route', {}).get('stages', [])
        if len(st) != 3 or not any(s.get('checklist') for s in st) or not any(s.get('tips') for s in st):
            bad_route.append(f"{mv['name']}/{ps['name']}/{c['id']}")
    report(not bad_route, '모든 원인이 3단계·재평가 체크리스트·복귀 팁을 갖췄다', bad_route)
    ex_all = list(exercises(b))
    hollow = [f"{mv['name']}/{ps['name']}/{c['id']}/{e.get('name')}" for mv, ps, c, st, k, e in ex_all
              if not all(e.get(f) for f in ('name', 'why', 'how', 'cue', 'sets'))]
    report(not hollow, f'모든 운동({len(ex_all)}개)에 이름·왜·방법·큐·세트가 있다', hollow)

    # ---- 감별 로직 문서 ----
    doc = open(DOC, encoding='utf-8').read()
    date = re.search(r'생성일: (\d{4}-\d{2}-\d{2})', doc).group(1)
    report(gen(b, date) == doc, f'{DOC} 가 정본에서 다시 만든 것과 같다 (다르면 scripts/generate_pt_review_doc.py 실행)')

    # ---- 표기 규칙 (docs/VIDEO_REVIEW_RULES.md) ----
    texts = list(text_fields(b))
    report(not [s for _, s in texts if '견갑골' in s or '어깨뼈' in s], '본문에 견갑골·어깨뼈가 없다 (날개뼈로 통일)',
           [s[:40] for _, s in texts if '견갑골' in s or '어깨뼈' in s])
    cue_bad = [s[:50] for k, s in texts if k in ('how', 'cue') and BANNED_CUE.search(s)]
    report(not cue_bad, 'how·cue 에 금지 표현(~지 마세요·~않게 등)이 없다', cue_bad)
    memo = [s[:50] for _, s in texts if '규칙 적용' in s or '상위 결함' in s or re.search(r'\d단계와 동일', s)]
    report(not memo, '본문에 내부 메모·단계 번호 참조·"상위 결함" 표현이 없다', memo)
    mode_names = sorted({e['name'] for *_, e in ex_all if MODE_IN_NAME.search(e['name'])})
    report(not mode_names, '운동명에 운동 방식 용어(등척성·편심성 등)가 없다', mode_names)
    test_names = sorted({t['name'] for _, _, t in tests(b) if '테스트' in t['name']})
    report(not test_names, '검사 제목에 "테스트"가 없다 ("검사"로 통일)', test_names)

    # ---- 정본 ↔ data/phase-exercises.json ----
    report(load_phase() == export_phase(b), 'data/phase-exercises.json 이 정본에서 만든 것과 같다 (다르면 scripts/export_phase_exercises.py 실행)')

    # ---- 참고 수치 ----
    no_video = sum(1 for *_, e in ex_all if not str(e.get('video_url', '')).startswith('http'))
    print(f'[참고] 영상이 없는 운동 {no_video}/{len(ex_all)} · 원인 {len(list(causes(b)))} · 검사 {len(list(tests(b)))}')
    print(f'\n결과: 실패 {len(fails)} · 주의 {len(warns)}')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
