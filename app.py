"""
Repo-root entry for Streamlit. Run from this folder:

    streamlit run app.py

This loads the real Market Intel Agent so you never hit a missing file or an old copy elsewhere.
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_TARGET = _ROOT / "Generative-AI-Projects_bob" / "market-intel-agent" / "app.py"

if not _TARGET.is_file():
    sys.stderr.write(f"Market Intel app not found at:\n  {_TARGET}\n")
    raise SystemExit(1)

# Real app expects imports relative to market-intel-agent/
_MIA = str(_TARGET.parent)
if _MIA not in sys.path:
    sys.path.insert(0, _MIA)

runpy.run_path(str(_TARGET), run_name="__main__")
