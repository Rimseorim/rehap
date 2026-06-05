# HANDOFF - 2026-06-05 18:00

## 완료
- Railway 연결 복구 (레포명 rahap1 → rehap 변경, main 브랜치 자동배포 연결)
- rehap1/rehap2 폴더 삭제, 루트 구조로 통합 (bb6cc78)
- CLAUDE.md 프로젝트 구조·배포 정보 업데이트
- `selectRetestResult()` 분리 — retestMode 플래그 이중역할 제거
- `go('x')` → named nav 함수(`goToX()`) 전체 교체 (a899651)
- `docs/SCREENS.md` 화면 전환 지도 작성 (16개 화면, 흐름도, 버튼 목록)

## 진행중
- 화면별 버튼·질문 검수 작업
  - 중단 지점: 감별 흐름(로그인→재활탭→통증부위→스쿼트×무릎) 까지 확인
  - 원인 화면에서 "기록 저장에 실패했습니다" 토스트 발생 (데모모드라 예상된 동작, 무시 가능)
  - 다음 스텝: route → session_feedback → complete → recovery_test 순서로 이어서 확인

## 대기
- BUNDLED 운동 데이터 phase 필드 추가 (어떤 운동이 A/B인지 결정 필요)
- 대체 WOD "시작하기" 버튼 실제 기능 연결
- 카카오·구글·네이버 OAuth 백엔드 연동
- 실제 운동 영상 URL 입력
- Playwright 브라우저 검수 마무리 (node_modules 생성됨, .gitignore 추가 필요)

## 결정사항 / 주의
- 앱 데이터: `index.html` 내부 BUNDLED 데이터 사용. `data/rehab.json` 미사용
- 배포: Railway `motivated-prosperity` → `github.com/Rimseorim/rehap` main 푸시 시 자동배포
- 배포 URL: `web-production-28002.up.railway.app`
- `node_modules/`, `package.json`, `package-lock.json` 생성됨 (playwright 설치) → .gitignore에 추가 필요
- recovery_test 화면: retestMode 여부로 버튼 핸들러 분리 완료 (selectRetestResult / selectTestResult)
- 상태폭발 리팩터: 지금 당장 화면 병합 불필요. 동작 추가 후 패턴 보이면 그때 진행

## 다음 세션 권장 첫 프롬프트
`/resume` — node_modules .gitignore 추가 후 route~complete~recovery 화면 버튼 검수 이어서
