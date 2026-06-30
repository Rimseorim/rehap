# HANDOFF - 2026-06-30

## 완료

- cause-case3 (후방 관절낭·회전근개 경직, 내회전·수평 내전 제한, 가동성 부족형) Phase A+B — **8동작 전부 완료**
  - back-squat ✓ (25fcb21)
  - deadlift ✓ (dc35bf9)
  - pullup ✓ (e2dd7c1)
  - kipping ✓ (03d75f5)
  - row ✓ (2780643)
  - vertical-press ✓ (bcbc920)
  - horizontal-press ✓ (5421145)
  - lunge — 이전 세션에서 완료 여부 불명확, data/phase-exercises.json에서 확인 필요
- origin/main push 완료 (5421145)

## 진행중

없음

## 대기

- **lunge/shoulder/cause-case3**: data/phase-exercises.json 확인 후 미완료 시 작성
- **cause-case4 (전거근·하부 승모근 약화, 근력 부족형)**: 8동작 전부
- **cause-d (특이소견 없음)**: 8동작 전부

## 결정사항 / 주의

- 설계안 채팅 포맷: 운동마다 `**출처** / **target** / **why** / **sets** / **cue** / **how**` 전부 상세하게. Phase B는 `**탈출 경로** / **progression_note**` 추가
- 출처 필수 명시: txt(어깨 재활 프로그램.txt) / 어깨 DB / 흉근 DB / 웹서치 / 모델 지식
- 토론(debate.py)은 사용자가 명시적으로 요청할 때만 실행. 기본 흐름 = 설계안 채팅 → 피드백 → 스크립트
- 반박 없으면 반박이 없는 이유도 설명
- cause-case3 Phase B 무게 기준: 30~40% (가동성 부족형)
- 세이프티 바 가이드: 바벨 벤치 3~4단계는 반드시 인라인으로 세이프티 바 세팅 명시

## 다음 세션 권장 첫 프롬프트: /resume
