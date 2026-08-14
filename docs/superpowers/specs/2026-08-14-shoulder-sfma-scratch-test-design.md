# 어깨 SFMA 상지패턴 자가측정 검사 도입 (task #16)

## 배경 / 문제

어깨 감별 흐름에는 두 개의 경로가 있다.

- **통증 없음(동작만 안 됨) 경로** (`q1`→`q3` Lumbar Lock→`q4` Apley's Scratch): 이미 SFMA 상지패턴을 랜드마크 기반 자가측정(각도계 불필요)으로 잘 구현하고 있다.
- **통증 있음 경로**: 5개 동작(로우·풀업·키핑·수평프레스·수직프레스) 모두 `flex`/`arc` 다음 2번째 검사가 동작마다 다르다 — 실제 데이터 확인 결과 각자 그 동작에 특이적인 근력·부하 검사를 쓰고 있다.

  | 동작 | 통증경로 2단계 검사 | fail → |
  |---|---|---|
  | 로우 | `test-shoulder-h-abd` (수평외전 저항) | `cause-dp` |
  | 풀업 | `test-shoulder-hang` (데드행 부하) | `cause-dp` |
  | **키핑** | **`test-shoulder-ext`** (후방 신전, 통증 유무만 확인) | **`cause-case3`** |
  | 수평프레스 | `test-shoulder-h-add` (수평내전 저항) | `cause-dp` |
  | 수직프레스 | `test-shoulder-empty-can` (극상근 저항) | `cause-dp` |

  이 중 **키핑의 `test-shoulder-ext`만** 모호하다 — 신전 시 통증 여부만 볼 뿐 랜드마크·좌우비교가 없는데도 `cause-case3`(후방 관절낭·회전근개 경직 — 내회전 제한)로 라우팅된다. 나머지 4개는 각자 근거 있는 저항/부하 검사라 이번 범위에서 제외.

- 5개 동작 모두 어깨 **외회전(ER)을 재는 검사는 통증 경로에 전혀 없다** — 이 공백은 키핑의 `test-shoulder-ext`를 교체하는 것으로 채운다 (나머지 4개 동작은 이번 범위 밖이므로 ER 공백이 남지만, 각자 다른 근거 있는 검사를 이미 쓰고 있어 별도 task로 논의).

## 목표

- 통증 경로에 외회전 검사를 추가한다.
- `test-shoulder-ext`를 랜드마크 기반의 명확한 검사로 교체한다.
- 새 검사를 새로 발명하지 않고, 이미 앱에 있고 검증된 **Apley's Scratch 검사**(q4) 문구·판정 기준을 통증 경로에 그대로 이식해 재사용한다. 외회전(위로 넘긴 팔)과 내회전(아래로 돌린 팔)을 한 검사로 동시에 측정하므로 검사 1개 추가로 ER 신설 + ext 교체를 함께 해결한다.

## 변경 대상

**키핑(`kipping`) 1개 동작만** — 어깨 `pain_sites` 내 통증 경로 `tests` 배열 수정. (`test-shoulder-ext`는 전체 파일에 정의가 1곳뿐이고, 참조하는 곳도 키핑의 `test-shoulder-flex.pass_next` 1곳뿐임을 스크립트로 확인함.)

```
변경 전: test-shoulder-flex → test-shoulder-ext(test 노드) → test-shoulder-core
변경 후: test-shoulder-flex → q-shoulder-scratch(question 노드, 신규) → cause-dp / cause-case3 / test-shoulder-core
```

`test-shoulder-ext` 노드는 삭제하고 `q-shoulder-scratch`로 교체한다.

## 신규 노드: `q-shoulder-scratch` (question 노드, test 노드 아님)

3분기 라우팅이 필요하므로 `test` 노드(pass/fail 2분기 스키마)가 아니라, `q3`/`q4`와 동일한 **`question` 노드 형식(`choices` 배열)**으로 만든다. `test-shoulder-flex`의 `pass_next`가 `"q:q-shoulder-scratch"`를 가리키도록 바꾼다 (기존엔 `"test:test-shoulder-ext"`).

| 필드 | 내용 |
|---|---|
| id | `q-shoulder-scratch` |
| text | Apley's Scratch 검사: 한 손은 어깨 뒤로 위에서 아래로, 반대 손은 허리 뒤로 아래에서 위로 뻗어 등 뒤에서 가까이 할 때 어떤가요? |
| sub | 거울 앞에서 양쪽 다 해보고 비교하세요. 찝히거나 날카롭게 아프면 충돌증후군일 수 있습니다. |
| choices (3개, q4 문구 재사용) | 아래 참고 |

### 분기 로직 (3-way, q4 문구 재사용)

| 선택지 | 판정 | 다음 |
|---|---|---|
| 한쪽이든 양쪽이든, 팔이 많이 제한되고 찝혀요 | 충돌증후군 의심 | `cause:cause-dp` |
| 팔 범위는 어느 정도 되지만 한쪽이 훨씬 뻑뻑해요 | 후방 관절낭·회전근개 경직 | `cause:cause-case3` (기존 `test-shoulder-ext`의 fail 목적지 유지) |
| 대칭으로 잘 돼요 (통증 원인은 다른 곳) | 회전 가동성은 정상, 탐색 계속 | `test:test-shoulder-core` (기존 pass_next 유지) |

이렇게 하면 no-pain 경로 q4와 문구가 완전히 동일해져, 사용자가 두 경로 중 어디로 왔든 같은 검사 방식·같은 판정 기준을 겪게 된다 (일관성).

### 부가 수정: q4 편측 편향 문구 수정 (기존 no-pain 경로)

리뷰 중 발견: 첫 번째 선택지 "한쪽 팔이 많이 제한되고 찝혀요"가 편측만 전제하고 있어 **양쪽 다 찝히는 경우 답할 선택지가 없다**. 목적지(`cause-dp`)는 편측이든 양측이든 동일(오버헤드 중단·보호 우선 처방이 같음)하므로 문구만 포괄적으로 수정한다.

```
변경 전: "한쪽 팔이 많이 제한되고 찝혀요"
변경 후: "한쪽이든 양쪽이든, 팔이 많이 제한되고 찝혀요"
```

`next`(목적지)는 변경 없음, `text`만 수정. 신규 `q-shoulder-scratch`가 이 문구를 그대로 재사용하므로, **기존 `q4`도 동일하게 수정**해 두 경로 간 문구를 계속 일치시킨다.

대상: `q4`가 존재하는 5개 동작(로우·풀업·키핑·수평프레스·수직프레스) 전부 — BUNDLED JSON 내 중복 정의된 5곳 모두 수정 필요.

## 영향 없음 / 명시적 제외

- `test-shoulder-flex`: 변경 없음 (기존 근거로 충분, 키핑 포함 전 동작).
- 로우·풀업·수평프레스·수직프레스의 통증경로 2단계 검사(`h-abd`/`hang`/`h-add`/`empty-can`): 각자 근거 있는 별개 검사라 이번 범위 밖.
- no-pain 경로(`q3`/`q4`의 구조 자체): 이미 잘 되어 있어 변경 없음. `q4` 선택지 텍스트 1줄만 수정(아래).

## 검증 계획

- 키핑의 BUNDLED JSON에서 `test-shoulder-flex.pass_next`가 `"q:q-shoulder-scratch"`로, `test-shoulder-ext` 노드 자체가 삭제됐는지 확인.
- `test-shoulder-ext`가 전체 파일에서 더 이상 참조되지 않는지 확인(삭제 전 최종 재확인).
- 브라우저에서 키핑 통증 경로 진입 → 새 질문 표시 → 3분기 라우팅(`cause-dp`/`cause-case3`/`test-shoulder-core`) 확인.
- 5개 동작(로우·풀업·키핑·수평프레스·수직프레스) `q4`의 첫 선택지 문구가 모두 "한쪽이든 양쪽이든..."으로 수정됐는지, `next` 목적지는 그대로인지 확인.
