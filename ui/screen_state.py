# ui/screen_state.py
step_box = None
timer_box = None
transcript_box = None

def bind_gui(step, timer, transcript):
    global step_box, timer_box, transcript_box
    step_box = step
    timer_box = timer
    transcript_box = transcript

def update_step(text):
    if step_box:
        step_box.update_step(text)

def update_timer(text):
    if timer_box:
        timer_box.update_timer(text)

def add_transcript(text):
    if transcript_box:
        transcript_box.update_transcript(text)