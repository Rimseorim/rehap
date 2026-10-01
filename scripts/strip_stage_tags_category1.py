"""운동명 뒤 단계 표기 꼬리표(1부류 45곳) 정리.

index.html BUNDLED와 data/phase-exercises.json의 운동 name만 정확 일치로 치환한다.
다른 필드는 건드리지 않는다. --apply 없이 실행하면 점검만 한다.
"""
import json
import re
import sys

INDEX_PATH = 'index.html'
PHASE_PATH = 'data/phase-exercises.json'

EXPLICIT = {
    '볼륨 점진 복귀 (밴드 약화 → 무보조)': '약한 밴드 보조 키핑 풀업',
    '약한 밴드 → 무보조 볼륨 점진 복귀': '약한 밴드 보조 풀업',
    '덤벨 RDL — 와이드 스탠스': '와이드 스탠스 덤벨 RDL',
    '덤벨 RDL — 정상 스탠스': '정상 스탠스 덤벨 RDL',
    '덤벨 RDL — 무릎 아래까지': '무릎 아래까지 내리는 덤벨 RDL',
    '덤벨 RDL — Full ROM': '끝까지 내리는 덤벨 RDL',
    '덤벨/바벨 로우 → 점진 (도구+무게)': '바벨 로우',
    '스캡 풀업 (발끝 보조): 가동범위 확대': '스캡 풀업 (발끝 보조)',
    '바벨 로우 (정규 그립, 30~40% → 점진)': '바벨 로우 (정규 그립)',
}
SUFFIXES = [
    ' — 무게 점진 복귀', ' — 무게 점진 도입', ' (30~40% → 점진)',
    ' → 점진 (도구+무게)', ' → 점진', ': 부하 도입', ' — 부하 도입',
    ': 가동범위 확대', ' — Full ROM',
]
TARGET = re.compile(r'점진|Full ROM|스탠스|무릎 아래까지|부하 도입|가동범위 확대')
TAG = re.compile(r'[—–:→]| - |\(30')


def new_name(n):
    if not (TAG.search(n) and TARGET.search(n)):
        return None
    if n in EXPLICIT:
        return EXPLICIT[n]
    for s in SUFFIXES:
        if n.endswith(s):
            return n[:-len(s)]
    raise SystemExit('매핑 없음: ' + n)


def is_ex(o):
    return isinstance(o, dict) and isinstance(o.get('name'), str) and 'why' in o and 'cue' in o


def fix(o, log):
    if isinstance(o, dict):
        if is_ex(o):
            nn = new_name(o['name'])
            if nn is not None:
                log.append((o['name'], nn, o['why']))
                o['name'] = nn
            return
        for v in o.values():
            fix(v, log)
    elif isinstance(o, list):
        for v in o:
            fix(v, log)


apply = '--apply' in sys.argv

with open(INDEX_PATH, encoding='utf-8') as f:
    html = f.read()
start = html.index('BUNDLED = ') + len('BUNDLED = ')
bundled, length = json.JSONDecoder().raw_decode(html[start:])
log_i = []
fix(bundled, log_i)

with open(PHASE_PATH, encoding='utf-8') as f:
    phase = json.load(f)
log_p = []
fix(phase['movements'], log_p)

print('index.html 변경', len(log_i), '/ phase-exercises.json 변경', len(log_p))
for old, new, why in log_i:
    flag = '' if re.search(r'무게|부하|도입|점진|범위|볼륨', why) else '  ※why에 단계 설명 없음'
    print(f'{old}  =>  {new}{flag}')

if apply:
    new_raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
    html = html[:start] + new_raw + html[start + length:]
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(PHASE_PATH, 'w', encoding='utf-8') as f:
        json.dump(phase, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('적용 완료')
