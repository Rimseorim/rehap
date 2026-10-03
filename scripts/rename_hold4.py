"""보류 4곳 운동명 변경 (index.html BUNDLED + data/phase-exercises.json). --apply 없으면 점검만."""
import json
import sys

RENAME = {
    '이상근 스트레칭': '엉덩이 깊은 근육(이상근) 스트레칭',
    '이상근 스트레칭 — 누운 비둘기 자세': '엉덩이 깊은 근육(이상근) 스트레칭',
    '빈 바벨 프론트 스쿼트 — 크로스 그립 (부상 전 30~40%)': '크로스 그립 빈 바벨 프론트 스쿼트',
    '맨몸 프레스 패턴: 팔꿈치 각도 각인': '맨몸 프레스',
    '맨몸 프레스 패턴: 상방회전 궤적 확인': '맨몸 프레스',
}


def walk(o, log):
    if isinstance(o, dict):
        if o.get('name') in RENAME and 'how' in o:
            log.append(o['name'])
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
    for n in li:
        print(' ', n)
    if apply:
        raw = json.dumps(bundled, ensure_ascii=False, separators=(',', ':'))
        open('index.html', 'w', encoding='utf-8').write(html[:start] + raw + html[start + length:])
        with open('data/phase-exercises.json', 'w', encoding='utf-8') as f:
            json.dump(phase, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print('적용 완료')
