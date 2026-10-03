"""strip_paren_tags.py(e685ada)로 지운 괄호 꼬리표 중, 정보가 why·sets·cue·how에 없는 것만 이름에 되살린다.

단계·부하 표기(경부하·무게 점진 등)는 규칙대로 삭제를 유지한다. 되살릴 대상은 그 외 조각 중
조각의 핵심 단어가 본문(why·sets·cue·how)에 모두 있지 않은 것.
--apply 없으면 점검만.
"""
import json
import re
import subprocess
import sys
from collections import defaultdict

BASE = 'e685ada~1'
LOAD = re.compile(r'경부하|중부하|정상 부하|무게|%|점진|초저중량|초경부하|부하 도입|부하 증가|보수적 강도|진폭|볼륨|동적 부하|무부하 패턴')
TAIL = re.compile(r'\(([^()]*)\)\s*$')
STEM = re.compile(r'^(.*?)\s*\([^()]*\)\s*$')
LATIN = re.compile(r'[A-Za-z]')
restored = defaultdict(list)


def body(o):
    return ' '.join([o.get('why', ''), o.get('sets', ''), o.get('cue', '')] + list(o.get('how', [])))


def toks(p):
    return [t for t in re.split(r'[^가-힣0-9~%]+', p) if len(t) >= 2]


def parts_of(name):
    m = TAIL.search(name)
    return [p.strip() for p in m.group(1).split(',') if p.strip()] if m else []


def fix_pair(a, b):
    """a: 옛 항목, b: 현재 항목. b['name']을 필요하면 되살린 이름으로 바꾼다."""
    if a['name'] == b['name']:
        return
    old_parts = parts_of(a['name'])
    new_parts = parts_of(b['name'])
    bd = body(b)
    want = []
    for p in old_parts:
        if p in new_parts:
            want.append(p)
            continue
        if LATIN.search(p) or LOAD.search(p):
            continue
        ts = toks(p)
        if ts and all(t in bd for t in ts):
            continue
        want.append(p)
        restored[(a['name'], p)].append(1)
    if want == new_parts:
        return
    m = STEM.match(a['name'])
    stem = m.group(1) if m else a['name']
    b['name'] = f"{stem} ({', '.join(want)})" if want else stem


def walk(a, b):
    if isinstance(a, dict):
        if 'how' in a and 'name' in a:
            fix_pair(a, b)
            return
        for k in a:
            if k in b:
                walk(a[k], b[k])
    elif isinstance(a, list) and len(a) == len(b):
        for x, y in zip(a, b):
            walk(x, y)


def git_show(path):
    return subprocess.check_output(['git', 'show', f'{BASE}:{path}']).decode('utf-8')


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    html = open('index.html', encoding='utf-8').read()
    start = html.index('BUNDLED = ') + len('BUNDLED = ')
    new_b, length = json.JSONDecoder().raw_decode(html[start:])
    old_h = git_show('index.html')
    os_ = old_h.index('BUNDLED = ') + len('BUNDLED = ')
    old_b = json.JSONDecoder().raw_decode(old_h[os_:])[0]
    walk(old_b, new_b)
    n_index = len(restored)
    print('index 되살린 (이름, 조각) 고유', n_index, '/ 건수', sum(len(v) for v in restored.values()))
    for (n, p), v in sorted(restored.items(), key=lambda x: x[0][1]):
        print(f'  {len(v)}건 | {n} | {p}')
    restored.clear()
    new_p = json.load(open('data/phase-exercises.json', encoding='utf-8'))
    old_p = json.loads(git_show('data/phase-exercises.json'))
    walk(old_p['movements'], new_p['movements'])
    print('data 되살린 건수', sum(len(v) for v in restored.values()))
    if apply:
        raw = json.dumps(new_b, ensure_ascii=False, separators=(',', ':'))
        open('index.html', 'w', encoding='utf-8').write(html[:start] + raw + html[start + length:])
        with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
            json.dump(new_p, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print('적용 완료')
