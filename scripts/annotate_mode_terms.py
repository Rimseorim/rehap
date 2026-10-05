"""운동 방식 용어에 규칙서 표기(풀이 괄호)를 필드별 첫 등장에 붙인다 (docs/VIDEO_REVIEW_RULES.md 운동 방식 용어 표).

대상: 끝범위·브레이싱·릴리즈·숄더 패킹·PAILs/RAILs.
index.html BUNDLED + data/phase-exercises.json 에 같은 치환을 적용한다. --apply 없으면 점검만.
건드리지 않는 것: 이름·제목·세트 표기, 화면에 안 나오는 필드, 이미 괄호 안에 있거나 풀이가 붙은 표현,
"패시브 릴리즈"·"액티브 행"·"[PAILs]" 라벨·등척성·편심성 (문장을 새로 써야 해서 따로 승인받는다).
"""
import json
import re
import sys
from collections import Counter

SKIP = {'id', 'next', 'pass_next', 'fail_next', 'video_url', 'target_area'}
NAME_LIKE = {'name', 'title', 'tag', 'sets', 'set', 'equipment'}
# (용어, 표기, 쉬운 말이 앞에 오는가) — 쉬운 말이 앞이면 조사를 쉬운 말 받침에 맞춘다
TERMS = [
    ('PAILs/RAILs', '끝에서 힘주고 버티기(PAILs/RAILs)', False),
    ('숄더 패킹', '숄더 패킹(어깨 내려 고정하기)', False),
    ('끝범위', '움직임의 맨 끝(끝범위)', True),
    ('릴리즈', '릴리즈(뭉친 곳 눌러 풀기)', False),
    ('브레이싱', '브레이싱(배에 힘줘 몸통 잡기)', False),
]
JOSA = {'를': '을', '가': '이', '는': '은', '와': '과', '로': '으로'}


def fix(s, pairs=None):
    for term, label, easy_first in TERMS:
        i = s.find(term)
        if i < 0:
            continue
        j = i + len(term)
        if s[:i].count('(') > s[:i].count(')'):
            continue  # 이미 괄호 안
        if s[j:j + 1] == '(' or s[j:j + 2] == ' (':
            continue  # 이미 풀이가 붙음
        if term == '릴리즈' and s[:i].endswith('패시브 '):
            continue  # "패시브 릴리즈"는 따로 본다
        josa = ''
        if easy_first and s[j:j + 1] in JOSA and (j + 1 == len(s) or s[j + 1] in ' ,.·)'):
            josa = JOSA[s[j]]
            j += 1
        new = label + josa
        if pairs is not None:
            tail = re.match(r'\S*(?: \S+)?', s[j:]).group(0)
            pairs[(s[i:j] + tail, new + tail)] += 1
        s = s[:i] + new + s[j:]
    return s


def walk(o, pairs, key=None):
    """문자열을 제자리에서 고치고, 바뀐 문자열 수를 돌려준다."""
    n = 0
    items = o.items() if isinstance(o, dict) else enumerate(o) if isinstance(o, list) else ()
    for k, v in items:
        field = k if isinstance(o, dict) else key
        if isinstance(v, str):
            if field not in SKIP and field not in NAME_LIKE:
                new = fix(v, pairs)
                if new != v:
                    o[k] = new
                    n += 1
        else:
            n += walk(v, pairs, field)
    return n


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    apply = '--apply' in sys.argv
    html = open('index.html', encoding='utf-8').read()
    start = html.index('BUNDLED = ') + len('BUNDLED = ')
    bundled, length = json.JSONDecoder().raw_decode(html[start:])
    same = json.dumps(bundled, ensure_ascii=False, separators=(',', ':')) == html[start:start + length]
    print('index 재직렬화 동일:', same)
    pi, pd = Counter(), Counter()
    ni = walk(bundled, pi)
    phase = json.load(open('data/phase-exercises.json', encoding='utf-8'))
    nd = walk(phase, pd)
    print('바뀐 문자열: index', ni, '/ data', nd, '| 치환: index', sum(pi.values()), '/ data', sum(pd.values()))
    for (old, new), c in pi.most_common():
        print(f'  {c:3d}  {old}  =>  {new}')
    only_data = [(k, c) for k, c in pd.items() if k not in pi]
    if only_data:
        print('data 에만 있는 문맥:')
        for (old, new), c in only_data:
            print(f'  {c:3d}  {old}  =>  {new}')
    if apply:
        if not same:
            sys.exit('index.html 재직렬화가 원문과 달라 중단')
        raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
        open('index.html', 'w', encoding='utf-8').write(html[:start] + raw + html[start + length:])
        with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
            json.dump(phase, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print('적용 완료')
