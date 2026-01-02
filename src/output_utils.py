from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def ensure_output_dir(run_id: str) -> Path:
    out_dir = get_project_root() / "output" / run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def make_run_id(prefix: str = "run") -> str:
    # Example: run_20260102_235959
    return f"{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def save_pipeline_state(out_dir: Path, state: Dict[str, Any]) -> None:
    write_json(out_dir / "final_state.json", state)


def save_step_output(out_dir: Path, step_name: str, state: Dict[str, Any]) -> None:
    """Persist known pipeline artifacts by convention."""

    mapping = {
        "insight_process": [("insight_report_md", "insight_report.md")],
        "product_develop": [("product_report_md", "product_report.md")],
        "product_review": [("product_review_json", "product_review.json")],
        "marketing_contents": [
            ("plot_report_md", "plot_report.md"),
            ("marketing_videos_json", "marketing_videos.json"),
        ],
    }

    for key, filename in mapping.get(step_name, []):
        val = state.get(key)
        if val is None:
            continue
        # Most artifacts are strings.
        write_text(out_dir / filename, str(val))
