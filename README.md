\# 🎓 Local Lecture Agent



A private, offline AI assistant that records lectures, transcribes them verbatim, and generates professional study notes using local LLMs.



\## 🚀 Features

\- 100% Local \& Private: runs entirely on your machine

\- Agentic workflow:

&nbsp; - The Ears: transcription using OpenAI Whisper (local)

&nbsp; - The Brain: summarization and reasoning using Llama 3 via Ollama

&nbsp; - The Hands: automated PDF report generation

\- Clean separation between verbatim transcript and synthesized notes

\- Planning Agent (topic breakdown)

\- Question-Answering Agent grounded strictly in the transcript



\## 🛠 Tech Stack

\- Python 3.10+

\- Streamlit

\- Ollama (local LLM inference)

\- OpenAI Whisper

\- FPDF

\- FFmpeg



\## 📦 Installation



```bash

git clone https://github.com/deshm084/lecture-agent.git

cd lecture-agent

pip install -r requirements.txt

\## 🖥 Demo Screenshots



\### Main Interface – Transcription, Notes \& Planning Agent

!\[Main UI](assets/lecture-agent-main-ui.png)



\### Q\&A Agent – Grounded Question Answering

!\[Q\&A Agent](assets/lecture-agent-qa-agent.png)



