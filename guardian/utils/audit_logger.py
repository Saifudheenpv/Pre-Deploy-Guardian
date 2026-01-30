# guardian/utils/audit_logger.py

import json
from datetime import datetime
from pathlib import Path

HISTORY_FILE = Path("guardian/data/deploy_history.json")

def log_event(event: dict):
    event["timestamp"] = datetime.utcnow().isoformat()

    if not HISTORY_FILE.exists():
        HISTORY_FILE.write_text("[]")

    history = json.loads(HISTORY_FILE.read_text())
    history.append(event)

    HISTORY_FILE.write_text(json.dumps(history, indent=2))
