import json
import time
from voice.tts import speak
from cooking.step_generator import get_next_step
from cooking.timer_engine import run_timer
from voice.voice_listener import listen_for_command
from ui.screen_state import update_step
from voice.command_router import route_voice_command

def start_cooking_session(recipe_name, ingredients, cook_time):
    speak(f"Let's start cooking {recipe_name}. I'm getting the steps ready...")
    steps_json = get_next_step(recipe_name, ingredients, cook_time)
    
    try:
        steps = json.loads(steps_json)["steps"]
    except Exception as e:
        print("Error parsing steps JSON:", e)
        speak("Sorry, I couldn’t parse the steps.")
        return

    for step in steps:
        step_text = step["instruction"]
        duration = step.get("duration", "0 min")
        speak(f"Step {step['step_number']}: {step_text}")
        print(f"\n[{step['step_number']}] {step_text} ({duration})")

        # Convert to seconds
        try:
            minutes = int(duration.split()[0])
        except:
            minutes = 0

        # Start timer
        if minutes > 0:
            speak(f"This will take {minutes} minutes. Timer started.")
            run_timer(minutes * 60)
        else:
            speak("No specific time mentioned for this step.")

        # Wait for user input before next step
        speak("Say 'next' when you're ready, or 'repeat' to hear again.")
        while True:
            cmd = listen_for_command()
            result = route_voice_command(cmd, step_text, recipe_name, step['step_number'], ingredients)
            if result == "next":
                break
            elif result == "repeat":
                speak(step_text)
