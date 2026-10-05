"""본문에 남은 줄임말 "견갑"을 날개뼈로 맞춘다 (견갑골·어깨뼈 → 날개뼈 통일의 후속).

index.html BUNDLED + data/phase-exercises.json 에 같은 치환을 적용한다. --apply 없으면 점검만.
건드리지 않는 것: 이름·제목 등 이름류 필드, 운동 이름을 가리키는 "견갑 세팅"·"견갑 슬라이드",
해부명 "견갑와"(관절 오목)·"견갑거근" 등 뒤에 다른 글자가 붙은 낱말. "견갑면"은 "날개뼈 평면"으로 쓴다.
"""
import json
import re
import sys
from collections import Counter

SKIP = {'id', 'next', 'pass_next', 'fail_next', 'video_url', 'target_area'}
NAME_LIKE = {'name', 'title', 'tag', 'sets', 'set', 'equipment'}
JOSA = {'을': '를', '이': '가', '은': '는', '과': '와'}
PAT = re.compile(r'견갑면|견갑(?! 세팅| 슬라이드)(을|이|은|과)?(?=[\s,.·)(→]|의|만|도|에|$)')


def fix(s, pairs=None):
    def rep(m):
        if m.group(0) == '견갑면':
            new = '날개뼈 평면'
        else:
            new = '날개뼈' + JOSA.get(m.group(1) or '', '')
        if pairs is not None:
            tail = re.match(r'\S*(?: \S+)?', s[m.end():]).group(0)[:10]
            pairs[(m.group(0) + tail, new + tail)] += 1
        return new
    return PAT.sub(rep, s)


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
    if apply:
        if not same:
            sys.exit('index.html 재직렬화가 원문과 달라 중단')
        raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
        open('index.html', 'w', encoding='utf-8').write(html[:start] + raw + html[start + length:])
        with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
            json.dump(phase, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print('적용 완료')
