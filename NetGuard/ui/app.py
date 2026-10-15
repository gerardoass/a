from __future__ import annotations

import os
import sys
import threading
import time
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

import customtkinter as ctk

# ----------------------------------------------------------------------
# Ancla de sys.path: garantiza que `ui` y `core` sean resolubles tanto
# en desarrollo como dentro del bundle --onefile (__file__ apunta a
# _MEIPASS/ui/app.py, por lo que parent.parent == raiz del bundle).
# ----------------------------------------------------------------------
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

# ----------------------------------------------------------------------
# Imports internos del paquete: RELATIVOS ESTRICTOS.
# Resuelven via __package__ = "ui", sin depender de la tabla absoluta
# del importador congelado.
# ----------------------------------------------------------------------
try:
    from . import theme
    from .theme import (BG_BASE, BG_CARD, BG_DEEP, BG_ELEV, BG_PANEL, LedDot,
                        NeonButton, NeonFrame, ScanBar, StatCard, bind_tree,
                        device_icon, glyph_icon)
except ImportError:  # red de seguridad si el paquete se aplana
    import ui.theme as theme  # type: ignore[no-redef]
    from ui.theme import (BG_BASE, BG_CARD, BG_DEEP, BG_ELEV, BG_PANEL, LedDot,
                          NeonButton, NeonFrame, ScanBar, StatCard, bind_tree,
                          device_icon, glyph_icon)  # type: ignore[no-redef]

from .console import Console

# ----------------------------------------------------------------------
# Nucleo de red
# ----------------------------------------------------------------------
try:
    from core import admin, arp, flood, latency, netinfo, oui, proc, scanner
    from core.scanner import Device, State
except ImportError:
    import admin, arp, flood, latency, netinfo, oui, proc, scanner  # type: ignore
    from scanner import Device, State  # type: ignore

APP = "NETGUARD"
VER = "2.0"