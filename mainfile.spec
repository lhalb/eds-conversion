# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\ebeam\\PycharmProjects\\eds-conversion\\main.py'],
             binaries=[],
             datas=[],
             hiddenimports=['scipy.special.cython_special'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['IPython', 'FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas + [
          ('icons/chart.png', 'icons/chart.png', 'DATA'),
          ('icons/file.png', 'icons/file.png', 'DATA'),
          ('icons/folder.png', 'icons/folder.png', 'DATA'),
          ('icons/green_light-512px.png', 'icons/green_light-512px.png', 'DATA'),
          ('icons/red_light-512px.png', 'icons/red_light-512px.png', 'DATA'),
          ('icons/start-512px.png', 'icons/start-512px.png', 'DATA'),
          ],
          [],
          name='EDS-Analysis',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='icons/appicon.ico',
          version='version.rc')
