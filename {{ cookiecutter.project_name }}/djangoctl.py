#!/usr/bin/env python3
import os
import shutil

import click


@click.group(context_settings={'help_option_names': ['-h', '--help']})
def main():
    pass


@click.command()
def dirs():
    for path in ['static/assets', 'static/collected']:
        if not os.path.exists(path):
            print('Creating dir %s' % path)
            os.makedirs(path, exist_ok=True)
        else:
            print('Dir already exists: %s' % path)


@click.command()
def static():
    os.execlp('./manage.py', './manage.py', 'collectstatic', '--link', '--noinput')


@click.command()
def run():
    os.execlp('./manage.py', './manage.py', 'runserver', '--settings=project.settings_debug', '0.0.0.0:8001')
    

@click.command()
def shell():
    os.execlp('./manage.py', './manage.py', 'shell_plus')


@click.command()
def secret_key():
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())


@click.command()
def convert_subdir_web():
    res = input(
        'DANGER! Are you sure you want convert project to subdir web?'
        ' Type "convert" to continue: '
    )
    if res == 'convert':
        # Empty dirs
        for path in ['web', 'unused_files', 'unused_files/project']:
            print('[OK] Creating directory %s' % path)
            os.makedirs(path, exist_ok=True)

        # Empty files
        for path in ['web/__init__.py']:
            print('[OK] Creating file %s' % path)
            with open(path, 'w') as out:
                out.write('')

        # Main files: x --> web/x
        for path, new_path in [
                ('board', 'board'),
                ('static', 'static'),
                ('templates', 'templates'),
                ('project/settings_debug.py', 'settings_debug.py'),
                ('project/settings_local.py', 'settings_local.py'),
                ('project/settings.py', 'settings.py'),
                ('project/urls.py', 'urls.py'),
                ('project/wsgi.py', 'wsgi.py'),
                ('project/asgi.py', 'asgi.py'),
            ]:
            if os.path.exists(path):
                print('[OK] Moving directory %s to web/%s' % (path, new_path))
                shutil.move(path, 'web/%s' % new_path)
            else:
                print(
                    '[FAIL] Can\'t move %s to web/%s. Source does not exists'
                    % (path, new_path)
                )

        # Unused files
        for path in [
                'Makefile', 'requirements.txt', 'var',
                'project/config.py',
                'project/database.py',
            ]:
            if os.path.exists(path):
                print('[OK] Moving file %s to unused_files/%s' % (path, path))
                shutil.move(path, 'unused_files/%s' % path)
            else:
                print(
                    '[FAIL] Can\'t move file %s to unsed_files/%s. Source does not exists'
                    % (path, path)
                )

        # Remove project dir
        if os.path.exists('project'):
            for fname in os.listdir('project'):
                if fname not in ('__init__.py', '__pycache__'):
                    print('[FATAL] Unprocessed file project/%s' % fname)
                    sys.exit(1)
            print('Removing directory project')
            shutil.rmtree('project')
        else:
            print('[FAIL] Can\'t remove directory project, it does not exist.')

        # Fix references
        for path, search, replace in (
                ['manage.py', "'project.settings'", "'web.settings'"],
                ['djangoctl.py', "settings=project.settings", "settings=web.settings"],
                ['web/urls.py', "'board.urls'", "'web.board.urls'"],
                ['web/settings.py', "'board'", "'web.board'"],
                ['web/settings.py', "'project.urls'", "'web.urls'"],
                ['web/settings.py', "'project.wsgi.application'", "'web.wsgi.application'"],
                ['web/settings.py', "'templates'", "'web.templates'"],
            ):
            with open(path) as inp:
                data = inp.read()
            new_data = data.replace(search, replace)
            with open(path, 'w') as out:
                out.write(new_data)
            flag = 'CHANGED' if data != new_data else 'NOT CHANGED'
            print('[%s] %s: %s --> %s' % (flag, path, search, replace))

    else:
        print('Unknown response. Cancelig')
        sys.exit(1)


main.add_command(dirs)
main.add_command(static)
main.add_command(run)
main.add_command(shell)
main.add_command(secret_key)
main.add_command(convert_subdir_web)


if __name__ == '__main__':
    main()
