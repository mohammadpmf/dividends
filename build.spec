# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import os
import crispy_forms

def get_crispy_forms_path():
    return os.path.dirname(crispy_forms.__file__)


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config/', 'config/'),
        ('dividends/', 'dividends/'),
        ('templates/', 'templates/'),
        ('static/', 'static/'),
        ('manage.py', '.'),
        
        # Include crispy_forms templates and static files
        (get_crispy_forms_path(), 'crispy_forms'),
        
        (os.path.join(get_crispy_forms_path(), 'templates'), 'crispy_forms/templates'),
        
    ],
    hiddenimports=[
        'django',
        'django.core',
        'django.contrib',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.humanize',
        'crispy_forms',
        'crispy_bootstrap5',
        'bootstrap5',
        'dividends',
        'config',
        'mysql',
        'MySQLdb',
        'crispy_forms',
        'crispy_forms.templatetags',
        'crispy_forms.templatetags.crispy_forms_filters',
        'crispy_forms.templatetags.crispy_forms_field',
        'crispy_forms.templatetags.crispy_forms_utils',        
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='config',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Set to False if you don't want console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)