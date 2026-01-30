# guardian/data/history_reader.py

import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

HISTORY_FILE = Path("guardian/data/deploy_history.json")

def show_history():
    console = Console()

    if not HISTORY_FILE.exists():
        console.print("No history found.")
        return

    history = json.loads(HISTORY_FILE.read_text())

    table = Table(title="📜 Deployment History")
    table.add_column("Time")
    table.add_column("Repo")
    table.add_column("Decision")
    table.add_column("Status")

    for h in history:
        table.add_row(
            h.get("timestamp", ""),
            h.get("repo", ""),
            h.get("decision", ""),
            h.get("status", "")
        )

    console.print(table)
