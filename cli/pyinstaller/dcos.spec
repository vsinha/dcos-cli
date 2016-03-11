# -*- mode: python -*-
import os

a = Analysis(['../dcoscli/main.py'],
             pathex=[os.getcwd()],
             datas=[('../dcoscli/data/help/*', 'dcoscli/data/help'),
                    ('../../dcos/data/config-schema/*', 'dcos/data/config-schema'),
                    ('../dcoscli/data/config-schema/*', 'dcoscli/data/config-schema')
                    ])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='dcos',
          debug=False,
          strip=None,
          upx=True,
          console=True)
