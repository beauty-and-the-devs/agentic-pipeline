from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv


def test_openrouter_call_smoke() -> None:
    """Requires OPENROUTER_API_KEY to be set (skips if missing)."""

    # Allow `import src...` without requiring editable install
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    load_dotenv()

    if not os.getenv("OPENROUTER_API_KEY"):
        # pytest가 없어도 import 가능한 형태를 유지하기 위해 raise 대신 return
        return

    from src.agent.DataExtractAgent import DataExtractAgent

    agent = DataExtractAgent()
    out = agent.run({"hello": "world", "tiktok": {"views": 123}})

    assert isinstance(out, str)
    assert len(out) > 0
