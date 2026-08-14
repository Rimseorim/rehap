# 어깨 SFMA 상지패턴 자가측정(Apley's Scratch) 도입 — 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 키핑 통증 경로의 모호한 후방신전 검사(`test-shoulder-ext`)를 Apley's Scratch 기반 3분기 질문(`q-shoulder-scratch`)으로 교체하고, 기존 Apley's Scratch 질문(`q4`, 7개 동작)의 편측 편향 문구를 고친다.

**Architecture:** `index.html` 안에 BUNDLED 데이터(JS 객체 리터럴)로 임베드된 JSON을 직접 문자열 치환으로 수정한다. 별도 빌드 스텝 없음 — `index.html`이 곧 배포 산출물. 각 수정 후 `node -e`로 BUNDLED 객체를 파싱해 구조·개수를 검증한다(이 프로젝트에 pytest/jest 같은 테스트 프레임워크 없음 — Node 스크립트 파싱이 곧 테스트, `[[project_phase_ab_merge_status]]` 관례와 동일).

**Tech Stack:** 순수 HTML/JS (프레임워크 없음), Node.js는 검증용 스크립트 실행에만 사용.

**참고 스펙:** `docs/superpowers/specs/2026-08-14-shoulder-sfma-scratch-test-design.md`

---

## Task 1: 키핑 `test-shoulder-flex` → 신규 질문 `q-shoulder-scratch` 라우팅 추가

**Files:**
- Modify: `index.html` (BUNDLED 데이터 내 `kipping.pain_sites[shoulder].questions` 배열)

키핑의 어깨 `questions` 배열 끝(`q4` 다음)에 새 질문 노드를 삽입한다. 아직 `test-shoulder-flex`의 `pass_next`는 건드리지 않는다(Task 2에서 처리) — 이 순서로 하면 중간에 앱을 열어봐도 항상 유효한 상태를 유지한다.

- [ ] **Step 1: 삽입 위치 확인**

Run:
```bash
node -e "
const fs=require('fs');
const s=fs.readFileSync('index.html','utf8');
const mi=s.indexOf('\"kipping\":{\"id\":\"kipping\"');
const shi=s.indexOf('\"id\":\"shoulder\"', mi);
const ti=s.indexOf('\"tests\":[', shi);
console.log(s.slice(ti-120, ti+10));
"
```
Expected 출력 끝부분이 다음과 일치해야 함: `...{"id":"c3","text":"대칭으로 잘 돼요","next":"cause:cause-case4"}]}],"tests":[{`

- [ ] **Step 2: 질문 노드 삽입 (Edit)**

`old_string` (키핑 블록에서만 매치 — `test-shoulder-flex`의 "키핑의 전방 스윙" 문구로 유일성 확보):
```
"next":"cause:cause-case4"}]}],"tests":[{"id":"test-shoulder-flex","name":"능동 어깨 굴곡 검사","purpose":"팔을 머리 위로 완전히 들 수 있는지 확인합니다. 키핑의 전방 스윙 국면에서 필요한 기본 가동범위입니다.
```

`new_string`:
```
"next":"cause:cause-case4"},{"id":"q-shoulder-scratch","text":"Apley's Scratch 검사: 한 손은 어깨 뒤로 위에서 아래로, 반대 손은 허리 뒤로 아래에서 위로 뻗어 등 뒤에서 가까이 할 때 어떤가요?","sub":"거울 앞에서 양쪽 다 해보고 비교하세요. 찝히거나 날카롭게 아프면 충돌증후군일 수 있습니다.","choices":[{"id":"c1","text":"한쪽이든 양쪽이든, 팔이 많이 제한되고 찝혀요","next":"cause:cause-dp"},{"id":"c2","text":"팔 범위는 어느 정도 되지만 한쪽이 훨씬 뻑뻑해요","next":"cause:cause-case3"},{"id":"c3","text":"대칭으로 잘 돼요","next":"test:test-shoulder-core"}]}]}],"tests":[{"id":"test-shoulder-flex","name":"능동 어깨 굴곡 검사","purpose":"팔을 머리 위로 완전히 들 수 있는지 확인합니다. 키핑의 전방 스윙 국면에서 필요한 기본 가동범위입니다.
```

(주의: 원본에서 `]}],"tests"` 였던 것이 새 객체가 배열 안에 추가되며 `}]}],"tests"`로 바뀐다 — 새 질문 객체를 닫는 `}`가 하나 추가되고 그 뒤 배열/부모객체 닫는 `]}` `]`는 그대로 유지되는 구조를 눈으로 재확인할 것.)

- [ ] **Step 3: 구조 검증**

Run:
```bash
node -e "
const fs=require('fs');
const s=fs.readFileSync('index.html','utf8');
const needle='\"id\":\"q-shoulder-scratch\"';
let i=-1,c=0;
while((i=s.indexOf(needle,i+1))!==-1)c++;
console.log('q-shoulder-scratch count:', c);
"
```
Expected: `q-shoulder-scratch count: 1`

- [ ] **Step 4: JSON 유효성(괄호 균형) 확인 — 브라우저에서 바로 열어 콘솔 에러 없는지 확인**

`index.html`을 브라우저로 열고 개발자 콘솔에 JS 파싱 에러가 없는지 확인한다 (문자열 치환이라 괄호 개수가 어긋나면 즉시 전체 앱이 깨진다).

- [ ] **Step 5: 커밋**

```bash
git add index.html
git commit -m "feat: 키핑 어깨 질문에 Apley's Scratch(q-shoulder-scratch) 신규 추가

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>"
```

---

## Task 2: 키핑 `test-shoulder-flex.pass_next` 재배선 + `test-shoulder-ext` 삭제

**Files:**
- Modify: `index.html` (BUNDLED 데이터 내 `kipping.pain_sites[shoulder].tests` 배열)

`test-shoulder-flex`의 `pass_next`를 `test:test-shoulder-ext`에서 `q:q-shoulder-scratch`로 바꾸고, 그 사이에 있던 `test-shoulder-ext` 노드 전체를 삭제한다. 두 변경이 인접해 있으므로 Edit 1번으로 처리한다.

- [ ] **Step 1: 사전 확인 — `test-shoulder-ext`가 파일 전체에서 1곳뿐인지 재확인**

Run:
```bash
node -e "
const fs=require('fs');
const s=fs.readFileSync('index.html','utf8');
const needle='\"id\":\"test-shoulder-ext\"';
let i=-1,c=0;
while((i=s.indexOf(needle,i+1))!==-1)c++;
console.log('test-shoulder-ext count:', c);
"
```
Expected: `test-shoulder-ext count: 1` — 1이 아니면 STOP, 다른 동작에도 있다는 뜻이므로 계획을 다시 검토한다.

- [ ] **Step 2: Edit 실행**

`old_string`:
```
"pass_next":"test:test-shoulder-ext","fail_next":"cause:cause-case1","video_url":""},{"id":"test-shoulder-ext","name":"어깨 후방 신전 가동성 검사","purpose":"팔을 몸 뒤로 뻗을 때 통증이 없는지 확인합니다. 키핑 후방 스윙 국면에서 어깨 과신전이 필요합니다.","steps":["허리를 세우고 양팔을 옆에 내려두세요","팔꿈치를 편 채 양팔을 등 뒤쪽으로 최대한 들어 올리세요","통증 없이 들어 올릴 수 있는 높이를 확인하세요"],"note":"상체가 앞으로 숙여지지 않도록 허리를 세우세요.","pass_text":"등 뒤로 팔이 올라갈 때 통증이 없어요","fail_text":"등 뒤로 올릴 때 어깨가 아프거나 많이 제한돼요","pass_next":"test:test-shoulder-core","fail_next":"cause:cause-case3","video_url":""},{"id":"test-shoulder-core"
```

`new_string`:
```
"pass_next":"q:q-shoulder-scratch","fail_next":"cause:cause-case1","video_url":""},{"id":"test-shoulder-core"
```

- [ ] **Step 3: 검증**

Run:
```bash
node -e "
const fs=require('fs');
const s=fs.readFileSync('index.html','utf8');
console.log('ext still present:', s.includes('\"id\":\"test-shoulder-ext\"'));
console.log('flex pass_next fixed:', s.includes('\"id\":\"test-shoulder-flex\",\"name\":\"능동 어깨 굴곡 검사\",\"purpose\":\"팔을 머리 위로 완전히 들 수 있는지 확인합니다. 키핑의 전방 스윙 국면에서 필요한 기본 가동범위입니다.'));
const mi=s.indexOf('\"kipping\":{\"id\":\"kipping\"');
const shi=s.indexOf('\"id\":\"shoulder\"', mi);
const ti=s.indexOf('\"tests\":[', shi);
console.log(s.slice(ti, ti+700));
"
```
Expected:
- `ext still present: false`
- `flex pass_next fixed: true`
- 출력된 tests 배열 앞부분이 `test-shoulder-flex`(`pass_next`: `q:q-shoulder-scratch`) 바로 다음에 `test-shoulder-core`로 이어짐

- [ ] **Step 4: 브라우저 수동 확인**

`index.html`을 열고: 키핑 선택 → 어깨 → 통증 있음 → (phase 질문) → 능동 굴곡 검사 pass → **새 Apley's Scratch 질문이 뜨는지** → 3개 선택지 각각 눌러서 `cause-dp` / `cause-case3` / `test-shoulder-core`로 정확히 이동하는지 확인.

- [ ] **Step 5: 커밋**

```bash
git add index.html
git commit -m "feat: 키핑 test-shoulder-ext를 Apley's Scratch 질문으로 교체

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>"
```

---

## Task 3: `q4` 편측 편향 문구 일괄 수정 (7개 동작)

**Files:**
- Modify: `index.html` (스쿼트·데드리프트·로우·풀업·키핑·수평프레스·수직프레스 7곳의 `q4` 선택지 `c1` 텍스트)

- [ ] **Step 1: 사전 확인**

Run:
```bash
node -e "
const fs=require('fs');
const s=fs.readFileSync('index.html','utf8');
const needle='\"text\":\"한쪽 팔이 많이 제한되고 찝혀요\"';
let i=-1,c=0;
while((i=s.indexOf(needle,i+1))!==-1)c++;
console.log('count:', c);
"
```
Expected: `count: 7`

- [ ] **Step 2: 일괄 치환 (Edit, replace_all: true)**

`old_string`:
```
"text":"한쪽 팔이 많이 제한되고 찝혀요"
```

`new_string`:
```
"text":"한쪽이든 양쪽이든, 팔이 많이 제한되고 찝혀요"
```

`replace_all: true`로 7곳 전부 한 번에 치환.

- [ ] **Step 3: 검증**

Run:
```bash
node -e "
const fs=require('fs');
const s=fs.readFileSync('index.html','utf8');
const oldNeedle='\"text\":\"한쪽 팔이 많이 제한되고 찝혀요\"';
const newNeedle='\"text\":\"한쪽이든 양쪽이든, 팔이 많이 제한되고 찝혀요\"';
function count(n){let i=-1,c=0;while((i=s.indexOf(n,i+1))!==-1)c++;return c;}
console.log('old remaining:', count(oldNeedle));
console.log('new count:', count(newNeedle));
"
```
Expected: `old remaining: 0`, `new count: 8` (기존 7곳 + Task 1에서 새로 만든 `q-shoulder-scratch`의 `c1`도 이미 이 표현을 쓰므로 +1)

- [ ] **Step 4: `next` 목적지 불변 확인**

Run:
```bash
node -e "
const fs=require('fs');
const s=fs.readFileSync('index.html','utf8');
const re=/\"text\":\"한쪽이든 양쪽이든, 팔이 많이 제한되고 찝혀요\",\"next\":\"(cause:cause-dp)\"/g;
console.log('matches with correct next:', (s.match(re)||[]).length);
"
```
Expected: `matches with correct next: 8`

- [ ] **Step 5: 브라우저 수동 확인**

7개 동작 중 아무 동작이나 골라 어깨 → 통증 없음 → Lumbar Lock pass → Apley's Scratch 질문에서 첫 선택지 문구가 "한쪽이든 양쪽이든..."으로 바뀌었는지 확인.

- [ ] **Step 6: 커밋**

```bash
git add index.html
git commit -m "fix: Apley's Scratch 질문 편측 편향 문구 수정 — 양측 찝힘도 포함하도록 7곳 일괄 수정

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>"
```

---

## Task 4: 최종 회귀 확인

**Files:** 없음 (검증만)

- [ ] **Step 1: 전체 JSON 구조 파싱 가능 여부 최종 확인**

Run:
```bash
node -e "
const fs=require('fs');
const s=fs.readFileSync('index.html','utf8');
console.log('file size:', s.length);
console.log('q-shoulder-scratch:', (s.match(/\"id\":\"q-shoulder-scratch\"/g)||[]).length);
console.log('test-shoulder-ext:', (s.match(/\"id\":\"test-shoulder-ext\"/g)||[]).length);
console.log('old biased text:', (s.match(/한쪽 팔이 많이 제한되고 찝혀요/g)||[]).length);
"
```
Expected: `q-shoulder-scratch: 1`, `test-shoulder-ext: 0`, `old biased text: 0`

- [ ] **Step 2: 브라우저 전체 스모크 테스트**

`index.html`을 열고 7개 동작 각각 어깨 pain_site를 통증 있음/없음 양쪽 경로로 한 번씩 끝까지 진행해 에러 없이 원인(cause) 화면까지 도달하는지 확인. (키핑은 반드시 새 질문 경로 포함해서 확인.)

- [ ] **Step 3: HANDOFF 대기 목록에서 #16 완료 처리 필요 시 다음 세션에 반영**

이번 작업 완료 후 `docs/HANDOFF.md` 작성 시 task #16을 완료 목록으로 옮긴다 (지금 당장 할 필요는 없음 — `/handoff` 시점에 처리).
