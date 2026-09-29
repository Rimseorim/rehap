"""PT/전문의 검수용 감별 로직 문서(docs/pt_review_전체동작.md)를 index.html BUNDLED에서 생성한다.

사용:
  python scripts/generate_pt_review_doc.py                    # 현재 index.html -> docs/pt_review_전체동작.md
  python scripts/generate_pt_review_doc.py --rev 57acfa7 --out out.md --date 2026-08-29   # 과거 커밋 기준(검증용)

문서에는 질문 분기, 검사(이름·목적·통과/실패 문구·다음 단계), 원인(이름·설명), 위험신호만 넣는다.
재활 루트 운동, 검사 안내 단계(steps)·주의문(note)은 넣지 않는다.
"""
import argparse
import json
import subprocess
from datetime import date

HEADER = """# 재활 감별 로직 검수 문서 (전체 동작)

생성일: {date}

PT/전문의 검수용. 앱 UI 대신 감별 질문·검사·원인·처방 로직만 텍스트로 정리했습니다.
각 원인(cause)의 "재활 루트" 세부 운동은 분량상 생략 — 원인 분류·감별 로직·전반적 처방 방향의 임상적 타당성 위주로 봐주시면 됩니다.

---

"""


def load_bundled(rev):
    if rev:
        html = subprocess.run(['git', 'show', f'{rev}:index.html'], capture_output=True).stdout.decode('utf-8')
    else:
        html = open('index.html', encoding='utf-8').read()
    start = html.index('BUNDLED = ') + len('BUNDLED = ')
    return json.JSONDecoder().raw_decode(html[start:])[0]


def gen(b, gen_date):
    out = [HEADER.format(date=gen_date)]
    for m in b['manifest']:
        mv = b[m['id']]
        out.append(f'# {mv["name"]}\n\n')
        for ps in mv['pain_sites']:
            out.append(f'## {ps["name"]}\n\n')
            out.append('### 질문 분기\n')
            for q in ps.get('questions', []):
                line = f'- **{q["id"]}** "{q["text"]}"'
                if q.get('sub'):
                    line += f' _({q["sub"]})_'
                out.append(line + '\n')
                for c in q.get('choices', []):
                    out.append(f'  - "{c["text"]}" → {c["next"]}\n')
            out.append('\n### 테스트\n')
            for t in ps.get('tests', []):
                out.append(f'- **{t["id"]}** ({t["name"]}): {t["purpose"]}\n')
                out.append(f'  - pass("{t["pass_text"]}") → {t["pass_next"]} / fail("{t["fail_text"]}") → {t["fail_next"]}\n')
            out.append('\n### 원인(cause)\n')
            for c in ps['causes']:
                tag = c.get('tag')
                label = f'[{tag}] ' if tag and tag != c['name'] else ''
                out.append(f'- **{c["id"]}** {label}{c["name"]}\n')
                out.append(f'  {c["description"]}\n')
            out.append('\n### 위험신호(danger)\n')
            danger = ps.get('danger') or []
            if isinstance(danger, dict):
                danger = [danger]
            for d in danger:
                out.append(f'- **{d["title"]}**: {d["reason"]}\n')
                out.append(f'  - 조치: {d["action"]}\n')
            out.append('\n---\n\n')
    return ''.join(out)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--rev', default=None)
    ap.add_argument('--out', default='docs/pt_review_전체동작.md')
    ap.add_argument('--date', default=date.today().isoformat())
    a = ap.parse_args()
    text = gen(load_bundled(a.rev), a.date)
    with open(a.out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print('작성:', a.out, len(text.splitlines()), '줄')
