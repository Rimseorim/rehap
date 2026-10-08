# HANDOFF - 2026-10-05 22:27

## 완료
- [x] 규칙서 `docs/VIDEO_REVIEW_RULES.md` 갱신: 운동 방식 용어 표·how·cue 말투 규칙, 「일괄 적용한 표기 (2026-10-05)」 표
- [x] 문구 일괄 수정 (index.html 정본 기준, 전부 배포됨)
  - 견갑골·어깨뼈·견갑 → 날개뼈 322곳 (`scripts/unify_scapula_term.py`, `scripts/unify_scapula_short.py`)
  - 운동 방식 용어 풀이·문구 (`scripts/annotate_mode_terms.py`, `scripts/rewrite_mode_terms.py`)
  - 본문 고유 700문장: 원어 풀이, how·cue 부정문 → 긍정문, 내부 메모 말투, 단계 번호 참조, 양성 (`scripts/apply_rewrite_map.py`)
  - 이름: 검사 제목 49·원인명 21·운동명 29. 이름에서 뺀 운동 방식 정보가 없던 18곳은 cue 에 한 문장 보충
- [x] SSOT 구조: 정본 = `index.html` 의 BUNDLED 하나
  - 읽기·쓰기 창구 `scripts/rehab_data.py`, 이음새 점검 `scripts/check_seams.py`(현재 실패 0·주의 1)
  - `data/phase-exercises.json` 은 `scripts/export_phase_exercises.py` 로 정본에서 생성 (동작 id·원인·문구 정본과 일치, 예전 `phase_a_b` 13묶음 제거)
  - 커밋 전 자동 점검 `.githooks/pre-commit` (clone 후 `git config core.hooksPath .githooks` 1회), 레포 CLAUDE.md 에 절차 명시
- [x] 첫 로딩 개선: 머리 순서(화면 설정·글꼴 링크를 데이터 앞으로), Pretendard 조각 방식(v1.3.9), 아이콘 글꼴 761KB → 사용 7종 인라인 스타일 2.8KB (`scripts/build_icon_css.py`). 가상 기기·느린 4G 기준 글꼴 3,066KB → 329KB, 로딩 완료 21.0초 → 7.8초 (아이콘 교체 전 측정)
- [x] 검수판 3개 새 링크 게시 (이 계정 소유·비공개, 공유 설정 필요). 영상 칸은 썸네일 42장 + 새 탭 링크
  - 원인·루트 `https://claude.ai/artifact/PByrDU27N6ncm77pgkgzpc`
  - 영상 `https://claude.ai/artifact/8ch1bjjonBHwXTGQmBiagm`
  - 감별 로직 `https://claude.ai/artifact/3bTkWenYGR4f3PwRSpE8mE`
- [x] 로컬 백업 `C:\dev\backups\bodycheck\rehap-20261005-2220.bundle`(레포 전체, `git clone <bundle>`) + `rehap-files-20261005-2220.zip`. dev-root `.gitignore` 로 원격 제외
- [x] 바탕화면 메모: `보류한 이름.txt`, `재검사 질문.txt`

## 진행중
- [ ] 검수판 3개는 2026-10-05 21:2x 정본 기준이다: 중단 지점 = 그 뒤 정본 변경(아이콘·사본 데이터)은 화면 문구와 무관해 재게시 안 함 / 다음 스텝 = 정본 문구가 바뀌면 scratchpad 의 `build_mirrors.py` 방식(화면 코드 유지, 데이터만 BUNDLED 에서 채움)으로 같은 링크에 다시 게시. scratchpad 는 세션 종료 시 사라지므로 필요하면 스크립트를 레포 `scripts/` 로 옮길 것

## 대기
- [ ] **[급함] 백엔드 서버 부재**: `https://web-production-28002.up.railway.app` 전 경로가 Railway 404 "Application not found". 운영 앱의 카카오·네이버·구글 로그인과 기록 저장이 동작하지 않는다(데모·브라우저 저장은 동작). Railway 프로젝트 `motivated-prosperity` 는 협업자 계정. 서버 상태와 계정·기록 데이터 잔존 여부를 협업자에게 확인
- [ ] 전용 재검사 22개가 화면에 나오지 않음 (`goRetest` 가 목록의 첫 감별 검사를 고름). 질문 메모 = 바탕화면 `재검사 질문.txt`, 협업자 답 대기 (사용자: "답이 오면 한다")
- [ ] 첫 화면이 로그인 — 사용자 결정으로 보류(패스)
- [ ] 성공 기준 측정 장치 — 사용자: 추후 회의
- [ ] 임상 검수(PT) — 사용자: 추후. 확인 필요 문구: PAILs/RAILs 라벨 풀이, 양성(증상이 나타남), "우울"→"내리기" 해석, 손목 신전근이 배측굴곡을 제한한다는 서술, "골반의" 보충, 손목 편심성 운동명 변경
- [ ] `backend/auth.py` 서명 키가 코드에 문자열로 있음 (공개 레포, 협업자와 협의)
- [ ] 실제 갤럭시에서의 화면 밀림 미확인 (무선 adb 무응답). 아이콘 교체 후 배포본 재측정 안 함
- [ ] 표에 없는 의학 용어(회전근개·전거근·신전·굴곡 등), 영문 낀 운동명 111종, 영상 미등록 1,787칸·같은 영상 14건 — 손대지 않음

## 결정사항 / 주의
- 보류한 이름 18개는 그대로 둔다 (사용자 결정, 다시 묻지 않음)
- 데이터는 `index.html` 에서만 고친다 → `export_phase_exercises.py` · `generate_pt_review_doc.py` 로 사본 재생성 → `check_seams.py`. `merge_phase_ab_into_bundled.py` 실행 금지
- 일괄 문구 수정은 고유 문자열 "old → new" 표 → `apply_rewrite_map.py`(숫자·괄호·풀이 중복 검증) 순. 병렬 작업자도 정본을 직접 고치지 않는다
- main push = GitHub Pages 자동 배포. 레포 루트 `.nopush`(자동 push 차단)·`.autopush-hold`(`.claude/settings.local.json` 제외)는 미추적 로컬 마커
- 아티팩트 화면은 iframe·외부 이미지를 막는다 → 영상은 링크·인라인 썸네일로
- Pretendard 원본 글꼴이 PC 에 설치돼 있어 PC 크롬 측정은 글꼴 다운로드가 재현되지 않는다 → `local()` 제거 또는 가상 기기로 측정

## 다음 세션 권장 첫 프롬프트
`/resume`
