# 회복테스트/원인 콘텐츠 검토 — 다음 작업 안내 (고관절 → 손목 → 팔꿈치 → 흉근)

새 세션에서 이 파일만 읽으면 바로 작업 시작 가능하도록 작성함.

## 배경/목적

`index.html`의 BUNDLED 데이터(8개 동작 × 35개 통증부위)에 있는 모든 선별검사/직접테스트/회복테스트가
연결된 cause(원인)의 description과 메커니즘상 맞는지 검토하는 작업.

- 전체 진행 현황·완료된 부위 결과: `docs/RETEST_CONTENT_REVIEW.md`
- 완료: 무릎, 허리, 발목, 어깨 (어깨는 4건 수정 완료)
- 남은 작업: **고관절 → 손목 → 팔꿈치 → 흉근**

## 작업 전 반드시 참조할 메모리 (auto memory)

- `feedback_report_order` — 통증부위/동작 나열 순서 (앱 manifest 순서)
  - 통증부위: 무릎→허리→발목→어깨→**고관절→손목→팔꿈치→흉근**
  - 동작: 스쿼트→런지→데드리프트→풀업→키핑→로우→수직프레스→수평프레스 (해당 부위 가진 동작만)
- `feedback_review_doc_workflow` — **`docs/RETEST_CONTENT_REVIEW.md`에 바로 쓰지 말 것**.
  먼저 채팅으로 표+이슈 보여주고, 사용자가 "작성해"라고 하면 그때 파일에 반영.
  (index.html 코드 수정은 사용자가 "고치자"고 하면 바로 가능 — 이건 문서 작성과 별개)
- `feedback_dont_repeat` — 이미 결정/완료된 항목 다시 "다음 할 일"로 제안하지 않기
- `feedback_prioritize_by_user_value` — 우선순위는 작업량이 아니라 사용자 효과 기준

## index.html 데이터 추출 방법 (중요 — Grep 도구 못 씀)

BUNDLED 데이터는 4번째 줄, 약 637,179자짜리 단일 라인. Grep 도구는 이 라인을
`[Omitted long matching line]`로 생략해버려서 쓸 수 없음.

**Bash 도구 + grep -bo (byte offset) + tail/head 조합 사용**:

```bash
# 1. 원하는 id/텍스트의 byte offset 찾기
grep -bo '"id":"cause-xxx"' index.html

# 2. 해당 offset부터 N바이트 읽기 (cause 객체 하나는 보통 2000~3000자면 description+stage1까지 보임)
tail -c +<offset> index.html | head -c 3000

# pass_next/fail_next 같은 라우팅만 빠르게 보고 싶을 때
grep -o '"id":"test-xxx"[^}]*"pass_next":"[^"]*","fail_next":"[^"]*"' index.html
```

python3는 Git Bash 환경에 없음 — 쓰지 말 것.

## 동작별 pain_site 존재 여부 (참고용 추정 — 작업 시 재확인)

manifest(파일 앞부분 ~1700바이트) 기준 추정치. 실제 시작 전에
`grep -bo '"id":"hip"\|"id":"wrist"\|"id":"elbow"\|"id":"chest"' index.html`
로 재확인 권장.

- **고관절(hip)**: 스쿼트, 런지, 데드리프트
- **손목(wrist)**: 스쿼트, 데드리프트, 키핑, 로우, 수직프레스
- **팔꿈치(elbow)**: 풀업, 키핑, 로우, 수직프레스, 수평프레스
- **흉근(chest)**: 수평프레스만

## 검토 체크리스트 (cause 1개당)

1. **cause.description의 메커니즘** ↔ 그 cause로 라우팅되는 선별검사(questions의 `"next":"cause:xxx"`)
   또는 직접테스트(`pass_next`/`fail_next`)가 실제로 그 메커니즘을 검증하는 검사인지
2. **회복테스트** — `goRetest()` 로직: `tests`에서 `fail_next === "cause:" + causeId`인 테스트(확인검사)를 우선 선택,
   없으면 `pass_next === "cause:" + causeId" 기준 fallback. retestMode에서는 pass_next/fail_next 무시,
   pass/fail outcome만 처리 (의도된 동작, project CLAUDE.md 참조)
3. (참고) route.stages exercises의 "why"가 cause.description과 부합하는지 — 메인 체크 아님

## 보고/문서화 형식

`docs/RETEST_CONTENT_REVIEW.md`의 무릎/허리/발목/어깨 섹션과 동일한 형식:

```
## {부위} (동작1 → 동작2 → ...) — 검토 완료

| 동작 | 원인 | 검사 | 판정 |
|---|---|---|---|
| ... | ... | ... | 일치/보류/수정 필요 |

### 수정 완료 (있는 경우)
- ...

**{부위} 결론**: N개 원인 전부 일치 (보류 N건 / 수정 N건).
```

작성 전 반드시 채팅으로 먼저 보여주고 승인받기 (워크플로우 메모리 참조).
완료 후 `## 진행 예정` 체크리스트에서 해당 부위 `[x]`로 변경.

## 진행 예정 체크리스트 (docs/RETEST_CONTENT_REVIEW.md 기준 현황)

- [x] 무릎
- [x] 허리
- [x] 발목
- [x] 어깨
- [ ] 고관절 ← **다음 작업**
- [ ] 손목
- [ ] 팔꿈치
- [ ] 흉근
