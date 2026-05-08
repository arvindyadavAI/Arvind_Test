from __future__ import annotations

from collections import deque
from typing import Dict, List, Set

from .models import WorkflowEdge, WorkflowGraph, XmlNode

REF_ATTRS = {"ref", "refid", "target", "id", "path", "name"}


def _find_entry(nodes: Dict[str, XmlNode], entry_id: str) -> str | None:
    if entry_id in nodes:
        return entry_id
    for uid, node in nodes.items():
        if node.attributes.get("id") == entry_id:
            return uid
    return None


def analyze_workflow(nodes: Dict[str, XmlNode], entry_id: str) -> WorkflowGraph:
    entry_uid = _find_entry(nodes, entry_id)
    if not entry_uid:
        raise ValueError(f"Entry node not found: {entry_id}")

    edges: List[WorkflowEdge] = []
    assumptions: List[str] = []
    visited: Set[str] = set()
    queue = deque([entry_uid])

    while queue:
        uid = queue.popleft()
        if uid in visited:
            continue
        visited.add(uid)
        node = nodes[uid]

        for child_uid in node.child_uids:
            edges.append(WorkflowEdge(uid, child_uid, "child", "nested XML child element"))
            queue.append(child_uid)

        for attr_name, attr_value in node.attributes.items():
            if attr_name.lower() not in REF_ATTRS:
                continue
            if attr_value == uid:
                continue
            if attr_value in nodes:
                edges.append(WorkflowEdge(uid, attr_value, "reference", f"attribute {attr_name}"))
                queue.append(attr_value)
            else:
                for candidate_uid, candidate in nodes.items():
                    if candidate.attributes.get("id") == attr_value or candidate.attributes.get("path") == attr_value:
                        edges.append(WorkflowEdge(uid, candidate_uid, "inferred_reference", f"inferred from {attr_name}"))
                        queue.append(candidate_uid)
                        assumptions.append(
                            f"Inferred relationship from {uid}.{attr_name}='{attr_value}' to {candidate_uid}."
                        )
                        break

    sub_nodes = {uid: nodes[uid] for uid in visited}
    return WorkflowGraph(entry_uid=entry_uid, nodes=sub_nodes, edges=edges, assumptions=sorted(set(assumptions)))


def categorize_node(node: XmlNode) -> str:
    blob = f"{node.tag} {' '.join(f'{k}={v}' for k, v in node.attributes.items())} {node.text}".lower()
    if any(k in blob for k in ["if", "when", "condition"]):
        return "conditional_logic"
    if any(k in blob for k in ["calc", "formula", "sum", "multiply", "rate"]):
        return "calculation"
    if any(k in blob for k in ["table", "lookup"]):
        return "lookup"
    if any(k in blob for k in ["result", "premium", "total"]):
        return "output"
    return "data_or_component"
