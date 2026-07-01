# HANDOFF - 2026-07-01

## 완료

- cause-dp Phase A (7동작 공통) ✓
- cause-case1 Phase A+B: 7동작 ✓
- cause-case2 Phase A+B: 7동작 ✓
- cause-case3 Phase A+B: 7동작 ✓ (런지는 shoulder pain_site 없음 — 정상)
- cause-case4 Phase A+B: 7동작 ✓
  - back-squat (06e6125), deadlift (b8057a3), pullup (136f67c), kipping (bee076c), row (5335612), vertical-press (9774b89), horizontal-press (00e3912)
- origin/main push 완료 (00e3912)

## 진행중

없음

## 대기

- **cause-d (특이소견 없음)**: 7동작 전체 — 다음 작업
  - 특이소견없음형 프레임워크: 무부하 패턴 → 가동범위/지지 → 부하 → 도구+무게
  - 각 동작마다: 웹서치 → 설계안 채팅 → 피드백 → 스크립트 → 커밋

## 결정사항 / 주의

- 설계안 채팅 포맷: 운동마다 `**출처** / **target** / **why** / **sets** / **cue** / **how**` 전부 상세하게. Phase B는 `**탈출 경로** / **progression_note**` 추가
- 출처 필수 명시: txt(어깨 재활 프로그램.txt) / 어깨 DB / 흉근 DB / 웹서치 / 모델 지식
- 반박 없으면 반박이 없는 이유도 설명
- Phase B 감각 기준 순서: 기본은 "전면 말림 → 날개뼈 겉돎". 동작별 예외 시 progression_note에 역학적 이유 명시 필수
- 세이프티 바 가이드: 바벨 벤치/스쿼트 3~4단계는 반드시 인라인으로 세이프티 바 세팅 명시
- 런지는 shoulder pain_site 없음 → cause-d에서도 런지 제외 (6동작)

## 다음 세션 권장 첫 프롬프트: /resume
