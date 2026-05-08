from __future__ import annotations

import json
from pathlib import Path

from .models import WorkflowGraph
from .workflow_analyzer import categorize_node


def write_nodes_json(graph: WorkflowGraph, output_path: str) -> str:
    payload = {
        "entry_uid": graph.entry_uid,
        "nodes": [
            {
                "uid": uid,
                "tag": node.tag,
                "attributes": node.attributes,
                "category": categorize_node(node),
            }
            for uid, node in graph.nodes.items()
        ],
        "edges": [edge.__dict__ for edge in graph.edges],
        "assumptions": graph.assumptions,
    }
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return output_path


def generate_markdown(graph: WorkflowGraph, xml_file: str, diagram_path: str, output_path: str) -> str:
    lines = [
        "# ViewRatingWorkflow - Technical Workflow Document",
        "",
        f"- **Input XML:** `{xml_file}`",
        f"- **Entry Node:** `{graph.entry_uid}` (highlighted in diagram)",
        f"- **Diagram:** `{diagram_path}`",
        "",
        "## Summary of Detected Workflow",
        f"Detected **{len(graph.nodes)} nodes** and **{len(graph.edges)} relationships** from the entry node.",
        "",
        "## Detected XML Nodes",
        "| UID | Tag | Category | Key Attributes |",
        "|---|---|---|---|",
    ]
    for uid, node in graph.nodes.items():
        attrs = ", ".join(f"{k}={v}" for k, v in list(node.attributes.items())[:4])
        lines.append(f"| {uid} | {node.tag} | {categorize_node(node)} | {attrs} |")

    lines.extend([
        "",
        "## Workflow Detection Logic",
        "- Traverses nested child XML elements from the entry node.",
        "- Detects direct references via attributes: `ref`, `refid`, `target`, `id`, `path`, `name`.",
        "- Uses inferred linking when attribute values match another node's `id`/`path`.",
        "",
        "## Rating-Domain Interpretation",
        "- Entry/output context is interpreted around `TotalResult` as final rating outcome.",
        "- Intermediate calculation nodes likely represent base rate and modifier computations.",
        "- Conditional nodes likely represent eligibility rules, discounts, or surcharges.",
        "",
        "## Simple Rating Example (Illustrative)",
        "If XML does not fully specify arithmetic details, this demo uses an illustrative flow:",
        "1. Base premium = 1000",
        "2. Territory factor = 1.10",
        "3. Claims surcharge = 1.15",
        "4. Final premium (`TotalResult`) = 1000 x 1.10 x 1.15 = 1265",
        "",
        "## Assumptions and Limitations",
    ])
    if graph.assumptions:
        lines.extend([f"- {a}" for a in graph.assumptions])
    else:
        lines.append("- No inferred relationships were required for this run.")

    lines.extend([
        "- XML semantics vary by rating engine; this demo uses portable heuristics.",
        "",
        "## Suggested Future Enhancements",
        "- Add engine-specific XML adapters.",
        "- Add richer expression parsing for exact formula extraction.",
        "- Export interactive diagrams (e.g., HTML with drill-down).",
    ])

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    return output_path
