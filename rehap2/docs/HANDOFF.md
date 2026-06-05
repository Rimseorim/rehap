# HANDOFF - 2026-06-05 15:30

## 완료
- recovery_test() null 가드 추가 — 테스트 데이터 없을 때 조용히 죽던 버그 수정 (`rehap2/index.html`)
- rehap2/Procfile 생성 (배포용)
- 루트 구버전 파일 삭제 (backend/, data/, index.html, rehab.db)

## 진행중
- rehap2 → 루트 구조 통합 작업
  - 중단 지점: 루트 구버전 파일 삭제 완료, rehap1 폴더 삭제 미완료 (프로세스 점유)
  - 다음 스텝: rehap1 수동 삭제 후 → rehap2 파일들 01.test 루트로 이동 → Claude Code 루트에서 재시작

## 대기
- BUNDLED 운동 데이터에 phase 필드 추가 (어떤 운동이 A/B인지 결정 필요)
- 대체 WOD "시작하기" 버튼 실제 기능 연결
- 다른 cause들 실제 운동 데이터 추가 (squat/knee 외 대부분 비어있음)
- 카카오·구글 OAuth 백엔드 연동
- 실제 운동 영상 URL 입력

## 결정사항 / 주의
- rehap1 = 폐기 예정, git 미추적 상태, 삭제해도 무방
- 앱은 rehap2/index.html의 BUNDLED 데이터 사용. data/rehab.json 미사용
- 배포 구조 변경 중: rehap2(작업) → 루트로 통합 → git push
- recovery_test 체인 구조 (elbow 등): retestMode에서 pass_next 무시하고 outcome만 처리 (의도된 동작)
- GitHub remote: https://github.com/Rimseorim/rahap1.git

## 다음 세션 권장 첫 프롬프트
`/resume` — rehap1 수동 삭제 후 rehap2 파일들 루트로 이동 완료했는지 확인부터
