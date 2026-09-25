"""Use real APM to check install, frozen restoration, resources, and tampering."""
import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile
import yaml

ROOT = Path(__file__).resolve().parents[1]


def run(*args, cwd, check=True):
    return subprocess.run(args, cwd=cwd, check=check)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', help='Published owner/repository#full-commit; otherwise local package')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='stamped-apm-') as temp:
        base = Path(temp)
        package = base / 'package'
        package.mkdir()
        shutil.copy2(ROOT / 'apm.yml', package / 'apm.yml')
        shutil.copytree(ROOT / 'skills', package / 'skills')
        dependency = {'path': '../package', 'skills': ['stamped-assess']}
        if args.source:
            name, commit = args.source.rsplit('#', 1)
            if len(commit) != 40 or any(c not in '0123456789abcdef' for c in commit):
                parser.error('source must use a full commit hash')
            dependency = {'git': name, 'ref': commit, 'skills': ['stamped-assess']}
        consumer = base / 'consumer'
        consumer.mkdir()
        (consumer / 'apm.yml').write_text(yaml.safe_dump({
            'name': 'assessment-consumer', 'version': '0.0.0',
            'targets': ['agent-skills', 'claude'], 'dependencies': {'apm': [dependency]},
        }, sort_keys=False))
        (consumer / '.gitignore').write_text('/apm_modules/\n/.agents/skills/\n/.claude/skills/\n')
        run('git', 'init', '--quiet', cwd=consumer)
        # The disposable fixture has no organization policy or credentials.
        run('apm', 'install', '--no-policy', cwd=consumer)
        original = {name: (consumer / name).read_bytes() for name in ('apm.yml', 'apm.lock.yaml', '.gitignore')}
        for folder in (consumer, base / 'fresh'):
            if folder != consumer:
                folder.mkdir()
                for name, content in original.items():
                    (folder / name).write_bytes(content)
                run('git', 'init', '--quiet', cwd=folder)
                run('apm', 'install', '--frozen', '--no-policy', cwd=folder)
            for deployed in (folder / '.agents/skills/stamped-assess', folder / '.claude/skills/stamped-assess'):
                for source in (package / 'skills/stamped-assess').rglob('*'):
                    if source.is_file():
                        target = deployed / source.relative_to(package / 'skills/stamped-assess')
                        assert target.is_file(), f'missing {target}'
                        assert target.read_bytes() == source.read_bytes(), f'changed {target}'
                run('git', 'check-ignore', str(deployed / 'SKILL.md'), cwd=folder)
            assert all((folder / name).read_bytes() == content for name, content in original.items())
            run('apm', 'audit', '--ci', '--no-policy', cwd=folder)
        victim = base / 'fresh/.agents/skills/stamped-assess/SKILL.md'
        victim.write_text(victim.read_text() + '\nUnexpected local change.\n')
        assert run('apm', 'audit', '--ci', '--no-policy', cwd=base / 'fresh', check=False).returncode != 0
        print('Installation, frozen restoration, both agent targets, resources, and tamper detection passed.')


if __name__ == '__main__':
    main()
