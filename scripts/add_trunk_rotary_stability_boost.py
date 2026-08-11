# -*- coding: utf-8 -*-
"""
task #12: 트렁크스태빌리티/로터리스태빌리티 - 기존 코어안정성 계열 cause 보강
- 수평프레스-허리 cause-b: 진단 테스트를 사이드플랭크(정적 측면 버티기)에서
  푸쉬업 자세 반사 안정성 검사(프레스 패턴에 더 가까운 테스트)로 교체
- 로우-허리 cause-a: 주관적 자가판단 질문("허리가 둥글게 말리는 편인가요?")은 유지하되,
  "네"로 답한 경우에만 버드독 로터리스태빌리티 검사(객관적 동작 테스트)로 재확인
  (전원 강제 검사는 5분 완주 원칙과 충돌해 하이브리드로 확정 - 2026-08-11)
"""
import json
import re

INDEX_PATH = "index.html"

with open(INDEX_PATH, encoding="utf-8") as f:
    html = f.read()

m = re.search(r"const BUNDLED\s*=\s*(\{[\s\S]*?\});", html)
if not m:
    raise SystemExit("BUNDLED constant not found")
bundled = json.loads(m.group(1))

# ══════════════════════════════════════════════════════════════════════
# 1) 수평프레스-허리: test-core-sideplank -> 푸쉬업 자세 반사 안정성 검사로 교체
# ══════════════════════════════════════════════════════════════════════
ph_lb = next(p for p in bundled["press-horizontal"]["pain_sites"] if p["id"] == "lower-back")
sideplank_idx = next(i for i, t in enumerate(ph_lb["tests"]) if t["id"] == "test-core-sideplank")
ph_lb["tests"][sideplank_idx] = {
    "id": "test-core-sideplank",
    "name": "푸쉬업 자세 반사 안정성 검사",
    "purpose": "벤치프레스처럼 팔로 미는 힘이 실릴 때 몸통이 반사적으로 안정을 유지하는지 확인합니다. 정적으로 버티는 능력보다 실제 프레스 동작과 더 가까운 조건입니다.",
    "steps": [
        "팔굽혀펴기 자세(플랭크)로 엎드리세요",
        "한쪽 손을 바닥에서 떼어 반대쪽 어깨를 살짝 터치하세요",
        "손을 뗄 때 골반이나 몸통이 좌우로 돌아가거나 허리가 처지는지 확인하세요",
        "반대쪽 손으로도 반복하세요"
    ],
    "note": "손을 떼는 순간 몸통이 버티는지가 핵심입니다. 속도보다 안정성을 우선 확인하세요.",
    "pass_text": "양쪽 다 몸통이 거의 안 돌아가고 안정적이에요",
    "fail_text": "손을 뗄 때 몸통이 확 돌아가거나 허리가 처져요",
    "pass_next": "cause:cause-d",
    "fail_next": "cause:cause-b",
    "video_url": ""
}

# ══════════════════════════════════════════════════════════════════════
# 2) 로우-허리: 하이브리드 방식
#    q2("허리가 둥글게 말리는 편인가요?")는 그대로 유지 (전원에게 신체 검사를
#    강제하면 5분 완주 원칙과 충돌 - "네" 응답자만 객관적 검사로 재확인)
#    - "네" -> 버드독 로터리스태빌리티 검사로 재확인 -> fail:cause-a / pass:test-hip-flexor
#    - "아니요" -> 기존 그대로 test-hip-flexor 직행 (변경 없음)
# ══════════════════════════════════════════════════════════════════════
rw_lb = next(p for p in bundled["row"]["pain_sites"] if p["id"] == "lower-back")

# q2의 "네" 분기만 검사로 재확인하도록 변경 ("아니요" 분기는 손대지 않음)
q2 = next(q for q in rw_lb["questions"] if q["id"] == "q2")
yes_choice = next(c for c in q2["choices"] if c["next"] == "cause:cause-a")
yes_choice["next"] = "test:test-row-rotary-stability"

# 신규 테스트 추가
rw_lb["tests"].insert(0, {
    "id": "test-row-rotary-stability",
    "name": "버드독 로터리스태빌리티 검사",
    "purpose": "로우 자세에서 허리가 말리는 게 실제로 코어가 회전·굴곡 부하를 못 버텨서인지 객관적으로 확인합니다.",
    "steps": [
        "네발기기 자세로 엎드리세요",
        "한쪽 팔과 반대쪽 다리를 동시에 쭉 뻗으세요",
        "뻗는 동안 허리가 아래로 처지거나 골반이 좌우로 돌아가는지 확인하세요",
        "반대쪽도 반복하세요"
    ],
    "note": "처짐이나 회전이 아주 살짝만 있어도 양성으로 봅니다. 완벽하게 수평을 유지해야 정상입니다.",
    "pass_text": "양쪽 다 몸통이 안정적으로 유지돼요",
    "fail_text": "뻗을 때 허리가 처지거나 골반이 돌아가요",
    "pass_next": "test:test-hip-flexor",
    "fail_next": "cause:cause-a",
    "video_url": ""
})

new_bundled_raw = json.dumps(bundled, ensure_ascii=False, separators=(",", ":"))
html = html[:m.start(1)] + new_bundled_raw + html[m.end(1):]

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("완료: 수평프레스-허리 사이드플랭크->푸쉬업안정성 교체, 로우-허리 로터리스태빌리티 검사 도입")
