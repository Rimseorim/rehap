# HANDOFF - 2026-06-18

## 완료
- 모델 Sonnet 4.6으로 변경

## 진행중
- **Phase A/B 운동 데이터 JSON 작성** (`data/phase-exercises.json`)
  - 중단 지점: 무릎/런지의 cause 확인 중
  - 현재 파일 상태: 스쿼트(무릎 cause-a/b/c), 런지(무릎 cause-a만), 데드(허리 cause-a), 풀업(어깨 cause-a), 키핑(어깨/손목 cause-a), 로우(허리 cause-a), 수직프레스(어깨 cause-a), 수평프레스(흉근 cause-a) — 모두 미완성
  - 다음 스텝: **index.html BUNDLED 데이터에서 모든 동작×통증부위의 cause 목록 추출 → 각 cause별 Phase A/B 작성**

## 대기
- 무릎/런지 cause 전체 목록 확인 (index.html에서 추출 필요)
- 무릎/데드리프트 cause 전체 목록 확인
- 나머지 통증부위(허리, 발목, 어깨, 고관절, 손목, 팔꿈치, 흉근) 전체 동작 cause 확인

## 결정사항 / 주의
- 작업 순서: **무릎→허리→발목→어깨→고관절→손목→팔꿈치→흉근** (UI 순서)
- 각 통증부위 내 동작 순서: **스쿼트→런지→데드리프트→풀업→키핑→로우→수직프레스→수평프레스**
- cause는 index.html BUNDLED 데이터에서 가져올 것 (data/rehab.json은 스쿼트만 있음)
- Phase A: 홀수날 a타입(스트레칭/가동성 4개) + 짝수날 b타입(활성화/저항 4개) = 총 8개
- Phase B: 4~5개 ROM progression sequence
- 영상 URL 포함 (유튜브 우선)
- `data/phase-exercises.json`이 신규 파일로 아직 미커밋 상태

## 다음 세션 권장 첫 프롬프트
`/resume` 후 "index.html에서 무릎/런지 cause 목록 추출해줘"
