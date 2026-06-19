const fs = require('fs');

const phaseRaw = fs.readFileSync('C:/dev/exercisematerials/01.test/data/phase-exercises.json', 'utf8');
const phase = JSON.parse(phaseRaw);

const mv = phase.movements.find(m => m.id === 'back-squat');
const ps = mv.pain_sites.find(s => s.id === 'knee');
const cause = ps.causes.find(c => c.id === 'cause-b');
const stage = cause.route.stages[0];

// 홀수날 4번: 사이드라잉 힙 어브덕션 → 사이드라잉 힙 어덕션 (내전근)
stage.phase_a[3] = {
  "set": "a",
  "order": 4,
  "type": "활성화",
  "name": "사이드라잉 힙 어덕션",
  "equipment": "없음",
  "target_area": "내전근",
  "why": "내전근을 직접 분리해 활성화합니다. 내전근이 제 역할을 해야 스쿼트 하강 시 무릎이 안정적으로 중립을 유지할 수 있습니다.",
  "sets": "양측 각 15회 · 3세트",
  "cue": "위쪽 다리는 바닥에 두고, 아래쪽 다리를 들어 올립니다. 골반이 흔들리지 않도록 고정합니다.",
  "how": [
    "옆으로 누워 위쪽 다리를 앞에 구부려 발을 바닥에 놓습니다",
    "아래쪽 다리를 곧게 편 채 천천히 들어 올립니다",
    "최대로 든 상태에서 1초 유지 후 천천히 내립니다",
    "양측 각 15회"
  ],
  "video_url": "https://www.youtube.com/watch?v=b8xKs6B1Zp8"
};

// Phase B 순서 재배치: 루프 밴드 박스 스쿼트 → 고블릿 스쿼트 → 맨몸 프리 스쿼트 → PVC 백스쿼트
stage.phase_b = [
  {
    "order": 1,
    "name": "루프 밴드 박스 스쿼트",
    "equipment": "루프 밴드 + 박스",
    "rom": "밴드 외전 저항 + 박스 깊이 제한 — 보조가 가장 많은 시작점",
    "why": "밴드가 무릎 외전을 요구해 둔근·내전근 동시 활성화를 강제하고, 박스가 깊이를 제한해 통증 없이 패턴을 익힙니다.",
    "sets": "10회 · 3세트",
    "cue": "무릎이 밴드에 지지 않도록 새끼발가락 방향으로 밀어냅니다. 박스에 살짝 터치하고 바로 올라옵니다.",
    "how": [
      "루프 밴드를 무릎 바로 위에 걸고 박스 앞에 섭니다",
      "천천히 앉으며 무릎이 새끼발가락 방향을 향하는지 확인합니다",
      "박스에 엉덩이가 살짝 닿으면 바로 일어섭니다",
      "10회"
    ],
    "video_url": "https://www.youtube.com/watch?v=fjuZGrlWLbY"
  },
  {
    "order": 2,
    "name": "고블릿 스쿼트",
    "equipment": "케틀벨 또는 덤벨 8~12kg",
    "rom": "밴드 없이, 무게가 상체를 수직으로 잡아줘 정렬 유지 보조",
    "why": "앞에 든 무게와 팔꿈치로 무릎 밀기 큐가 자연스럽게 둔근·내전근을 활성화합니다. 밴드 없이 스스로 정렬을 잡는 첫 단계.",
    "sets": "10회 · 3세트",
    "cue": "팔꿈치를 무릎 안쪽으로 밀어 무릎이 벌어지게 합니다.",
    "how": [
      "케틀벨을 가슴 앞에 양손으로 잡고 섭니다",
      "팔꿈치로 무릎 안쪽을 밀어내며 천천히 앉습니다",
      "최대 깊이에서 무릎이 발끝 방향을 유지하는지 확인합니다",
      "10회"
    ],
    "video_url": "https://www.youtube.com/watch?v=kIQcvQ6ew3k"
  },
  {
    "order": 3,
    "name": "맨몸 프리 스쿼트",
    "equipment": "없음",
    "rom": "보조 없이 둔근·내전근 스스로 무릎을 잡는 단계",
    "why": "외부 보조 없이 패턴이 유지되는지 확인합니다. 무릎이 안으로 들어오면 이전 단계로 돌아갑니다.",
    "sets": "15회 · 3세트",
    "cue": "하강 시 무릎이 안으로 들어오면 해당 세트를 즉시 중단합니다.",
    "how": [
      "발을 어깨너비, 발끝 30도 바깥으로 향하고 섭니다",
      "무릎이 새끼발가락 방향을 향하는 것을 의식하며 천천히 앉습니다",
      "거울이나 동영상으로 무릎 방향을 확인합니다",
      "15회"
    ],
    "video_url": "https://www.youtube.com/watch?v=9cy2Bi2n9-U"
  },
  {
    "order": 4,
    "name": "PVC 백스쿼트",
    "equipment": "PVC 파이프",
    "rom": "실제 WOD 자세 적용 — 바 위치에서 둔근·내전근 패턴 최종 확인",
    "why": "백스쿼트 자세에서 둔근·내전근 활성화 패턴을 확인합니다. PVC는 무게 부담 없이 실제 동작 자세를 점검하기에 적합합니다.",
    "sets": "15회 · 3세트",
    "cue": "하강 시 의도적으로 무릎을 새끼발가락 방향으로 밀어냅니다.",
    "how": [
      "PVC를 승모근 위에 올리고 양손으로 잡습니다",
      "발을 어깨너비, 발끝 30도 바깥으로 향합니다",
      "가슴을 세우고 무릎을 발끝 방향으로 밀며 앉습니다",
      "15회, 무릎 방향에 집중합니다"
    ],
    "video_url": "https://www.youtube.com/watch?v=Nxl7WKiFcA0"
  }
];

fs.writeFileSync(
  'C:/dev/exercisematerials/01.test/data/phase-exercises.json',
  JSON.stringify(phase, null, 2),
  'utf8'
);
console.log('cause-b 수정 완료 — 내전근 활성화 추가, Phase B 순서 재배치');
