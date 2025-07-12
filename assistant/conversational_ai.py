from ai.call_model import call_model
from assistant.context_memory import get_context
from prompts.live_assistant import LIVE_ASSISTANT_PROMPT

def handle_user_question(query):
    context = get_context()
    prompt = LIVE_ASSISTANT_PROMPT
    prompt = prompt.replace("{{recipe}}", context["recipe"])
    prompt = prompt.replace("{{step_number}}", str(context["step_number"]))
    prompt = prompt.replace("{{step_text}}", context["step_text"])
    prompt = prompt.replace("{{ingredients}}", context["ingredients"])
    prompt = prompt.replace("{{query}}", query)

    return call_model(prompt)
