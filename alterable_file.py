Analyze the following SQL and output a JSON representation of data lineage. Use the following format:

entities: a list of all tables/views.

Each entity has name, type ("table" or "view"), fields, and optional relations.

relations contain to (target entity name) and on (list of shared columns or pairs like [["local", "foreign"]]).

Ensure consistent formatting, no redundant data, and lowercase keys. Use the simplified structure below:

```json
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
```
SQL to analyze:

```sql
{sql}
```

