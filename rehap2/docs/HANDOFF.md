# HANDOFF - 2026-06-04 17:30

## 완료
- phase_q 감별 질문 전체 35개 pain site에 추가 (3a71a30)
  - "운동 시작하자마자" → Phase A / "어느 정도 반복한 후" → Phase B / "쉬는 중에도" → danger
  - timing형 q1 12개 제거 (phase_q로 통합), q1 내 중복 danger 선택지 16개 제거
- coming_soon 화면 진입 차단 제거 — 데드리프트 등 접근 가능 (3a71a30)
- phase 저장 키 `movementId-painSiteId-causeId` 조합으로 변경 (5be2d59)
  - 기존 `_default` 단독 키 → 여러 부위 동시 재활 시 충돌 문제 수정
  - _pending 임시 저장 → cause 확정 시 정식 키로 이동
- session_feedback 진행바 퍼센트(95%)·라벨("재활 루트") 추가 (98bed71)
- Phase B 업그레이드 모달 트리거 연결 (편함 2회 연속 + Phase A → 팝업)

## 진행중
- 없음

## 대기
- BUNDLED 운동 데이터에 phase 필드 추가 (어떤 운동이 A/B인지 사용자가 결정 필요)
  - 코드(필터링)는 준비됨, 데이터만 없는 상태
- 대체 WOD "시작하기" 버튼 실제 기능 연결
- 다른 cause들 실제 운동 데이터 추가 (squat/knee 외 대부분 비어있음)
- 카카오·구글 OAuth 백엔드 연동
- 실제 운동 영상 URL 입력

## 결정사항 / 주의
- 앱은 index.html 안의 BUNDLED 데이터를 사용. rehab.json은 사용 안 함
- 배포 구조: rehap2(작업) → Copy-Item → rehap1/index.html + 루트 index.html → git push
- phase_q는 BUNDLED에 entry_question으로 추가됨. 기존 q1은 유지 (단, timing형 12개는 제거)
- phase 키: `${movementId}-${painSiteId}-${causeId}` (예: squat-knee-cause-b)
- BUNDLED 운동에 phase 필드 없으면 필터링 코드가 전부 통과시킴 (모든 운동 노출) → 의도된 임시 상태
- 재활 단계: 기초재활→재평가→운동복귀 3단계 (BUNDLED 기준)
- 회복테스트 버튼은 기초재활 단계면 항상 활성화 (조건 없음), 넛지 텍스트만 조건부

## 다음 세션 권장 첫 프롬프트
`/resume`
