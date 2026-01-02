from __future__ import annotations

from typing import Any, Dict, TypedDict

from langgraph.graph import END, StateGraph

from src.pipelines import (
    run_insight_process,
    run_marketing_contents,
    run_product_develop_with_review,
)


class AppState(TypedDict, total=False):
    input_json: Dict[str, Any]
    insight_report_md: str


def build_app_graph() -> "StateGraph[AppState]":
    def insight_node(state: AppState) -> AppState:
        return run_insight_process(state.get("input_json", {}))

    def product_node(state: AppState) -> AppState:
        return run_product_develop_with_review(state, max_attempts=2)

    def marketing_node(state: AppState) -> AppState:
        return run_marketing_contents(state)

    g: StateGraph[AppState] = StateGraph(AppState)
    g.add_node("insight_process", insight_node)
    g.add_node("product_develop", product_node)
    g.add_node("marketing_contents", marketing_node)

    g.set_entry_point("insight_process")
    g.add_edge("insight_process", "product_develop")
    g.add_edge("product_develop", "marketing_contents")
    g.add_edge("marketing_contents", END)

    return g
