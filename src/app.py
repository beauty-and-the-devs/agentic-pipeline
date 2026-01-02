from __future__ import annotations

import json
import os
from typing import Any, Dict

from dotenv import load_dotenv

from src.pipelines import run_insight_process, run_marketing_contents, run_product_develop
from src.pipelines_graph import build_app_graph


def main() -> None:
    load_dotenv()

    if not os.getenv("OPENROUTER_API_KEY"):
        raise RuntimeError(
            "OPENROUTER_API_KEY is not set. Put it in /home/ubuntu/agentic-pipeline/.env or export it in your shell."
        )

    # TODO: 실제 입력 소스 연결 전까지는 샘플 JSON을 사용
    input_json: Dict[str, Any] = {
        "example": True,
        "note": "replace this with your collected MCP/Agent/PDF extracted JSON",
    }

    # 프로세스 순서: insight_process -> product_develop -> marketing_contents
    # 1) 기존 방식(순차 실행)
    state = run_insight_process(input_json)
    state = run_product_develop(state)
    state = run_marketing_contents(state)

    # 2) LangGraph 방식(동일 순서 그래프)
    # graph_state = build_app_graph().compile().invoke({"input_json": input_json})

    print("=== Final State ===")
    print(json.dumps(state, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
