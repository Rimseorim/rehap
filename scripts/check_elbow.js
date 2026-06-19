const fs = require('fs');
const html = fs.readFileSync('C:/dev/exercisematerials/01.test/index.html', 'utf8');
const match = html.match(/const BUNDLED=(\{[\s\S]*?\});<\/script>/);
const data = JSON.parse(match[1]);
const movements = ['kipping','row','press-vertical','press-horizontal'];
const baseline = ['cause-a','cause-b','cause-c','cause-d'];
movements.forEach(m => {
  const site = data[m].pain_sites.find(s => s.id === 'elbow');
  if (!site) { console.log(m + ': no elbow'); return; }
  const ids = site.causes.map(c => c.id).join(', ');
  const diff = site.causes.some(c => baseline.indexOf(c.id) === -1);
  console.log(m + ': ' + ids + ' ' + (diff ? '<<DIFF>>' : '(동일)'));
});
