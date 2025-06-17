🧪 1. Data Lineage POC
🔹 Objective:
Extract lineage from SQL (or dbt models) and answer basic lineage questions via GPT.

🔹 Steps:
Collect Inputs (1–2 hrs)

Gather ~5 SQL queries or dbt models.

Optionally include a sample DAG from Airflow or metadata graph (CSV/JSON).

Write a parser (2–4 hrs)

Use regex or sqlparse to extract SELECT, FROM, JOIN, AS logic.

Extract table and column dependencies.

Send context to OpenAI (2 hrs)

Prompt GPT with the SQL + ask: "What is the lineage of column X?"

Optionally visualize with tools like graphviz or networkx.

Create a Q&A CLI or web demo (2 hrs)

Let user input: “Where does the revenue field in table Z come from?”

Return the lineage path via GPT summary or JSON.

⏱️ Time Estimate: ~1 day (8–10 hrs)
✅ 2. Data Quality POC
🔹 Objective:
Use GPT to suggest validation tests from schema + sample data.

🔹 Steps:
Prepare test tables (1 hr)

JSON or CSV for a few tables with columns, types, and sample values.

Design prompt templates (2–3 hrs)

Prompt: "Suggest quality checks for this schema and data."

GPT returns ideas like:

amount >= 0

customer_id should not be NULL

created_at in last 30 days

Generate test logic (2–3 hrs)

Convert GPT output to dbt/YAML or Python (e.g., Great Expectations style).

Use templating (Jinja or string replace) to auto-generate test configs.

Run tests + report summary (2 hrs)

Build a CLI/web interface: Show pass/fail summary + GPT explanation of failed rules.

⏱️ Time Estimate: ~1 day
📈 3. Data Observability POC
🔹 Objective:
Monitor freshness/volume/null % of a few tables and summarize issues with GPT.

🔹 Steps:
Capture sample metrics (2–3 hrs)

Create mock metrics: row_count, null_pct, last_updated, etc.

Could be a CSV log file or in-memory dict.

Detect anomalies (2 hrs)

Simple rules: row_count deviation > 3σ, freshness > 24hr, null_pct > 10%.

Summarize anomalies with GPT (2–3 hrs)

Feed the metrics + thresholds to GPT: “Explain the health of table X.”

GPT returns: "Table orders is stale (last updated 3 days ago). Also, 12% of rows have null amount."

Optional: Alerting demo (1–2 hrs)

Send GPT summary to console, Slack, or email.

⏱️ Time Estimate: ~1 day
