# ai/step_generator.py

from ai.call_model import call_model
from prompts.detailed_steps import STEP_PROMPT_TEMPLATE

def get_steps_for_recipe(recipe_name, ingredients, cook_time):
    prompt = STEP_PROMPT_TEMPLATE \
        .replace("{{recipe_name}}", recipe_name) \
        .replace("{{ingredients}}", ingredients) \
        .replace("{{cook_time}}", cook_time)

    response = call_model(prompt)
    return response
