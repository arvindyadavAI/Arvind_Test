from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from .models import WorkflowGraph


def generate_diagram(graph: WorkflowGraph, output_path: str) -> str:
    g = nx.DiGraph()
    for uid, node in graph.nodes.items():
        label = node.attributes.get("id", uid)
        g.add_node(uid, label=label)
    for edge in graph.edges:
        g.add_edge(edge.source_uid, edge.target_uid, relation=edge.relation)

    plt.figure(figsize=(14, 9))
    pos = nx.spring_layout(g, seed=7)
    node_colors = ["#ffcc00" if n == graph.entry_uid else "#9ecae1" for n in g.nodes]
    nx.draw_networkx_nodes(g, pos, node_size=1600, node_color=node_colors, edgecolors="black")
    nx.draw_networkx_edges(g, pos, arrows=True, arrowstyle="->", width=1.5)
    labels = {n: g.nodes[n]["label"] for n in g.nodes}
    nx.draw_networkx_labels(g, pos, labels=labels, font_size=8)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.title("ViewRatingWorkflow: Rating Flow")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=180)
    plt.close()
    return output_path
