"""운동명 꼬리표 2부류 나 18곳 삭제 + why 보충 3곳.

category2 이후 남은 목적 설명 꼬리표(원어 낀 이름·보류 4곳 제외)를 모두 삭제한다.
data/phase-exercises.json에는 index에 없는 항목이 있어, index에서 바뀐 이름만 data에도 적용한다.
--apply 없이 실행하면 점검만 한다. 검수판은 apply_to(obj)로 같은 변환을 적용한다.
"""
import json
import sys

import strip_name_tags_category2 as c2

INDEX_PATH = 'index.html'
PHASE_PATH = 'data/phase-exercises.json'

WHY_ADD = {
    '버드독 — 힙 힌지 후방 사슬 협응':
        ' 엉덩이를 뒤로 빼는 힌지에서 허리가 대신 젖혀지지 않도록, 골반을 고정한 채 팔다리를 분리해 움직이는 연습입니다.',
    '사이드라잉 힙 어브덕션 — 천장관절 안정화':
        ' 엉덩이 옆 근육(중둔근)이 골반을 옆에서 잡아 줘야 런지 때 천장관절에 걸리는 좌우 부하가 고르게 나뉩니다.',
    '클램셸 — 고관절 굴곡 보상 억제를 위한 외회전 준비':
        ' 고관절이 덜 굽혀지는 상태에서는 무릎이 안으로 모이며 허리가 대신 굽혀지기 쉬워서, 본 동작 전에 엉덩이 옆 근육(중둔근)부터 깨웁니다.',
}
ALLOWED = None


def fix(o, log):
    if isinstance(o, dict):
        if c2.is_ex(o):
            n = o['name']
            if c2.LATIN.search(n) or n in c2.HOLD or (ALLOWED is not None and n not in ALLOWED):
                return
            stem, tag = c2.split_name(n)
            if not tag:
                return
            if n in WHY_ADD:
                o['why'] = o['why'].rstrip() + WHY_ADD[n]
            o['name'] = stem
            log.append((n, stem))
            return
        for v in o.values():
            fix(v, log)
    elif isinstance(o, list):
        for v in o:
            fix(v, log)


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    with open(INDEX_PATH, encoding='utf-8') as f:
        html = f.read()
    start = html.index('BUNDLED = ') + len('BUNDLED = ')
    bundled, length = json.JSONDecoder().raw_decode(html[start:])
    log_i = []
    fix(bundled, log_i)
    ALLOWED = {old for old, _ in log_i}
    with open(PHASE_PATH, encoding='utf-8') as f:
        phase = json.load(f)
    log_p = []
    fix(phase['movements'], log_p)
    print('index.html 변경', len(log_i), '/ phase-exercises.json 변경', len(log_p))
    for old, new in log_i:
        print(f'{old}  =>  {new}')
    if apply:
        new_raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
        html = html[:start] + new_raw + html[start + length:]
        with open(INDEX_PATH, 'w', encoding='utf-8') as f:
            f.write(html)
        with open(PHASE_PATH, 'w', encoding='utf-8') as f:
            json.dump(phase, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print('적용 완료')
