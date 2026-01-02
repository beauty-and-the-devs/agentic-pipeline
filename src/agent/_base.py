from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Protocol

import yaml
from langchain_openai import ChatOpenAI


@dataclass
class PromptBundle:
    version: str
    writer: str
    system_prompt: str
    question_template: str


def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"YAML not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Invalid YAML format (expected mapping): {path}")
    return data


def load_prompt_bundle(prompt_path: Path) -> PromptBundle:
    data = load_yaml(prompt_path)
    required = ["version", "writer", "system_prompt", "question_template"]
    missing = [k for k in required if k not in data]
    if missing:
        raise KeyError(f"Missing keys in prompt YAML {prompt_path}: {missing}")

    return PromptBundle(
        version=str(data["version"]),
        writer=str(data["writer"]),
        system_prompt=str(data["system_prompt"]),
        question_template=str(data["question_template"]),
    )


def load_model_spec(model_spec_path: Path, *, kind: str = "text_gen") -> Dict[str, Any]:
    """Load model spec YAML.

    Supports both legacy flat format:
      llm_lib/model_name/temperature/type

    and new format:
      text_gen: { ... }
      video_gen: { ... }

    Parameters
    ----------
    kind:
      Which top-level spec to use in the new format. Default: "text_gen".
    """

    spec = load_yaml(model_spec_path)

    # New nested format
    if "text_gen" in spec or "video_gen" in spec:
        sub = spec.get(kind)
        if not isinstance(sub, dict):
            raise KeyError(
                f"Missing or invalid '{kind}' section in model spec YAML {model_spec_path}"
            )
        spec = sub

    required = ["llm_lib", "model_name", "temperature", "type"]
    missing = [k for k in required if k not in spec]
    if missing:
        raise KeyError(f"Missing keys in model spec YAML {model_spec_path}: {missing}")
    return spec


def format_question(template: str, input_data: Any) -> str:
    return template.replace("{{input}}", yaml.safe_dump(input_data, allow_unicode=True))


def build_openrouter_llm(model_name: str, temperature: float) -> ChatOpenAI:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    return ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        model=model_name,
        temperature=temperature,
        default_headers={
            "HTTP-Referer": os.getenv("OPENROUTER_SITE_URL", ""),
            "X-Title": os.getenv("OPENROUTER_APP_NAME", "agentic-pipeline"),
        },
    )


class Agent(Protocol):
    def run(self, input_json: Dict[str, Any]) -> str: ...
