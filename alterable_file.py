repo/
├── pipeline.py         # Multi-step ETL pipeline with intentional errors
├── lineage.json        # Lineage metadata output
├── analyze.py          # AI assistant to analyze logs + metadata
├── alert.py            # Alert generator (prints console alert)
├── data.csv            # Sample input data
└── README.md           # How to run the POC

# pipeline.py
import pandas as pd
import traceback
import json
from datetime import datetime

LINEAGE_FILE = "lineage.json"

lineage = {
    "job_name": "etl_csv_pipeline",
    "steps": [],
    "timestamp": datetime.utcnow().isoformat()
}

try:
    # Step 1: Load data
    step = {"step": "load_csv", "input": "data.csv"}
    df = pd.read_csv("data.csv")
    step["status"] = "success"
    step["columns"] = list(df.columns)
    lineage["steps"].append(step)

    # Step 2: Clean data - remove rows with nulls in 'value'
    step = {"step": "drop_nulls", "operation": "df.dropna(subset=['value'])"}
    df = df.dropna(subset=['value'])
    step["status"] = "success"
    lineage["steps"].append(step)

    # Step 3: Transform data - convert 'value' to integer and calculate tax
    step = {"step": "transform", "operation": "df['value'] = df['value'].astype(int); df['tax'] = df['value'] * 0.1"}
    df['value'] = df['value'].astype(int)  # possible failure if non-numeric
    df['tax'] = df['value'] * 0.1
    step["status"] = "success"
    lineage["steps"].append(step)

    # Step 4: Rename columns - intentional failure if column missing
    step = {"step": "rename_columns", "operation": "df.rename(columns={'nonexistent_col': 'new_col'})"}
    df = df.rename(columns={'nonexistent_col': 'new_col'})  # triggers error
    step["status"] = "success"
    lineage["steps"].append(step)

    print("Pipeline succeeded.")

except Exception as e:
    step["status"] = "failed"
    step["error"] = traceback.format_exc()
    lineage["steps"].append(step)
    lineage["error"] = step["error"]
    print("Pipeline failed. Run analyze.py for more info.")

finally:
    with open(LINEAGE_FILE, "w") as f:
        json.dump(lineage, f, indent=2)

# analyze.py
import json

with open("lineage.json") as f:
    lineage = json.load(f)

print("\n🤖 AI DEBUG ASSISTANT\n---------------------------")
print(f"Job: {lineage['job_name']}")
print(f"Timestamp: {lineage['timestamp']}")

for step in lineage.get("steps", []):
    status = step.get("status")
    print(f"\nStep: {step['step']} | Status: {status}")
    if status == "failed":
        print("\n⚠️  Failure Details:")
        print(step.get("error"))

        # Simulated AI diagnosis
        if "KeyError" in step.get("error", ""):
            print("\n🧠 AI Suggests:")
            print("- You tried to rename a column that doesn't exist.")
            print("- Double-check the column name in the DataFrame and confirm it was loaded correctly.")
        elif "ValueError" in step.get("error", ""):
            print("\n🧠 AI Suggests:")
            print("- You may have non-numeric data in the 'value' column.")
            print("- Use df['value'].apply(pd.to_numeric, errors='coerce') to safely convert.")

# alert.py
import json

with open("lineage.json") as f:
    lineage = json.load(f)

print("\n🚨 ALERT: Job Failure Detected")
print(f"Job: {lineage['job_name']}")
print(f"Time: {lineage['timestamp']}")

for step in lineage.get("steps", []):
    if step.get("status") == "failed":
        print(f"❌ Failed Step: {step['step']}")
        print(f"Error Summary: {step['error'].splitlines()[-1]}")
        print("Suggested Fix: Run `analyze.py` for AI recommendations.")

# data.csv
id,name,value
1,Alice,100
2,Bob,
3,Charlie,abc

# README.md
# AI-Powered Data Observability POC (Enhanced Version)

## Overview
This is a POC for AI-powered observability. It tracks pipeline steps, captures metadata, and uses an AI assistant to debug failures.

## Pipeline Steps
1. Load CSV
2. Drop nulls from 'value'
3. Convert 'value' to int, calculate 'tax'
4. Rename column (intentional failure)

## How It Works
- `pipeline.py`: runs a multi-step ETL job with metadata tracking
- `lineage.json`: captures job details, inputs, outputs, errors
- `analyze.py`: AI assistant diagnoses issues and gives fixes
- `alert.py`: prints out structured failure alert

## Run the Demo
```bash
pip install pandas
python pipeline.py       # Runs pipeline and logs lineage
python analyze.py        # Simulates AI diagnosis
python alert.py          # Alerts and suggestions
```

## What's Next
- Plug in real LLMs with Ollama or local APIs
- Replace JSON with OpenLineage events
- Add data validation and quality checks
