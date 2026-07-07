# HANDOFF - 2026-07-07 17:15

## 완료
- `data/phase-exercises.json`의 Phase A(홀짝 세트)/Phase B(4단계 진급) 149건을 `index.html` BUNDLED에 실제 병합 (`7335a04`)
- 병합 중 발견된 고아 데이터(pullup/vertical-press/kipping shoulder cause-a — 실제 앱엔 cause-dp/case1~4/cause-d만 존재) 제거
- Phase A/B UI 설계를 두 차례 재작업 끝에 최종 확정 + 구현:
  - `getTodaySet()` 'a'/'b' → 'a'/'a_b' 수정 (`d45cc96`)
  - 예전 "3회 편했다 → Phase B 전환 모달" 게이트 제거, A/B를 독립 트랙으로 (`893014e`)
  - 최종 UI: Phase A(준비운동) → "다음" → Phase B(진행단계) 2단계 순차 페이지 (`5f0957e`)
  - 진급 판단 시점을 세션 직후 → 다음 세션 시작 시점으로 이동 (다음날 통증 반영), "이전 단계로 돌아가기" 링크 추가 (`de819a6`)
- 전 과정 Playwright로 렌더링/카드 개수/모달/스테이지 전이 스모크 테스트 완료
- push 완료, 배포 확인: 실제 서비스는 GitHub Pages(`rimseorim.github.io/rehap/`)이고 Railway(`web-production-28002.up.railway.app`)는 백엔드 API 헬스체크 전용이었음을 발견 — CLAUDE.md에 반영 (`7f18a38`), push 완료

## 진행중
없음. 요청된 작업 전부 완료 및 배포 반영 확인됨.

## 대기
없음.

## 결정사항 / 주의
- Phase A/B는 예전 "블록 전환" 개념이 아니라 **독립된 두 트랙**: Phase A(홀짝 날 준비운동, 항상 노출) + Phase B(4단계 진급, 자체 진행). 향후 관련 로직 건드릴 때 이 모델 전제로 작업할 것.
- 진급 판단은 "즉시 반응"이 아니라 "지연 반응"(다음 세션에서 판단) 패턴 — 재활 앱 특성상 통증이 다음날 나타날 수 있음을 항상 고려.
- `data/phase-exercises.json`을 앞으로 또 수정/검증할 일이 있으면 pain-site id뿐 아니라 **cause id도 BUNDLED와 대조** 필수 (이번에 어깨 cause-a 고아 데이터를 뒤늦게 발견한 원인).
- 배포 주소 구분: 프론트엔드=GitHub Pages, 백엔드(auth/records)=Railway. 둘 다 main push 시 자동 배포.
- 관련 메모리 파일: `project_phase_ab_merge_status.md`, `feedback_no_unilateral_defer.md`, `project_shoulder_cause_framework.md` (모두 이번 세션에 갱신됨)

## 다음 세션 권장 첫 프롬프트
`/resume`
