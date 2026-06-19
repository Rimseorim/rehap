# HANDOFF - 2026-06-19

## 완료
- 무릎/스쿼트 cause-a~d Phase A/B 작성 (`data/phase-exercises.json`)
- 무릎/런지 cause-a~e Phase A/B 작성 (cause-a-mild 제거됨)
- 무릎/데드리프트 cause-a~d Phase A/B 작성
- cause-c (IT밴드/TFL) 클램쉘·사이드라잉 어브덕션 큐 cause별 차별화
- 덤벨·케틀벨 무게 큐잉 규칙 확정 및 기존 항목 소급 적용 (8개)
- index.html BUNDLED 데이터 수정 (허리/데드 cause-b, 고관절 cause-c 태그·진단명)
- Phase 작성 규칙 메모리 저장

## 진행중
- **`data/phase-exercises.json` Phase A/B 작성** — 무릎 완료, 허리부터 시작
  - 중단 지점: 무릎/데드리프트 cause-d 완료 후 세션 종료
  - 다음 스텝: 허리 db.zip 추출 후 **허리/스쿼트 cause-a**부터 설계안 제시 → 승인 → 작성

## 대기
- 허리 (스쿼트→런지→데드→풀업→키핑→로우→수직프레스→수평프레스) 전 cause
- 발목, 어깨, 고관절, 손목, 팔꿈치, 흉근 전 cause

## 결정사항 / 주의
- **Phase A 구조**: 홀수날(set:"a") 스트레칭2+활성화2 / 짝수날(set:"a_b") 스트레칭2+활성화2
- **Phase B 구조**: 4동작 ROM progression, YouTube URL 필수, 보조 명분 포함
- **덤벨·케틀벨 큐**: 등장 시 무게 권장(여성4~6kg/남성8~12kg) + "이번 단계의 핵심은 무거운 무게가 아니라 [목표]입니다" 필수
- **같은 운동 다른 cause**: 명칭 소제목 + 큐 반드시 차별화
- **작업 순서**: 설계안 채팅 먼저 → 승인 후 스크립트 작성
- **DB 파일**: `C:\dev\exercisematerials\01.test\DB\` 폴더에 통증부위별 zip — 추출 후 CSV 참조
- **Notion DB**: 무릎 재활 DB 등 운동별 핵심가이드·주의/보상작용 활용 가능
- phase-exercises.json 파일과 스크립트들 미커밋 상태

## 다음 세션 권장 첫 프롬프트
`/resume` 후 "허리 db.zip 열고 허리/스쿼트 cause-a Phase 설계해줘"
