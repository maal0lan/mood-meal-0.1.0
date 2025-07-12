STEP_PROMPT_TEMPLATE = """
You are a professional recipe AI. Based on the provided recipe name, ingredients, and cook time, generate detailed, step-by-step cooking instructions.

Recipe Name: {{recipe_name}}
Ingredients: {{ingredients}}
Estimated Cook Time: {{cook_time}}

Respond ONLY in this strict JSON format:

{
  "steps": [
    {
      "step_number": 1,
      "instruction": "Preheat the oven to 180°C...",
      "duration": "5 min"
    },
    ...
  ]
}

Each step must be clear and concise. Include approximate duration for each step.
"""
