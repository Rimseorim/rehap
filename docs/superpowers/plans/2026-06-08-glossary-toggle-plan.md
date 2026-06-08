# 전문용어 설명(`?` 토글) 기능 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 운동 카드와 원인 설명 화면에서, 본문은 전문용어를 유지한 채 `?` 토글을
누르면 그 자리에서 쉬운 풀이가 펼쳐지는 기능을 추가한다.

**Architecture:** `index.html` 내부 `BUNDLED` JSON에 `glossary`(용어→풀이 평면
매핑) 데이터를 추가하고, 텍스트에서 등장하는 용어를 자동 감지해 기존
`<details>` 패턴과 동일한 톤의 토글 HTML을 생성하는 범용 함수
`getGlossaryTerms`/`glossaryToggle`을 만든다. 이 함수를 `route()`(운동 카드)와
`cause()`(원인 설명) 두 화면의 렌더링 템플릿에 호출 한 줄씩 추가해 적용한다.

**Tech Stack:** Vanilla JS (단일 `index.html`), Python(데이터 빌드 스크립트,
기존 `scripts/` 패턴), Node.js(헬퍼 함수 검증), Playwright(브라우저 스모크 검증
— 이미 `package.json`에 설치돼 있으나 이번이 첫 사용)

**참고 — 이 프로젝트엔 자동화된 단위 테스트 스위트가 없다** (단일 HTML +
브라우저 전역 함수 구조). 따라서 "테스트"는 ① 데이터 무결성을 확인하는 Python
검증 스크립트, ② 순수 함수 로직을 확인하는 Node 어설션 스크립트, ③ 실제 화면
동작을 확인하는 1회성 Playwright 스모크 스크립트로 구성한다. 이 스크립트들은
`scripts/` 아래 임시 검증용으로 작성하고, 검증이 끝나면 삭제한다 (영구 테스트
스위트를 새로 들이는 건 이번 작업 범위 밖 — YAGNI).

설계 근거: `docs/superpowers/specs/2026-06-08-glossary-toggle-design.md`

---

### Task 1: `BUNDLED.glossary` 데이터 추가

**Files:**
- Modify: `index.html:4` (BUNDLED JSON 블록)
- Create (임시, 검증 후 삭제): `scripts/_add_glossary.py`

- [ ] **Step 1: 용어집 추가 스크립트 작성**

`scripts/_add_glossary.py` 파일을 새로 만든다:

```python
import io, json, re

GLOSSARY = {
    # 근육·뼈·구조물명 (19)
    "요추": "허리뼈",
    "흉추": "등뼈",
    "견갑골": "어깨뼈",
    "슬개골": "무릎뼈",
    "족관절": "발목 관절",
    "천장관절": "골반 뒤쪽, 엉치뼈와 골반이 만나는 관절",
    "전거근": "갈비뼈 옆쪽을 감싸 어깨뼈를 고정하는 근육",
    "회전근개": "어깨 관절을 감싸 안정시키는 4개의 근육",
    "신전근": "관절을 펴는 근육",
    "장요근": "골반과 허벅지를 이어 다리를 들어 올리는 근육",
    "굴곡근": "관절을 굽히는 근육",
    "외전근": "팔다리를 몸 바깥쪽으로 벌리는 근육",
    "관절낭": "관절을 감싸 보호하는 막",
    "다열근": "허리를 숙였다 펼 때 척추뼈 하나하나를 잡아주는 근육",
    "복횡근": "숨을 내쉴 때 배가 들어가게 만드는, 배 속 깊은 근육",
    "중둔근": "엉덩이 옆쪽에서 골반을 받쳐주는 근육",
    "대둔근": "엉덩이에서 가장 큰 근육",
    "소둔근": "엉덩이 깊숙한 곳의 작은 근육",
    "이상근": "엉덩이 깊은 곳에서 고관절을 돌리는 근육",
    # 동작·개념·진단명 (8)
    "등척성": "관절을 움직이지 않고 그 자세 그대로 힘만 주는 동작",
    "편심성": "근육이 늘어나면서 버티는 동작 (예: 천천히 내려가기)",
    "건병증": "힘줄에 반복 자극이 쌓여 약해진 상태",
    "충돌증후군": "어깨뼈와 위팔뼈 사이 공간이 좁아져 힘줄이 끼이는 증상",
    "가동범위": "관절이 움직일 수 있는 범위",
    "배측굴곡": "발끝을 정강이 쪽으로 들어 올리는 움직임",
    "슬개대퇴": "무릎뼈와 허벅지뼈가 맞닿는 부분",
    "회외": "손바닥을 위로 향하게 돌리는 동작",
}

assert len(GLOSSARY) == 27, f"용어 27개여야 하는데 {len(GLOSSARY)}개"

with io.open('index.html', encoding='utf-8') as f:
    lines = f.readlines()

m = re.match(r'(<script>const BUNDLED=)(\{.*\})(;</script>.*)', lines[3], re.S)
assert m, "BUNDLED 블록을 찾지 못함"
data = json.loads(m.group(2))
assert 'glossary' not in data, "glossary 키가 이미 존재함 — 스크립트를 두 번 실행하지 않았는지 확인"
data['glossary'] = GLOSSARY

new_json = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
lines[3] = m.group(1) + new_json + m.group(3)

with io.open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.writelines(lines)

print(f"glossary {len(GLOSSARY)}개 항목 추가 완료")
```

- [ ] **Step 2: 스크립트 실행**

Run: `python scripts/_add_glossary.py`
Expected output: `glossary 27개 항목 추가 완료`

- [ ] **Step 3: 데이터 무결성 검증**

다음 명령으로 결과를 확인한다 (별도 파일 생성 없이 인라인 실행):

```bash
python -c "
import io, json, re
with io.open('index.html', encoding='utf-8') as f:
    txt = f.read()
m = re.search(r'const BUNDLED=(\{.*\});</script>', txt)
data = json.loads(m.group(1))
assert 'glossary' in data
assert len(data['glossary']) == 27
assert data['glossary']['등척성'] == '관절을 움직이지 않고 그 자세 그대로 힘만 주는 동작'
assert data['glossary']['복횡근'] == '숨을 내쉴 때 배가 들어가게 만드는, 배 속 깊은 근육'
print('OK — glossary', len(data['glossary']), '개 항목 확인')
"
```

Expected: `OK — glossary 27 개 항목 확인` (JSON 파싱이 실패하면 `json.JSONDecodeError` 발생 — 그 경우 Step 1의 정규식/직렬화를 점검)

- [ ] **Step 4: 임시 스크립트 삭제 및 커밋**

```bash
rm scripts/_add_glossary.py
git add index.html
git commit -m "feat: BUNDLED에 전문용어 설명용 glossary 데이터(27종) 추가"
```

---

### Task 2: `getGlossaryTerms` / `glossaryToggle` 헬퍼 함수 추가

**Files:**
- Modify: `index.html:484` (Phase A/B 시스템 블록 바로 뒤에 추가)
- Create (임시, 검증 후 삭제): `scripts/_verify_glossary_helpers.mjs`

- [ ] **Step 1: 검증 스크립트 작성 (먼저 작성 — 아직 실패해야 정상)**

`scripts/_verify_glossary_helpers.mjs` 파일을 만든다:

```js
import fs from 'fs';
import assert from 'assert';

const html = fs.readFileSync(new URL('../index.html', import.meta.url), 'utf-8');

const bundledMatch = html.match(/const BUNDLED=(\{.*\});<\/script>/s);
assert(bundledMatch, 'BUNDLED 블록을 찾지 못함');
const BUNDLED = JSON.parse(bundledMatch[1]);
assert(BUNDLED.glossary, 'BUNDLED.glossary가 없음 — Task 1을 먼저 완료하세요');

const termsFnMatch = html.match(/function getGlossaryTerms\(text\) \{[\s\S]*?\n\}/);
assert(termsFnMatch, 'getGlossaryTerms 함수 정의를 찾지 못함 — 아직 추가 전이면 정상(RED)');
const toggleFnMatch = html.match(/function glossaryToggle\(text\) \{[\s\S]*?\n\}/);
assert(toggleFnMatch, 'glossaryToggle 함수 정의를 찾지 못함 — 아직 추가 전이면 정상(RED)');

const build = new Function('BUNDLED', `
  ${termsFnMatch[0]}
  ${toggleFnMatch[0]}
  return { getGlossaryTerms, glossaryToggle };
`);
const { getGlossaryTerms, glossaryToggle } = build(BUNDLED);

assert.deepStrictEqual(
  getGlossaryTerms('통증 없는 등척성 수축으로 어깨 근육을 깨웁니다'),
  ['등척성']
);
assert.deepStrictEqual(
  getGlossaryTerms('아무 전문용어도 없는 평범한 문장입니다'),
  []
);

const withTerms = glossaryToggle('등척성 수축과 편심성 동작을 함께 훈련합니다');
assert(withTerms.includes('<details'), '용어가 있으면 <details>를 반환해야 함');
assert(withTerms.includes('등척성') && withTerms.includes('편심성'), '감지된 용어를 모두 포함해야 함');
assert(withTerms.includes(BUNDLED.glossary['등척성']), '용어 풀이 텍스트를 포함해야 함');

assert.strictEqual(
  glossaryToggle('아무 전문용어도 없는 문장'),
  '',
  '용어가 없으면 빈 문자열을 반환해야 함'
);

console.log('PASS — getGlossaryTerms / glossaryToggle 검증 통과');
```

- [ ] **Step 2: 실행해서 실패 확인 (RED)**

Run: `node scripts/_verify_glossary_helpers.mjs`
Expected: `AssertionError [ERR_ASSERTION]: getGlossaryTerms 함수 정의를 찾지 못함 — 아직 추가 전이면 정상(RED)` 로 실패

- [ ] **Step 3: 헬퍼 함수 구현**

`index.html:484`(Phase A/B 시스템 블록의 마지막 줄, `function updatePhaseStats` 정의 끝) 바로 뒤에 다음 블록을 추가한다:

```js

/* ── 용어 설명(Glossary) ── */
function getGlossaryTerms(text) {
  return Object.keys(BUNDLED.glossary).filter(term => text.includes(term));
}
function glossaryToggle(text) {
  const terms = getGlossaryTerms(text);
  if (!terms.length) return '';
  return `
  <details class="glossary-toggle" style="display:inline-block;margin-left:6px;vertical-align:middle">
    <summary style="list-style:none;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;
      width:22px;height:22px;border-radius:50%;border:1px solid var(--border);
      font-size:12px;font-weight:700;color:var(--text-sub)">?</summary>
    <div class="card" style="margin-top:8px;display:flex;flex-direction:column;gap:8px">
      ${terms.map(t => `
        <div>
          <strong style="font-size:var(--t4)">${t}</strong>
          <p style="color:var(--text-sub);font-size:var(--t4);margin-top:2px">${BUNDLED.glossary[t]}</p>
        </div>`).join('')}
    </div>
  </details>`;
}
```

- [ ] **Step 4: 실행해서 통과 확인 (GREEN)**

Run: `node scripts/_verify_glossary_helpers.mjs`
Expected: `PASS — getGlossaryTerms / glossaryToggle 검증 통과`

- [ ] **Step 5: 임시 스크립트 삭제 및 커밋**

```bash
rm scripts/_verify_glossary_helpers.mjs
git add index.html
git commit -m "feat: getGlossaryTerms/glossaryToggle 헬퍼 함수 추가"
```

---

### Task 3: 운동 카드(`route()`)에 `?` 토글 적용

**Files:**
- Modify: `index.html:1651`

- [ ] **Step 1: 운동 카드 제목 줄에 토글 삽입**

`index.html:1650-1653`의 다음 블록을 찾는다:

```html
        <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:8px">
          <h3 style="margin:0">${ex.name}</h3>
          <button onclick="openVideoModal('${ex.video_url||''}')" style="flex-shrink:0;background:var(--dark);color:white;border:none;border-radius:6px;padding:5px 10px;font-size:var(--t4);font-weight:600;cursor:pointer">▶ 영상</button>
        </div>
```

`<h3>` 줄을 다음으로 교체한다 (운동명 옆에 토글 추가, `why`+`cue` 텍스트를 함께 검사):

```html
          <h3 style="margin:0">${ex.name}${glossaryToggle((ex.why||'') + ' ' + (ex.cue||''))}</h3>
```

- [ ] **Step 2: 동작 확인**

브라우저에서 확인하기 어려운 환경이므로, 우선 정적으로 다음을 확인한다:

```bash
grep -n "glossaryToggle((ex.why" index.html
```

Expected: `1651:          <h3 style="margin:0">${ex.name}${glossaryToggle((ex.why||'') + ' ' + (ex.cue||''))}</h3>` 형태로 한 줄 출력 (실제 줄 번호는 달라질 수 있음 — 핵심은 매치되는 줄이 1개여야 함)

- [ ] **Step 3: 커밋**

```bash
git add index.html
git commit -m "feat: 운동 카드에 전문용어 ? 토글 적용"
```

---

### Task 4: 원인 설명(`cause()`) 화면에 `?` 토글 적용

**Files:**
- Modify: `index.html:1535`

- [ ] **Step 1: 원인 설명 텍스트 옆에 토글 삽입**

`index.html:1532-1536`의 다음 블록을 찾는다:

```html
    <div class="card" style="display:flex;flex-direction:column;gap:10px">
      <span class="cause-tag">${c.tag}</span>
      <h2 class="t2">${c.name}</h2>
      <p class="t3">${c.description}</p>
    </div>
```

`<p class="t3">` 줄을 다음으로 교체한다:

```html
      <p class="t3">${c.description}${glossaryToggle(c.description)}</p>
```

- [ ] **Step 2: 동작 확인**

```bash
grep -n "c.description}\${glossaryToggle" index.html
```

Expected: `1535:      <p class="t3">${c.description}${glossaryToggle(c.description)}</p>` 형태로 한 줄 출력

- [ ] **Step 3: 커밋**

```bash
git add index.html
git commit -m "feat: 원인 설명 화면에 전문용어 ? 토글 적용"
```

---

### Task 5: 브라우저 스모크 검증 (Playwright)

**Files:**
- Create (임시, 검증 후 삭제): `scripts/_smoke_glossary.mjs`

이 작업은 실제 화면에서 토글이 보이고 펼쳐지는지 눈으로 확인하기 위한
1회성 검증이다. 영구 테스트 스위트가 아니므로 검증 후 스크립트를 삭제한다.

- [ ] **Step 1: 로컬 정적 서버 실행**

`index.html`은 빌드 없이 정적 파일이므로 Python 내장 서버로 띄운다:

```bash
python -m http.server 8000 &
echo $! > /tmp/glossary_smoke_server.pid
```

- [ ] **Step 2: 스모크 스크립트 작성**

`scripts/_smoke_glossary.mjs` 파일을 만든다. 등척성/편심성 등 용어가 등장하는
것으로 확인된 화면(예: `squat` 동작 → `shoulder` 부위 진단 결과 화면)으로
이동해 토글의 존재와 펼침 동작을 확인한다:

```js
import { chromium } from 'playwright';
import assert from 'assert';

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 375, height: 812 } });
await page.goto('http://localhost:8000/index.html');

// glossary 데이터가 로드됐는지 우선 확인
const glossaryCount = await page.evaluate(() => Object.keys(window.BUNDLED?.glossary || {}).length);
assert.strictEqual(glossaryCount, 27, `glossary 항목 수가 27이어야 하는데 ${glossaryCount}`);

// cause() 화면으로 직접 상태를 주입해 이동 (감별 흐름을 다 타지 않고 검증에 집중)
await page.evaluate(() => {
  S.movementId = 'squat';
  S.painSiteId = 'shoulder';
  S.causeId = BUNDLED.squat.pain_sites.find(p => p.id === 'shoulder').causes[0].id;
  go('cause');
});

await page.waitForSelector('.glossary-toggle summary');
const toggle = page.locator('.glossary-toggle summary').first();
assert.ok(await toggle.isVisible(), '? 토글이 보여야 함');

await toggle.click();
await page.waitForTimeout(200);
const isOpen = await page.locator('.glossary-toggle').first().evaluate(el => el.open);
assert.strictEqual(isOpen, true, '클릭하면 펼쳐져야 함(details[open])');

await page.screenshot({ path: 'scripts/_smoke_glossary_open.png' });

await toggle.click();
const isClosed = await page.locator('.glossary-toggle').first().evaluate(el => !el.open);
assert.strictEqual(isClosed, true, '다시 클릭하면 접혀야 함');

console.log('PASS — 화면에서 ? 토글 표시/펼침/접힘 확인됨. 스크린샷: scripts/_smoke_glossary_open.png');
await browser.close();
```

- [ ] **Step 3: 실행 및 스크린샷 확인**

Run: `node scripts/_smoke_glossary.mjs`
Expected: `PASS — 화면에서 ? 토글 표시/펼침/접힘 확인됨. 스크린샷: scripts/_smoke_glossary_open.png`

`scripts/_smoke_glossary_open.png`를 Read 도구로 열어 `?` 토글이 펼쳐진
모습이 디자인 의도(375px 화면에서 카드 안에 자연스럽게 들어맞는지)대로
보이는지 육안으로 확인한다.

- [ ] **Step 4: 정리**

```bash
kill $(cat /tmp/glossary_smoke_server.pid)
rm scripts/_smoke_glossary.mjs scripts/_smoke_glossary_open.png /tmp/glossary_smoke_server.pid
```

(커밋할 변경사항 없음 — 검증 전용 작업)

---

## 완료 기준

- `BUNDLED.glossary`에 27개 용어가 들어있고 (Task 1)
- `getGlossaryTerms`/`glossaryToggle` 함수가 동작하며 (Task 2)
- 운동 카드와 원인 설명 화면 양쪽에서 `?` 토글이 보이고, 클릭하면 펼쳐지고
  접힌다 (Task 3·4·5)

이후 용어집 27개 항목의 실제 문구를 다듬는 콘텐츠 작업은 별도로 진행한다
(설계 문서의 "범위 밖" 항목 — `BUNDLED.glossary` 객체의 값만 수정하면 되므로
이 플랜의 구조 변경 없이 독립적으로 처리 가능).
