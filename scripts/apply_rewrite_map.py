"""고유 문자열 단위로 만든 고쳐쓰기 표(old → new)를 index.html BUNDLED + data/phase-exercises.json 에 적용한다.

사용: python scripts/apply_rewrite_map.py <작업폴더> [--apply]
작업폴더: body_XX.json(입력)·out_body_XX.json(결과)·names.json·out_names.json, 선택으로 overrides.json({old: new}, 검증 없이 우선 적용).
--apply 없으면 점검만 한다. 숫자가 달라지거나 괄호 짝이 안 맞는 결과는 적용하지 않고 flagged.json 으로 남긴다.
"""
import glob
import json
import os
import re
import sys
from collections import Counter

SKIP = {'id', 'next', 'pass_next', 'fail_next', 'video_url', 'target_area'}
NAME_LIKE = {'name', 'title', 'tag', 'sets', 'set', 'equipment'}
REF = re.compile(r'\d단계')
DUP = re.compile(r'(\([^()]{2,24}\)).*\1')
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')


def problems(old, new):
    p = []
    if sorted(re.findall(r'\d+', REF.sub('', old))) != sorted(re.findall(r'\d+', REF.sub('', new))):
        p.append('숫자')
    for a, b in ('()', '[]'):
        if old.count(a) == old.count(b) and new.count(a) != new.count(b):
            p.append('괄호짝')
    if not new.strip() or not 0.5 <= len(new) / max(1, len(old)) <= 2.6:
        p.append('길이')
    if DUP.search(new) and not DUP.search(old):
        p.append('풀이중복')
    if EMOJI.search(new):
        p.append('이모지')
    return p


def load_maps(work):
    body, flagged, missing = {}, [], 0
    for src in sorted(glob.glob(os.path.join(work, 'body_*.json'))):
        out = os.path.join(work, 'out_' + os.path.basename(src))
        if not os.path.exists(out):
            print('결과 없음:', os.path.basename(out))
            continue
        olds = {r['id']: r['text'] for r in json.load(open(src, encoding='utf-8'))}
        news = {r['id']: r for r in json.load(open(out, encoding='utf-8'))}
        missing += len(set(olds) - set(news))
        for i, old in olds.items():
            new = news.get(i, {}).get('new', old)
            if not isinstance(new, str) or new == old:
                continue
            p = problems(old, new)
            if p:
                flagged.append({'id': i, 'why': p, 'old': old, 'new': new})
            else:
                body[old] = new
    names = {'tests': {}, 'causes': {}, 'exercises': {}}
    path = os.path.join(work, 'out_names.json')
    if os.path.exists(path):
        raw = json.load(open(path, encoding='utf-8'))
        for kind in names:
            for r in raw.get(kind, []):
                if r.get('new') and r['new'] != r['old']:
                    names[kind][r['old']] = r
    over = os.path.join(work, 'overrides.json')
    if os.path.exists(over):
        body.update(json.load(open(over, encoding='utf-8')))
    return body, names, flagged, missing


def how_text(o):
    how = o.get('how')
    return (' '.join(how) if isinstance(how, list) else str(how or '')) + ' ' + str(o.get('cue') or '')


def walk(o, body, names, stat, refs, key=None):
    if isinstance(o, dict):
        name = o.get('name')
        if 'how' in o and name in names['exercises']:
            r = names['exercises'][name]
            sentence, kws = r.get('mode_sentence'), r.get('keywords') or []
            if sentence and not any(k in how_text(o) for k in kws) and isinstance(o.get('cue'), str):
                o['cue'] = (o['cue'].rstrip() + ' ' + sentence).strip()
                stat['운동 큐 보충'] += 1
            o['name'] = r['new']
            stat['운동명'] += 1
        elif 'pass_text' in o and name in names['tests']:
            o['name'] = names['tests'][name]['new']
            stat['검사 제목'] += 1
        elif 'description' in o and name in names['causes']:
            o['name'] = names['causes'][name]['new']
            stat['원인명'] += 1
    items = o.items() if isinstance(o, dict) else enumerate(o) if isinstance(o, list) else ()
    for k, v in items:
        field = k if isinstance(o, dict) else key
        if isinstance(v, str):
            if field in SKIP or field in NAME_LIKE:
                continue
            new = body.get(v, v)
            for old_name, new_name in refs:
                if old_name in new:
                    new = new.replace(old_name, new_name)
                    stat['본문 속 운동 이름'] += 1
            if new != v:
                o[k] = new
                stat['본문'] += 1
        else:
            walk(v, body, names, stat, refs, field)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    work = sys.argv[1]
    apply = '--apply' in sys.argv
    body, names, flagged, missing = load_maps(work)
    print('고쳐쓰기 표: 본문', len(body), '/ 검사 제목', len(names['tests']), '/ 원인명', len(names['causes']), '/ 운동명', len(names['exercises']))
    print('검증에서 제외:', len(flagged), dict(Counter(w for f in flagged for w in f['why'])), '/ 결과에 빠진 id:', missing)
    json.dump(flagged, open(os.path.join(work, 'flagged.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    news = Counter(r['new'] for r in names['exercises'].values())
    print('운동명 새 이름이 겹치는 묶음:', {n: c for n, c in news.items() if c > 1})
    strip = lambda s: re.sub(r' \([^)]*\)$', '', s)
    refs = sorted({(strip(o), strip(r['new'])) for o, r in names['exercises'].items() if len(strip(o)) >= 6 and strip(o) != strip(r['new'])}, key=lambda x: -len(x[0]))

    html = open('index.html', encoding='utf-8').read()
    start = html.index('BUNDLED = ') + len('BUNDLED = ')
    bundled, length = json.JSONDecoder().raw_decode(html[start:])
    same = json.dumps(bundled, ensure_ascii=False, separators=(',', ':')) == html[start:start + length]
    phase = json.load(open('data/phase-exercises.json', encoding='utf-8'))
    si, sd = Counter(), Counter()
    walk(bundled, body, names, si, refs)
    walk(phase, body, names, sd, refs)
    print('index 재직렬화 동일:', same)
    print('index 적용:', dict(si))
    print('data  적용:', dict(sd))
    if apply:
        if not same:
            sys.exit('index.html 재직렬화가 원문과 달라 중단')
        raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
        open('index.html', 'w', encoding='utf-8').write(html[:start] + raw + html[start + length:])
        with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
            json.dump(phase, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print('적용 완료')
