# Voice Assistant with Web Automation & AI Chat

This is a Python-based personal voice assistant capable of executing voice commands for browsing the internet, fetching news, interacting with Spotify, taking notes, setting focus timers, and even chatting using an integrated LLM model (Ollama).

## ✨ Features

- 🎙️ **Voice Recognition**: Listens for commands via microphone input.
- 🗣️ **Text-to-Speech (TTS)**: Speaks responses using `pyttsx3`.
- 🌐 **Web Automation**: Opens websites like Google, YouTube, Quora, Spotify, Amazon, and weather reports based on user commands.
- 📰 **News Fetching**: Fetches top headlines from BBC using NewsAPI.
- ✅ **To-Do List Manager**: Add and view tasks from a persistent text file.
- ⏲️ **Focus Timer**: 15-minute focus mode with notification on completion.
- 🖼️ **Image Generation Shortcut**: Opens an image editor with a text prompt.
- 🤖 **AI Chat Assistant**: Falls back to Ollama-based chatbot for open-ended queries.

## 🛠️ Requirements

Install the dependencies using pip:

```bash
pip install pyttsx3 SpeechRecognition requests plyer wikipedia ollama
