# HANDOFF - 2026-08-14 (2)

## 완료
- task #16 SFMA 상지패턴 자가측정(Apley's Scratch) 도입 — 키핑 어깨 통증경로에 `q-shoulder-scratch` 질문 신규 추가(`test-shoulder-ext` 삭제·교체), 7개 동작(스쿼트·데드리프트·로우·풀업·키핑·수평프레스·수직프레스) `q4` 편측편향 문구("한쪽 팔이"→"한쪽이든 양쪽이든") 일괄 수정. 스펙: `docs/superpowers/specs/2026-08-14-shoulder-sfma-scratch-test-design.md`, 계획: `docs/superpowers/plans/2026-08-14-shoulder-sfma-scratch-test.md`. subagent-driven-development로 구현(3-task, spec+code review 통과), Playwright로 브라우저 실동작(키핑 3분기 라우팅 전부, 로우 q4 문구) 확인 완료. 커밋 `1f29ebb`~`cf7241f`, push 완료(`7d45dde`, origin/main 반영, 자동배포 트리거됨).
- docs/HANDOFF.md 아카이브 이동 스테이징 누락분 정리 커밋(`7d45dde`).

## 진행중
(없음)

## 대기 (task 목록, 완료분 제외) — 총 10개

**설계 필요**:
- #17 안내문구/보조신호 배치 정책 설계 (SFMA2 응급신호 + YBT 좌우비대칭 신호 노출 위치, 개별 추가 시 화면 산만해질 위험 있어 정책부터) — **다음 세션 시작점으로 추천**

**큰 작업 / 후순위**:
- #6 긍정적 언어 사용 원칙 전체 재검토 (index.html 전수 조사)
- #7 캐리 철학 검증
- #10 감별질문 전체 애매성 스캔
- #14 모터컨트롤 자가측정 문항 재설계

**문서화**:
- #4 3R 리인포스 — why 필드 근거 보강 (콘텐츠 작성 시 참고)
- #5 YBT 상지버전 — 운동복귀 체크리스트 후보
- #8 임상 근거 통합 문서 작성 검토

**최종 논의(제일 마지막)**:
- #18 복합 원인 후보 배정 우선순위 로직

**신규**:
- #20 기존 stage-3(운동복귀) 팁 483개에 구체 운동 인라인 백필 — 정책만 확정, 미착수

## 결정사항 / 주의
- `.claude/settings.local.json` 로컬 변경분은 계속 커밋 안 함 (관례 유지)
- task 진행 순서는 번호 순이 아니라 난이도/준비도 우선순위 그룹 순 (설계 필요 → 큰 작업 → 문서화 → 최종논의)
- **task #16 진행 중 스펙을 두 번 정정한 경험**: 처음엔 "flex→ext→core 체인이 3개 동작(풀업·키핑·수직프레스) 공통"이라고 잘못 가정했으나, 실제 코드 확인 결과 5개 동작 모두 2단계 검사가 동작마다 다름(로우=h-abd, 풀업=hang, 키핑=ext, 수평프레스=h-add, 수직프레스=empty-can) — `test-shoulder-ext`는 키핑에만 존재. q4 스코프도 처음엔 "5개 동작"으로 잘못 썼다가 실제로는 7개(스쿼트·데드리프트 포함, 런지만 어깨 pain_site 없어 제외)로 정정. **교훈**: BUNDLED 데이터는 동작별로 독립 정의되어 있어 "같은 패턴일 것"이라 가정하지 말고 항상 Node 스크립트로 각 동작을 개별 확인할 것.
- **subagent-driven-development 진행 중 구조 버그 발견 사례**: Task 1 구현 시 컨트롤러(나)가 제시한 old_string/new_string 자체의 괄호 카운팅이 틀려서, 신규 질문 노드가 형제가 아니라 q4의 choices 배열 안에 중첩되는 버그가 났음. spec-reviewer 서브에이전트가 브라켓-depth 추적 스크립트로 잡아냄 → 같은 에이전트에 SendMessage로 수정 지시 → 재검증 통과. **교훈**: 컨트롤러가 만든 old/new string도 무조건 맞다고 믿지 말고, 구현 subagent에게 "제시된 old_string을 실제 파일과 먼저 대조하라"는 지시를 항상 포함시킬 것 (Task 2/3부터 반영함).
- 이 프로젝트는 main 브랜치에 직접 커밋하는 관례 (feature 브랜치 없음), 사용자가 명시적으로 재확인함.
- Playwright가 Node에 설치돼 있음(`node_modules/playwright`) — 브라우저 스모크 테스트 시 스크립트를 프로젝트 루트 안에 임시로 써서 실행(모듈 resolve 때문에 프로젝트 밖 스크래치패드에서는 require 실패), 끝나면 삭제. 데모 로그인은 "데모로 시작" 링크로 진입 가능.

## 다음 세션 권장 첫 프롬프트
/resume
