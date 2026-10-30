"""Double-click (or auto-start) launcher: opens the Orion window without a console."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from orion.cli import main  # noqa: E402

sys.exit(main([]))
