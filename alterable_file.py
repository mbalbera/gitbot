import json
import uuid
from datetime import datetime
import traceback
import os

def emit_lineage(job_name, system, environment, step_name, operation=None, status="success", error=None, inputs=None, outputs=None, lineage_file="lineage.json"):
    lineage = {
        "job_name": job_name,
        "run_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "system": system,
        "environment": environment,
        "steps": [{
            "step": step_name,
            "operation": operation,
            "status": status,
            "error": error
        }],
        "inputs": inputs or [],
        "outputs": outputs or []
    }

    if os.path.exists(lineage_file):
        with open(lineage_file) as f:
            try:
                existing = json.load(f)
                existing["steps"].append(lineage["steps"][0])
                lineage = existing
            except Exception:
                pass  # corrupted or malformed file

    with open(lineage_file, "w") as f:
        json.dump(lineage, f, indent=2)
