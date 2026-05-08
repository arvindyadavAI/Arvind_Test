# ViewRatingWorkflow

Runnable demo tool for analyzing insurance rating XML workflows starting from an entry node.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python view_rating_workflow.py --xml ./sample/sample_rating.xml --entry-id data.TotalResult --output-dir ./output
```

## Outputs

- `output/workflow_document.md`
- `output/workflow_diagram.png`
- `output/workflow_nodes.json`

## Notes

- Handles invalid XML and missing entry node with clear errors.
- Uses heuristic dependency detection for flexible XML structures.
