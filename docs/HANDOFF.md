# HANDOFF - 2026-09-23 (세션 인계, 2회차)

## 완료
- **런지 모션 영상 검수** 진행 중 — 공유 테스트(스쿼트와 중복) 4개 제외한 신규 테스트 검수 시작
  - 스쿼트-런지 공유 테스트 4개 확인: test-ankle-df / test-hip-fadir / test-hip-thomas / test-hip-trendelenburg (이미 스쿼트 때 검수 완료됨)
  - **무릎 `test-valgus`(런지 무릎 정렬 테스트)**: video_url 오류 발견·수정 (`xCVKkf17jXE`는 실제로 Trendelenburg 영상이었음 — valgus 3개 인스턴스가 전부 잘못된 영상을 공유하고 있었음). 런지 인스턴스만 올바른 영상(`shorts/EzPzk9DBBvM`)으로 교체 완료. **데드리프트 `test-valgus`/`test-valgus-lateral` 2곳은 아직 미해결** — 올바른 영상 못 찾음, 보류 중
    - 모순되는 note("무릎을 구부릴 필요 없이 하강 자세만 취하면 됩니다") 삭제
  - **허리 `test-hip-flexor`(토마스 검사)**: 이름을 새 명명 규칙에 맞춰 "토마스 검사 — 고관절 앞쪽 근육 긴장 확인"으로 변경(런지 인스턴스만). steps를 Physiopedia/Orthofixar 근거로 검증해 절차 오류 수정(양 무릎 당기는 단계 누락돼 있던 것 → 4개 인스턴스 전체(런지/로우/수평프레스/수직프레스) 반영, 사실오류라 전체 적용). note의 "굴곡근" 표현도 정리
- **용어 치환**: "고관절 외전근/중둔근" → "엉덩이 옆 근육(중둔근)" 47건, "장요근" → "고관절 앞쪽 근육(장요근)" 61건 전부 index.html + 검수판 양쪽 반영
- **버그 발견·수정**: index.html과 검수판 둘 다 YouTube 임베드 URL 파싱 정규식이 `/shorts/` 링크를 못 읽던 버그 → 둘 다 수정
- **CLAUDE.md**: "쉬운 말로 쓴다" 원칙 핵심 원칙 2번 밑에 추가
- **`docs/VIDEO_REVIEW_RULES.md` 신규 작성** — 검수판과 함께 다른 사람에게 전달할 규칙 문서. 포함 내용:
  - 수정 범위 규칙(사실오류=전체적용 / 문구스타일=인스턴스만)
  - 검수 완료 기준
  - 영상 신뢰성 검증(영상만 믿지 말고 임상 자료로 교차검증)
  - 영상 링크 규칙(동작 등장 시점 기준 타임스탬프, 길이 기준 아님)
  - 용어 규칙 + 범위 경계(신전/굴곡/회전근개 등 수백~수천 건은 지금 범위 아님, "카피 전체 검토" 때 처리)
  - 테스트명 규칙("[원어] 검사 — [쉬운 설명]" 형식, 대시 통일, 인명은 한글 표기)
- 검수판 Artifact 버전: v41까지 반영 (`https://claude.ai/artifact/3S2juJAfWMDJG2yWoo1pDe`)
- **아직 커밋 안 함** — CLAUDE.md, index.html 수정사항 + `docs/VIDEO_REVIEW_RULES.md` 신규 파일 전부 uncommitted

## 진행중
- 런지 모션 검수 — 무릎(`test-valgus` 완료), 허리(`test-hip-flexor` 완료) 끝. **발목·고관절 아직 안 함**
  - 발목: `test-ankle-stability-retest`, `test-achilles-overload-retest` (신규 메인 테스트 없음, retest만 존재 — 이전 세션에서 확인됨)
  - 고관절: 4개 공유 테스트 전부라 신규 검수 대상 없음 (건너뛰어도 됨)
  - 중단 지점: 사용자가 "발목으로 넘어갈까요?"에 답하기 직전
  - 다음 스텝: 런지/발목 대표 테스트(`test-ankle-stability-retest` 또는 `test-achilles-overload-retest`) 골라서 검수 시작

## 대기
- **데드리프트 `test-valgus`/`test-valgus-lateral` video_url 미해결** — 올바른 무릎 정렬(valgus) 시연 영상을 못 찾음. Sports Injury Clinic 채널엔 없음. 사용자 보유 영상 소스가 있으면 물어볼 것
- 다음 세션: 런지 → 발목 → 고관절(스킵 가능) 순으로 마무리 후 데드리프트 모션 검수 진입 예정
- PT/전문의 임상 검수 — 여전히 유일한 진짜 배포 블로커
- "글귀(카피) 전체 검토" — 사용자 직접 예정. `docs/VIDEO_REVIEW_RULES.md`에 범위 경계용 용어 목록(신전/굴곡/회전근개 등) 기록해둠, 이걸 참고해서 시작하면 됨
- Railway 백엔드 FRONTEND_URL, SQLite 영속성 — 로그인 이관 방향 미결정, 이월 계속
- **CLAUDE.md·index.html·docs/VIDEO_REVIEW_RULES.md 커밋 필요** (다음 세션 시작 시 우선 처리 권장)

## 결정사항 / 주의
- **검수 완료 기준**: 제목/영상만 보고 완료 선언 금지 — steps/note/passText/failText 본문까지 확인해야 완료 (`docs/VIDEO_REVIEW_RULES.md` 참조)
- **명명 규칙 신설**: 테스트명은 "[원어(인명/약어)] 검사 — [쉬운 설명]" 형식으로 통일. 단, 기존 4개 중복 인스턴스는 문구 스타일 수정 스코프라 검토한 것(런지)만 바꿈 — 나머지 3곳(수평프레스/수직프레스/로우)은 각 동작 검수 때 처리하기로 함
- **용어 치환 스코프**: `target_area`처럼 화면에 렌더링 안 되는 필드는 치환 대상에서 제외 (렌더링 여부는 코드에서 `.필드명` 접근 확인 후 판단)
- **영상 신뢰성**: 영상만 보고 판단하지 말고 절차가 의심되면 WebSearch로 임상 근거(Physiopedia, Orthofixar 등) 확인 후 수정 — 이번 세션에서 사용자가 직접 지적해 확립된 규칙
- 브라우저 자동화로 유튜브 영상 재생이 이 세션에서 계속 버퍼링/멈춤 현상 있었음 (Modified Thomas Test 영상) — 필요시 사용자 직접 확인이 더 빠를 수 있음
- Artifact는 index.html의 수동 미러이므로 매번 최신 버전 fetch→전체 Read→Edit→publish 순서 지켜야 함

## 다음 세션 권장 첫 프롬프트
`/resume`
