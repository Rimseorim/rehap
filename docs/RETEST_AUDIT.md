# 회복테스트(goRetest) 매칭 미스매치 audit — 2026-06-14

목표: 어깨 q3/q4(1순위), 허리 과부하(2순위 일부), 무릎/발목(3순위) 외 나머지 cause들도
"goRetest가 매칭하는 테스트가 회복 확인용으로 적합한가"를 전부 검토.

## Q(질문)·원인배정 구조 검토 결론
Q는 안 고쳐도 됨. 모든 cause는 타당한 질문 흐름으로 도달함:
- "직접식별형"(과부하/과사용/IT밴드/SI관절 등): 질문에서 바로 cause로 분기, 처음부터 그 원인용 테스트가 tests 배열에 없었음.
- "rule-out형"(코어약화/패턴오류 등): 한 검사로 두 원인을 가르는 구조(통과=원인X, 탈락=원인Y). 탈락 쪽은 그 검사가 곧 원인 검사라 회복테스트로 적합하지만,
  통과 쪽 원인은 그 검사 메커니즘과 무관해서 회복테스트로 부적합.

→ 결론: 진단 로직 변경 불필요. **13건 모두 "신규 회복테스트 콘텐츠 추가"로 해결**.
   타입은 cause 메커니즘에 따라 동작검사 / 증상설문으로 구분.

## 신규 회복테스트 필요 — 증상설문형 (과부하/과사용 계열) 7건 — 완료
- [x] row/허리 cause-c (과부하/과사용) — test-row-overload-retest 추가
- [x] press-h/흉근 cause-a (대흉근 건병증, 하강 시 과부하) — test-pec-tendinopathy-retest 추가
- [x] press-h/흉근 cause-c (과사용, 볼륨·빈도 급증) — test-chest-overuse-retest 추가
- [x] deadlift/무릎 cause-a (슬개대퇴 압박 과부하) — test-pf-compression-retest 추가
- [x] lunge/무릎 cause-d (PFPS, 대퇴사두근 과부하) — test-quad-overload-retest 추가
- [x] lunge/발목 cause-c (아킬레스건 과부하) — test-achilles-overload-retest 추가
- [x] squat/무릎 cause-c (훈련 볼륨 과부하) — test-knee-volume-overload-retest 추가

## 신규 회복테스트 필요 — 동작검사형 (구조적/메커니즘 불일치) 6건 — 완료
- [x] lunge/허리 cause-b (코어 약화 → 요추중립 유지불가) — test-core-plank-retest 추가
- [x] press-v/허리 cause-b (코어 약화) — test-core-plank-retest 추가
- [x] press-h/허리 cause-b (코어 약화) — test-core-plank-retest 추가
- [x] squat/허리 cause-b (흉추 가동성부족→요추과부하) — test-tspine-extension-retest 추가
- [x] row/허리 cause-a (라운드백/요추굴곡패턴) — test-row-flexion-retest 추가
- [x] lunge/허리 cause-c (천장관절 부하 불균형, SI관절) — test-si-joint-retest 추가

모두 goRetest 시뮬레이션 + Playwright 렌더링으로 검증 완료 (2026-06-14).

## 적합/수정불요 확인됨 (참고용, 손대지 않음)
- lunge/발목 cause-a-mild → test-ankle-df (같은 메커니즘, 적합)
- deadlift/허리 cause-a (round back) → test-flexion (적합)
- pullup/허리 cause-a (보상패턴, hollow body 유지불가) → test-back-hollow (적합)
- squat/허리 cause-a, cause-c → 적합 매칭됨
- lunge/허리 cause-a, row/허리 cause-b → 적합 매칭됨
- lunge·deadlift/무릎 cause-c (IT밴드) → test-itband-retest (3순위에서 추가완료)
- lunge/발목 cause-b (인대불안정) → test-ankle-stability-retest (3순위에서 추가완료)
- kipping/어깨 cause-dp (보호단계) → test-shoulder-flex (통증재현검사, 적합)
- squat/발목 cause-d (컨디셔닝부족) → test-ba-ankle-df (애매하나 큰 무리 없음)

## 진행 순서 (사용자 영향 기준, 진행 중)
1. 동작검사형 코어약화 3건 (lunge/press-v/press-h 허리 cause-b) — 빈도 높음
2. 증상설문형 7건 (과부하/과사용 계열)
3. 동작검사형 나머지 3건 (squat 허리 cause-b, row 허리 cause-a, lunge 허리 cause-c/SI관절)
