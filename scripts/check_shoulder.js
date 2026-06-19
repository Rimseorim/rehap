const fs = require('fs');
const html = fs.readFileSync('C:/dev/exercisematerials/01.test/index.html', 'utf8');
const match = html.match(/const BUNDLED=(\{[\s\S]*?\});<\/script>/);
const data = JSON.parse(match[1]);
const movements = ['kipping','row','press-vertical','press-horizontal'];
const baseline = ['cause-dp','cause-case1','cause-case2','cause-case3','cause-case4','cause-d'];
movements.forEach(m => {
  const site = data[m].pain_sites.find(s => s.id === 'shoulder');
  if (!site) { console.log(m + ': no shoulder'); return; }
  const ids = site.causes.map(c => c.id).join(', ');
  const diff = site.causes.some(c => baseline.indexOf(c.id) === -1);
  console.log(m + ': ' + ids + ' ' + (diff ? '<<DIFF>>' : '(동일)'));
});
