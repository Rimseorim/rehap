# 페르소나 시뮬레이션 테스트 실행 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 8명의 페르소나로 로컬 `index.html`을 claude-in-chrome 브라우저 자동화로 실제 조작해 사용성·데이터 문제를 찾고, 페르소나별 보고서 8개 + 통합 요약 1개를 산출한다.

**Architecture:** 각 페르소나는 독립적인 브라우저 탭에서 순차 실행한다(병렬 아님 — 같은 로컬 파일을 여러 탭에서 동시에 조작하면 상태 추적이 꼬임). 각 태스크는 "탭 열기 → 페르소나 성격대로 진행 → 관찰 기록 → md 저장 → 커밋"의 동일 패턴을 반복한다. 스펙은 `docs/superpowers/specs/2026-09-18-persona-test-design.md`.

**Tech Stack:** claude-in-chrome MCP 브라우저 자동화, 로컬 `file://` 경로, Markdown 산출물.

---

## 사전 준비

- [ ] **Step 0: index.html 로컬 경로 확인 및 브라우저 도구 로드**

Run: 현재 파일 절대경로 확인
```
C:\dev\exercisematerials\01.test\index.html
```
파일 URL: `file:///C:/dev/exercisematerials/01.test/index.html`

ToolSearch 호출로 다음 도구 한 번에 로드:
```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find
```

- [ ] **Step 1: docs/persona-tests 디렉토리 확인**

Run: `mkdir -p "C:/dev/exercisematerials/01.test/docs/persona-tests"` (Bash) — Write 도구는 존재하지 않는 상위 디렉토리에도 파일을 생성하므로 실제로는 첫 페르소나 보고서 저장 시 자동 생성됨. 이 스텝은 생략 가능, 생성 확인용으로만 사용.

---

## 공통 페르소나 실행 절차 (태스크 1~8에 동일 적용)

각 페르소나 태스크는 아래 5개 서브스텝을 따른다:

1. `tabs_create_mcp`로 새 탭 열고 `navigate`로 `file:///C:/dev/exercisematerials/01.test/index.html` 로드
2. 동작 선택 → 통증부위 선택 → 감별 질문에 페르소나 성격대로 답변 (아래 표의 "답변 전략" 참고) → danger 안내가 뜨면 화면 캡처 후 기록, 아니면 cause 판정 → 재활 루트 화면까지 진행
3. 진행 중 다음을 매 화면마다 관찰·기록: (a) 클릭/입력이 의도대로 동작했는지, (b) 문구가 페르소나 기준으로 이해됐는지, (c) 레이아웃 깨짐 여부, (d) 최종 배정된 cause/루트가 시나리오와 논리적으로 맞는지
4. `docs/persona-tests/persona-N-{동작}.md`로 보고서 작성 (아래 "보고서 포맷" 참고)
5. 탭 닫고(`tabs_close_mcp`) 커밋

**답변 전략 매핑:**
- IT숙련=미숙 → 아이콘/버튼 의미가 애매하면 첫 클릭에서 주저하는 모습을 보고서에 남기고, 실제로는 올바른 요소를 찾아 진행(진행 자체는 막히지 않되 헤맨 지점을 기록)
- 증상설명정확도=부정확 → 질문이 구체적 신체 동작을 물어도 "그냥 아파요" 식으로 애매한 선택지를 고르는 경향(선택지 중 가장 포괄적인 것 선택)
- 증상민감도=예민 → 통증 강도·빈도를 묻는 질문에 상위 단계(더 심각한 쪽) 선택
- 증상민감도=둔감 → 같은 질문에 하위 단계(덜 심각한 쪽) 선택
- 병원권유수용도=거부감 → 위험신호 감지 질문(안정 시 통증 지속, 저림, 방사통 등)에서 실제 시나리오상 해당되더라도 "아니요/괜찮아요" 쪽을 먼저 시도 — **단, 이건 danger 분기가 실제로 뜨는지 앱의 판정 로직을 검증하는 것이 목적이므로, 시나리오에 명시된 위험신호 항목 자체는 스펙대로 답한다.** 거부감은 "위험 아닌 애매한 부가 질문"에서만 축소 답변으로 표현
- 병원권유수용도=수용적 → danger 안내가 뜨면 순순히 병원 권유를 받아들이는 반응으로 기록

**보고서 포맷** (`persona-N-{동작}.md`):
```markdown
# 페르소나 N: {나이/성별} · {동작}

## 프로필
- IT숙련도: / 증상설명정확도: / 증상민감도: / 병원권유수용도: / 크로스핏경력:
- 시나리오: {통증부위 + 검증목적}

## 진행 기록
1. {화면명}: {페르소나가 한 행동} → {관찰된 반응/문제}
2. ...

## 발견된 문제
- [심각도: 안전/데이터/사용성/오탈자] {문제 설명} — {화면/위치}

## 최종 결과
- 배정된 cause/루트: {결과}
- 시나리오 의도와 일치 여부: {일치/불일치, 이유}
```

---

### Task 1: 페르소나 1 — 스쿼트 (32세 남, IT숙련/정확/둔감/수용적/숙련)

**Files:**
- Create: `docs/persona-tests/persona-1-squat.md`

- [ ] **Step 1: 브라우저로 스쿼트 → 무릎 앞쪽 통증 시나리오 진행**

동작에서 "스쿼트" 선택 → 통증부위 "무릎" → "앞쪽" 계열 선택지 진행. 증상 질문에는 평이한 중간 강도로 답변(둔감이므로 하위 단계 선택). 위험신호 해당 없는 표준 케이스이므로 danger 없이 cause 판정까지 진행 예상.

- [ ] **Step 2: 관찰 기록하며 보고서 작성**

위 "보고서 포맷"대로 `docs/persona-tests/persona-1-squat.md` 작성. 특히 IT숙련+수용적 조합이므로 막힘없이 완주하는지가 베이스라인 기준.

- [ ] **Step 3: 탭 닫고 커밋**

```bash
git add docs/persona-tests/persona-1-squat.md
git commit -m "test: 페르소나1(스쿼트) 시뮬레이션 실행 결과 기록"
```

---

### Task 2: 페르소나 2 — 런지 (24세 여, IT미숙/정확/둔감/거부감/초보)

**Files:**
- Create: `docs/persona-tests/persona-2-lunge.md`

- [ ] **Step 1: 브라우저로 런지 → 경미한 무릎 통증 시나리오 진행**

동작 "런지" → 통증부위 "무릎" → 경미한 통증 계열 선택지(위험신호 아님). IT미숙이므로 화면 요소(버튼/아이콘) 클릭 전 `find`나 `read_page`로 요소 위치 재확인하는 과정을 거치며 "헤맨 지점"으로 기록. 위험신호 아닌 부가질문에서는 축소 답변(거부감) 시도.

- [ ] **Step 2: danger 오탐 여부 확인 후 보고서 작성**

실제로는 위험신호가 아니므로 danger 화면 없이 정상적으로 재활 루트까지 도달해야 함 — 만약 거부감으로 인한 축소 답변 때문에 오히려 잘못된 cause로 빠지면 "데이터" 심각도로 기록.

- [ ] **Step 3: 탭 닫고 커밋**

```bash
git add docs/persona-tests/persona-2-lunge.md
git commit -m "test: 페르소나2(런지) 시뮬레이션 실행 결과 기록"
```

---

### Task 3: 페르소나 3 — 데드리프트 (45세 남, IT숙련/부정확/예민/수용적/숙련)

**Files:**
- Create: `docs/persona-tests/persona-3-deadlift.md`

- [ ] **Step 1: 브라우저로 데드리프트 → 무릎 바깥쪽 통증(구조적 밸거스) 시나리오 진행**

동작 "데드리프트" → 통증부위 "무릎" → "바깥쪽" 계열 선택. [[project_shallow_branch_pattern]]에서 수정된 `test-valgus-lateral` 노드가 이 경로에 걸리는지가 핵심. 증상설명 부정확이므로 통증 위치를 다소 뭉뚱그려 답하되, 정렬 관련 질문(무릎이 안쪽으로 모이는지 등)에는 "그렇다"로 답해 구조적 밸거스 케이스임을 반영.

- [ ] **Step 2: 정렬 검사 노드 도달 여부 회귀 검증 기록**

`test-valgus-lateral` 또는 동일 계열 정렬 검사가 실제로 나타나는지, fail 시 cause-b로 연결되는지 확인. 안 나타나면 "안전/데이터" 최상위 심각도로 기록(회귀 발생).

- [ ] **Step 3: 탭 닫고 커밋**

```bash
git add docs/persona-tests/persona-3-deadlift.md
git commit -m "test: 페르소나3(데드리프트) 시뮬레이션 실행 결과 기록 - 밸거스 회귀검증"
```

---

### Task 4: 페르소나 4 — 풀업 (27세 여, IT미숙/부정확/예민/거부감/초보)

**Files:**
- Create: `docs/persona-tests/persona-4-pullup.md`

- [ ] **Step 1: 브라우저로 풀업 → 어깨 통증(Drop Arm 해당) 시나리오 진행**

동작 "풀업" → 통증부위 "어깨" 계열 진행. Drop Arm(팔이 힘없이 떨어짐)에 해당하는 위험신호 질문이 나오면, **스펙에 명시된 안전 핵심 시나리오이므로 실제 증상(Drop Arm 양성)은 정확히 답한다** — 거부감 성향은 그 앞뒤의 부가 질문(통증 빈도 등)에서만 축소 답변으로 표현.

- [ ] **Step 2: danger 화면 정상 노출 여부 확인**

Drop Arm 양성 답변 이후 "지금 바로 운동을 멈추세요" danger 화면이 반드시 떠야 함. 만약 재활 루트로 빠지면 **최상위(안전) 심각도**로 즉시 기록.

- [ ] **Step 3: 탭 닫고 커밋**

```bash
git add docs/persona-tests/persona-4-pullup.md
git commit -m "test: 페르소나4(풀업) 시뮬레이션 실행 결과 기록 - 위험신호 검증"
```

---

### Task 5: 페르소나 5 — 키핑 (38세 남, IT숙련/정확/예민/수용적/초보)

**Files:**
- Create: `docs/persona-tests/persona-5-kipping.md`

- [ ] **Step 1: 브라우저로 키핑 → 손목 통증(안정시 저림 지속) 시나리오 진행**

동작 "키핑" → 통증부위 "손목" 계열. 안정 시에도 저림이 지속된다는 위험신호 질문에 정확히 "예"로 답변(예민+정확 조합이므로 세부 증상을 있는 그대로 정확히 전달).

- [ ] **Step 2: danger 화면 정상 노출 확인 (수용적 기준선)**

danger 화면이 뜨면 수용적 반응으로 기록하고 병원 권유 문구가 명확한지 확인. 이 결과를 페르소나4(거부감)와 비교할 수 있도록 보고서에 명시.

- [ ] **Step 3: 탭 닫고 커밋**

```bash
git add docs/persona-tests/persona-5-kipping.md
git commit -m "test: 페르소나5(키핑) 시뮬레이션 실행 결과 기록"
```

---

### Task 6: 페르소나 6 — 로우 (51세 여, IT미숙/정확/둔감/거부감/숙련)

**Files:**
- Create: `docs/persona-tests/persona-6-row.md`

- [ ] **Step 1: 브라우저로 로우 → 허리 통증 + 방사통 시나리오 진행**

동작 "로우" → 통증부위 "허리" 계열. 다리로 저림·방사통이 있다는 위험신호 질문에는 **스펙대로 정확히 "예"로 답변** — 거부감은 부가 질문에서만 표현.

- [ ] **Step 2: danger 화면 정상 노출 여부 확인 (두 번째 안전 핵심 시나리오)**

페르소나4와 마찬가지로 danger 화면이 반드시 떠야 함. IT미숙 조합이라 화면 요소 인식에서 헤맨 지점도 함께 기록.

- [ ] **Step 3: 탭 닫고 커밋**

```bash
git add docs/persona-tests/persona-6-row.md
git commit -m "test: 페르소나6(로우) 시뮬레이션 실행 결과 기록 - 위험신호 검증"
```

---

### Task 7: 페르소나 7 — 수직 프레스 (29세 남, IT숙련/부정확/둔감/수용적/초보)

**Files:**
- Create: `docs/persona-tests/persona-7-vertical-press.md`

- [ ] **Step 1: 브라우저로 수직 프레스 → 사타구니/고관절 통증 시나리오 진행**

동작 "수직 프레스" → 통증부위 "고관절"(또는 사타구니 매핑 항목) 계열, 표준 강도로 진행. 위험신호 없는 베이스라인 케이스.

- [ ] **Step 2: 보고서 작성**

부정확한 증상설명(포괄적 선택지 위주)이 최종 cause 판정 정확도에 영향을 주는지 기록.

- [ ] **Step 3: 탭 닫고 커밋**

```bash
git add docs/persona-tests/persona-7-vertical-press.md
git commit -m "test: 페르소나7(수직프레스) 시뮬레이션 실행 결과 기록"
```

---

### Task 8: 페르소나 8 — 수평 프레스 (41세 여, IT미숙/부정확/예민/거부감/숙련)

**Files:**
- Create: `docs/persona-tests/persona-8-horizontal-press.md`

- [ ] **Step 1: 브라우저로 수평 프레스 → 가슴/어깨 통증 시나리오 진행**

동작 "수평 프레스" → 통증부위 "가슴" 또는 "어깨" 계열. 부정확+예민 조합 — 통증 강도는 상위 단계로 답하되 위치 설명은 애매하게(포괄적 선택지) 답변.

- [ ] **Step 2: 오분류 여부 확인**

애매한 답변 조합이 실제로 부적절한 cause로 이어지는지가 검증 포인트. 이어지면 "데이터" 심각도로 기록.

- [ ] **Step 3: 탭 닫고 커밋**

```bash
git add docs/persona-tests/persona-8-horizontal-press.md
git commit -m "test: 페르소나8(수평프레스) 시뮬레이션 실행 결과 기록"
```

---

### Task 9: 통합 요약 작성

**Files:**
- Create: `docs/persona-tests/summary.md`
- Read (참고): `docs/persona-tests/persona-1-squat.md` ~ `persona-8-horizontal-press.md`

- [ ] **Step 1: 8개 보고서의 "발견된 문제" 섹션 취합**

각 보고서의 문제 항목을 심각도(안전 > 데이터 > 사용성 > 오탈자) 순으로 정렬해 하나의 표로 작성.

```markdown
# 페르소나 테스트 통합 요약

## 발견된 문제 (심각도순)

| 심각도 | 동작 | 문제 | 위치 |
|---|---|---|---|
| 안전 | ... | ... | ... |
| 데이터 | ... | ... | ... |
| 사용성 | ... | ... | ... |
| 오탈자 | ... | ... | ... |

## 페르소나별 완주 여부

| # | 동작 | 완주 | 최종 결과 | 시나리오 일치 |
|---|---|---|---|---|
| 1 | 스쿼트 | | | |
...

## 다음 액션 제안
- {우선순위 높은 순으로 후속 조치 제안}
```

- [ ] **Step 2: 커밋**

```bash
git add docs/persona-tests/summary.md
git commit -m "test: 페르소나 테스트 8건 통합 요약 작성"
```

---

## Self-Review 결과

- **스펙 커버리지**: 8명 프로필/시나리오 전부 태스크화(Task 1~8), 산출물(페르소나별 md + summary) Task 9까지 반영. 실행 대상(로컬 file://), 답변 전략(성격→행동 매핑)까지 명시.
- **플레이스홀더 스캔**: 요약 표(Task 9)의 셀은 실행 시점에 채워지는 데이터 슬롯이라 "TBD"가 아님 — 실행 전에는 당연히 빈 표 구조만 존재.
- **일관성**: 보고서 파일명·경로가 스펙의 `docs/persona-tests/` 및 태스크 전체에서 동일하게 사용됨.
