from __future__ import annotations

import json
import logging
import os
import time
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv
from tqdm.auto import tqdm

from src.pipelines import (
    run_insight_process,
    run_marketing_contents,
    run_product_develop_with_review,
)


def _setup_logging() -> None:
    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO"),
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def main() -> None:
    _setup_logging()
    load_dotenv()

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

    steps = [
        "insight_process (DataExtractAgent -> InsightGeneratorAgent)",
        "product_develop (+review loop)",
        "marketing_contents (PlotGeneratorAgent -> MarketingVideoGeneratorAgent)",
    ]

    state: Dict[str, Any] = {"input_json": input_json}

    with tqdm(total=len(steps), desc="Pipeline", unit="step") as pbar:
        t0 = time.time()
        logging.info("[1/3] Running insight_process...")
        state = run_insight_process(input_json)
        pbar.update(1)
        logging.info("insight_process done (%.2fs)", time.time() - t0)

        t1 = time.time()
        logging.info("[2/3] Running product_develop_with_review...")
        state = run_product_develop_with_review(state, max_attempts=2)
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
        pbar.update(1)
        logging.info("marketing_contents done (%.2fs)", time.time() - t2)

    logging.info("Pipeline finished (%.2fs total)", time.time() - t0)

    print("=== Final State ===")
    print(json.dumps(state, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
