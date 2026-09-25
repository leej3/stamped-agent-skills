"""Install the skill's exact public tool dependency into a disposable environment."""
from pathlib import Path
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='stamped-dependency-') as temp:
    base = Path(temp)
    subprocess.run([sys.executable, '-m', 'venv', str(base / 'env')], check=True)
    python = base / 'env/bin/python'
    subprocess.run([str(python), '-m', 'pip', 'install', '-r',
                    str(root / 'skills/stamped-assess/requirements.txt')], check=True, cwd=base)
    cli = base / 'env/bin/stamped-assess'
    for kind in ('use_case', 'object', 'rubric', 'assessment', 'review'):
        subprocess.run([str(cli), 'schema', kind], check=True, cwd=base,
                       stdout=subprocess.DEVNULL)
    subprocess.run([str(python), '-c',
                    'from stamped_assessment.store import references; references()'],
                   check=True, cwd=base)
    print('Pinned public assessment dependency installs with all schemas and reference data.')
