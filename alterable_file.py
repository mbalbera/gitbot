import pandas as pd
import sys
from collections import defaultdict

def load_file(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("File must be a CSV or XLSX.")

def to_markdown(df):
    markdown_output = ""
    tables = defaultdict(list)

    # Normalize headers (lowercase and stripped)
    df.columns = [col.strip().lower() for col in df.columns]
    headers = df.columns.tolist()

    # Required: find table name and column name fields
    # We expect *at least* table name and column name to exist
    table_name_col = next((h for h in headers if 'table' in h), None)
    column_name_col = next((h for h in headers if 'column' in h and 'name' in h), None)

    if not table_name_col or not column_name_col:
        raise ValueError("Missing required 'table name' or 'column name' column.")

    # Other fields are optional — just collect whatever is there
    extra_fields = [h for h in headers if h not in {table_name_col, column_name_col}]

    for _, row in df.iterrows():
        table_name = row[table_name_col]
        column_name = row[column_name_col]

        details = {}
        for field in extra_fields:
            value = row.get(field, '')
            if pd.notna(value) and str(value).strip():
                details[field] = value

        tables[table_name].append({
            'column_name': column_name,
            'details': details
        })

    # Build markdown
    for table, columns in tables.items():
        markdown_output += f"## {table}\n\n"
        for col in columns:
            markdown_output += f"- {col['column_name']}:\n"
            for key, value in col['details'].items():
                markdown_output += f"  - {key}: {value}\n"
        markdown_output += "\n"

    return markdown_output

def main(file_path, output_path):
    df = load_file(file_path)
    markdown = to_markdown(df)

    with open(output_path, 'w') as f:
        f.write(markdown)

    print(f"Markdown saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <input.csv|xlsx> <output.md>")
    else:
        main(sys.argv[1], sys.argv[2])
