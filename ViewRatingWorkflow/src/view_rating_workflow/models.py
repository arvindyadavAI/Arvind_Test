from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class XmlNode:
    uid: str
    tag: str
    attributes: Dict[str, str]
    text: str
    parent_uid: Optional[str] = None
    child_uids: List[str] = field(default_factory=list)


@dataclass
class WorkflowEdge:
    source_uid: str
    target_uid: str
    relation: str
    reason: str


@dataclass
class WorkflowGraph:
    entry_uid: str
    nodes: Dict[str, XmlNode]
    edges: List[WorkflowEdge]
    assumptions: List[str]
