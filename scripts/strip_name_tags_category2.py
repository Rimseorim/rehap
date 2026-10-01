"""운동명 뒤 목적 설명 꼬리표 중 why에 내용이 이미 있는 것(2부류 가 + 다 일부) 삭제.

index.html BUNDLED와 data/phase-exercises.json의 운동 name만 정확 일치로 치환한다.
--apply 없이 실행하면 점검만 한다. board_apply(data) 로 검수판 JSON에도 쓸 수 있다.
"""
import json
import re
import sys

INDEX_PATH = 'index.html'
PHASE_PATH = 'data/phase-exercises.json'

LATIN = re.compile(r'Posterior Capsule|Prone Shoulder|W→Y|Scapular Setting|Arm Bar|Band Row')
ALLOWED = None  # 설정되면 이 이름만 변경 (data에만 있는 항목 보호)
HOLD = {  # 보류: 이름을 따로 정한다
    '이상근 스트레칭 — 누운 비둘기 자세',
    '빈 바벨 프론트 스쿼트 — 크로스 그립 (부상 전 30~40%)',
    '맨몸 프레스 패턴: 팔꿈치 각도 각인',
    '맨몸 프레스 패턴: 상방회전 궤적 확인',
}
FORCE = {  # why 겹침이 낮아도 방법 정보라 삭제
    '흉추 회전 스트레칭 — 옆누워',
    '광배근 스트레칭 — 기둥 활용',
    '맨몸 스쿼트 — 팔 앞으로 모으기 (통증호 회피)',
}


def split_name(n):
    stem, sep, tag = n.partition(' — ')
    if not sep:
        stem, sep, tag = n.partition(': ')
    return stem, tag if sep else ''


def is_ex(o):
    return isinstance(o, dict) and isinstance(o.get('name'), str) and 'why' in o and 'cue' in o


def decide(o):
    """삭제 후 새 이름 또는 None"""
    n = o['name']
    if LATIN.search(n) or n in HOLD or (ALLOWED is not None and n not in ALLOWED):
        return None
    stem, tag = split_name(n)
    if not tag:
        return None
    if n in FORCE:
        return stem
    words = re.findall(r'[가-힣A-Za-z0-9]{2,}', tag)
    hit = [w for w in words if w in o['why']]
    if len(hit) >= 2 or (words and len(hit) / len(words) >= 0.5):
        return stem
    return None


def fix(o, log):
    if isinstance(o, dict):
        if is_ex(o):
            nn = decide(o)
            if nn is not None:
                log.append((o['name'], nn))
                o['name'] = nn
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
