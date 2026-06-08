# 전문용어 설명(`?` 토글) 기능 설계

날짜: 2026-06-08

## 배경

운동 카드의 "왜 이 운동인가"(`why`)와 `cause()` 화면의 원인 설명(`description`)에
임상·해부학 전문용어가 섞여 있다 (`why`/`cue` 기준 21종 450회, `cause.description`
기준 17종 다수 등장 — 편심성 22회·굴곡근 19회·요추 11회 등).

CLAUDE.md 핵심 원칙("이유를 붙인다")상 설명 텍스트는 사용자가 이해해야 의미가
있는데, 일부 용어는 크로스핏 취미러도 낯설 수 있다. 그렇다고 본문 자체를 모두
풀어쓰면 ① 문장이 늘어지고 ② 전문성에 대한 신뢰감이 떨어질 수 있다.

→ **본문은 전문용어를 유지하되, `?` 토글을 눌렀을 때만 쉬운 풀이를 보여주는
방식**으로 절충한다. 이미 앱에 있는 `<details>`(방법/왜 이 운동인가 접기) 패턴과
같은 톤 — "기본은 단순하게, 필요한 사람만 펼쳐보게".

## 1. 데이터 구조 — `BUNDLED.glossary`

기존 `BUNDLED` JSON에 최상위 키로 평면 매핑 객체를 추가한다.

```json
"glossary": {
  "등척성": "관절을 움직이지 않고 그 자세 그대로 힘만 주는 동작",
  "편심성": "근육이 늘어나면서 버티는 동작 (예: 천천히 내려가기)",
  "다열근": "허리를 숙였다 펼 때 척추뼈 하나하나를 잡아주는 근육",
  "복횡근": "숨을 내쉴 때 배가 들어가게 만드는, 배 속 깊은 근육"
}
```

- 시작 범위: 기존 검토에서 실제 검출한 27개 용어 (근육·뼈 이름 19 + 동작
  개념어 8 — 부록 참고)
- **용어집 27개 항목의 실제 문구는 별도 콘텐츠 작성/검수 작업**으로 분리한다.
  (예: "복횡근 → 코르셋처럼 배를 감싸는 근육"처럼 비유가 또 다른 전문 이미지를
  부르는 경우가 있어, 구현 단계에서 표현을 한 번 더 다듬어야 한다)
- 데이터 구조 자체는 "용어: 풀이" 평면 문자열 매핑이면 충분하므로, 문구 품질
  이슈는 구조 설계에 영향을 주지 않는다.

## 2. 카드(텍스트)별 용어 자동 감지

수동 태깅 없이, 렌더링 시점에 텍스트와 `glossary` 키를 대조해 등장하는
용어만 추출한다.

```js
function getGlossaryTerms(text) {
  return Object.keys(BUNDLED.glossary).filter(term => text.includes(term));
}
```

- 결과가 빈 배열이면 `?` 토글 자체를 렌더링하지 않는다
  (운동 카드 기준 140장 중 83장, 59%는 토글 없음)
- `glossary`에 새 용어를 추가하기만 하면 모든 화면에 자동 반영 — 별도 매핑
  데이터를 유지·동기화할 필요 없음

## 3. `?` 토글 UI

기존 `<details>` 패턴(`index.html:1655`, `:1666` — "방법"/"왜 이 운동인가")을
그대로 따르되, `summary`만 `?` 아이콘 모양으로 만든 범용 헬퍼로 분리한다.

```js
function glossaryToggle(text) {
  const terms = getGlossaryTerms(text);
  if (!terms.length) return '';
  return `
  <details class="glossary-toggle" style="display:inline-block;margin-left:6px">
    <summary style="list-style:none;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;
      width:22px;height:22px;border-radius:50%;border:1px solid var(--border);
      font-size:12px;font-weight:700;color:var(--text-sub)">?</summary>
    <div style="margin-top:8px;display:flex;flex-direction:column;gap:8px">
      ${terms.map(t => `
        <div>
          <strong style="font-size:var(--t4)">${t}</strong>
          <p style="color:var(--text-sub);font-size:var(--t4);margin-top:2px">${BUNDLED.glossary[t]}</p>
        </div>`).join('')}
    </div>
  </details>`;
}
```

- 위치: 운동 카드는 제목 줄(운동명 옆, 영상 버튼과 나란히)
- 동작 방식: 클릭하면 그 자리에서 펼쳐지고, 다시 클릭하면 접힘 (전체 화면을
  덮는 모달이 아님 — 닫기 버튼·오버레이 같은 별도 UI 요소가 필요 없어 구현이
  단순하고, 기존 `<details>` 톤과 일관됨)
- 한 카드/문단에 용어가 여러 개(최대 3개, 23장에서 발견) 있어도 토글 하나에
  목록으로 모이므로 화면이 물음표로 어지러워지지 않음

## 4. 확장성 — 다른 화면에서 재사용

`getGlossaryTerms`/`glossaryToggle`을 운동 카드 전용으로 만들지 않고 **임의의
텍스트를 받는 범용 함수**로 설계한다. 적용 지점은 호출 한 줄만 추가하면 된다.

| 화면/필드 | 호출 |
|---|---|
| 운동 카드 (`route()`) | `glossaryToggle(ex.why + ' ' + ex.cue)` |
| 원인 설명 (`cause()`) | `glossaryToggle(c.description)` |
| 팁 단계 (`stage.tips`) | `glossaryToggle(tip.body)` |

`cause.description`(원래 "사용자 눈높이 설명"으로 정의된 필드)에도 전문용어
17종이 다수 등장하는 것을 확인했다 (편심성 22회·굴곡근 19회·요추 11회 등) —
오히려 사용자가 원인을 처음 마주하는 화면이라 여기서의 효용이 더 클 수 있다.

→ **1차 적용 범위: 운동 카드 + `cause()` 화면.** 이후 `glossary`에 용어만
추가하면 다른 화면(`tips` 등)도 같은 함수로 바로 확장 가능.

## 부록 — 1차 용어집 후보 (27종, 실제 검출 기준)

검토 과정에서 `why`/`cue`/`description`에 실제로 등장하는 것을 확인한
임상·해부 용어 목록 (`includes` 매칭 검출 결과). 실제 풀이 문구는 구현
단계에서 별도로 다듬는다 (1번 섹션 참고).

**근육·뼈·구조물명** (19종): 요추·흉추·견갑골·슬개골·족관절·천장관절·
전거근·회전근개·신전근·장요근·굴곡근·외전근·관절낭·다열근·복횡근·
중둔근·대둔근·소둔근·이상근

**동작·개념·진단명** (8종): 등척성·편심성·건병증·충돌증후군·가동범위·
배측굴곡·슬개대퇴·회외

## 범위 밖 (이번 설계에서 다루지 않음)

- `glossary` 27개 항목의 실제 문구 작성/검수 (별도 콘텐츠 작업)
- 용어 자동 감지의 형태소 변형 대응(예: "굴곡근"이 "굴곡근들" 형태로 등장하는
  경우) — 현재 데이터 표본에서는 발견되지 않아 단순 `includes` 매칭으로 충분
