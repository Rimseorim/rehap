const fs = require('fs');

// ── index.html 수정 ──
const html = fs.readFileSync('C:/dev/exercisematerials/01.test/index.html', 'utf8');
const match = html.match(/const BUNDLED=(\{[\s\S]*?\});<\/script>/);
const bundled = JSON.parse(match[1]);

// 1. 허리/데드리프트 cause-b
const deadLB = bundled.deadlift.pain_sites.find(s => s.id === 'lower-back');
const deadCauseB = deadLB.causes.find(c => c.id === 'cause-b');
deadCauseB.tag = '가동성 부족';
deadCauseB.name = '고관절 신전 가동성 부족 → 요추 과신전 보상';
deadCauseB.description = '힙힌지 동작에서 고관절이 충분히 신전되지 않으면 척추가 대신 꺾여 보상합니다. 락아웃 단계에서 허리를 과하게 뒤로 젖히는 패턴이 대표적입니다. 고관절 신전 가동성과 고관절 굴곡근 유연성을 먼저 회복해야 합니다.';

console.log('1. 허리/데드 cause-b 수정 완료');

// 2. 고관절/스쿼트 cause-c
const sqHip = bundled.squat.pain_sites.find(s => s.id === 'hip');
const sqHipCauseC = sqHip.causes.find(c => c.id === 'cause-c');
sqHipCauseC.tag = '근력 부족·과긴장';
sqHipCauseC.name = '중둔근 약화 및 이상근 보상 과긴장';
sqHipCauseC.description = '중둔근이 약화되면 대퇴골이 안으로 무너지는 것을 이상근이 대신 잡으려 과보상합니다. 결과적으로 이상근이 과긴장되어 고관절 바깥쪽·엉덩이에 통증이 생깁니다. 중둔근 활성화와 이상근 이완을 함께 진행해야 합니다.';

console.log('2. 고관절/스쿼트 cause-c 수정 완료');

// 3. 고관절/런지 cause-c
const luHip = bundled.lunge.pain_sites.find(s => s.id === 'hip');
const luHipCauseC = luHip.causes.find(c => c.id === 'cause-c');
luHipCauseC.tag = '근력 부족·과긴장';
luHipCauseC.name = '중둔근 약화 및 이상근 보상 과긴장';
luHipCauseC.description = '런지 중 중둔근이 충분히 작동하지 않으면 이상근이 고관절을 안정시키기 위해 과보상합니다. 이상근 과긴장으로 고관절 바깥쪽·엉덩이에 통증이 생깁니다. 중둔근 활성화와 이상근 이완을 함께 진행해야 합니다.';

console.log('3. 고관절/런지 cause-c 수정 완료');

// index.html 저장
const newBundled = JSON.stringify(bundled);
const newHtml = html.replace(match[1], newBundled);
fs.writeFileSync('C:/dev/exercisematerials/01.test/index.html', newHtml, 'utf8');
console.log('index.html 저장 완료');

// ── phase-exercises.json 수정 ──
const phaseRaw = fs.readFileSync('C:/dev/exercisematerials/01.test/data/phase-exercises.json', 'utf8');
const phase = JSON.parse(phaseRaw);

// 1. 허리/데드리프트 cause-b
const pdDeadlift = phase.movements.find(m => m.id === 'deadlift');
const pdDeadLB = pdDeadlift && pdDeadlift.pain_sites.find(s => s.id === 'low_back');
const pdDeadCauseB = pdDeadLB && pdDeadLB.causes.find(c => c.id === 'cause-b');
if (pdDeadCauseB) {
  pdDeadCauseB.tag = '가동성 부족';
  pdDeadCauseB.name = '고관절 신전 가동성 부족 → 요추 과신전 보상';
  pdDeadCauseB.description = deadCauseB.description;
  console.log('phase-exercises: 허리/데드 cause-b 수정');
}

// 2. 고관절/스쿼트 cause-c
const pdSqMv = phase.movements.find(m => m.id === 'back-squat');
const pdSqHip = pdSqMv && pdSqMv.pain_sites.find(s => s.id === 'hip');
const pdSqCauseC = pdSqHip && pdSqHip.causes.find(c => c.id === 'cause-c');
if (pdSqCauseC) {
  pdSqCauseC.tag = '근력 부족·과긴장';
  pdSqCauseC.name = '중둔근 약화 및 이상근 보상 과긴장';
  pdSqCauseC.description = sqHipCauseC.description;
  console.log('phase-exercises: 고관절/스쿼트 cause-c 수정');
}

// 3. 고관절/런지 cause-c
const pdLuMv = phase.movements.find(m => m.id === 'lunge');
const pdLuHip = pdLuMv && pdLuMv.pain_sites.find(s => s.id === 'hip');
const pdLuCauseC = pdLuHip && pdLuHip.causes.find(c => c.id === 'cause-c');
if (pdLuCauseC) {
  pdLuCauseC.tag = '근력 부족·과긴장';
  pdLuCauseC.name = '중둔근 약화 및 이상근 보상 과긴장';
  pdLuCauseC.description = luHipCauseC.description;
  console.log('phase-exercises: 고관절/런지 cause-c 수정');
}

fs.writeFileSync('C:/dev/exercisematerials/01.test/data/phase-exercises.json', JSON.stringify(phase, null, 2), 'utf8');
console.log('phase-exercises.json 저장 완료');
