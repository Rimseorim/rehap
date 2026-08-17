# danger 카드 SFMA2 응급신호 문구 추가 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 원인 확정(`cause()`) 화면의 danger 카드에, 통증부위(어깨/발목/허리)별로 SFMA2 근거 응급신호 문구를 조건부로 추가한다.

**Architecture:** `index.html` 내 단일 `<script>`에 정의된 `cause()` 함수(약 1438행)를 수정한다. 통증부위→추가 신호 매핑 객체를 새로 두고, 기존 하드코딩된 카드 항목(부종/열감) 마크업을 재사용 가능한 헬퍼 함수로 뽑아낸 뒤, `S.painSiteId`에 해당하는 신호가 있으면 같은 스타일로 이어붙인다. 새 UI 컴포넌트나 상태 필드는 없음 — 순수 정적 텍스트 렌더링.

**Tech Stack:** Vanilla JS, 템플릿 리터럴 기반 렌더링 (프레임워크 없음). 이 프로젝트엔 unit test 러너가 없으므로, 검증은 Node 스크립트로 데이터 구조 확인 + Playwright 브라우저 스모크 테스트로 진행한다 (task #16과 동일한 검증 방식).

---

## 참고 문서

- 스펙: `docs/superpowers/specs/2026-08-17-danger-card-sfma2-signals-design.md`
- 현재 `cause()` 함수 원문: `index.html:1438-1468`
- `S.painSiteId`는 이미 앱 상태에 존재하며 화면 진입 시 항상 설정되어 있음 (`index.html:805` `getPainSite()`가 이를 참조).

---

### Task 1: `EXTRA_DANGER_SIGNS` 매핑 + `cause()` 함수 수정

**Files:**
- Modify: `index.html:1438-1468` (`function cause()`)

- [ ] **Step 1: `cause()` 함수 직전에 매핑 객체와 헬퍼 함수 추가**

`index.html`에서 `function cause() {` 라인(1438) 바로 위에 아래 코드를 삽입한다:

```javascript
const EXTRA_DANGER_SIGNS = {
  shoulder: {
    title: '저항할 때 팔이 갑자기 뚝 떨어져요',
    sub: '팔을 바깥으로 돌린 상태를 유지하지 못하는 경우'
  },
  ankle: {
    title: '종아리 한쪽만 눈에 띄게 부었어요',
    sub: '양쪽을 비교했을 때 확실히 차이 나는 경우'
  },
  'lower-back': {
    title: '양쪽 다리에 동시에 저림이나 힘빠짐이 있어요',
    sub: '사타구니·엉덩이 안쪽 감각이 둔하거나 대소변 조절이 갑자기 안 되는 경우 포함'
  }
};

function dangerSignItem(title, sub) {
  return `
      <div style="display:flex;gap:10px;align-items:flex-start">
        <span style="color:var(--danger);font-weight:700;flex-shrink:0;font-size:16px">!</span>
        <div>
          <p style="margin:0;font-size:var(--t4);font-weight:600;color:var(--danger)">${title}</p>
          <p style="margin:3px 0 0;font-size:var(--t4);color:var(--text-sub)">${sub}</p>
        </div>
      </div>`;
}
```

- [ ] **Step 2: 기존 `cause()` 함수 본문을 헬퍼 재사용 + 조건부 항목 추가로 교체**

`index.html:1438-1468`의 `function cause() { ... }` 전체를 아래로 교체한다:

```javascript
function cause() {
  const c = getCause();
  const extraSign = EXTRA_DANGER_SIGNS[S.painSiteId];
  return `
    ${contextBar()}
    <div>
      <h1 class="t1">원인을 찾았습니다</h1>
    </div>
    <div class="card" style="display:flex;flex-direction:column;gap:10px">
      <span class="cause-tag">${c.tag}</span>
      <h2 class="t2">${c.name}</h2>
      <p class="t3">${c.description}${glossaryToggle(c.description)}</p>
    </div>
    <div style="background:var(--danger-bg);border:1px solid var(--danger);border-radius:10px;padding:12px 14px;display:flex;flex-direction:column;gap:10px">
      ${dangerSignItem('관절이 눈에 띄게 부어있어요', '운동 후뿐 아니라 지금도 부어있는 경우')}
      ${dangerSignItem('만지면 열감이 느껴져요', '다른 쪽 관절과 비교했을 때 확실히 따뜻함')}
      ${extraSign ? dangerSignItem(extraSign.title, extraSign.sub) : ''}
      <p style="margin:4px 0 0;font-size:var(--t4);color:var(--danger);font-weight:600">위 항목에 해당된다면 재활 전 전문의 진단을 먼저 받으세요.</p>
    </div>
    <button class="btn-primary" onclick="goToRoute()">재활 루트 보기</button>`;
}
```

- [ ] **Step 3: Node로 구문 오류 여부 확인**

`index.html`은 브라우저 전용 스크립트라 Node로 직접 require는 안 되지만, JS 구문 유효성은 Node의 파서로 확인할 수 있다.

Run:
```bash
node --check <(node -e "
const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const m = html.match(/<script>([\s\S]*)<\/script>/);
process.stdout.write(m[1]);
")
```

Windows/PowerShell에서 프로세스 치환(`<(...)`)이 안 되면 대신:

```bash
node -e "
const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const m = html.match(/<script>([\s\S]*)<\/script>/);
fs.writeFileSync('/tmp/_extract.js', m[1]);
"
node --check /tmp/_extract.js
```

Expected: 에러 없이 종료 (구문 오류 있으면 `SyntaxError`와 줄 번호 출력됨).

- [ ] **Step 4: 커밋**

```bash
git add index.html
git commit -m "feat: danger 카드에 어깨/발목/허리 SFMA2 응급신호 문구 추가"
```

(커밋 메시지 마지막 줄에 `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` 추가)

---

### Task 2: Playwright 브라우저 스모크 테스트

**Files:**
- Create (임시, 검증 후 삭제): `01.test/_smoke_danger_card.js`

**사전 조건:** 로컬 정적 서버로 `index.html`을 서빙해야 Playwright가 로드할 수 있다. `python -m http.server` 또는 `npx serve` 등 프로젝트에 이미 있는 방식을 사용한다. HANDOFF 기록상 Playwright는 `node_modules/playwright`에 이미 설치돼 있다.

- [ ] **Step 1: 정적 서버 백그라운드 실행**

```bash
cd C:/dev/exercisematerials/01.test
python -m http.server 8765 &
```

- [ ] **Step 2: 스모크 스크립트 작성**

`01.test/_smoke_danger_card.js` (프로젝트 루트 안에 작성 — require 모듈 resolve 때문에 스크래치패드에서는 실행 불가, HANDOFF 기록 참고):

```javascript
const { chromium } = require('playwright');

const CASES = [
  // [movementId, painSiteId, 기대 텍스트 존재 여부]
  { path: '#squat/knee',       expectText: null }, // 매핑 없는 부위 → 추가 문구 없어야 함
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // 1) 어깨 관련 cause 화면 도달 후 회전근개 문구 확인
  //    (실제 진입 경로는 앱 흐름을 따라 클릭으로 진행 — 동작 선택 → 통증부위 선택 → 감별질문 응답 → cause 화면)
  await page.goto('http://localhost:8765/index.html');
  await page.click('text=데모로 시작').catch(() => {});
  // 이하 각 동작(예: 수직프레스)×어깨 조합으로 진행해 cause 화면 도달
  // 실제 선택지 라벨은 index.html BUNDLED 데이터를 참고해 채워 넣는다.

  const shoulderCauseHtml = await page.content();
  console.log('[check] 어깨 문구 존재:', shoulderCauseHtml.includes('저항할 때 팔이 갑자기 뚝 떨어져요'));

  await browser.close();
})();
```

이 스크립트는 앱의 실제 클릭 경로(동작 선택 → 통증부위 선택 → 감별질문)를 그대로 따라가야 하므로, 실행 전에 대상 동작×통증부위 조합의 실제 질문/선택지 텍스트를 `index.html`의 BUNDLED 데이터에서 확인해 스크립트에 채워 넣는다 (예: 수직프레스×어깨 → `phase_q` → `test-shoulder-arc`... 등 `cause-dp` 계열로 도달하는 경로 1개를 선택).

- [ ] **Step 3: 실행 및 결과 확인**

```bash
node _smoke_danger_card.js
```

Expected 출력: `[check] 어깨 문구 존재: true`

같은 방식으로 발목(`ankle`)×해당 동작 조합에서 `종아리 한쪽만 눈에 띄게 부었어요`, 허리(`lower-back`)×해당 동작 조합에서 `양쪽 다리에 동시에 저림이나 힘빠짐이 있어요` 문구가 뜨는지 각각 확인한다. 반대로 무릎(`knee`)×해당 동작 조합에서는 세 문구 중 어느 것도 뜨지 않고 기존 2개 항목(부종/열감)만 있는지 확인한다.

- [ ] **Step 4: 임시 스크립트 삭제 및 서버 종료**

```bash
rm 01.test/_smoke_danger_card.js
```

백그라운드로 띄운 `python -m http.server`는 프로세스 종료.

---

## Self-Review 체크리스트 (참고용, 구현자가 완료 후 확인)

- [ ] 어깨/발목/허리 각 3개 문구가 정확한 텍스트로 들어갔는가 (스펙 표와 대조)
- [ ] 무릎·손목·팔꿈치·흉근 등 매핑에 없는 pain site에서는 추가 항목이 전혀 뜨지 않는가
- [ ] 기존 2개 공통 항목(부종/열감) 순서와 문구가 그대로 유지됐는가
- [ ] `dangerSignItem` 헬퍼가 기존 인라인 스타일과 동일한 마크업을 생성하는가 (시각적 차이 없어야 함)
