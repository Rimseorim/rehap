"""정본(index.html BUNDLED)에서 data/phase-exercises.json 을 다시 만든다.

사용: python scripts/export_phase_exercises.py      (레포 루트에서 실행)
방향은 항상 정본 → 사본이다. 이 파일을 직접 고치거나 거꾸로 합치지 않는다.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rehab_data import PHASE, export_phase, exercises, load_bundled, save_phase  # noqa: E402

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    b, _ = load_bundled()
    phase = export_phase(b)
    save_phase(phase)
    n_causes = sum(len(ps['causes']) for mv in phase['movements'] for ps in mv['pain_sites'])
    n_ex = sum(len(st.get('phase_a', [])) + len(st.get('phase_b', []))
               for mv in phase['movements'] for ps in mv['pain_sites'] for c in ps['causes'] for st in c['route']['stages'])
    print(f'{PHASE} 작성: 동작 {len(phase["movements"])} · 원인 {n_causes} · Phase A/B 운동 {n_ex} (정본 전체 운동 {len(list(exercises(b)))})')
