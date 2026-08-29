const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const marker = 'const BUNDLED = ';
const start = html.indexOf(marker) + marker.length;
let i = start, depth = 0, inStr = false, esc = false;
for (; i < html.length; i++) {
  const c = html[i];
  if (inStr) {
    if (esc) esc = false;
    else if (c === '\\') esc = true;
    else if (c === '"') inStr = false;
  } else {
    if (c === '"') inStr = true;
    else if (c === '{') depth++;
    else if (c === '}') { depth--; if (depth === 0) { i++; break; } }
  }
}
const jsonStr = html.slice(start, i);
const data = JSON.parse(jsonStr);
fs.writeFileSync('scripts/_bundled_extract.json', jsonStr);

const movName = process.argv[2];
const mov = data[movName];
const reFig = /\d+\s*(회|초|분|세트)/;

for (const site of mov.pain_sites) {
  for (const cause of site.causes) {
    const stage3 = cause.route.stages.find(s => s.id === 'stage-3');
    if (!stage3 || !stage3.tips) continue;
    const concrete = stage3.tips.filter(t => reFig.test(t.body));
    if (concrete.length === 0) {
      console.log(`=== ${site.name} / ${cause.name} (${cause.id}) ===`);
      const stage1 = cause.route.stages.find(s => s.id === 'stage-1');
      console.log('phase_a:', JSON.stringify((stage1 && stage1.phase_a) || [], null, 0));
      stage3.tips.forEach((t, idx) => console.log(`  tip${idx}: [${t.title}] ${t.body}`));
    }
  }
}
