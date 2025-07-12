import tkinter as tk
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tkinter import ttk
from ai.preprocress_input import preprocess_input
from ai.recipe_suggester import get_recipe_suggestions
from cooking.live_chef import start_cooking_session
from gui.cooking_window import CookingWindow


class MoodMealMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MoodMeal 🍽️ - Your Voice Cooking Assistant")
        self.geometry("800x600")

        self.intro = ttk.Label(self, text="Tell me what you have or feel like cooking (time, mood, ingredients)", font=("Arial", 14), wraplength=700)
        self.intro.pack(pady=20)

        self.input_box = ttk.Entry(self, font=("Arial", 12), width=80)
        self.input_box.pack(pady=10)

        self.submit_button = ttk.Button(self, text=" Suggest Recipes", command=self.handle_first_input)
        self.submit_button.pack(pady=10)

        self.result_text = tk.Text(self, height=12, width=90, font=("Arial", 11))
        self.result_text.pack(pady=10)

        self.recipe_label = ttk.Label(self, text="Type your chosen recipe name:", font=("Arial", 12))
        self.recipe_label.pack(pady=5)

        self.recipe_entry = ttk.Entry(self, font=("Arial", 12), width=50)
        self.recipe_entry.pack()

        self.start_button = ttk.Button(self, text="🔥 Start Live Cooking", command=self.start_live_cook)
        self.start_button.pack(pady=5)

        self.skip_button = ttk.Button(self, text="😤 Nah I’ll cook myself", command=self.show_static_steps)
        self.skip_button.pack(pady=5)

    def handle_first_input(self):
        raw_input = self.input_box.get()
        structured_context = preprocess_input(raw_input)
        suggestions = get_recipe_suggestions(structured_context)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, suggestions)

    def start_live_cook(self):
        recipe = self.recipe_entry.get()
        # Basic assumption; you can link to stored data for actual ingredients and time
        ingredients = "eggs, tomato, rice"
        cook_time = "30 min"
        CookingWindow(self, recipe, ingredients, cook_time)

    def show_static_steps(self):
        # For non-live cooking
        from ai.step_generator import get_steps_for_recipe
        recipe = self.recipe_entry.get()
        steps_json = get_steps_for_recipe(recipe, "eggs, tomato", "30 min")
        import json
        try:
            steps = json.loads(steps_json)["steps"]
            step_list = "\n\n".join([f"{s['step_number']}. {s['instruction']}" for s in steps])
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "Here are the full steps:\n\n" + step_list)
        except Exception as e:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "Failed to generate steps.\n" + str(e))

if __name__ == "__main__":
    app = MoodMealMain()
    app.mainloop()
