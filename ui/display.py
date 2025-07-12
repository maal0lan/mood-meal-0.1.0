
from rich.panel import Panel
from rich.console import Console
from rich.layout import Layout
from time import sleep
from ui.screen_state import get_state

console = Console()

def render():
    layout = Layout()
    layout.split_column(
        Layout(name="transcript"),
        Layout(name="step"),
        Layout(name="timer")
    )

    while True:
        state = get_state()
        transcript_text = "\n".join(state["transcript_log"][-5:])
        layout["transcript"].update(
            Panel(transcript_text or "Listening...", title="🎙️ Transcript")
        )
        layout["step"].update(
            Panel(state["current_step"], title="📋 Step")
        )
        layout["timer"].update(
            Panel(state["timer_left"], title="⏱️ Timer")
        )

        console.clear()
        console.print(layout)
        sleep(1)
