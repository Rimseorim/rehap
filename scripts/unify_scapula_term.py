"""견갑골·어깨뼈를 날개뼈로 통일하고 조사를 맞춘다 (docs/VIDEO_REVIEW_RULES.md 용어 표기).

index.html BUNDLED + data/phase-exercises.json 에 같은 치환을 적용한다. --apply 없으면 점검만.
target_area 등 화면에 렌더링되지 않는 필드는 건드리지 않는다.
"""
import json
import re
import sys
from collections import Counter

SKIP = {'id', 'next', 'pass_next', 'fail_next', 'video_url', 'target_area'}
JOSA = {'이나': '나', '으로': '로', '이': '가', '가': '가', '을': '를', '은': '는', '과': '와'}
PAT = re.compile(r'(견갑골(?:\(어깨뼈\))?|어깨뼈(?:\(견갑골\))?)(이나|으로|이|가|을|은|과)?')


def fix(s, pairs=None):
    def rep(m):
        word, josa = m.group(1), m.group(2) or ''
        if word == '견갑골' and s[max(0, m.start() - 4):m.start()] == '날개뼈(':
            return m.group(0)  # "날개뼈(견갑골)" 병기는 그대로 둔다
        end = m.end()
        if josa and word.startswith('견갑골') and (end == len(s) or s[end] in ' ,.·)'):
            josa = JOSA[josa]
        new = '날개뼈' + josa
        if pairs is not None:
            tail = re.match(r'\S*(?: \S+)?', s[end:]).group(0)
            pairs[(m.group(0) + tail, new + tail)] += 1
        return new
    return PAT.sub(rep, s)


def walk(o, pairs, key=None):
    """문자열을 제자리에서 고치고, 바뀐 문자열 수를 돌려준다."""
    n = 0
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, str):
                if k not in SKIP:
                    new = fix(v, pairs)
                    if new != v:
                        o[k] = new
                        n += 1
            else:
                n += walk(v, pairs, k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if isinstance(v, str):
                if key not in SKIP:
                    new = fix(v, pairs)
                    if new != v:
                        o[i] = new
                        n += 1
            else:
                n += walk(v, pairs, key)
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
