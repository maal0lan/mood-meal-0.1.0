INPUT_CLEANING_PROMPT = """
You are an input preprocessor. Convert the following free-text sentence into valid JSON with the keys:
- ingredients (string, comma-separated)
- time (string)
- weather (string)
- cuisine (optional string)

Input: "{{input}}"

Return ONLY the cleaned JSON structure.
"""
