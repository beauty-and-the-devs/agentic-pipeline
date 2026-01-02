from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from src.agent._base import build_openrouter_llm, load_model_spec, load_prompt_bundle


PROMPT_PATH = (
    Path(__file__).resolve().parents[2]
    / "resources"
    / "prompt"
    / "product_develop"
    / "ProductReviewAgent.yml"
)
MODEL_SPEC_PATH = (
    Path(__file__).resolve().parents[2]
    / "resources"
    / "spec"
    / "model_spec.yml"
)


class ProductReviewAgent:
    """Evaluates ProductDevelopAgent output and returns strict pass/fail JSON as a string."""

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
        # NOTE: Prompt uses a placeholder token (not python .format), so we replace it safely.
        report_md = inputs.get("product_develop_report_markdown", "")
        question = self.prompt.question_template.replace(
            "<<product_develop_report_markdown>>",
            str(report_md),
        )

        messages = [("system", self.prompt.system_prompt), ("user", question)]
        result = self.llm.invoke(messages)
        return getattr(result, "content", str(result))
