# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller: un unico .exe sin consola, con manifest UAC admin."""
from PyInstaller.utils.hooks import collect_all, collect_submodules

scapy_d, scapy_b, scapy_h = collect_all("scapy")
ctk_d, ctk_b, ctk_h = collect_all("customtkinter")
pil_d, pil_b, pil_h = collect_all("PIL")

hidden = (scapy_h + ctk_h + pil_h
          + collect_submodules("scapy.layers")
          + ["scapy.arch.windows", "scapy.layers.l2", "scapy.layers.inet",
             "scapy.sendrecv", "PIL._tkinter_finder"])

a = Analysis(["main.py"], pathex=[],
             binaries=scapy_b + ctk_b + pil_b,
             datas=scapy_d + ctk_d + pil_d,
             hiddenimports=hidden, hookspath=[], runtime_hooks=[],
             excludes=["matplotlib", "numpy.testing", "pytest", "IPython",
                       "PyQt5", "PyQt6", "PySide2", "PySide6"],
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas, [],
          name="NetGuard", debug=False, strip=False, upx=True,
          runtime_tmpdir=None, console=False, uac_admin=True, icon=None)