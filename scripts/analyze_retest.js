const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const marker = 'const BUNDLED=';
const start = html.indexOf(marker) + marker.length;
let i = start;
if (html[i] !== '{') throw new Error('unexpected start');
let depth = 0, inStr = false, esc = false;
for (; i < html.length; i++) {
  const c = html[i];
  if (inStr) {
    if (esc) { esc = false; continue; }
    if (c === '\\') { esc = true; continue; }
    if (c === '"') { inStr = false; continue; }
    continue;
  } else {
    if (c === '"') { inStr = true; continue; }
    if (c === '{') depth++;
    else if (c === '}') { depth--; if (depth === 0) { i++; break; } }
  }
}
const BUNDLED = JSON.parse(html.slice(start, i));

// Resolve a question's choices down to their ultimate "next" targets (test:/cause:/danger),
// following q:qN chains. Returns array of {path, text, finalNext}
function resolveChoices(psd, qid, prefix) {
  const q = (psd.questions || []).find(x => x.id === qid);
  if (!q) return [];
  let out = [];
  for (const ch of q.choices || []) {
    const label = prefix ? `${prefix}>${ch.text}` : ch.text;
    if (typeof ch.next === 'string' && ch.next.startsWith('q:')) {
      out = out.concat(resolveChoices(psd, ch.next.slice(2), label));
    } else {
      out.push({ path: label, next: ch.next });
    }
  }
  return out;
}

const seen = new Map();

for (const m of BUNDLED.manifest) {
  const mdata = BUNDLED[m.id];
  if (!mdata) continue;
  for (const psd of mdata.pain_sites || []) {
    if (!psd || psd.coming_soon) continue;
    const causes = psd.causes || [];
    const tests = psd.tests || [];
    const sig = JSON.stringify({
      causes: causes.map(c => [c.id, c.name, c.tag]),
      tests: tests.map(t => [t.id, t.pass_next, t.fail_next]),
      entry: resolveChoices(psd, psd.entry_question, '').map(x => [x.path, x.next])
    });
    if (!seen.has(sig)) seen.set(sig, []);
    seen.get(sig).push(`${m.name}(${m.id})`);
  }
}

let idx = 0;
for (const [sig, movements] of seen) {
  idx++;
  const data = JSON.parse(sig);
  console.log(`\n##### TEMPLATE ${idx} — movements: ${movements.join(', ')} #####`);
  console.log('causes: ' + data.causes.map(c => `${c[0]}=${c[1]} [${c[2]}]`).join(' | '));
  console.log('entry choices -> :');
  for (const [path, next] of data.entry) {
    console.log(`  [${path}] -> ${next}`);
  }
  console.log('tests:');
  for (const [tid, pass, fail] of data.tests) {
    console.log(`  ${tid}: pass->${pass}  fail->${fail}`);
  }
}
console.log(`\nTOTAL TEMPLATES: ${idx}`);
