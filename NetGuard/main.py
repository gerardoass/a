#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NetGuard v2.0 - Punto de entrada.

Importa la GUI por ruta directa (ui.app), nunca a traves del
__init__ del paquete, y ancla la raiz a sys.path antes de cualquier
import interno.
"""
from __future__ import annotations

import ctypes
import os
import sys


# ----------------------------------------------------------------------
def _base_dir() -> str:
    if getattr(sys, "frozen", False):
        return getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(sys.executable)))
    return os.path.dirname(os.path.abspath(__file__))


def _bootstrap_path() -> None:
    base = _base_dir()
    if base and base not in sys.path:
        sys.path.insert(0, base)


def _dpi() -> None:
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass


def _fatal(msg: str) -> None:
    try:
        ctypes.windll.user32.MessageBoxW(None, msg, "NetGuard - Error fatal", 0x10)
    except Exception:
        print(msg)


# ----------------------------------------------------------------------
def main() -> None:
    _bootstrap_path()
    _dpi()

    from core import admin
    admin.ensure_admin(auto_elevate=True)

    # RUTA DIRECTA: nunca "from ui import run"
    from ui.app import run

    try:
        run()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as exc:
        import traceback
        _fatal(f"{exc}\n\n{traceback.format_exc()}")
        raise


if __name__ == "__main__":
    main()