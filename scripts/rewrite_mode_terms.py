"""패시브·액티브 행·PAILs/RAILs 라벨·등척성·편심성 문구를 승인된 쉬운 말 문구로 바꾼다 (2026-10-05 문구안 9종).

index.html BUNDLED + data/phase-exercises.json 에 같은 치환을 적용한다. --apply 없으면 점검만.
건드리지 않는 것: 이름·제목·세트 표기, 화면에 안 나오는 필드, 이미 괄호 안에 풀이로 들어간 표현.
남겨 둔 것(새 문구 승인 필요): "편심성 운동처럼"·"편심성으로 늘어나며"·"편심성 수축으로"·"편심성 통제/제어"·"등척성 장력/긴장".
"""
import json
import re
import sys
from collections import Counter

SKIP = {'id', 'next', 'pass_next', 'fail_next', 'video_url', 'target_area'}
NAME_LIKE = {'name', 'title', 'tag', 'sets', 'set', 'equipment'}

HOLD = '제자리에서 힘만 주며 버티'
ECC_LOAD = '근육이 늘어나면서 힘을 쓰는 '
ECC_TRAIN = '천천히 내리며 힘 쓰는 '
JOSA = {'를': '을', '가': '이', '와': '과'}
RULES = [
    (r'패시브 릴리즈합니다', '힘을 뺀 채 눌러 풀어 줍니다(패시브 릴리즈)'),
    (r'(쪽|굴곡근|신전근) 패시브 릴리즈\.', r'\1을 힘을 뺀 채 눌러 풀어 줍니다(패시브 릴리즈).'),
    (r'폼롤러 패시브 릴리즈만', '폼롤러로 힘을 뺀 채 눌러 푸는 것(패시브 릴리즈)만'),
    (r'패시브 릴리즈는', '힘을 뺀 채 눌러 푸는 것(패시브 릴리즈)은'),
    (r'에 능동 신장 없이 패시브 이완합니다', '을 스스로 늘리지 않고 힘을 뺀 채 풀어 줍니다(패시브 이완)'),
    (r'패시브 매달리기', '힘을 빼고 매달리기(패시브 행)'),
    (r'\[PAILs\]', '[PAILs: 끝에서 밀며 버티기]'),
    (r'\[RAILs\]', '[RAILs: 더 깊이 당기며 버티기]'),
    (r'(\d+초)간? 등척성 수축하세요', r'\1 동안 ' + HOLD + '세요'),
    (r'(\d+초) 등척성 (?:수축|홀드)$', r'\1 동안 ' + HOLD + '기'),
    (r'등척성으로', HOLD + '는 방식(등척성)으로'),
    (r'등척성 (운동|근력)', lambda m: f'{HOLD}는 {m.group(1)}(등척성 {m.group(1)})'),
    (r'늘어나며 편심성 부하', '늘어나며 힘을 쓰는 부하(편심성 부하)'),  # "늘어나며 … 늘어나면서" 겹침 방지
    (r'편심성 (과?부하)', lambda m: f'{ECC_LOAD}{m.group(1)}(편심성 {m.group(1)})'),
    (r'편심성 손목 (신전|굴곡) 강화(를|가)', lambda m: f'{ECC_TRAIN}손목 {m.group(1)} 강화 운동(편심성 강화){JOSA[m.group(2)]}'),
    (r'편심성 강화(를|가|와)', lambda m: f'{ECC_TRAIN}강화 운동(편심성 강화){JOSA[m.group(1)]}'),
]
RULES = [(re.compile(p), r) for p, r in RULES]
GLOSS = re.compile(r'\((?:패시브 릴리즈|패시브 이완|등척성|등척성 운동|편심성 부하|편심성 과부하|편심성 강화)\)')
ACTIVE = '액티브 행'
ACTIVE_LABEL = '액티브 행(날개뼈를 내려 매달리기)'


def depth(s, i):
    return s[:i].count('(') - s[:i].count(')')


def fix(s, pairs=None):
    for pat, rep in RULES:
        src = s

        def sub(m):
            if depth(src, m.start()) > 0:
                return m.group(0)  # 이미 괄호 안
            new = m.expand(rep) if isinstance(rep, str) else rep(m)
            if pairs is not None:
                pairs[(src[max(0, m.start() - 10):m.end() + 6], new)] += 1
            return new
        s = pat.sub(sub, s)
    # 같은 풀이 괄호가 한 필드에 두 번 나오면 첫 번째만 남긴다
    seen = set()

    def once(m):
        if m.group(0) in seen:
            return ''
        seen.add(m.group(0))
        return m.group(0)
    s = GLOSS.sub(once, s)
    # 액티브 행: 필드 첫 등장이 풀이 없이 나올 때만 붙인다 (앞뒤에 날개뼈 설명이 있으면 이미 풀이된 것으로 본다)
    i = s.find(ACTIVE)
    if i >= 0:
        j = i + len(ACTIVE)
        explained = depth(s, i) > 0 or s[j:j + 1] == '(' or '날개뼈' in s[max(0, i - 18):i] or '날개뼈' in s[j:j + 12]
        if not explained:
            if pairs is not None:
                pairs[(s[max(0, i - 10):j + 6], ACTIVE_LABEL)] += 1
            s = s[:i] + ACTIVE_LABEL + s[j:]
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
