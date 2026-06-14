# HANDOFF - 2026-06-14 17:26

## 완료
- 회복테스트(goRetest) 13건 신규 추가 (index.html 내 BUNDLED 데이터, 이번 커밋에 포함) — RETEST_AUDIT.md 13건 모두 [x] 처리, goRetest 시뮬레이션+Playwright 검증 완료
- 13건 + 신규발견 1건(test-lowerback-overload-retest, x3 사용) = 총 14건에 대해 "정식검사+영상" 교체 매핑안 작성 → docs/RETEST_VALIDATED_TESTS.md
- 전체 53개 고유 테스트 전수 점검·분류 완료
  - A그룹(39개): 코젠스/토마스/FADIR/트렌델렌버그/Apley's/TFCC/Ober's/할로우바디/데드행 등 표준검사·표준동작 — 내용 변경 불필요, 영상 링크만 추가
  - B그룹(룸바락 3종): "그대로 유지" 결정 존중, Seated Wall Angel test와 동작·메커니즘 일치 — 이름/내용 안 바꾸고 영상만 매칭
  - C그룹(14건): 교체 필요 (위 매핑안)

## 진행중
- 14건 교체 — 콘텐츠 작성/반영 아직 시작 안 함
  - 중단 지점: docs/RETEST_VALIDATED_TESTS.md 매핑표. 14건 중 9건만 후보 URL 검색됨(McKenzie Press-up, Decline Step-Down, 싱글레그 힐레이즈, 싱글레그 디클라인 스쿼트, 흉추신전가동성, ASLR). #2/3 펙검사(길이/저항), #8-10 McGill 플랭크, #12 토터치/SFMA MSF는 URL 미확정. 찾은 URL도 검색결과 제목/링크일 뿐 실제 재생 검증 안 됨.
  - 다음 스텝: 14건 전체 구체 영상 URL 확정(웹서치) → 접속 가능 여부 확인 → 사용자 승인 받고 index.html에 콘텐츠 작성/반영 (구조: pass_next/fail_next 유지, name/purpose/steps/note/pass_text/fail_text/video_url만 교체. 4·5는 디클라인 스텝다운 1개 검사 공유 가능, #1과 test-lowerback-overload-retest는 McKenzie 신전검사로 통합)

## 대기
- A그룹(39개)·B그룹(3개) 영상 링크 추가 — 14건 작업 끝난 뒤, 별도 승인 받아 진행

## 결정사항 / 주의
- 13건 신규 회복테스트를 "정식검사+영상" 기준 재검토한 결과 절반 정도(#1,2,3,11,13)는 처음 제안한 SFMA/FMS 매핑이 부적합(과도한 부하/파트너 필요/메커니즘 불일치) → McKenzie 신전검사, 펙 길이검사/저항검사, ASLR, 흉추신전가동성 등으로 재매핑함
- 신규 발견: test-lowerback-overload-retest(deadlift/press-h/press-v 허리, x3) — 13건의 #1(row 과부하)과 동일한 "증상설문형" → #1과 통합해 McKenzie 신전검사를 4개 동작이 공유하도록 제안
- 룸바락(Lumbar Lock) 3종은 과거 세션에서 "그대로 유지"로 결정됨 — 이번에도 이름/내용은 안 바꾸고 Wall Angel 동작 영상만 매칭

## 다음 세션 권장 첫 프롬프트
/resume
