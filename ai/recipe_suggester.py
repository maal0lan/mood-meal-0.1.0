from prompts.recipe_suggestion import RECIPE_PROMPT_TEMPLATE
from ai.call_model import call_model

def get_recipe_suggestions(context_json):
    prompt = RECIPE_PROMPT_TEMPLATE.replace("{{context}}", context_json)
    return call_model(prompt)
