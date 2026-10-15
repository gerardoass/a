from __future__ import annotations

import queue
import sys
import time
import tkinter as tk
from pathlib import Path

# ----------------------------------------------------------------------
# Ancla de sys.path (misma logica que en app.py)
# ----------------------------------------------------------------------
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

# ----------------------------------------------------------------------
# Tema: import relativo estricto
# ----------------------------------------------------------------------
try:
    from . import theme
except ImportError:  # red de seguridad
    import ui.theme as theme  # type: ignore[no-redef]