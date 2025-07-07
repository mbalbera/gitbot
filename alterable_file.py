Analyze the following SQL and output a JSON representation of data lineage using this structure:

{
  "entities": [
    {
      "name": "Schema.TableName",
      "type": "table" or "view",
      "fields": ["field1", "field2"],
      "relations": [
        {"to": "OtherSchema.OtherTable", "on": ["fieldName"]},
        {"to": "OtherSchema.AnotherTable", "on": [["localField", "foreignField"]]}
      ]
    }
  ]
}

Rules:
- All keys should be lowercase.
- Omit null or empty keys (e.g. no `relations` if none exist).
- Be consistent and concise.
- Include field names even if not joined on.
- Use full entity names including schema (like `Sales.Product`).

Now analyze this SQL:

{chunk}
