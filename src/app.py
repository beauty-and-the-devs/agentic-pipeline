from __future__ import annotations

import json
import logging
import os
import time
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv
from tqdm.auto import tqdm

from src.output_utils import ensure_output_dir, make_run_id, save_pipeline_state, save_step_output
from src.pipelines import (
    run_insight_process,
    run_marketing_contents,
    run_product_develop_with_review,
)


def _setup_logging(*, log_path: Path) -> None:
    # Log to both terminal (stdout) and a file.
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_format = "%(asctime)s | %(levelname)s | %(message)s"

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    # Avoid duplicate handlers if main() is called multiple times.
    if root_logger.handlers:
        for h in list(root_logger.handlers):
            root_logger.removeHandler(h)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(logging.Formatter(log_format))

    log_path.parent.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(log_format))

    root_logger.addHandler(stream_handler)
    root_logger.addHandler(file_handler)

    logging.info("Logging to %s", log_path)


def main() -> None:
    load_dotenv()

    run_id = os.getenv("RUN_ID") or make_run_id()
    out_dir = ensure_output_dir(run_id)

    _setup_logging(log_path=out_dir / "run.log")

    if not os.getenv("OPENROUTER_API_KEY"):
        raise RuntimeError(
            "OPENROUTER_API_KEY is not set. Put it in /home/ubuntu/agentic-pipeline/.env or export it in your shell."
        )

    # Load test input JSON (resources/test/input_data.json)
    input_path = Path(__file__).resolve().parents[1] / "resources" / "test" / "input_data.json"
    input_text = input_path.read_text(encoding="utf-8")

    # NOTE: resources/test/input_data.json contains a leading `// filepath: ...` comment which is not valid JSON.
    # We strip full-line `// ...` comments before parsing.
    cleaned_lines = [ln for ln in input_text.splitlines() if not ln.lstrip().startswith("//")]
    input_json: Dict[str, Any] = json.loads("\n".join(cleaned_lines))

    # Also persist the input we used for this run.
    (out_dir / "input_data.json").write_text(
        json.dumps(input_json, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    steps = [
        "insight_process (DataExtractAgent -> InsightGeneratorAgent)",
        "product_develop (+review loop)",
        "marketing_contents (PlotGeneratorAgent -> MarketingVideoGeneratorAgent)",
    ]

    state: Dict[str, Any] = {"input_json": input_json}

    with tqdm(total=len(steps), desc="Pipeline", unit="step") as pbar:
        t0 = time.time()
        logging.info("run_id=%s output_dir=%s", run_id, out_dir)

        logging.info("[1/3] Running insight_process...")
        state = run_insight_process(input_json)
        save_step_output(out_dir, "insight_process", state)
        pbar.update(1)
        logging.info("insight_process done (%.2fs)", time.time() - t0)

        t1 = time.time()
        logging.info("[2/3] Running product_develop_with_review...")
        state = run_product_develop_with_review(state, max_attempts=2)
        save_step_output(out_dir, "product_develop", state)
        save_step_output(out_dir, "product_review", state)
        pbar.update(1)
        logging.info(
            "product_develop_with_review done (%.2fs) pass=%s attempts=%s",
            time.time() - t1,
            state.get("product_review_pass"),
            state.get("product_develop_attempts"),
        )

        t2 = time.time()
        logging.info("[3/3] Running marketing_contents...")
        state = run_marketing_contents(state)
        save_step_output(out_dir, "marketing_contents", state)
        pbar.update(1)
        logging.info("marketing_contents done (%.2fs)", time.time() - t2)

    logging.info("Pipeline finished (%.2fs total)", time.time() - t0)

    save_pipeline_state(out_dir, state)

    print("=== Final State ===")
    print(json.dumps(state, ensure_ascii=False, indent=2))
    print(f"\nSaved outputs to: {out_dir}")


if __name__ == "__main__":
    main()
