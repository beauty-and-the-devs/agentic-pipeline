from __future__ import annotations

from typing import Any, Dict, TypedDict

from langgraph.graph import StateGraph

from src.agent.DataExtractAgent import DataExtractAgent
from src.agent.InsightGeneratorAgent import InsightGeneratorAgent
from src.agent.PlotGeneratorAgent import PlotGeneratorAgent
from src.agent.ProductDevelopAgent import ProductDevelopAgent


class PipelineState(TypedDict, total=False):
    input_json: Dict[str, Any]
    insight_report_md: str
    product_report_md: str
    plot_report_md: str


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
    graph = build_insight_process_graph().compile()
    return graph.invoke({"input_json": input_json})


def run_product_develop(state: PipelineState) -> PipelineState:
    agent = ProductDevelopAgent()
    # TODO: FormatFileMCP 연동 전까지는 빈 문자열로 둠
    result = agent.run(
        {
            "formatfile_mcp_markdown": state.get("formatfile_mcp_markdown", ""),
            "insight_report_markdown": state.get("insight_report_md", ""),
            "feedback_markdown_optional": state.get("feedback_markdown_optional", ""),
        }
    )
    return {**state, "product_report_md": result}


def run_marketing_contents(state: PipelineState) -> PipelineState:
    agent = PlotGeneratorAgent()
    result = agent.run(
        {
            "product_report_markdown": state.get("product_report_md", ""),
            "insight_report_markdown": state.get("insight_report_md", ""),
        }
    )
    return {**state, "plot_report_md": result}
