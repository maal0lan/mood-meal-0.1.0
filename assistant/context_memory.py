context = {
    "recipe": "",
    "step_number": 0,
    "step_text": "",
    "ingredients": "",
    "history": []
}

def update_context(recipe, step_number, step_text, ingredients=""):
    context["recipe"] = recipe
    context["step_number"] = step_number
    context["step_text"] = step_text
    if ingredients:
        context["ingredients"] = ingredients

def add_user_query(query):
    context["history"].append(query)
    if len(context["history"]) > 10:
        context["history"].pop(0)

def get_context():
    return context
