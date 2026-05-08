from __future__ import annotations

import argparse
from pathlib import Path

from .diagram_generator import generate_diagram
from .document_generator import generate_markdown, write_nodes_json
from .workflow_analyzer import analyze_workflow
from .xml_parser import XmlParseError, parse_xml


def main() -> int:
    parser = argparse.ArgumentParser(description="ViewRatingWorkflow demo")
    parser.add_argument("--xml", required=True, help="Path to local XML file")
    parser.add_argument("--entry-id", default="data.TotalResult", help="Entry node id")
    parser.add_argument("--output-dir", default="./output", help="Output directory")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        nodes, _ = parse_xml(args.xml)
        graph = analyze_workflow(nodes, args.entry_id)
    except XmlParseError as exc:
        print(f"[ERROR] {exc}")
        return 2
    except ValueError as exc:
        print(f"[ERROR] {exc}")
        return 3

    diagram = generate_diagram(graph, str(output_dir / "workflow_diagram.png"))
    nodes_json = write_nodes_json(graph, str(output_dir / "workflow_nodes.json"))
    doc = generate_markdown(graph, args.xml, diagram, str(output_dir / "workflow_document.md"))

    print("Generated artifacts:")
    print(f"- {diagram}")
    print(f"- {nodes_json}")
    print(f"- {doc}")
    return 0
