# 🟢 Waitless Pro (v2.1)

**A local-first, privacy-focused AI lecture companion built for speed and stability.**

### 📸 Application Demo

| Studio Mode (Input) | Smart Notes (Output) |
|:------------------:|:-------------------:|
| ![Dashboard](assets/dashboard.png) | ![Results](assets/results.png) |

---

Waitless Pro captures lecture audio, transcribes it locally using OpenAI Whisper, and generates structured study notes using Llama 3 via Ollama. It also supports transcript-grounded Q&A and PDF export — all running fully offline.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-ff4b4b)
![Privacy](https://img.shields.io/badge/Privacy-Local%20Processing-green)

---

## 🚀 Key Features

- 🎙️ **Studio Mode** – Record or upload lecture audio
- ⚡ **Instant Performance** – Heavy models loaded once (cache-ready)
- 💾 **Persistence Ready** – Architecture supports autosave of transcripts & notes
- 🔒 **Privacy First** – 100% local processing, no cloud calls
- 📝 **Smart Notes** – Converts raw transcripts into structured academic notes
- 💬 **Tutor Mode** – Ask questions strictly grounded in the lecture transcript
- 📄 **Export** – Download notes + transcript as PDF

---

## 🛠 Tech Stack

- **Frontend:** Streamlit (Custom CSS UI)
- **ASR:** OpenAI Whisper (`base`, `small`, `medium`)
- **LLM:** Ollama (`llama3`)
- **PDF:** FPDF
- **Backend:** Python

---

## ⚙️ Installation

### 1️⃣ Prerequisites

- Python **3.10+**
- [Ollama](https://ollama.com/) installed and running
- FFmpeg installed (required for audio decoding)

Pull the Llama model:
```bash
ollama pull llama3
2️⃣ Clone & Install
bash
Copy code
git clone https://github.com/deshm084/lecture-agent.git
cd lecture-agent
pip install -r requirements.txt
🏃 Usage
Run the application locally:

bash
Copy code
python -m streamlit run app.py
Workflow
Record or upload a lecture

Start the processing pipeline

View:

📝 Structured notes

💬 Tutor Q&A

📜 Full transcript

Download notes as PDF

📂 Project Structure
text
Copy code
lecture-agent/
├── app.py                 # Main Streamlit app
├── src/                   # Core agents (transcriber, summarizer, tutor)
├── images/                # UI screenshots / assets
├── requirements.txt       # Dependencies
└── README.md              # Documentation
🤝 Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss your ideas.

Built with ❤️ by Sanskruti

markdown
Copy code

---

### ✅ What I fixed (important)
- ❌ Removed broken Markdown links like `[https://...]`
- ❌ Removed `git init` (you already have a repo)
- ✅ Correct Windows-friendly run command
- ✅ Matches your **actual project**
- ✅ Reads like a **real production repo**

If you want next:
- 🔥 “v2.2” autosave + caching code
- 🔥 Badges for Whisper / Ollama
- 🔥 Screenshots section
- 🔥 License file (MIT)

Just say the word.
