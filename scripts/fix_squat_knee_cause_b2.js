const fs = require('fs');

const phaseRaw = fs.readFileSync('C:/dev/exercisematerials/01.test/data/phase-exercises.json', 'utf8');
const phase = JSON.parse(phaseRaw);

const mv = phase.movements.find(m => m.id === 'back-squat');
const ps = mv.pain_sites.find(s => s.id === 'knee');
const cause = ps.causes.find(c => c.id === 'cause-b');
const stage = cause.route.stages[0];

// 홀수날 4번: 사이드라잉 힙 어브덕션으로 복구 (대둔근 집중)
stage.phase_a[3] = {
  "set": "a",
  "order": 4,
  "type": "활성화",
  "name": "사이드라잉 힙 어브덕션",
  "equipment": "없음",
  "target_area": "중둔근·대둔근",
  "why": "클램쉘보다 더 큰 범위에서 중둔근·대둔근을 강화합니다. 다리를 곧게 펴서 수행해 기능적 외전 근력을 높입니다.",
  "sets": "양측 각 15회 · 3세트",
  "cue": "발끝이 천장이 아닌 약간 아래를 향하게 합니다. 골반이 흔들리면 안 됩니다.",
  "how": [
    "옆으로 누워 다리를 곧게 뻗습니다",
    "위쪽 다리를 45도 정도까지 천천히 들어 올립니다",
    "1초 유지 후 천천히 내립니다",
    "양측 각 15회"
  ],
  "video_url": ""
};

// 짝수날 2번: 로우 런지 → 로우 런지+토르소 회전
stage.phase_a_b[1] = {
  "set": "b",
  "order": 2,
  "type": "스트레칭",
  "name": "로우 런지 + 토르소 회전",
  "equipment": "없음",
  "target_area": "고관절 굴곡근 + 흉추",
  "why": "고관절 굴곡근 이완과 동시에 흉추 회전 가동성을 확보합니다. 대둔근 활성화에 앞서 고관절 앞쪽 공간을 열고 상체 정렬을 함께 준비합니다.",
  "sets": "양측 각 45초 + 회전 5회 · 2세트",
  "cue": "골반을 앞으로 밀어 고관절 앞쪽을 늘린 뒤, 앞 무릎 쪽으로 팔을 들어 회전합니다.",
  "how": [
    "한쪽 무릎을 바닥에 대고 런지 자세를 취합니다",
    "골반을 앞으로 밀며 고관절 앞쪽을 30초 늘립니다",
    "앞발 쪽 팔을 천장으로 들어 올리며 상체를 회전합니다",
    "5회 회전 후 반대쪽 실시"
  ],
  "video_url": ""
};

// 짝수날 3번: 단하지 힙 브리지 → 사이드라잉 힙 어덕션 (내전근)
stage.phase_a_b[2] = {
  "set": "b",
  "order": 3,
  "type": "활성화",
  "name": "사이드라잉 힙 어덕션",
  "equipment": "없음",
  "target_area": "내전근",
  "why": "내전근을 직접 분리해 활성화합니다. 내전근이 제 역할을 해야 스쿼트 하강 시 무릎이 중립을 유지할 수 있습니다.",
  "sets": "양측 각 15회 · 3세트",
  "cue": "위쪽 다리를 앞에 구부려 발을 바닥에 놓고, 아래쪽 다리를 곧게 들어 올립니다. 골반 고정.",
  "how": [
    "옆으로 누워 위쪽 다리를 앞에 구부려 발을 바닥에 놓습니다",
    "아래쪽 다리를 곧게 편 채 천천히 들어 올립니다",
    "최대로 든 상태에서 1초 유지 후 천천히 내립니다",
    "양측 각 15회"
  ],
  "video_url": "https://www.youtube.com/watch?v=b8xKs6B1Zp8"
};

fs.writeFileSync(
  'C:/dev/exercisematerials/01.test/data/phase-exercises.json',
  JSON.stringify(phase, null, 2),
  'utf8'
);
console.log('cause-b 재수정 완료');
