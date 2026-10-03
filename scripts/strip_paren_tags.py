"""운동명 끝 괄호 꼬리표 정리 (index.html BUNDLED + data/phase-exercises.json).

괄호 안을 쉼표로 쪼개 조각마다 판정한다.
- 영문 포함(원어 병기) / 운동 정체를 가르는 변형(그립·스탠스·도구·자세·부위) -> 유지
- 단계·부하 표기(경부하, 무게 점진, 부상 직전 무게의 50~60% 등) -> 삭제
- 그 외 목적·방법 설명 -> why·sets·cue·how에 단어 절반 이상 있으면 삭제, 없으면 보류(유지)
--apply 없으면 점검만. 보류 목록은 출력한다.
"""
import json
import re
import sys

LOAD = re.compile(r'경부하|중부하|정상 부하|무게|%|점진|초저중량|부하 도입|보수적 강도|진폭|볼륨|동적 부하|무부하 패턴')
IDENT = re.compile(
    r'그립|스탠스|밴드|폼롤러|문틀|네발|서서|앉아|측와|기둥|철봉|릭|무릎 (위|높이|구부린|아래)|지지|장요근|비복근|이상근'
    r'|내/외회전|큰 원|매달리|닐링|회내|버전|빈 바|바 없이|스트랩|리스트 랩|할로우|코브라|턱 업|프로네이션|안쪽|양손'
    r'|엎드려|허벅지 높이|정강이|힐 없이|발끝 바닥|전 범위|짝수날|오버핸드|서서|스윙|아치')
TAIL = re.compile(r'\s*\(([^()]*)\)\s*$')
LATIN = re.compile(r'[A-Za-z]')


def text_of(o):
    return ' '.join([o.get('why', ''), o.get('sets', ''), o.get('cue', '')] + list(o.get('how', [])))


def tokens(p):
    return [t for t in re.split(r'[^가-힣]+', p) if len(t) >= 2]


def classify(part, body):
    if LATIN.search(part) or IDENT.search(part):
        return 'keep'
    if LOAD.search(part):
        return 'drop'
    toks = tokens(part)
    if toks and sum(t in body for t in toks) * 2 >= len(toks):
        return 'drop'
    return 'hold'


def new_name(o, held):
    m = TAIL.search(o['name'])
    if not m:
        return None
    stem = o['name'][:m.start()]
    parts = [p.strip() for p in m.group(1).split(',') if p.strip()]
    body = text_of(o)
    kept = []
    for p in parts:
        c = classify(p, body)
        if c == 'keep':
            kept.append(p)
        elif c == 'hold':
            kept.append(p)
            held.append((o['name'], p))
    if len(kept) == len(parts):
        return None
    return f"{stem} ({', '.join(kept)})" if kept else stem


COLLIDE = []


def walk(o, log, held):
    if isinstance(o, dict):
        for k in ('phase_a', 'phase_b'):
            lst = o.get(k)
            if isinstance(lst, list) and lst and all(isinstance(e, dict) and 'how' in e for e in lst):
                olds = [e['name'] for e in lst]
                news = [new_name(e, held) or e['name'] for e in lst]
                cnt = {n: news.count(n) for n in news}
                for e, old, new in zip(lst, olds, news):
                    if new == old:
                        continue
                    if cnt[new] > 1 and olds.count(old) == 1:
                        COLLIDE.append((old, new))  # 지우면 같은 목록에서 이름이 겹침 -> 유지
                        continue
                    log.append((old, new))
                    e['name'] = new
                o = {kk: vv for kk, vv in o.items() if kk != k}
        for v in o.values():
            walk(v, log, held)
    elif isinstance(o, list):
        for v in o:
            walk(v, log, held)


def collisions(o, out):
    if isinstance(o, dict):
        for k in ('phase_a', 'phase_b'):
            if isinstance(o.get(k), list):
                names = [e.get('name') for e in o[k] if isinstance(e, dict)]
                out += len(names) - len(set(names))
        for v in o.values():
            out = collisions(v, out)
    elif isinstance(o, list):
        for v in o:
            out = collisions(v, out)
    return out


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    html = open('index.html', encoding='utf-8').read()
    start = html.index('BUNDLED = ') + len('BUNDLED = ')
    bundled, length = json.JSONDecoder().raw_decode(html[start:])
    col0 = collisions(bundled, 0)
    li, held = [], []
    walk(bundled, li, held)
    phase = json.load(open('data/phase-exercises.json', encoding='utf-8'))
    lp, held_p = [], []
    walk(phase['movements'], lp, held_p)
    print('index 변경', len(li), '/ data 변경', len(lp), '/ 같은 목록 내 이름 겹침', col0, '->', collisions(bundled, 0))
    print('같은 목록에서 이름이 겹쳐 유지한 것', len(COLLIDE))
    print('--- 변경 예 (고유)')
    for old, new in sorted(set(li))[:60]:
        print(f'  {old}  =>  {new}')
    print('--- 보류 (근거 없음, 유지됨)')
    from collections import Counter
    for (n, p), k in sorted(Counter(held).items(), key=lambda x: -x[1]):
        print(f'  {k} | {n} | {p}')
    if apply:
        raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
        open('index.html', 'w', encoding='utf-8').write(html[:start] + raw + html[start + length:])
        with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
            json.dump(phase, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print('적용 완료')
