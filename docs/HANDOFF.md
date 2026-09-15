# HANDOFF - 2026-09-15 00:00

## 완료
- danger(병원 권유) 화면 도달 시 `localStorage` 진행상태 삭제하도록 수정 (`c83be8b`) — 재진입 시 홈으로 복귀, 이전엔 화면 안 끄고 나가면 재진입 시 danger 화면이 그대로 다시 뜨는 문제였음
- 자동 이어하기(`init()`의 `loadProgress()`) 동작 방식 재점검 — danger 제외 나머지 구간(감별 도중)은 현행 자동복원 유지로 결론
- "내 기록" 화면은 원인 확정(`S.screen === 'cause'`) 이후 기록만 노출됨을 코드로 확인 (`index.html:919`, `saveRehabRecord`)
- `backend/routers/auth.py`의 `FRONTEND_URL` 오타 발견 및 수정 (`/health` → `/rehap`, 미커밋 상태) — 네이버 로그인 콜백 리다이렉트 경로 버그

## 진행중
- **백엔드(Railway) 실제 가동 준비** — 사용자가 "기록보기 등이 설정되게 하자"고 요청
  - 중단 지점: `backend/routers/auth.py:14` FRONTEND_URL 수정만 하고 커밋 여부 확인 중 `/easy`·`/handoff`로 흐름 전환됨
  - 다음 스텝: FRONTEND_URL 수정 커밋 여부 확정 → Railway 대시보드에서 `NAVER_CLIENT_ID`/`NAVER_CLIENT_SECRET` 환경변수 설정 여부 확인 → 서비스 재시작(재배포)은 사용자가 직접 해야 함(Claude는 Railway 접근 권한/CLI 없음) → 재시작 후 `web-production-28002.up.railway.app/` 헬스체크로 확인

## 대기
- **PT/전문의 임상 검수** — 유일한 진짜 배포 블로커, 사용자가 검수용 아티팩트 공유 예정
- **SQLite 영속성 문제** — `backend/database.py:4`, Railway는 재배포마다 파일시스템 초기화되어 `rehab.db` 기록이 날아감. 실제 기록보기 기능을 오래 쓰려면 볼륨 마운트 또는 PostgreSQL 전환 필요 (아직 미결정)
- 이용약관/개인정보처리방침 문서화 — 로그인 이관 확정 전까진 갭으로 취급
- 카카오/구글 로그인 실연동 — 우선순위 낮음/보류
- `saveProgress()`가 시작 시점 언제/왜 추가됐는지 근거 불명 — 2026-05-04 대량 커밋(`c4b538d`)에서 처음 등장, 그 이전 세션 기록 없어 추적 불가로 결론(현재는 기능 유지하기로 확정, danger만 예외 처리 완료)

## 결정사항 / 주의
- **로그인 기능 방향 재확인 필요**: `[[project_login_deprioritized]]` 메모(8/29)엔 "로그인은 다른 앱으로 이관, 이 앱엔 불필요"로 돼 있었으나, 이번 세션에서 사용자가 "데모 살리고 기록보기 설정하자"로 요청 — 데모는 유지, 로그인(네이버)/기록 API는 실제로 켜는 방향. 카카오·구글 로그인은 여전히 스텁 상태로 두는지는 미확인, 다음 세션에서 재확인 필요.
- danger 화면 자동복원 이슈는 이번 세션에서 완전히 해결됨(재판단 불필요) — `saveProgress()`에서 danger 진입 시 `localStorage.removeItem` 처리.
- Railway 서비스 시작/환경변수 설정은 Claude가 직접 못 함 — 매 세션 이 사실 재확인 불필요, `docs/archive` 기록으로 충분.

## 다음 세션 권장 첫 프롬프트
`/resume`
