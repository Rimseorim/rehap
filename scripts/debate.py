"""
재활앱 Phase 설계 멀티모델 토론 파이프라인

토론 흐름:
  1. Claude가 설계안을 scripts/debate_draft.md에 저장
  2. python scripts/debate.py  → 4개 모델이 동시 검토
  3. 결과를 Claude에 붙여넣기 → Claude 반박
  4. python scripts/debate.py  → 4개 모델 재검토
  5. 반복 → 합의 선언 후 Claude가 스크립트 작성
"""

import os
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = Path(__file__).parent.parent
CHECKLIST = Path(r"C:\Users\tjfla\OneDrive\Desktop\재활앱_설계_표준_체크리스트.md")
DRAFT = BASE / "scripts" / "debate_draft.md"
HISTORY = BASE / "scripts" / "debate_history.md"

MODELS = [
    {"id": "google/gemma-4-31b-it:free",  "name": "Gemma (Google)"},
    {"id": "openai/gpt-oss-120b:free",    "name": "GPT-OSS (OpenAI)"},
]


def get_api_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        import winreg
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as reg:
                key, _ = winreg.QueryValueEx(reg, "OPENROUTER_API_KEY")
        except Exception:
            pass
    if not key:
        print("[오류] OPENROUTER_API_KEY 환경변수가 없습니다.")
        sys.exit(1)
    return key


def load(path: Path) -> str:
    if not path.exists():
        print(f"[오류] 파일 없음: {path}")
        sys.exit(1)
    return path.read_text(encoding="utf-8")


MAX_RETRIES = 3
RETRY_DELAYS = [5, 15, 30]


def call_model(model_id: str, system: str, user: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    payload = json.dumps({
        "model": model_id,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user",   "content": user},
        ]
    }).encode("utf-8")

    for attempt in range(MAX_RETRIES):
        req = urllib.request.Request(url, data=payload, method="POST")
        req.add_header("Authorization", f"Bearer {get_api_key()}")
        req.add_header("Content-Type", "application/json")
        req.add_header("HTTP-Referer", "https://github.com/rehab-debate")

        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if "choices" not in data:
                    return f"[오류] 응답 형식 오류 — choices 키 없음. 원본: {str(data)[:300]}"
                return data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8")
            if e.code == 429 and attempt < MAX_RETRIES - 1:
                wait = RETRY_DELAYS[attempt]
                print(f"  ⚠ {model_id} 429 rate limit — {wait}초 후 재시도 ({attempt+1}/{MAX_RETRIES-1})")
                import time; time.sleep(wait)
                continue
            return f"[실패 {e.code}] {body[:300]}"
        except Exception as e:
            return f"[실패] {str(e)}"

    return f"[실패] {MAX_RETRIES}회 재시도 모두 실패"


def build_prompts(role: str, checklist: str, history: str, new_input: str):
    system = f"""당신은 재활 운동 Phase 설계 전문가입니다.
아래 체크리스트가 유일한 판단 기준입니다. 감정 없이 논리로만 반응하세요.

## 체크리스트
{checklist}"""

    if role == "first":
        user = f"""Claude가 아래 설계안을 제안했습니다. 체크리스트 기준으로 엄격하게 검토하세요.

## 설계안
{new_input}

형식:
## 위반 항목
(체크리스트 항목명 + 구체적 근거 + 수정 제안)

## 잘 된 점

## 종합 판정
반드시 "합의 가능" 또는 "수정 필요" 중 하나로 끝내세요."""

    else:
        user = f"""지금까지 토론 기록입니다.

## 토론 기록
{history}

## Claude의 최신 반박/수정안
{new_input}

납득되는 부분은 인정하고, 여전히 문제인 부분은 구체적 근거로 재반박하세요.

## 종합 판정
반드시 "합의 가능" 또는 "수정 필요" 중 하나로 끝내세요."""

    return system, user


def run_all_models(role: str, checklist: str, history: str, new_input: str) -> dict:
    system, user = build_prompts(role, checklist, history, new_input)
    results = {}

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(call_model, m["id"], system, user): m
            for m in MODELS
        }
        for future in as_completed(futures):
            m = futures[future]
            result = future.result()
            if result.startswith("[실패") or result.startswith("[오류"):
                print(f"  ✗ {m['name']} 실패")
            else:
                print(f"  ✓ {m['name']} 성공")
            results[m["name"]] = result

    return results


def append_history(round_num: int, speaker: str, content: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n\n=== 라운드 {round_num} — {speaker} ({ts}) ===\n{content}\n"
    with HISTORY.open("a", encoding="utf-8") as f:
        f.write(entry)


def get_round_num() -> int:
    if not HISTORY.exists():
        return 1
    return HISTORY.read_text(encoding="utf-8").count("=== 라운드") + 1


def format_reviews(reviews: dict) -> str:
    lines = []
    for name, text in reviews.items():
        lines.append(f"\n{'─'*50}\n### {name}\n{text}")
    return "\n".join(lines)


def main():
    checklist = load(CHECKLIST)
    draft = load(DRAFT)
    history = HISTORY.read_text(encoding="utf-8") if HISTORY.exists() else ""
    round_num = get_round_num()

    print(f"\n{'='*55}")
    print(f"  라운드 {round_num} — 4개 모델 검토 중...")
    print(f"{'='*55}\n")

    if round_num == 1:
        reviews = run_all_models("first", checklist, "", draft)
        combined = format_reviews(reviews)
        print(combined)
        append_history(round_num, "Claude 설계안", draft)
        append_history(round_num, "모델 검토", combined)
    else:
        print("[ Claude 반박/수정안을 입력하세요 ]")
        print("  (입력 완료 후 빈 줄에서 Enter 두 번)\n")
        lines = []
        empty_count = 0
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line == "":
                empty_count += 1
                if empty_count >= 2:
                    break
            else:
                empty_count = 0
                lines.append(line)
        claude_input = "\n".join(lines)
        append_history(round_num, "Claude 반박", claude_input)

        updated_history = HISTORY.read_text(encoding="utf-8")
        reviews = run_all_models("debate", checklist, updated_history, claude_input)
        combined = format_reviews(reviews)
        print(combined)
        append_history(round_num, "모델 검토", combined)

    # 합의 여부 집계
    agree = sum(1 for t in reviews.values() if "합의 가능" in t)
    total = len(reviews)

    print(f"\n{'='*55}")
    print(f"  합의 판정: {agree}/{total} 모델이 합의 가능")
    if agree == total:
        print("  → 전원 합의. Claude에게 '합의됨, 스크립트 작성해줘' 전달하세요.")
    else:
        print("  → 위 검토 결과를 Claude에게 붙여넣고 반박받으세요.")
        print("  → 반박 후 다시 실행: python scripts/debate.py")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
