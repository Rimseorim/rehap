# HANDOFF - 2026-09-29 19:28

## 완료
- **어깨 cause-dp Phase B 7동작 전체 완료** (런지는 어깨 통증 부위 없음). data/phase-exercises.json + index.html BUNDLED 양쪽 반영, 동작별 4개씩 검증, 전부 push됨 (main `36db833..c718323`)
  - 스쿼트 `bd87c7b`, 데드리프트·풀업 `e3b61b0`, 키핑 `d1acae6`, 로우 `bc090db`, 수직 프레스 `c48dd5d`, 수평 프레스 `c718323`
  - 스크립트: `scripts/add_{deadlift,pullup,kipping,row,vertical_press,horizontal_press}_shoulder_cause_dp_phase_b.py`
- 메모리 `project_shoulder_cause_framework` 갱신 (cause-dp Phase B 완료 + 설계 원칙 기록)
- **사고 복구**: 커밋 `bd87c7b`에서 병합 스크립트가 낡은 data로 index.html을 덮어써 약 70개 원인의 수정분(쉬운 말 65건, 내부 메모 "DB 수록 운동." 15건 노출, 꼬리표 18건, 로우 허리 b 이름 등)이 되돌려진 채 배포돼 있었음. 검수판(=`36db833` 상태)을 기준으로 index.html·data 양쪽을 복구·푸시. 병합 스크립트는 `--force-overwrite-all` 없으면 실행 안 되게 막고 CLAUDE.md에 금지 기록
- 런지 발목 빈 cue 4건 채움, 밴드 거골 후방 견인 스트레칭 위치 표현("발목 앞쪽 접히는 부위") 4곳 통일, "종아리·발바닥 복합 스트레칭" 6곳을 "발바닥·발가락 스트레칭"으로 정정(스쿼트 발목 a는 종아리 단계가 있어 유지). 검수판 v6 게시(어깨 Phase B 28개·발목 수정 포함)
- 이전 HANDOFF(2026-09-26)를 `docs/archive/HANDOFF-2026-09-29.md`로 이동

## 진행중
- **재활 운동명 뒤 꼬리표 정리** (이월, 중단 지점 = 잔여 약 29개를 짝 단위 목록으로 제시하기 전)
  - 범위 밖 잔여: "— 무게 점진 복귀/도입" 계열 b4, "— 와이드 스탠스"·"— Full ROM" 등이 붙은 b2·b3, 키핑 손목 b·c·d b1 "데드 행 (매달리기만)" 등. 이번 정리에 넣을지 미결정
  - 다음 스텝: 짝(이름 겹침) 단위로 목록 제시 → 결정 후 index.html·검수판 양쪽 반영. 별도로 "2단계와 동일" 같은 앞 단계 번호 참조 문구를 8동작 전체에서 검색(로우 허리 b3 1건만 수정, 나머지 미검색), 로우 허리 b1 why "고관절 굴곡근" 쉬운 말 표기 수정
- **데드리프트 모션 검수** 시작 전 (이월): 무릎(`test-valgus`/`test-valgus-lateral`) → 허리 → 어깨 → 손목 → 고관절 순

## 대기
- 원인명 규칙 적용: 152개 원인명 중 "배측굴곡"·"외측"·"테스트"에 걸리는 목록 정리 후 승인 받기
- "양성" 표현 약 43곳 잔존(전체 정리 여부 미결정), 런지 발목 안정성 재검사 목적문 "외측 인대", "견갑골(어깨뼈)"→"날개뼈" 전수 변경(미실시). 이번 cause-dp Phase B 신규 문구는 "날개뼈"로 작성함
- 벽 발목 가동성 운동 시작 거리 5cm vs 검사 8cm 의도 여부 판단 필요
- 한글/영어 운동명 통일 판단(사용자가 유튜브·네이버로 확인 후 결정). 의학용어 포함 운동명 개수 미집계
- 방법(how) 5요소 작성 기준 보류
- 진급 기준(`progression_note`) 문구 "상위 결함 검사 프로토콜(감별 진단)로 리턴…"이 Phase B 카드에 렌더링됨 → 쉬운 말로 수정 필요
- 상대 검수자에게 줄 것: `VIDEO_REVIEW_RULES.md`, 영상 검수판 링크, 원인·루트 검수판(현재 비공개라 공유 설정 필요). 원인·루트 검수판은 이번 Phase B 28개 운동(7동작×4) 미반영 상태라 갱신 필요 여부 판단. 감별 로직 문서(`https://claude.ai/code/artifact/ba2c3e4d-e4d1-4dca-bfec-a0dbd8b1f4d1`)는 2026-08-29 버전이라 갱신 필요
- 운동 video_url 미등록: 이번 Phase B 28개 포함 대부분 `TBD`. 데드리프트 `test-valgus` 영상 미해결
- 용어사전 설계 문서 2개(`docs/superpowers/specs|plans/2026-06-08-glossary-toggle-*`) 삭제 여부 미정
- PT/전문의 임상 검수 — 여전히 유일한 진짜 배포 블로커. 특히 이번 cause-dp Phase B(통증호 통과·그립·궤적 큐)는 임상 검수 대상. Railway 백엔드·로그인 이관 방향 미결정

## 결정사항 / 주의
- **cause-dp Phase B 설계 원칙**: 1단계 통증호 밖 패턴 → 2단계 통증 직전 높이까지 통제된 통과(동작·팔 분리, 반동 금지, 내릴 때 2~3초) → 3단계 경부하 → 4단계 도구+부상 전 30~40%. 풀업·키핑 4단계는 "볼륨 점진 복귀"(3단계와 같은 보조 수준·그립 유지, 무보조·오버그립 복귀 문구는 넣지 않음, 기존 풀업 원인들과 동일 구조)
- 힘 뺀 데드행 대신 액티브 행(날개뼈 내림). 덤벨·풀업 그립은 중립/언더핸드 권장(키핑은 오버핸드 기본이라 미적용). 그립 너비·각도는 수치 확정 대신 기준으로("팔뚝이 바닥과 수직"). 위치는 뼈 기준("가슴뼈 아래쪽, 명치 바로 위"), 젖꼭지 라인·"명치 아래" 부적합
- 사용자가 다른 AI 반박 문구를 붙여 오면 무조건 수용하지 말고 항목별로 수용/부분수용/불수용 판단 (이번에도 오류 지적 다수: 오버그립 정의 오류, 명치 위치, 훅그립 무관 등)
- 반영은 해당 cause만 수정하는 스크립트(python, Write로 파일 생성 후 Bash 실행). **`merge_phase_ab_into_bundled.py` 실행 금지**(전체 덮어쓰기, 실제로 사고 발생, 이제 `--force-overwrite-all` 필요). bundled id: vertical-press→press-vertical, horizontal-press→press-horizontal
- 데이터 동기화 상태: index.html, data/phase-exercises.json, 검수판 3곳의 Phase A/B가 09-29 기준 같음. 앞으로 문구를 고칠 때 3곳을 함께 갱신할 것
- `lunge/ankle/cause-a-mild` 삭제 완료(원인 152→151개): 2026-06-23 b91df94에서 cause-a로 통합했으나 원인 정의가 잔해로 남아 도달 불가였음. index.html·data/movements/lunge.json(검사 분기 pass_next도 cause-a로)·pt_review_전체동작.md·RETEST_CONTENT_REVIEW.md·검수판(v7)에서 제거. 복구는 b91df94 이전 커밋에서. `docs/need/retest_templates.txt`·`transform_stages.py`에는 잔해가 남아 있을 수 있음(미확인, 과거 생성물·스크립트라 그대로 둠). 감별 로직 문서·Artifact는 09-29 재생성으로 반영됨
- 미해결: 검수 요청 범위(물리치료사=원인·처방 이유, 코치=큐·방법·단계) 안내 문구를 `VIDEO_REVIEW_RULES.md`에 넣을지 미결정. 규칙 파일·검수판만 외부에 넘길 예정이므로 미결 항목(벽 발목 5cm/8cm, "양성", "외측"·"배측굴곡" 처리)을 파일에 "결정/미결"로 적어야 함
- 이번 세션 중 auto mode 안전성 검사기가 일시 장애로 Bash/Write를 막은 적 있음(복구됨). 터미널이 오후 3시 17분경 한 번 꺼졌으나 원인 미확인
- 운동명: 표준명 그대로, 대시·괄호 뒤 목적·단계 표기 삭제. 용어 표기: 의학·해부 용어=쉬운 말(원어), 운동·기술 용어=용어(쉬운 말), "날개뼈"로 통일
- 검수판 Artifact: 영상 검수판 v49 `https://claude.ai/artifact/3S2juJAfWMDJG2yWoo1pDe`, 원인·루트 검수판 `https://claude.ai/artifact/YG6sHXLeqdYs4HzsAaYVRg`. 게시 시 "최신 read → 전체 파일 Read" 후 publish
- `index.html`은 한 줄 minified라 Edit 불가 → python으로 BUNDLED JSON 파싱 후 수정·재직렬화. 스크립트는 세션 임시 폴더에 두면 사라지므로 `scripts/`에 둠
- push는 main 자동 배포. 이번 handoff 커밋은 아직 push 안 함

## 다음 세션 권장 첫 프롬프트
`/resume`
