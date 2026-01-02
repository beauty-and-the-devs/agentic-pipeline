
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from src.agent._base import (
    build_openrouter_llm,
    format_question,
    load_model_spec,
    load_prompt_bundle,
)


PROMPT_PATH = (
    Path(__file__).resolve().parents[2]
    / "resources"
    / "prompt"
    / "insight_process"
    / "InsightGeneratorAgent.yml"
)
MODEL_SPEC_PATH = (
    Path(__file__).resolve().parents[2]
    / "resources"
    / "spec"
    / "model_spec.yml"
)


class InsightGeneratorAgent:
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

    def run(self, input_json: Dict[str, Any]) -> str:
        question = format_question(self.prompt.question_template, input_json)
        messages = [("system", self.prompt.system_prompt), ("user", question)]
        result = self.llm.invoke(messages)
        return getattr(result, "content", str(result))
