
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from src.agent._base import (
    build_openrouter_llm,
    load_model_spec,
    load_prompt_bundle,
)


PROMPT_PATH = (
    Path(__file__).resolve().parents[2]
    / "resources"
    / "prompt"
    / "product_develop"
    / "ProductDevelopAgent.yml"
)
MODEL_SPEC_PATH = (
    Path(__file__).resolve().parents[2]
    / "resources"
    / "spec"
    / "model_spec.yml"
)


class ProductDevelopAgent:
    def __init__(self) -> None:
        self.prompt = load_prompt_bundle(PROMPT_PATH)
        self.model_spec = load_model_spec(MODEL_SPEC_PATH)

        if self.model_spec.get("llm_lib") != "openrouter":
            raise ValueError(
                f"Unsupported llm_lib={self.model_spec.get('llm_lib')} (expected 'openrouter')"
            )

        self.llm = build_openrouter_llm(
            model_name=str(self.model_spec["model_name"]),
            temperature=float(self.model_spec["temperature"]),
        )

    def run(self, inputs: Dict[str, Any]) -> str:
        # ProductDevelopAgent.yml은 {formatfile_mcp_markdown} 같은 중괄호 포맷을 포함(이중 중괄호 아님)
        question = self.prompt.question_template.format(
            formatfile_mcp_markdown=inputs.get("formatfile_mcp_markdown", ""),
            insight_report_markdown=inputs.get("insight_report_markdown", ""),
            feedback_markdown_optional=inputs.get("feedback_markdown_optional", ""),
        )
        messages = [("system", self.prompt.system_prompt), ("user", question)]
        result = self.llm.invoke(messages)
        return getattr(result, "content", str(result))
