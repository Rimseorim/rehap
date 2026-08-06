# -*- coding: utf-8 -*-
"""
task #11+#15 통합: 데드리프트-허리 ASLR/코어 재검사 로직 도입
- test-flexion의 fail 분기(후굴 통증)를 곧장 cause-b로 보내지 않고
  신규 테스트(test-aslr-core: 다리 들어올리기 + 코어 재검사)를 거치도록 변경
- cause-d 트리거 조건을 "굴곡·신전 모두 통증"에서
  "신전 통증 + 코어에 힘줘도 안 풀리지 않고 풀리는 경우"까지 포함하도록 description 확장
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

dl_lb = next(p for p in bundled["deadlift"]["pain_sites"] if p["id"] == "lower-back")

# 1) test-flexion fail_next 변경
test_flexion = next(t for t in dl_lb["tests"] if t["id"] == "test-flexion")
assert test_flexion["fail_next"] == "cause:cause-b"
test_flexion["fail_next"] = "test:test-aslr-core"

# 2) 신규 테스트 삽입
dl_lb["tests"].append({
    "id": "test-aslr-core",
    "name": "다리 들어올리기 + 코어 재검사",
    "purpose": "신전 시 통증이 진짜 고관절 뻣뻣함 때문인지, 코어가 골반을 못 잡아줘서 허리가 대신 신전으로 보상하는 건지 구분합니다.",
    "steps": [
        "바닥에 누워 무릎을 편 채 한쪽 다리를 천천히 들어올리세요",
        "허벅지 뒤쪽·엉덩이가 당겨서 어디까지 올라가는지 확인하세요",
        "배에 살짝 힘을 주고(아랫배를 등 쪽으로 당기듯) 같은 동작을 다시 해보세요",
        "힘을 줬을 때 더 높이 올라가거나 편해지는지 확인하세요"
    ],
    "note": "허벅지 뒤쪽이 당기는 느낌 자체보다, 배에 힘을 줬을 때 변화가 있는지가 핵심입니다.",
    "pass_text": "배에 힘을 주니 더 올라가거나 편해져요",
    "fail_text": "힘을 줘도 그대로 뻣뻣해요",
    "pass_next": "cause:cause-d",
    "fail_next": "cause:cause-b"
})

# 3) cause-d description 확장 (트리거 조건 넓힘, Phase 콘텐츠는 그대로)
cause_d = next(c for c in dl_lb["causes"] if c["id"] == "cause-d")
old_desc = "데드리프트 중 허리를 앞으로 숙일 때와 뒤로 젖힐 때 모두 통증이 있다면, 특정 방향의 자세 오류보다는 코어 안정성과 고관절·흉추 가동성이 함께 부족해 척추가 양쪽 방향 모두에서 부하를 제대로 분산하지 못하는 경우입니다. 한 가지 동작만 고쳐서는 해결되지 않고, 안정성과 가동성을 함께 만들어야 합니다."
assert cause_d["description"] == old_desc
cause_d["description"] = (
    "허리를 뒤로 젖힐 때(또는 앞뒤 모두) 통증이 있고, 배에 힘을 주면 증상이 덜해진다면 "
    "특정 방향의 자세 오류보다는 코어가 골반을 제대로 잡아주지 못해 척추가 대신 부하를 떠안는 경우입니다. "
    "고관절 자체보다 코어 안정성 회복이 우선입니다."
)

new_bundled_raw = json.dumps(bundled, ensure_ascii=False, separators=(",", ":"))
html = html[:m.start(1)] + new_bundled_raw + html[m.end(1):]

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("완료: 데드리프트-허리 ASLR/코어 재검사 로직 추가")
