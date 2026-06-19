const fs = require('fs');
const d = fs.readFileSync('C:/dev/exercisematerials/01.test/data/phase-exercises.json', 'utf8');
const j = JSON.parse(d);
const m = j.movements[0];
const ps = m.pain_sites[0];
const c = ps.causes[0];
console.log('cause keys:', Object.keys(c));
console.log('route keys:', Object.keys(c.route));
console.log('stages count:', c.route.stages.length);
c.route.stages.forEach((s, i) => {
  console.log('stage[' + i + '] keys:', Object.keys(s));
});
