"""운동명 꼬리표 3부류(원어 낀 이름 13곳) 정리. why에 특화 내용이 이미 있어 보충 없음.

index.html BUNDLED + data/phase-exercises.json 에 같은 이름 변경을 적용한다. --apply 없으면 점검만.
"""
import json
import sys

PCS = '후면 관절낭 스트레칭 (Posterior Capsule Stretch)'
SS = '견갑 세팅 (Scapular Setting)'
PSS = '엎드려 견갑 슬라이드 (W→Y, Prone Shoulder Slides)'

RENAME = {
    'Posterior Capsule Stretch — 데드리프트 락아웃 특화': PCS,
    'Posterior Capsule Stretch — 벤치프레스 팔꿈치 각도 특화': PCS,
    'Posterior Capsule Stretch — 오버헤드 락아웃 특화': PCS,
    'Posterior Capsule Stretch — 오버헤드 당김 각도 특화': PCS,
    'Posterior Capsule Stretch — 로우 당김 범위 특화': PCS,
    'Posterior Capsule Stretch — 랙 포지션 각도 특화': PCS,
    'Scapular Setting': SS,
    'Scapular Setting — 복압 독립형 견갑 후인·하강': SS,
    'Prone Shoulder Slides (W→Y 이동)': PSS,
    '엎드려 견갑 슬라이드 (W→Y)': PSS,
    'Band Row — 데드리프트 특화': '밴드 로우',
    '터키시 겟업 1단계 — Arm Bar': '터키시 겟업 암 바',
}


def walk(o, log):
    if isinstance(o, dict):
        if o.get('name') in RENAME and 'how' in o:
            log.append((o['name'], RENAME[o['name']]))
            o['name'] = RENAME[o['name']]
        for v in o.values():
            walk(v, log)
    elif isinstance(o, list):
        for v in o:
            walk(v, log)


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    html = open('index.html', encoding='utf-8').read()
    start = html.index('BUNDLED = ') + len('BUNDLED = ')
    bundled, length = json.JSONDecoder().raw_decode(html[start:])
    li = []
    walk(bundled, li)
    phase = json.load(open('data/phase-exercises.json', encoding='utf-8'))
    lp = []
    walk(phase['movements'], lp)
    print('index', len(li), 'data', len(lp))
    for old, new in li:
        print(f'  {old}  =>  {new}')
    if apply:
        raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
        open('index.html', 'w', encoding='utf-8').write(html[:start] + raw + html[start + length:])
        with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
            json.dump(phase, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print('적용 완료')
