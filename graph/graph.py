from langgraph.graph import StateGraph, END
from graph.state import RedTeamState
from graph.nodes.planner import planner_node
from graph.nodes.executor import executor_node
from graph.nodes.judge import judge_node
from graph.nodes.reporter import reporter_node

def build_graph():
    # initialize the graph with our state
    graph = StateGraph(RedTeamState)

    # --- add all nodes ---
    graph.add_node("planner", planner_node)
    graph.add_node("executor", executor_node)
    graph.add_node("judge", judge_node)
    graph.add_node("reporter", reporter_node)

    # --- define the flow ---
    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "judge")
    graph.add_edge("judge", "reporter")
    graph.add_edge("reporter", END)

    # compile and return
    return graph.compile()