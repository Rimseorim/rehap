const fs = require('fs');
const phase = JSON.parse(fs.readFileSync('C:/dev/exercisematerials/01.test/data/phase-exercises.json', 'utf8'));

// 케틀벨/덤벨 등장 Phase B 항목에 무게 큐 prefix 추가
// 형식: [무게 안내] + [단계 핵심] + [기존 큐]

const weightPrefix = (gender, purpose) =>
  `본인이 10회 이상 무리 없이 들 수 있는 가벼운 케틀벨 또는 덤벨(여성 4~6kg / 남성 8~12kg 권장)을 준비하세요. 이번 단계의 핵심은 무거운 무게를 드는 것이 아니라, ${purpose}. `;

const updates = [
  // 무릎/스쿼트 cause-a Phase B step 3: 고블릿 스쿼트
  {
    mv: 'back-squat', ps: 'knee', cause: 'cause-a', pb_order: 3,
    purpose: '발뒤꿈치를 지면에 유지한 채 발목 배측굴곡 가동범위를 최대한 활용하는 능력을 확인하는 것입니다'
  },
  // 무릎/스쿼트 cause-b Phase B step 2: 고블릿 스쿼트
  {
    mv: 'back-squat', ps: 'knee', cause: 'cause-b', pb_order: 2,
    purpose: '팔꿈치 큐를 유지하며 둔근·내전근이 무릎 정렬을 스스로 잡는지 확인하는 것입니다'
  },
  // 무릎/스쿼트 cause-c Phase B step 2: 고블릿 스쿼트
  {
    mv: 'back-squat', ps: 'knee', cause: 'cause-c', pb_order: 2,
    purpose: '무게 중심 보조를 받아 무릎 전면 압박 없이 깊이 앉는 감각을 회복하는 것입니다'
  },
  // 무릎/스쿼트 cause-d Phase B step 2: 고블릿 스쿼트
  {
    mv: 'back-squat', ps: 'knee', cause: 'cause-d', pb_order: 2,
    purpose: '전방 부하의 도움을 받아 뒤꿈치를 지면에 붙인 채 Full ROM으로 앉는 패턴을 익히는 것입니다'
  },
  // 무릎/런지 cause-b Phase B step 3: 고블릿 런지
  {
    mv: 'lunge', ps: 'knee', cause: 'cause-b', pb_order: 3,
    purpose: '전방 부하로 상체 중립을 유지하며 둔근·내전근이 무릎 정렬을 스스로 잡는지 확인하는 것입니다'
  },
  // 무릎/런지 cause-c Phase B step 3: 고블릿 와이드 스탠스 런지
  {
    mv: 'lunge', ps: 'knee', cause: 'cause-c', pb_order: 3,
    purpose: 'TFL 과활성화 없이 엉덩이 뒤쪽으로 하중을 받아내는 고관절 주도 패턴을 인지하는 것입니다'
  },
  // 무릎/런지 cause-d Phase B step 3: 고블릿 미니 런지
  {
    mv: 'lunge', ps: 'knee', cause: 'cause-d', pb_order: 3,
    purpose: '45도 각도를 유지하며 무릎이 아닌 엉덩이 뒤쪽으로 하중을 받아내는 감각을 주입하는 것입니다'
  },
  // 무릎/런지 cause-e Phase B step 2: 고블릿 런지
  {
    mv: 'lunge', ps: 'knee', cause: 'cause-e', pb_order: 2,
    purpose: '전방 부하의 상체 중립 보조를 받아 균형과 정렬을 자연스럽게 잡는 감각을 익히는 것입니다'
  }
];

let count = 0;
updates.forEach(u => {
  const mv = phase.movements.find(m => m.id === u.mv);
  if (!mv) return;
  const ps = mv.pain_sites.find(s => s.id === u.ps);
  if (!ps) return;
  const cause = ps.causes.find(c => c.id === u.cause);
  if (!cause) return;
  const pb = cause.route.stages[0].phase_b;
  const step = pb.find(s => s.order === u.pb_order);
  if (!step) return;

  // 이미 "핵심은" 포함된 경우 중복 추가 방지
  if (step.cue.includes('핵심은')) {
    console.log('이미 적용됨 - 스킵:', u.mv, u.cause, 'step', u.pb_order);
    return;
  }

  step.cue = weightPrefix('', u.purpose) + step.cue;
  console.log('업데이트:', u.mv + '/' + u.ps + '/' + u.cause + ' step' + u.pb_order);
  count++;
});

fs.writeFileSync('C:/dev/exercisematerials/01.test/data/phase-exercises.json', JSON.stringify(phase, null, 2), 'utf8');
console.log('\n총', count, '개 항목 업데이트 완료');
