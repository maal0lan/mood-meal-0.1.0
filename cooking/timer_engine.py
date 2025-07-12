import asyncio
from ui.screen_state import update_timer
from voice.tts import speak

async def run_timer(seconds):
    halfway = seconds // 2
    for i in range(seconds):
        mins, secs = divmod(seconds - i, 60)
        update_timer(f"{mins:02d}:{secs:02d}")
        await asyncio.sleep(1)

        if i == halfway:
            speak("You're halfway through this step.")
        if i == seconds - 30:
            speak("Just 30 seconds left.")

    update_timer("—")
    speak("Time’s up for this step!")
