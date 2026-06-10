# HANDOFF - 2026-06-09 00:00

## 완료
- `feat: 전문용어 ? 토글 기능 추가` (7db6d5a) — BUNDLED.glossary 추가, glossaryToggle() 구현, cause/route 화면 적용
- `refactor: 본문 괄호 설명 제거` (9aac89b) — 용어집 중복 인라인 풀이 55건 제거
- `feat: glossary 15개 추가` (bb7a3f1) — TFL·대퇴직근·거골·비복근·가자미근·FAI·TFCC·valgus 등
- `feat: PAILs·RAILs·패킹 glossary 추가` (b96d7af) — 아치(arch)/팩킹 표기 통일
- `fix: 본문 치환 164건 정상 적용` (56ed0ea) — 건측→통증 없는 쪽, 슬관절→무릎관절, 쏠림현상 등
- glossary 최종 42개, 전체 괄호 설명 300+건 정리 완료
- GitHub push 완료 (main), Railway 자동 배포 트리거됨

## 진행중
- 없음

## 대기
- Railway 배포 완료 후 앱에서 ? 토글 동작 실제 확인

## 결정사항 / 주의
- 룸바락(Lumbar Lock), RDL, 코젠·토마스 테스트 — 텍스트 그대로 유지
- 전방경사·광배근·소흉근, 요추·흉추·견갑골·슬개골·족관절 — glossary 미추가 확정
- 브레이싱→복압 통일. 단, 운동 이름 "복압 브레이싱 연습"은 유지
- valgus 텍스트 → 쏠림현상 치환, glossary 키 valgus는 유지
- Python 스크립트 주의: 텍스트 치환은 반드시 data 딕셔너리 내부 재귀 치환 후 json.dumps 할 것 (lines[3] 직접 치환 후 재직렬화하면 덮어씌워지는 버그 발생)

## 다음 세션 권장 첫 프롬프트
`/resume` — Railway 배포 확인 후 앱 QA 또는 다음 기능 작업
