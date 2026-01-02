from __future__ import annotations

import json
import logging
from typing import Any, Dict, TypedDict

from langgraph.graph import StateGraph

from src.agent.DataExtractAgent import DataExtractAgent
from src.agent.InsightGeneratorAgent import InsightGeneratorAgent
from src.agent.MarketingVideoGeneratorAgent import MarketingVideoGeneratorAgent
from src.agent.PlotGeneratorAgent import PlotGeneratorAgent
from src.agent.ProductDevelopAgent import ProductDevelopAgent
from src.agent.ProductReviewAgent import ProductReviewAgent


logger = logging.getLogger(__name__)

try:
    # Optional: pipelines.py can show progress for retry loop if tqdm is installed.
    from tqdm.auto import tqdm  # type: ignore
except Exception:  # pragma: no cover
    tqdm = None  # type: ignore


class PipelineState(TypedDict, total=False):
    input_json: Dict[str, Any]
    insight_report_md: str
    product_report_md: str
    product_review_json: str
    product_review_pass: bool
    product_review_reason: str
    product_develop_attempts: int
    plot_report_md: str
    marketing_videos_json: str


def build_insight_process_graph() -> "StateGraph[PipelineState]":
    agent = DataExtractAgent()
    insight_agent = InsightGeneratorAgent()

    def data_extract_node(state: PipelineState) -> PipelineState:
        input_json = state.get("input_json", {})
        report = agent.run(input_json)
        return {**state, "insight_report_md": report}

    def insight_generate_node(state: PipelineState) -> PipelineState:
        # 현재는 DataExtract 결과(마크다운)를 그대로 입력으로 전달하는 형태로 뼈대만 둠
        report = insight_agent.run(
            {
                "insight_report": state.get("insight_report_md", ""),
                "raw_input": state.get("input_json", {}),
            }
        )
        return {**state, "insight_report_md": report}

    g: StateGraph[PipelineState] = StateGraph(PipelineState)
    g.add_node("data_extract", data_extract_node)
    g.add_node("insight_generate", insight_generate_node)
    g.set_entry_point("data_extract")
    g.add_edge("data_extract", "insight_generate")
    g.set_finish_point("insight_generate")
    return g


def run_insight_process(input_json: Dict[str, Any]) -> PipelineState:
    logger.info("[insight_process] start")
    graph = build_insight_process_graph().compile()
    out = graph.invoke({"input_json": input_json})
    logger.info("[insight_process] done")
    return out


def run_product_develop(state: PipelineState) -> PipelineState:
    logger.info("[product_develop] start")
    agent = ProductDevelopAgent()
    # TODO: FormatFileMCP 연동 전까지는 빈 문자열로 둠
    result = agent.run(
        {
            "formatfile_mcp_markdown": state.get("formatfile_mcp_markdown", ""),
            "insight_report_markdown": state.get("insight_report_md", ""),
            "feedback_markdown_optional": state.get("feedback_markdown_optional", ""),
        }
    )
    logger.info("[product_develop] done")
    return {**state, "product_report_md": result}


def run_product_review(state: PipelineState) -> PipelineState:
    logger.info("[product_review] start")
    agent = ProductReviewAgent()
    result = agent.run(
        {
            "product_develop_report_markdown": state.get("product_report_md", ""),
        }
    )
    logger.info("[product_review] done")
    return {**state, "product_review_json": result}


def run_marketing_contents(state: PipelineState) -> PipelineState:
    # Gate: do not proceed unless product review has passed.
    if state.get("product_review_pass") is not True:
        logger.error(
            "[marketing_contents] blocked: product_review_pass=%s reason=%s",
            state.get("product_review_pass"),
            state.get("product_review_reason"),
        )
        raise RuntimeError(
            "Product review did not pass. Fix product_report_md via ProductDevelopAgent feedback loop before marketing."
        )

    logger.info("[marketing_contents] start")

    logger.info("[marketing_contents] plot_generate start")
    plot_agent = PlotGeneratorAgent()
    plot_result = plot_agent.run(
        {
            "product_report_markdown": state.get("product_report_md", ""),
            "insight_report_markdown": state.get("insight_report_md", ""),
        }
    )
    state2: PipelineState = {**state, "plot_report_md": plot_result}
    logger.info("[marketing_contents] plot_generate done")

    logger.info("[marketing_contents] video_generate start")
    video_agent = MarketingVideoGeneratorAgent()
    videos_result = video_agent.run(
        {
            "FlagRegen": False,
            "PlotText": state2.get("plot_report_md", ""),
        }
    )
    logger.info("[marketing_contents] video_generate done")

    logger.info("[marketing_contents] done")
    return {**state2, "marketing_videos_json": videos_result}


def _parse_review_result(review_json_text: str) -> Dict[str, Any]:
    """Best-effort parse for ProductReviewAgent JSON output."""
    try:
        data = json.loads(review_json_text)
        if isinstance(data, dict):
            return data
    except Exception:
        pass
    return {"pass": False, "reason": "Invalid review JSON"}


def run_product_develop_with_review(
    state: PipelineState,
    *,
    max_attempts: int = 2,
) -> PipelineState:
    """Run ProductDevelopAgent and gate it with ProductReviewAgent.

    If review fails, feed the review reason back into ProductDevelopAgent and retry.
    """

    logger.info("[product_develop_with_review] start max_attempts=%s", max_attempts)

    current_state: PipelineState = dict(state)
    feedback = current_state.get("feedback_markdown_optional", "")

    attempts = 0
    last_reason = ""

    iterator = range(max_attempts)
    if tqdm is not None:
        iterator = tqdm(iterator, desc="product_develop_with_review", unit="attempt")  # type: ignore

    for _ in iterator:
        attempts += 1
        logger.info("[product_develop_with_review] attempt %s/%s", attempts, max_attempts)

        current_state = run_product_develop(
            {**current_state, "feedback_markdown_optional": feedback, "product_develop_attempts": attempts}
        )
        current_state = run_product_review(current_state)

        review = _parse_review_result(current_state.get("product_review_json", ""))
        passed = bool(review.get("pass"))
        last_reason = str(review.get("reason", ""))

        current_state = {
            **current_state,
            "product_review_pass": passed,
            "product_review_reason": last_reason,
        }

        logger.info(
            "[product_develop_with_review] review result pass=%s reason=%s",
            passed,
            (last_reason[:200] + "...") if len(last_reason) > 200 else last_reason,
        )

        if passed:
            logger.info("[product_develop_with_review] done (pass) attempts=%s", attempts)
            return current_state

        # Feed back the reviewer reason into ProductDevelopAgent (as markdown)
        feedback = f"# ProductReview Feedback\n\n{last_reason}\n"

    logger.warning(
        "[product_develop_with_review] done (fail) attempts=%s last_reason=%s",
        attempts,
        (last_reason[:200] + "...") if len(last_reason) > 200 else last_reason,
    )

    # Final state with failure info retained
    return {
        **current_state,
        "product_review_pass": False,
        "product_review_reason": last_reason,
        "product_develop_attempts": attempts,
    }
