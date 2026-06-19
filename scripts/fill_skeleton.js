const fs = require('fs');

const html = fs.readFileSync('C:/dev/exercisematerials/01.test/index.html', 'utf8');
const match = html.match(/const BUNDLED=(\{[\s\S]*?\});<\/script>/);
const bundled = JSON.parse(match[1]);

const phaseFile = fs.readFileSync('C:/dev/exercisematerials/01.test/data/phase-exercises.json', 'utf8');
const phaseData = JSON.parse(phaseFile);

// ID mappings: BUNDLED -> file
const mvMap = {
  'squat': 'back-squat',
  'lunge': 'lunge',
  'deadlift': 'deadlift',
  'pullup': 'pullup',
  'kipping': 'kipping',
  'row': 'row',
  'press-vertical': 'vertical-press',
  'press-horizontal': 'horizontal-press'
};
const mvNameMap = {
  'squat': '백스쿼트',
  'lunge': '런지',
  'deadlift': '데드리프트',
  'pullup': '풀업',
  'kipping': '키핑',
  'row': '로우',
  'press-vertical': '수직 프레스',
  'press-horizontal': '수평 프레스'
};
const psMap = {
  'knee': 'knee',
  'lower-back': 'low_back',
  'ankle': 'ankle',
  'shoulder': 'shoulder',
  'hip': 'hip',
  'wrist': 'wrist',
  'elbow': 'elbow',
  'chest': 'chest'
};
const psNameMap = {
  'knee': '무릎',
  'lower-back': '허리',
  'ankle': '발목',
  'shoulder': '어깨',
  'hip': '고관절',
  'wrist': '손목',
  'elbow': '팔꿈치',
  'chest': '흉근'
};

const bundledMovements = ['squat','lunge','deadlift','pullup','kipping','row','press-vertical','press-horizontal'];

let added = 0;

bundledMovements.forEach(bMvId => {
  const bMv = bundled[bMvId];
  if (!bMv) return;

  const fileId = mvMap[bMvId];
  const fileName = mvNameMap[bMvId];

  // Find or create movement in file
  let fileMv = phaseData.movements.find(m => m.id === fileId);
  if (!fileMv) {
    fileMv = { id: fileId, name: fileName, pain_sites: [] };
    phaseData.movements.push(fileMv);
    console.log('+ movement:', fileId);
  }

  bMv.pain_sites.forEach(bPs => {
    const filePsId = psMap[bPs.id];
    if (!filePsId) return;
    const filePsName = psNameMap[bPs.id];

    // Find or create pain_site in file movement
    let filePs = fileMv.pain_sites.find(ps => ps.id === filePsId);
    if (!filePs) {
      filePs = { id: filePsId, name: filePsName, causes: [] };
      fileMv.pain_sites.push(filePs);
      console.log('  + pain_site:', fileId + '/' + filePsId);
    }

    if (!bPs.causes) return;
    bPs.causes.forEach(bCause => {
      // Check if cause already exists
      const exists = filePs.causes.find(c => c.id === bCause.id);
      if (exists) return;

      // Add skeleton
      const skeleton = {
        id: bCause.id,
        label: bCause.label || '',
        tag: bCause.tag || '',
        name: bCause.name || '',
        description: bCause.description || '',
        priority_note: bCause.priority_note || '',
        route: {
          stages: [{
            id: 'stage-1',
            name: '기초재활',
            phase_a: [],
            phase_a_b: [],
            phase_b: []
          }]
        }
      };
      filePs.causes.push(skeleton);
      added++;
      console.log('    + cause:', fileId + '/' + filePsId + '/' + bCause.id);
    });
  });
});

fs.writeFileSync(
  'C:/dev/exercisematerials/01.test/data/phase-exercises.json',
  JSON.stringify(phaseData, null, 2),
  'utf8'
);
console.log('\n총 추가:', added, '개 cause 스켈레톤');
