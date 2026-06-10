# HANDOFF - 2026-06-10 00:00

## 완료
- glossary ? 토글 동작 검증 완료 (Playwright로 직접 확인) — route 화면에서 정상 표시
- `refactor: glossary 팝업 위치 고정 및 카드 크기 축소, 가동범위 제거` (2f11790) — push 완료, Railway 자동 배포 트리거됨
  - ? 버튼을 details→absolute positioned popup으로 변경 (버튼이 아래로 안 밀림, 옆에 카드 오픈)
  - 카드 크기 축소 (max-width 240px, font-size 11~12px)
  - glossary에서 "가동범위" 항목 제거

## 진행중
- 없음

## 대기
- Railway 배포 완료 후 새 ? 팝업 위치/크기 실제 확인 (선택)

## 결정사항 / 주의
- cause 화면 진단명(cause-tag/h2)에는 ? 버튼 추가 안 함 — 진단명은 전문용어 그대로 노출 의도
- "기록 저장에 실패했습니다." 토스트는 데모모드 한정 동작 — 처리 불필요 (확인됨)
- 검증 시 주의: Railway URL(`web-production-28002.up.railway.app`)은 백엔드 API 전용. 프론트엔드는 로컬 `index.html` 직접 열어서 확인 (`file:///...index.html` → 데모로 시작 → 재활 탭)
- 레포가 `Rimseorim/rahap1` → `Rimseorim/rehap`로 이동됨 (push 시 안내 메시지 확인됨, origin은 그대로 유지됨)

## 다음 세션 권장 첫 프롬프트
`/resume`
