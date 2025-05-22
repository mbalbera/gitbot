import json

def parse_classification_result(raw_output: str) -> dict:
    """
    Parses and validates the model's JSON output for SQL query classification.

    Args:
        raw_output (str): The raw string output from the AI model.

    Returns:
        dict: Parsed result with keys: 'result', 'message', and 'context'.

    Raises:
        ValueError: If the output is not valid JSON or doesn't match the expected schema.
    """
    try:
        parsed = json.loads(raw_output)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON output: {e.msg}") from e

    # Top-level keys
    required_keys = {"result", "message", "context"}
    if not isinstance(parsed, dict) or not required_keys.issubset(parsed.keys()):
        raise ValueError(f"Missing one or more required top-level keys: {required_keys}")

    # Validate 'result'
    if parsed["result"] not in {"VALID", "INVALID"}:
        raise ValueError(f"Invalid 'result' value: {parsed['result']} (must be 'VALID' or 'INVALID')")

    # Validate 'message'
    if not isinstance(parsed["message"], str):
        raise ValueError("'message' must be a string")

    # Validate 'context'
    context = parsed["context"]
    if not isinstance(context, dict):
        raise ValueError("'context' must be an object")

    expected_context_keys = {"intent", "target_tables", "relevant_fields", "filters_and_aggregations"}
    if not expected_context_keys.issubset(context.keys()):
        raise ValueError(f"Missing one or more required keys in 'context': {expected_context_keys}")

    if not isinstance(context["intent"], str):
        raise ValueError("'context.intent' must be a string")

    if not isinstance(context["target_tables"], list):
        raise ValueError("'context.target_tables' must be a list of strings")

    if not isinstance(context["filters_and_aggregations"], str):
        raise ValueError("'context.filters_and_aggregations' must be a string")

    if not isinstance(context["relevant_fields"], list):
        raise ValueError("'context.relevant_fields' must be a list of objects with 'name' and 'description'")

    for field in context["relevant_fields"]:
        if not isinstance(field, dict) or not {"name", "description"}.issubset(field.keys()):
            raise ValueError("Each item in 'context.relevant_fields' must have 'name' and 'description' fields")
        if not isinstance(field["name"], str) or not isinstance(field["description"], str):
            raise ValueError("Each 'name' and 'description' in 'relevant_fields' must be a string")

    return parsed
