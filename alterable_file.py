Analyze the following SQL and output a consistent JSON representation of data lineage with this format:

{{
  "entities": [
    {{
      "name": "Schema.TableName",
      "type": "table" or "view",
      "fields": ["field1", "field2"],
      "relations": [
        {{
          "source_table": "Schema.SourceTable",
          "field": "source_column",
          "target_table": "Schema.TargetTable",
          "field": "target_column"
        }}
      ]
    }}
  ]
}}

Guidelines:
- All keys must be lowercase.
- Use full table names including schema (e.g. "Sales.Product").
- Include fields that appear in SELECT, JOINs, or are referenced.
- Only include "relations" if that entity joins to another.
- Each relation represents a one-way join: source → target, including column names.
- Do not omit required fields, even if not joined on.
- Return valid, compact JSON.

Now analyze this SQL:

{sql}
"""
