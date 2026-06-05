# 화면 전환 지도

앱의 모든 화면과 버튼이 어디로 연결되는지 정리한 문서.
새 기능 추가 또는 협업 시 이 문서를 먼저 확인할 것.

---

## 화면 목록

| 화면 ID | 한글 이름 | 로그인 필요 | 설명 |
|---|---|---|---|
| `home` | 홈 | ✓ | 다이어리·기록 탭 |
| `login` | 로그인 | - | 이메일/비밀번호 |
| `signup` | 회원가입 | - | 이메일/비밀번호/닉네임 |
| `pain_site` | 통증 부위 선택 | ✓ | 어깨·무릎·허리 등 |
| `movement` | 동작 선택 | ✓ | 스쿼트·데드리프트 등 |
| `question` | 감별 질문 | ✓ | 트리 분기 질문 (루프 가능) |
| `test` | 직접 테스트 | ✓ | 동작 테스트 (루프 가능) |
| `cause` | 원인 확인 | ✓ | 감별 결과 + 재활 루트 진입 |
| `route` | 재활 루트 | ✓ | 단계별 운동 목록 |
| `session_feedback` | 세션 피드백 | ✓ | 쉬웠나/힘들었나 (stageIndex=0 완료 후) |
| `complete` | 단계 완료 | ✓ | 현재 단계 완료 화면 |
| `recovery_test` | 회복 테스트 | ✓ | 기초재활 완료 후 동작 재테스트 |
| `recovery_complete` | 회복 완료 | ✓ | 테스트 통과 축하 화면 |
| `danger` | 위험 신호 | - | 병원 방문 권유 |
| `my_records` | 내 기록 | ✓ | 운동 기록 목록 |
| `coming_soon` | 준비 중 | - | 미구현 동작 안내 |

---

## 화면 전환 흐름

```
[랜딩/비로그인]
  └─ "시작하기" → login
      ├─ 로그인 성공 → home
      └─ "회원가입" → signup → home

[감별 흐름] ── 원인을 찾는 과정
home
  └─ "지금 시작하기" → pain_site
      └─ 통증 부위 선택(selectPainSite) → movement
          └─ 동작 선택(selectMovement) → question
              └─ selectChoice(next)
                  ├─ next="danger"      → danger → home
                  ├─ next="q:xxx"       → question (루프)
                  ├─ next="test:xxx"    → test
                  │     └─ selectTestResult(next)
                  │           ├─ cause:xxx → cause
                  │           ├─ test:xxx  → test (루프)
                  │           └─ danger    → danger
                  └─ next="cause:xxx"   → cause

[재활 흐름] ── 원인 확정 후 운동하는 과정
cause
  └─ "재활 루트 보기" → route
      └─ 운동 체크 후 nextStage()
          ├─ stageIndex=0 → session_feedback → complete
          └─ stageIndex>0 → complete
              ├─ "다음 단계" → goNextStageFromComplete → route
              ├─ "이 단계 다시" → route
              └─ "회복 테스트" → goRetest → recovery_test
                    └─ selectRetestResult(outcome)
                          ├─ pass → stageIndex++ → recovery_complete → route
                          └─ fail → stageIndex=0  → route
```

---

## 뒤로가기(BACK_MAP)

```js
pain_site        ← home
movement         ← pain_site
question         ← movement
test             ← question
cause            ← test (testId 있을 때) / question (없을 때)
route            ← cause
complete         ← route
session_feedback ← route
recovery_test    ← complete
recovery_complete← recovery_test
danger           ← home
coming_soon      ← movement
```

---

## 화면 이동 함수 (index.html)

버튼 onclick에서 `go('screen')` 대신 아래 함수를 사용.
어디로 가는지 이름만 보고 바로 알 수 있도록.

```js
goHome()               // → home
goToLogin()            // → login
goToSignup()           // → signup
goToPainSite()         // → pain_site
goToMovement()         // → movement
goToQuestion()         // → question
goToTest()             // → test
goToCause()            // → cause
goToRoute()            // → route
goToComplete()         // → complete
goToSessionFeedback()  // → session_feedback
goToRecoveryTest()     // → recovery_test
goToRecoveryComplete() // → recovery_complete
goToDanger()           // → danger
goToMyRecords()        // → my_records
goToComingSoon()       // → coming_soon
```

---

## 새 화면/버튼 추가 시 체크리스트

1. 위 화면 목록에 추가
2. 흐름도에 진입/탈출 경로 표기
3. BACK_MAP에 뒤로가기 경로 추가 (`index.html:BACK_MAP`)
4. `goToXxx()` nav 함수 추가 (`index.html:goHome 블록`)
5. 로그인 필요 여부 확인 (`publicScreens` 배열)
