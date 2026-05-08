from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Tuple

from .models import XmlNode


class XmlParseError(Exception):
    pass


def parse_xml(xml_path: str) -> Tuple[Dict[str, XmlNode], ET.ElementTree]:
    path = Path(xml_path)
    if not path.exists():
        raise XmlParseError(f"XML file not found: {xml_path}")

    try:
        tree = ET.parse(path)
    except ET.ParseError as exc:
        raise XmlParseError(f"Invalid XML: {exc}") from exc

    root = tree.getroot()
    nodes: Dict[str, XmlNode] = {}

    def walk(elem: ET.Element, parent_uid: str | None = None, idx: int = 0) -> str:
        uid = elem.attrib.get("id") or f"{elem.tag}@{id(elem)}"
        if uid in nodes:
            uid = f"{uid}#{idx}"

        node = XmlNode(
            uid=uid,
            tag=elem.tag,
            attributes={k: str(v) for k, v in elem.attrib.items()},
            text=(elem.text or "").strip(),
            parent_uid=parent_uid,
        )
        nodes[uid] = node
        for i, child in enumerate(list(elem)):
            child_uid = walk(child, uid, i)
            node.child_uids.append(child_uid)
        return uid

    walk(root)
    return nodes, tree
