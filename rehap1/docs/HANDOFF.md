# HANDOFF - 2026-06-05 HH:MM

## 완료
- 직접 테스트(tests[]) 23개 슬롯 전체 채움 — 어깨(7)·팔꿈치(5)·손목(6)·고관절(3)·허리(2)
  - 어깨: Painful Arc / 동작별 2차 테스트 (squat 외회전, deadlift 내회전, pullup Dead Hang, kipping 후방신전, row 수평외전, press-v Empty Can, press-h 수평내전)
  - 팔꿈치: Cozen's → Reverse Cozen's 체인 (cause-a 외측 / b 내측 / c 이두건)
  - 손목: 신전 가동성(기도자세) → TFCC Stress 체인 (cause-a 가동성 / b 신전근 / c TFCC)
  - 고관절: FADIR → Thomas 체인 (squat·lunge), Hamstring → FADIR 체인 (deadlift)
  - 허리: 서서 과신전 검사 (kipping), Hollow Body Hold (pullup)
- 질문 흐름 → 테스트 체인 연결 (팔꿈치·손목·고관절·허리·어깨 통증경로)
  - 어깨: q2 c2(통증 경로)만 test 연결, q3·q4(Lumbar Lock·Apley's)는 유지
  - 고관절: 전체 cause 경로 → test 첫 번째
  - 허리: q2 cause 경로 → test 연결
- coming_soon 전체 해제 — deadlift·pullup·kipping·row 정식 진입 가능
- 번들 재빌드 — rehap1/index.html, rehap2/index.html
- rehap2 연동 — movement JSONs 전체 복사 + 번들 업데이트
- 통합 테스트 17케이스 전통과 확인

## 진행중
- 없음 (이번 세션 작업 모두 완료)

## 대기
- GitHub Pages 배포 (rehap1/index.html push → Rimseorim/rahap1)
- 어깨 q3·q4 내 cause-case1~4 경로 테스트 체인 확장 (현재 질문이 테스트 역할 중 — 기능은 정상)
- video_url 채우기 (현재 전부 빈 문자열, "▶ 영상으로 보기" 버튼은 유지)
- lunge.json 이후 동작 description·purpose·why 평문화 (이전 세션 대기 항목)
- PostgreSQL 전환 (현재 SQLite ephemeral)
- 네이버 앱 검수 신청
- rehap1/test_elbow_chain.png 잔여 파일 삭제 필요

## 결정사항 / 주의
- **번들 업데이트 방식**: `re.sub(r'const BUNDLED=\{.*?\};', ...)` — rehap1·rehap2 모두 동일
- **rehap2 연동**: rehap1/data/movements/ → rehap2/data/movements/ 복사 후 각자 bundle 재빌드
- **어깨 q3·q4 미연결 이유**: Lumbar Lock·Apley's Scratch가 이미 물리검사 형식이라 5개 원인을 2단계 체인으로 커버 불가, 질문 형식 유지가 더 정확
- **테스트 체인 구조**: tests[0]이 goRetest()에서 사용됨 (직접·회복 테스트 동일 내용)
- **백엔드 경로**: Railway는 루트 `backend/` 실행, `rehap1/backend/` 삭제됨
- **GitHub 레포**: `Rimseorim/rahap1` (오타 주의)
- **로컬 테스트**: localhost:8080, demo 계정 kim@rehab.com / 1234

## 다음 세션 권장 첫 프롬프트
`/resume` 후 "GitHub Pages 배포해줘"
