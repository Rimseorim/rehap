# 회복테스트 정식검사 교체 매핑 (검토안, 2026-06-14)

13개 신규 회복테스트(RETEST_AUDIT.md 완료 항목)를 정식/검증된 검사로 교체하는 안.
구조 영향 없음 (pass_next/fail_next 유지, 내용만 교체).

| # | 동작/부위/원인 | 현재 test id | 제안 검사 | 비고 |
|---|---|---|---|---|
| 1 | row/허리 — 과부하·과사용 | test-row-overload-retest | McKenzie 신전검사 (Prone Press-up) | |
| 2 | press-h/흉근 — 건병증(하강 시 과부하) | test-pec-tendinopathy-retest | 대흉근 길이검사 (Pec Major Stretch Test) | |
| 3 | press-h/흉근 — 과사용(볼륨급증) | test-chest-overuse-retest | 대흉근 저항검사 (Pec Major Resisted/MMT) | |
| 4 | deadlift/무릎 — PFPS 압박과부하 | test-pf-compression-retest | 디클라인 스텝다운 테스트 | 5와 공유 가능 |
| 5 | lunge/무릎 — PFPS 대퇴사두근과부하 | test-quad-overload-retest | 디클라인 스텝다운 테스트 | 4와 공유 가능 |
| 6 | lunge/발목 — 아킬레스건 과부하 | test-achilles-overload-retest | 싱글레그 힐레이즈(카프레이즈) 테스트 | |
| 7 | squat/무릎 — 훈련볼륨 과부하 | test-knee-volume-overload-retest | 싱글레그 디클라인 스쿼트 테스트 (점퍼니 검사) | |
| 8-10 | lunge/press-v/press-h 허리 — 코어약화 | test-core-plank-retest | McGill 플랭크 (유지, 영상만 추가) | |
| 11 | squat/허리 — 흉추가동성부족 | test-tspine-extension-retest | 흉추 신전 가동성 검사 | |
| 12 | row/허리 — 라운드백/요추굴곡패턴 | test-row-flexion-retest | 토터치/다분절굴곡 검사 (SFMA MSF) | |
| 13 | lunge/허리 — SI관절 불균형 | test-si-joint-retest | ASLR (Active Straight Leg Raise) | |

## 전체 테스트 전수 점검 (직접검사 포함, 고유 53개)

### A. 그대로 유지 — 표준검사명/크로스핏 표준동작, 영상 풍부 (영상 링크만 추가하면 됨, 39개)
코젠스/역코젠스/이두건유발(엘보), FADIR/토마스/트렌델렌버그(힙), Apley's Scratch/페인풀아크/
Empty Can/수평내전·외전저항/내회전저항/굴곡·신전ROM(숄더), TFCC압박/손목신전·굴곡저항(리스트),
무릎valgus, Ober's(IT밴드), 발목배측굴곡(weight-bearing lunge), 발목외측안정성(단일다리균형),
소흉근길이(도어웨이스트레치), 데드행, 할로우바디홀드, 전굴후굴유발(McKenzie 분류),
플랭크(코어), 딥스쿼트(고관절가동성), 90/90외회전, 좌골결절 벤트니스트레치 등.
→ 메커니즘·동작 일치 확인됨, 영상 검색만 하면 됨 (별도 작업).

### B. 룸바락(Lumbar Lock) 3종 — "그대로 유지" 결정 존중
test-shoulder-lumbarlock-rom/core/scapula (벽에 등 대고 팔 들기, ROM·코어분리·견갑골 체크).
**Seated Wall Angel test**(IJSPT 게재, 정식 스코어링 검사)와 동작·메커니즘 거의 동일.
내용/이름 변경 없이 "Wall Angel" 동작 영상만 매칭해서 추가 가능.

### C. 교체 필요 — 14건 (기존 13건 + 신규 발견 1건)
- 기존 13건: 위 표 참조.
- **신규 발견**: `test-lowerback-overload-retest` (deadlift·press-h·press-v lower-back, x3 사용) —
  "데드리프트 후 뻐근함이 줄었는지" 증상설문형, 13건의 #1(row 과부하)과 동일 메커니즘.
  → **#1 McKenzie 신전검사(Prone Press-up)와 통합** — 4개 동작(row+deadlift+press-h+press-v)
  허리 과부하 계열 cause 전체가 이 검사 1개를 공유하도록 통합.

## 최종 결론
- 즉시 콘텐츠 작성 대상: **14건** (13건 매핑표 + test-lowerback-overload-retest를 #1에 통합)
- A그룹(39개)·B그룹(3개)은 검사 내용 변경 없이 영상 링크만 추가 (별도 소규모 작업)
