from ai.call_model import call_model
from prompts.detailed_steps import STEP_PROMPT_TEMPLATE
import os
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def get_next_step(recipe_name, ingredients, cook_time):
    prompt = STEP_PROMPT_TEMPLATE \
        .replace("{{recipe_name}}", recipe_name) \
        .replace("{{ingredients}}", ingredients) \
        .replace("{{cook_time}}", cook_time)
        
    return call_model(prompt)
