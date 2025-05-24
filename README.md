# 🗣️ Clara – Customizable AI Voice Assistant

**Clara** is an intelligent, voice-activated personal assistant built with Python. It uses natural language processing, speech recognition, and generative AI (Google Gemini) to help you automate tasks, answer questions, browse the internet, and more – all with your voice.

---

## Features

- **Voice Command Recognition** – Listens and understands your voice in real time.
- **Text-to-Speech Responses** – Speaks back using natural-sounding voices (Zira support included).
- **AI-Powered Conversations** – Uses Gemini 1.5 Flash to answer questions intelligently and concisely.
- **Web Automation** – Opens YouTube, Google, Gmail, Stack Overflow, and more.
- **Camera Integration** – Captures images using your webcam.
- **Wikipedia Support** – Searches and summarizes information from Wikipedia.
- **Time Announcements** – Tells you the current time when asked.
- **System Commands** – Supports voice-controlled log off or shutdown.
- **Customizable** – Easily extend with your own commands and plugins.

---
## 📁 Repository Structure

This repository contains two main files:
```
clara-voice-assistant/
├── clara.py # Main program file containing Clara's logic and flow
├── my_secrets.py # Contains the Gemini API key (keep this private)
```

---
```python
# my_secrets.py
GEMINI_API_KEY = "your_gemini_api_key_here"
```
---

## Tech Stack

- [Python](https://www.python.org/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Pyttsx3](https://pypi.org/project/pyttsx3/)
- [Wikipedia API](https://pypi.org/project/wikipedia/)
- [ecapture](https://pypi.org/project/ecapture/)
- [Google Generative AI](https://ai.google.dev/)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/noornabeelak/Clara-Customizable-Voice-Assistance

