# -*- mode: python -*-
a = Analysis(['clearConsoleWidget27_new2.py'],
             pathex=['C:\\python'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
a.datas += [('favicon2.ico','C:\\python\\favicon2.ico','DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='clearConsoleWidget27_new2.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , version='version.txt', icon='favicon2.ico')
