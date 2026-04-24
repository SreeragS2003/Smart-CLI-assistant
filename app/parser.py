import json

def extract_json(text: str):
    """
    Extract JSON object from LLM response text.
    Handles extra text before/after JSON.
    """
    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        json_str = text[start:end]
        return json.loads(json_str)  # Converts to Python dict
    except Exception as e:
        return {
            "answer": "Parsing failed",
            "reasoning": text,
            "confidence": "low",
            "error": str(e)
        }


def validate_response(data: dict):
    """
    Ensure required fields exist.
    """
    required_keys = ["answer", "reasoning", "confidence"]

    for key in required_keys:
        if key not in data:
            data[key] = "missing"

    return data


def parse_response(text: str):
    """
    Full pipeline:
    raw text → json → validated output
    """
    data = extract_json(text)
    data = validate_response(data)
    return data