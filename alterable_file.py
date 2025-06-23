{
  "job_name": "etl_csv_pipeline",
  "steps": [
    {
      "step": "load_csv",
      "input": "data.csv",
      "status": "success",
      "columns": ["id", "name", "value"]
    },
    {
      "step": "drop_nulls",
      "operation": "df.dropna(subset=['value'])",
      "status": "success"
    },
    {
      "step": "transform",
      "operation": "df['value'] = df['value'].astype(int); df['tax'] = df['value'] * 0.1",
      "status": "success"
    },
    {
      "step": "rename_columns",
      "operation": "df.rename(columns={'nonexistent_col': 'new_col'})",
      "status": "failed",
      "error": "KeyError: \"['nonexistent_col'] not found in axis\""
    }
  ],
  "timestamp": "2025-06-20T15:23:45.000Z",
  "error": "KeyError: \"['nonexistent_col'] not found in axis\""
}
