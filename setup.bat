

```bat
@echo off
echo 🚀 Installing Ollama and pulling Mistral model...

REM Check for admin
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Please run this script as Administrator!
    pause
    exit /b
)

REM Download Ollama
echo 🔽 Downloading Ollama...
curl -L https://ollama.com/download/OllamaSetup.exe -o OllamaSetup.exe

echo 🧠 Installing Ollama...
start /wait OllamaSetup.exe

REM Add ollama to PATH if needed (usually handled by installer)
echo 🧲 Pulling Mistral model...
ollama pull mistral

echo ✅ Done! You can now run: ollama run mistral
pause
