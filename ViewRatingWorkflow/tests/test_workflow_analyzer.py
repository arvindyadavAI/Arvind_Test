from src.view_rating_workflow.workflow_analyzer import analyze_workflow
from src.view_rating_workflow.xml_parser import parse_xml


def test_entry_found_and_edges_present():
    nodes, _ = parse_xml("sample/sample_rating.xml")
    graph = analyze_workflow(nodes, "data.TotalResult")
    assert graph.entry_uid == "data.TotalResult"
    assert len(graph.edges) > 0
