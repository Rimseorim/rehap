# HANDOFF - 2026-10-08 23:10

## 완료
- [x] 재검사 문제 해결 (협업자 답변 바탕화면 `재검사 질문 답변.txt`, 2026-10-06 반영)
  - `index.html` `goRetest`: 전용 재검사(pass_next = fail_next = 그 원인)를 먼저 고른다. 없으면 예전 규칙 (커밋 2286078, 배포됨)
  - `scripts/rehab_data.py` `flow()` 도 같은 규칙 → `check_seams.py` 실패 0 · 주의 0
  - 검증: 정본 전체에서 예전·새 규칙 비교 → 바뀐 곳 22건 = 질문 목록 1~22번과 id 일치. 배포본 playwright 로 4건 + 대조군 1건 화면 확인(상태 직접 주입 방식, 클릭으로 따라간 것은 아님)
- [x] `docs/PT_REVIEW_TODO.md` 신설 — PT 임상 검수 확인 목록 (문구 6건 + 룸바락 근거·애플리 통과 기준). `docs/RETEST_VALIDATED_TESTS.md §B` 에 포인터
- [x] 협업자 회신 작성: 바탕화면 `재검사 반영 회신.txt` (사용자가 전달, pull + `git config core.hooksPath .githooks` 요청 포함)
- [x] 인계장 archive 정리: `docs/archive/` 최신 3개(09-29·10-03·10-05)만 유지
- [x] 첫 화면 로딩 측정 스크립트 `scripts/measure_load.py` (조건 고정·기준값 머리말). 2026-10-08 기준: 받은 양 509~512KB(문서 377·글꼴 111~114·스타일 21), Lighthouse 느린 4G 로딩 완료 2.9~3.4초, DevTools 느린 4G 4.2~4.3초
- [x] 검수판 3개 재게시 불필요 판단 (재검사 22개는 영상 검수판에 이미 있음, 문구 변경 없음)

## 진행중
- 없음

## 대기
- [ ] **[급함] 백엔드 서버 부재**: `https://web-production-28002.up.railway.app` 전 경로 Railway 404. 로그인·기록 저장 불가. 협업자 계정(`motivated-prosperity`) — 회신 파일에 확인 요청을 덧붙일지 제안만 한 상태
- [ ] 협업자 회신 전달 여부 확인 (사용자 몫)
- [ ] PT 임상 검수 — 사용자: 추후. 목록 = `docs/PT_REVIEW_TODO.md`
- [ ] 첫 화면 로그인(보류) · 성공 기준 측정(추후 회의) · `backend/auth.py` 서명 키(협업자 협의)
- [ ] 실제 갤럭시 화면 밀림 미확인 (무선 adb 무응답)
- [ ] 문서 377KB 가 남은 가장 큰 덩어리 — 줄이려면 데이터 분할 필요, "정본 = index.html 하나" 결정과 충돌해 보류
- [ ] 표에 없는 의학 용어·영문 낀 운동명 111종·영상 미등록 1,787칸 — 손대지 않음

## 결정사항 / 주의
- 재검사 선택 규칙: 전용 재검사 > 원인으로 실패하는 검사 > 원인으로 통과하는 검사. 화면(`goRetest`)과 점검(`flow()`)은 같은 규칙을 유지한다
- 룸바락 재검사는 그대로 사용(협업자 결정). 근거 논란은 PT 검수에서
- 21번 `test-core-sideplank` id 는 오류 아님 (동작마다 다른 이름으로 표시)
- 데이터는 `index.html` 에서만 고친다 → `export_phase_exercises.py`·`generate_pt_review_doc.py` → `check_seams.py`. `merge_phase_ab_into_bundled.py` 실행 금지
- main push = GitHub Pages 자동 배포. 협업 문서는 바탕화면 txt 로 주고받는다
- 로딩 측정은 `measure_load.py` 조건 그대로 — 조건을 바꾸면 기준값과 비교 불가

## 다음 세션 권장 첫 프롬프트
`/resume`
