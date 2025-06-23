import json

with open("lineage.json") as f:
    lineage = json.load(f)

print("\n🧠 NUCLEUS DIAGNOSTICS REPORT\n===============================")
print(f"Job: {lineage.get('job_name')}")
print(f"Run ID: {lineage.get('run_id')}")
print(f"System: {lineage.get('system')} | Env: {lineage.get('environment')}")
print(f"Timestamp: {lineage.get('timestamp')}\n")

steps = lineage.get("steps", [])

for i, step in enumerate(steps):
    print(f"Step {i+1}: {step.get('step')} | Status: {step.get('status')}\n")
    if step.get("operation"):
        print(f"  Operation: {step['operation']}")

    if step.get("status") == "failed":
        print(f"  ❌ Failure Detected:")
        print(f"  Error: {step['error'].splitlines()[-1]}")

        # NUCLEUS-powered suggestions
        print("\n  🤖 NUCLEUS Suggests:")

        error = step.get("error", "")

        if "KeyError" in error:
            print("  - Check if the referenced column exists in the DataFrame.")
            print("  - Use df.columns to inspect available columns before renaming.")

        elif "ValueError" in error and "int" in error:
            print("  - Invalid type conversion. Use pd.to_numeric(..., errors='coerce') before astype(int).")
            print("  - Add logging to check values in 'value' column before converting.")

        elif "PermissionError" in error:
            print("  - Confirm the destination has write permissions and credentials are correct.")

        else:
            print("  - Review the full stack trace and validate input/output integrity.")

    print("\n----------------------------------------")
