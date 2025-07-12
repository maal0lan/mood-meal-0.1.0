# 🍳 MoodMeal v0.1.0

> A voice-first, hands-free AI cooking assistant that guides you through personalized recipes — powered by Mistral via Ollama, wrapped in a sleek Tkinter GUI. Just speak. Cook. Slay.

---

## ✨ Features

- 🎙️ **Voice Input & Output**  
  Real-time speech-to-text and TTS (talks back with sass or sweetness — your choice).

- 🧠 **AI-Generated Recipes**  
  Based on your ingredients, weather, cook time, and vibes.

- 🥘 **Live Step-by-Step Cooking Guidance**  
  Spoken instructions, timers, progress — all in one hands-free interface.

- 🕒 **Built-in Cooking Timers**  
  Voice alerts for time-sensitive steps, including "halfway there" or "30 seconds left".

- 🗣️ **Ask Questions Mid-Cooking**  
  Ask anything while cooking — AI will explain, suggest, or cheer you on.

- 💻 **Offline GUI**  
  Minimalist Tkinter-based GUI with waveform animation and real-time interaction.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/maal0lan/mood-meal-0.1.0.git
cd mood-meal-0.1.0
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Ollama + Mistral

> Already included in `setup.bat`, or do it manually:

* Download Ollama: [https://ollama.com/download](https://ollama.com/download)
* Then run in terminal:

```bash
ollama run mistral
```

### 4️⃣ Install Python Dependencies

```bash
pip install -r req.txt
```

### 5️⃣ Launch MoodMeal GUI

```bash
python launcher.py
```

---

## 🧪 How to Use

### 🧾 Input Prompt (Text or Voice)

```text
I have eggs, bread, and some cheese — make me something quick.
Cook time: 15 mins. Weather: Rainy. I’m tired.
```

### ⏳ Step Generation (Wait \~2–3 min)

* AI generates **7 recipe suggestions**
* Top 4 are popular, bottom 3 are creative/unusual
* Recipes are personalized to weather, ingredients, and mood

---

## 🍳 Start Cooking!

* Click **"Start Live Cooking"**
* A separate cooking window opens
* AI reads steps aloud, tracks progress, and sets timers
* You can **ask questions**, say **“repeat”**, or **skip steps**
* Experimental voice command and timer support included

> Prefer just reading? Click **“Nah I’ll Cook”** and view the full steps instantly.

---

## ⚠️ Current Limitations (v0.1.0)

* Voice commands & timers are **experimental**
* Responses may lag depending on local LLM processing
* Not all cooking steps have accurate durations
* Window must be manually closed after completion

---

## 🔮 Coming in v0.2.0

* Full hands-free **voice-driven cooking**
* **Dynamic timers per step**, AI-calculated
* **Sarcasm, memory, and personalization** for recurring cooks
* Hugging Face API fallback for faster, cloud-based results

---

