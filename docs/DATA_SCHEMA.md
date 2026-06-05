# 데이터 입력 가이드

재활 가이드 JSON 데이터를 작성하는 사람이 읽는 문서입니다.

---

## 파일 위치

```
data/movements/
  manifest.json         ← 전체 동작 목록 (여기도 추가 필요)
  squat.json
  lunge.json
  deadlift.json
  pullup.json
  kipping.json
  press-vertical.json
  press-horizontal.json
  row.json
```

동작 하나 = 파일 하나. 새 동작 추가 시 `manifest.json`에도 등록해야 합니다.

---

## 통증 부위 ID 목록

pain_site의 `id` 값은 반드시 아래 목록에서만 사용하세요.  
**임의로 만들면 앱이 인식하지 못합니다.**

### 무릎
| id | 화면 표시 이름 | 설명 |
|---|---|---|
| `knee-front` | 무릎 앞쪽 | 슬개골·슬개건 주변 |
| `knee-lateral` | 무릎 바깥쪽 | IT밴드·외측 반월판 |
| `knee-medial` | 무릎 안쪽 | 내측 측부인대·내측 반월판 |
| `knee-behind` | 무릎 뒤쪽 | 오금·슬와부 |

### 허리
| id | 화면 표시 이름 | 설명 |
|---|---|---|
| `lower-back-bilateral` | 허리 양쪽 | 척추기립근 |
| `lower-back-center` | 허리 중앙 | 극돌기 주변 |
| `lower-back-si` | 허리-엉덩이 경계 | 천장관절(SI joint) |

### 발목
| id | 화면 표시 이름 | 설명 |
|---|---|---|
| `ankle-front` | 발목 앞쪽 | 전방 충돌, 배측굴곡 시 통증 |
| `ankle-behind` | 발목 뒤쪽·아킬레스 | 아킬레스건, 후방 충돌 |
| `ankle-lateral` | 발목 바깥쪽 | 외측 인대, 접질림 후유증 |

### 어깨
| id | 화면 표시 이름 | 설명 |
|---|---|---|
| `shoulder-front` | 어깨 앞쪽 | 이두 장두건, 전방 관절낭 |
| `shoulder-top` | 어깨 위쪽 | AC관절, 상부 충돌증후군 |
| `shoulder-back` | 어깨 뒤쪽 | 후방 관절낭, 회전근개 |
| `shoulder-lateral` | 어깨 옆쪽 | 삼각근 중부, 외측 충돌 |

### 고관절
| id | 화면 표시 이름 | 설명 |
|---|---|---|
| `hip-front` | 고관절 앞쪽 | 장요근, 서혜부 |
| `hip-lateral` | 고관절 바깥쪽 | 대퇴근막장근, 소둔근 |
| `hip-behind` | 고관절 뒤쪽 | 이상근, 좌골신경 |

### 손목
| id | 화면 표시 이름 | 설명 |
|---|---|---|
| `wrist-back` | 손목 등쪽 | 신근건, 등쪽 인대 |
| `wrist-palm` | 손목 손바닥쪽 | 굴근건, 수근관 |
| `wrist-thumb` | 손목 엄지쪽 | 드퀘르뱅 건초염 |

### 팔꿈치
| id | 화면 표시 이름 | 설명 |
|---|---|---|
| `elbow-lateral` | 팔꿈치 바깥쪽 | 테니스 엘보(외측 상과염) |
| `elbow-medial` | 팔꿈치 안쪽 | 골프 엘보(내측 상과염) |
| `elbow-front` | 팔꿈치 앞쪽 | 이두건, 전방 관절낭 |

### 흉근
| id | 화면 표시 이름 | 설명 |
|---|---|---|
| `chest-upper` | 흉근 상부 | 쇄골 아래, 전방 삼각근 경계 |
| `chest-mid` | 흉근 중부 | 흉골 중간 높이 |
| `chest-sternum` | 흉골 주변 | 흉골·늑연골 접합부 |

---

## JSON 전체 구조

```json
{
  "id": "동작-id",
  "name": "동작 이름(한국어)",
  "pain_sites": [
    {
      "id": "knee-front",
      "name": "무릎 앞쪽",
      "entry_question": "q1",
      "questions": [ ... ],
      "tests": [ ... ],
      "danger": { ... },
      "causes": [ ... ]
    }
  ]
}
```

---

## 각 항목 상세

### questions (감별 질문)

```json
{
  "id": "q1",
  "text": "질문 본문",
  "sub": "보충 설명 (없으면 null)",
  "choices": [
    {
      "id": "c1",
      "text": "선택지 텍스트",
      "next": "q:q2"
    },
    {
      "id": "c2",
      "text": "선택지 텍스트",
      "next": "danger"
    }
  ]
}
```

**next 값 규칙:**

| 값 | 이동 대상 |
|---|---|
| `q:q2` | 같은 pain_site 안의 질문 q2 |
| `test:test-id` | 같은 pain_site 안의 테스트 |
| `cause:cause-a` | 원인 확정 화면 (cause-a로 이동) |
| `danger` | 병원 권유 화면 |

---

### tests (동작 테스트)

```json
{
  "id": "test-id",
  "name": "테스트 이름",
  "purpose": "이 테스트로 무엇을 확인하는지 1~2문장",
  "steps": [
    "1단계 설명",
    "2단계 설명",
    "3단계 설명"
  ],
  "note": "주의사항 (없으면 생략 가능)",
  "video_url": "영상 URL (없으면 생략 가능)",
  "pass_text": "통과 버튼 텍스트",
  "fail_text": "실패 버튼 텍스트",
  "pass_next": "cause:cause-b",
  "fail_next": "cause:cause-a"
}
```

---

### danger (병원 권유)

pain_site마다 하나. 이 pain_site에서 즉시 병원 가야 하는 이유를 씁니다.

```json
{
  "title": "지금 바로 운동을 멈추세요",
  "reason": "왜 위험한지 1~2문장",
  "action": "어느 과 가야 하는지, 방문 전 준비사항"
}
```

---

### causes (원인 및 재활 루트)

```json
{
  "id": "cause-a",
  "label": "원인 A",
  "tag": "짧은 원인 키워드 (예: 족관절 가동성 제한)",
  "name": "원인 전체 이름",
  "description": "왜 이 원인인지 사용자 눈높이 설명 (3~5문장)",
  "priority_note": "다른 원인과 함께 있을 때 우선순위 안내 (없으면 생략)",
  "route": {
    "stages": [
      {
        "id": "stage-1",
        "name": "기초 재활",
        "duration": "1~2주",
        "exercises": [ ... ]
      },
      {
        "id": "stage-2",
        "name": "재평가",
        "type": "reassessment",
        "duration": "통과 시 다음 단계로",
        "checklist": [ ... ],
        "pass_note": "...",
        "fail_note": "..."
      },
      {
        "id": "stage-3",
        "name": "운동 복귀",
        "type": "tips",
        "duration": "꾸준히 유지",
        "tips": [ ... ]
      }
    ]
  }
}
```

**stage type 규칙:**
- 운동 나열 단계: `type` 생략, `exercises` 배열 작성
- 재평가 단계: `type: "reassessment"`, `checklist` + `pass_note` + `fail_note` 작성
- 복귀 단계: `type: "tips"`, `tips` 배열 작성

---

### exercises (운동 항목)

```json
{
  "name": "운동 이름",
  "why": "왜 이 운동인지 1~2문장 (통증 원인 → 이 운동의 효과 순서로)",
  "sets": "횟수·세트 표기 (예: 양측 각 10회 · 3세트)",
  "cue": "핵심 코칭 포인트 1문장",
  "how": [
    "동작 1단계",
    "동작 2단계",
    "동작 3단계"
  ],
  "video_url": "영상 URL (없으면 생략 가능)"
}
```

---

### reassessment checklist

```json
"checklist": [
  "해당 동작을 통증 없이 전 구간 수행할 수 있다",
  "가동 범위가 건측(반대쪽)과 동일하거나 더 나온다",
  "운동 후 24시간 내 통증이 악화되지 않는다"
],
"pass_note": "3가지 모두 해당되면 다음 단계로 이동하세요.",
"fail_note": "하나라도 해당 안 되면 1단계를 반복하세요."
```

체크리스트는 3개 권장. 통증 부위·원인에 맞게 내용 수정 가능.

---

### tips (운동 복귀 팁)

```json
"tips": [
  {
    "title": "팁 제목 (10자 이내)",
    "body": "팁 본문 2~3문장"
  }
]
```

팁은 4개 권장. 순서: WOD 전 준비 → 주의 신호 → 이 신호 오면 멈추세요 → 재발 방지 핵심.

---

## manifest.json 등록 방법

새 pain_site 추가 시 `manifest.json`에도 반드시 추가해야 합니다.

```json
{
  "id": "squat",
  "name": "스쿼트",
  "pain_sites": [
    { "id": "knee-front", "name": "무릎 앞쪽" },
    { "id": "knee-lateral", "name": "무릎 바깥쪽" }
  ]
}
```

---

## 최소 작성 예시 (knee-front × squat)

실제 내용은 비워두고 구조만 보여주는 뼈대입니다.

```json
{
  "id": "knee-front",
  "name": "무릎 앞쪽",
  "entry_question": "q1",
  "questions": [
    {
      "id": "q1",
      "text": "첫 번째 질문",
      "sub": null,
      "choices": [
        { "id": "c1", "text": "선택지 A", "next": "test:test-1" },
        { "id": "c2", "text": "선택지 B", "next": "danger" }
      ]
    }
  ],
  "tests": [
    {
      "id": "test-1",
      "name": "테스트 이름",
      "purpose": "테스트 목적",
      "steps": ["1단계", "2단계"],
      "pass_text": "통과 텍스트",
      "fail_text": "실패 텍스트",
      "pass_next": "cause:cause-b",
      "fail_next": "cause:cause-a"
    }
  ],
  "danger": {
    "title": "지금 바로 운동을 멈추세요",
    "reason": "위험 이유",
    "action": "병원 안내"
  },
  "causes": [
    {
      "id": "cause-a",
      "label": "원인 A",
      "tag": "원인 키워드",
      "name": "원인 전체 이름",
      "description": "원인 설명",
      "route": {
        "stages": [
          {
            "id": "stage-1",
            "name": "기초 재활",
            "duration": "1~2주",
            "exercises": [
              {
                "name": "운동 이름",
                "why": "왜 이 운동인지",
                "sets": "10회 · 3세트",
                "cue": "핵심 포인트",
                "how": ["1단계", "2단계", "3단계"]
              }
            ]
          },
          {
            "id": "stage-2",
            "name": "재평가",
            "type": "reassessment",
            "duration": "통과 시 다음 단계로",
            "checklist": [
              "기준 1",
              "기준 2",
              "기준 3"
            ],
            "pass_note": "3가지 모두 해당되면 다음 단계로 이동하세요.",
            "fail_note": "하나라도 해당 안 되면 1단계를 반복하세요."
          },
          {
            "id": "stage-3",
            "name": "운동 복귀",
            "type": "tips",
            "duration": "꾸준히 유지",
            "tips": [
              { "title": "팁 제목", "body": "팁 본문" }
            ]
          }
        ]
      }
    }
  ]
}
```
