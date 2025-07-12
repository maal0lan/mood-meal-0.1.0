# 🍳 MoodMeal v0.1.0

> A voice-first, hands-free AI cooking assistant that guides you step-by-step through recipes, personalized to your mood, weather, time, and ingredients. Built with Python, Tkinter GUI, and AI integration via Mistral-Ollama.

---

## ✨ Features

- 🎙️ Voice input/output (speech-to-text + TTS)
- 🧠 AI-generated recipes (based on ingredients, weather, time)
- 🥘 Live step-by-step cooking guidance
- 🕒 Cooking timers with voice alerts
- 🗣️ Ask assistant questions mid-cook
- 📈 Progress bar & transcript log
- 💻 Offline GUI (Tkinter) for hands-free usage(experimental)

---

## 🛠️ Installation & Setup

### 1. Clone the Repo
git clone https://github.com/maal0lan/mood-meal-0.1.0.git
cd mood-meal-0.1.0

### 2. create a virtual enviroment
python -m venv venv
venv\Scripts\activate

### 3. In meanwhile install OLLAMA 
just run "setup.bat" (if that doesnt work follow below)
Ollama from: https://ollama.com/download
Once installed, open terminal and run:
ollama run mistral

### 4. install all dependcies from req.txt
pip install -r req.txt

### 5. run the launcher.py
this will invoke gui/main_window.py

###  6. add in your prompt 
#### for example:

"I have eggs, bread, and some cheese — make me something quick. Cook time: 15 mins. Weather: Rainy. I’m tired." 

### 7. you have to wait 3-4 mins approx for generating 7 diffrent recipes where first 4 are the more popular and  last 3 are has mid popularity and has ingeridents that are not mentioned 

### 8. start live cooking where a seperate dialog box opens where all recipe list is shown and it will recite each step of the recipe you can also ask questions by typing or in voice input,and gives timers if it has a timer  (experimental but works if there is less delay on generating the answer  . voice input is experimental but in the cli when running the code from vscode powershell or in cmd the output is displayed also timer is still experimental but works at some part i cant fix it cleanly )

### 8. OR if you just need the process to make the recipe it give a step by step instructions shown on screen



### 9. manually close the window after completing the recipe

##### 10. future updates have APIs for faster execution and imporved memory when chatting with AI for sarcasm , also has timers that are precisely set for each step by an AI itself and has hands free full-on voice based assistance while cooking dynamically :)) (mood-meal-0.2.0)

