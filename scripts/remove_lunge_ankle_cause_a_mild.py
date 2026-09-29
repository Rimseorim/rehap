"""런지/발목 cause-a-mild 잔해 삭제 (2026-06-23 b91df94에서 cause-a로 통합했으나 정의가 남아 있던 것).

index.html BUNDLED와 data/movements/lunge.json에서 원인 정의를 지우고,
lunge.json의 검사 분기(test-ankle-df pass_next)를 index.html과 같은 cause-a로 맞춘다.
"""
import json

INDEX_PATH = 'index.html'
LUNGE_PATH = 'data/movements/lunge.json'
TARGET = 'cause-a-mild'

# 1) index.html
with open(INDEX_PATH, encoding='utf-8') as f:
    html = f.read()
start = html.index('BUNDLED = ') + len('BUNDLED = ')
bundled, length = json.JSONDecoder().raw_decode(html[start:])
ps = next(p for p in bundled['lunge']['pain_sites'] if p['id'] == 'ankle')
before = [c['id'] for c in ps['causes']]
assert TARGET in before, 'index.html에 이미 없음'
ps['causes'] = [c for c in ps['causes'] if c['id'] != TARGET]
# 남은 참조가 없는지 확인
dump = json.dumps(bundled, ensure_ascii=False)
assert TARGET not in dump, 'index.html에 다른 참조가 남아 있음'
new_raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
html = html[:start] + new_raw + html[start + length:]
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
print('index 원인:', before, '->', [c['id'] for c in ps['causes']])

# 2) data/movements/lunge.json
with open(LUNGE_PATH, encoding='utf-8') as f:
    lunge = json.load(f)
lps = next(p for p in lunge['pain_sites'] if p['id'] == 'ankle')
lps['causes'] = [c for c in lps['causes'] if c['id'] != TARGET]
n_fixed = 0
for t in lps.get('tests', []):
    if t.get('pass_next') == 'cause:' + TARGET:
        t['pass_next'] = 'cause:cause-a'
        n_fixed += 1
assert TARGET not in json.dumps(lunge, ensure_ascii=False), 'lunge.json에 참조가 남아 있음'
with open(LUNGE_PATH, 'w', encoding='utf-8') as f:
    json.dump(lunge, f, ensure_ascii=False, indent=2)
print('lunge.json 분기 수정:', n_fixed, '/ 원인:', [c['id'] for c in lps['causes']])
