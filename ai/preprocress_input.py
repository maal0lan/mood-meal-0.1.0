from prompts.input_cleaning import INPUT_CLEANING_PROMPT
from ai.call_model import call_model

def preprocess_input(natural_text):
    full_prompt = INPUT_CLEANING_PROMPT.replace("{{input}}", natural_text)
    response = call_model(full_prompt)
    return response  # ideally a JSON string
