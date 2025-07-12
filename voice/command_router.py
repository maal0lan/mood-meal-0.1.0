from assistant.conversational_ai import handle_user_question
from assistant.context_memory import update_context, add_user_query
from voice.tts import speak
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def route_voice_command(cmd, current_step, recipe_name, step_number, ingredients):
    lower = cmd.lower().strip()

    update_context(recipe_name, step_number, current_step, ingredients)

    if "next" in lower:
        return "next"

    elif "repeat" in lower:
        speak(current_step)
        return "stay"

    elif any(word in lower for word in ["tip", "help", "what if", "can i", "how", "why", "when"]):
        add_user_query(cmd)
        reply = handle_user_question(cmd)
        speak(reply)
        return "stay"

    elif "skip" in lower:
        speak("Skipping this step.")
        return "next"

    elif "pause" in lower:
        return "pause"

    elif "resume" in lower:
        return "resume"

    else:
        # fallback to AI Q&A
        print(f"[⚠️ Unmatched Command] → {cmd}")
        add_user_query(cmd)
        reply = handle_user_question(cmd)
        speak(reply)
        return "stay"
