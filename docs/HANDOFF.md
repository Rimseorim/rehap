# HANDOFF - 2026-06-20

## 완료
- 허리/스쿼트 cause-a~d Phase A/B (c56a26b 이전)
- 허리/런지 cause-a~d Phase A/B (cb53288)
- 허리/데드리프트 cause-a~d Phase A/B (c56a26b)
- 체크리스트 예외 조항 추가: 천장관절 예외1, 데드리프트 예외2, 과부하 recovery_note 규칙
- 메모리 전면 갱신 (feedback_phase_exercise_rules.md)

## 진행중
- **허리/데드리프트 cause-c** `recovery_note` + `priority_note` 휴식 가이드 추가 완료
- 다음 작업: **허리/풀업** cause 수 확인 후 설계 시작

## 대기
- 허리/풀업 → 허리/키핑 → 허리/로우 → 허리/수직프레스 → 허리/수평프레스
- 발목, 어깨, 고관절, 손목, 팔꿈치, 흉근 전 cause

## 결정사항 / 주의
- **debate.py**: 사용자가 직접 PowerShell에서 실행, 결과 붙여넣기. 반박문은 내가 작성해서 전달
- **PVC 오버헤드**: 웬만하면 넣지 말 것 (케틀벨·덤벨·빈 바벨 우선)
- **박스 동작 금지** (박스 스쿼트 등)
- **데드리프트 Phase B**: 맨몸 힙 힌지→맨몸 RDL→덤벨 RDL→빈 바벨 (예외 조항 2)
- **소제목 형식**: "[핵심타겟] 최종 통합 테스트"로 통일
- **과부하 cause**: recovery_note + priority_note 휴식 가이드 필수
- **DB**: `DB/허리_db_extracted/inner/*.csv` — cause-b부터 why/cue에 반영
- Gemma rate limit 자주 걸림 → GPT-OSS 단독 합의로도 진행 가능

## 다음 세션 권장 첫 프롬프트
`/resume` 후 "허리/풀업 cause 확인하고 설계 시작해줘"
