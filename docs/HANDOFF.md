# HANDOFF - 2026-06-19

## 완료
- 허리/스쿼트 cause-a Phase A/B 작성 → `data/phase-exercises.json`
- 허리/스쿼트 cause-b Phase A/B 작성 → `data/phase-exercises.json`
- 멀티모델 토론 파이프라인 구축 → `scripts/debate.py` (Gemma + GPT-OSS, OpenRouter 무료)
- 메모리 업데이트 (토론 파이프라인 + 진행 현황 + 규칙 전면 갱신)

## 진행중
- **허리/스쿼트 cause-c (코어 안정화 부족)** Phase A/B 설계
  - 중단 지점: cause-b 완료 후 세션 종료
  - 다음 스텝: debate_history.md 초기화 → 설계안 작성 → `python scripts/debate.py`

## 대기
- 허리/스쿼트 cause-c
- 허리 전체 동작: 런지 → 데드 → 풀업 → 키핑 → 로우 → 수직프레스 → 수평프레스
- 발목, 어깨, 고관절, 손목, 팔꿈치, 흉근 전 cause

## 결정사항 / 주의
- **토론 파이프라인**: `scripts/debate.py` → OpenRouter API (OPENROUTER_API_KEY 환경변수 등록됨)
- **사용 모델**: Gemma (google/gemma-4-31b-it:free) + GPT-OSS (openai/gpt-oss-120b:free)
- **Phase B set 키 없음**: 실제 DB 구조 확인됨. Phase B에 set 표기 불필요
- **새 cause 시작 시** debate_history.md 초기화 필수: `Set-Content "scripts\debate_history.md" -Value "# 토론 히스토리 — [부위/동작 cause-x]" -Encoding utf8`
- **체크리스트 경로**: `C:\Users\tjfla\OneDrive\Desktop\재활앱_설계_표준_체크리스트.md`
- **스크립트 파일들 미커밋 상태**: debate.py, add_lower_back_squat_cause_a.py, add_lower_back_squat_cause_b.py

## 다음 세션 권장 첫 프롬프트
`/resume` 후 "허리/스쿼트 cause-c 설계 시작해줘"
