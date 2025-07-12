import tkinter as tk
from tkinter import ttk
import asyncio
import threading
import json

from voice.voice_listener import listen_for_command
from voice.tts import speak
from voice.command_router import route_voice_command
from assistant.context_memory import update_context
from assistant.conversational_ai import handle_user_question
from cooking.step_generator import get_next_step
from cooking.timer_engine import run_timer
from gui.components.voice_waveform import WaveformWidget


class CookingWindow(tk.Toplevel):
    def __init__(self, master, recipe_name, ingredients, cook_time):
        super().__init__(master)
        self.title(f"Cooking: {recipe_name}")
        self.geometry("900x600")
        self.configure(bg="#1a1a1a")

        self.paused = False
        self.skip_current = False
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.cook_time = cook_time
        self.current_index = 0
        self.steps = []

        # UI setup
        self.left_frame = tk.Frame(self, bg="#1a1a1a")
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)
        self.step_listbox = tk.Listbox(self.left_frame, width=50, height=25, font=("Courier", 10))
        self.step_listbox.pack()

        self.right_frame = tk.Frame(self, bg="#1a1a1a")
        self.right_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)
        self.waveform = WaveformWidget(self.right_frame)
        self.waveform.pack(pady=5)
        self.step_label = ttk.Label(self.right_frame, text="Step will appear here", wraplength=400, font=("Arial", 14))
        self.step_label.pack(pady=10)

        self.timer_frame = tk.Frame(self.right_frame, bg="#1a1a1a")
        self.timer_frame.pack(pady=5)
        self.timer_label = ttk.Label(self.timer_frame, text="Timer: ⏱️", font=("Arial", 12))
        self.timer_label.grid(row=0, column=0, padx=10)
        self.status_label = ttk.Label(self.timer_frame, text="Status: Ready", font=("Arial", 12))
        self.status_label.grid(row=0, column=1, padx=10)

        self.progress = ttk.Progressbar(self.right_frame, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        self.transcript_label = ttk.Label(self.right_frame, text="You said: ", font=("Arial", 11))
        self.transcript_label.pack(pady=10)

        self.controls_frame = tk.Frame(self.right_frame, bg="#1a1a1a")
        self.controls_frame.pack(pady=10)
        self.pause_btn = tk.Button(self.controls_frame, text=" Pause", command=self.pause_timer, bg="#ffdd01", fg="black")
        self.pause_btn.grid(row=0, column=0, padx=5)
        self.resume_btn = tk.Button(self.controls_frame, text=" Resume", command=self.resume_timer, bg="#ddff01", fg="black")
        self.resume_btn.grid(row=0, column=1, padx=5)
        self.skip_btn = tk.Button(self.controls_frame, text=" Next Step", command=self.skip_step, bg="#ff5050", fg="white")
        self.skip_btn.grid(row=0, column=2, padx=5)

        self.query_entry = tk.Entry(self.right_frame, width=50)
        self.query_entry.pack(pady=5)
        self.ask_btn = tk.Button(self.right_frame, text="Ask Assistant", command=self.ask_backup_question)
        self.ask_btn.pack(pady=5)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        threading.Thread(target=self.load_steps).start()

    def load_steps(self):
        speak("Getting your recipe steps ready. Wait for 2 minutes while I generate those steps. Meanwhile, prepare the utensils.")
        steps_json = get_next_step(self.recipe_name, self.ingredients, self.cook_time)
        try:
            self.steps = json.loads(steps_json)["steps"]
            for step in self.steps:
                self.step_listbox.insert(tk.END, f"Step {step['step_number']}: {step['instruction']}")
            self.run_step_loop()
        except Exception as e:
            print("Failed to parse steps:", e)
            speak("Sorry, couldn’t load the recipe steps.")

    def update_step_ui(self):
        current = self.steps[self.current_index]
        step_text = current["instruction"]
        step_num = current["step_number"]
        self.step_label.config(text=f"Step {step_num}: {step_text}")
        self.step_listbox.selection_clear(0, tk.END)
        self.step_listbox.selection_set(self.current_index)
        self.step_listbox.activate(self.current_index)
        self.progress["value"] = self.current_index + 1

    def announce_step(self):
        step = self.steps[self.current_index]
        speak(f"Step {step['step_number']}: {step['instruction']}")

    def run_step_loop(self):
        self.progress["maximum"] = len(self.steps)
        asyncio.run(self._run_step_loop())

    async def _run_step_loop(self):
        while self.current_index < len(self.steps):
            step = self.steps[self.current_index]
            self.status_label.config(text="Active Step")
            step_text = step["instruction"]
            step_num = step["step_number"]
            duration = step.get("duration", "0 min")

            update_context(self.recipe_name, step_num, step_text, self.ingredients)
            self.update_step_ui()
            self.announce_step()
            await asyncio.sleep(0.5)

            try:
                mins = int(duration.split()[0])
            except:
                mins = 0

            self.skip_current = False
            if mins > 0:
                speak(f"This step takes {mins} minutes. Timer starts now.")
                await run_timer_async(mins * 60, self.timer_label, self)
            else:
                self.timer_label.config(text="No timer ⏱️")

            speak("Say 'next', 'repeat', 'skip', or ask a question.")
            while True:
                cmd = await asyncio.to_thread(listen_for_command)
                self.transcript_label.config(text=f"You said: {cmd}")
                action = route_voice_command(cmd, step_text, self.recipe_name, step_num, self.ingredients)

                if action == "next":
                    self.current_index += 1
                    break
                elif action == "repeat":
                    self.announce_step()
                elif action == "stay":
                    continue

        self.show_completion_button()

    def show_completion_button(self):
        self.finish_btn = tk.Button(self.right_frame, text="🎉 Finish Cooking", command=self.complete_cooking, bg="#66ff66", fg="black")
        self.finish_btn.pack(pady=10)

    def complete_cooking(self):
        speak("🎉 That’s it, baby. You cooked it! Enjoy your masterpiece.")
        self.post_completion_prompt()

    def post_completion_prompt(self):
        speak("Wanna go back and try another recipe? Or exit the app?")
        prompt = tk.Toplevel(self)
        prompt.title("What’s next?")
        prompt.geometry("300x150")
        tk.Label(prompt, text="What's next?").pack(pady=10)
        tk.Button(prompt, text="🔁 Try Another Recipe", command=lambda: [prompt.destroy(), self.on_close()]).pack(pady=5)
        tk.Button(prompt, text="❌ Exit", command=self.quit_app).pack(pady=5)

    def quit_app(self):
        speak("Goodbye. Come cook with me again!")
        self.destroy()
        self.master.destroy()

    def on_close(self):
        self.destroy()

    def pause_timer(self):
        self.paused = True
        speak("Paused.")

    def resume_timer(self):
        self.paused = False
        speak("Resuming.")

    def skip_step(self):
        self.skip_current = True
        self.current_index += 1
        if self.current_index < len(self.steps):
            self.update_step_ui()
            speak(f"Next{self.steps[self.current_index]['step_number']}")
            self.announce_step()
            
        else:
            self.update_step_ui()
            self.show_completion_button()

    def ask_backup_question(self):
        query = self.query_entry.get()
        if query.strip():
            answer = handle_user_question(query)
            self.transcript_label.config(text=f"AI: {answer}")
            speak(answer)
            self.query_entry.delete(0, tk.END)


# Timer with listening
async def run_timer_async(seconds, label_widget, cooking_window):
    halfway = seconds // 2

    async def countdown():
        for i in range(seconds):
            while cooking_window.paused:
                await asyncio.sleep(1)

            if cooking_window.skip_current:
                cooking_window.skip_current = False
                label_widget.config(text="Timer: ⏱️")
                cooking_window.status_label.config(text="⏭️ Step Skipped.")
                return

            mins, secs = divmod(seconds - i, 60)
            label_widget.config(text=f"Timer: {mins:02d}:{secs:02d}")
            await asyncio.sleep(1)

            if i == halfway:
                speak("You're halfway through this step.")
            if i == seconds - 30:
                speak("30 seconds left.")

        label_widget.config(text="Timer: ⏱️")
        cooking_window.status_label.config(text="⏰ Time’s up!")
        speak("⏰ Time’s up for this step!")

    async def listen_loop():
        while True:
            if cooking_window.paused:
                await asyncio.sleep(1)
                continue

            cmd = await asyncio.to_thread(listen_for_command)
            cooking_window.transcript_label.config(text=f"You said: {cmd}")

            if "pause" in cmd:
                cooking_window.paused = True
                speak("Paused.")
            elif "resume" in cmd:
                cooking_window.paused = False
                speak("Resuming.")
            elif "skip" in cmd:
                cooking_window.skip_current = True
                speak("Skipping the timer.")
                break
            elif any(q in cmd for q in ["what", "how", "can I", "why", "when"]):
                answer = handle_user_question(cmd)
                speak(answer)

            await asyncio.sleep(0.5)

    await asyncio.gather(countdown(), listen_loop())
