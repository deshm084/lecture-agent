import streamlit as st
import whisper
import ollama
from fpdf import FPDF
import tempfile
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Local Lecture Agent", layout="centered")
st.title("🎓 Local Lecture Agent (Free & Private)")
st.write("Runs 100% locally. No API keys. No internet.")

# --- SESSION STATE ---
if 'transcription' not in st.session_state:
    st.session_state.transcription = None
if 'notes' not in st.session_state:
    st.session_state.notes = None

# --- SIDEBAR ---
st.sidebar.header("Agent Settings")
model_size = st.sidebar.selectbox("Whisper Accuracy", ["base", "small", "medium"], index=0)
st.sidebar.info("base = fast | medium = more accurate (slower)")

# --- AUDIO INPUT ---
audio = st.audio_input("🎙️ Record Lecture")

if audio:
    st.success("Audio captured.")

    if st.button("▶ Start Agent"):
        # --- TRANSCRIPTION ---
        with st.spinner("Listening (Whisper running locally)..."):
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                    tmp.write(audio.getvalue())
                    audio_path = tmp.name

                model = whisper.load_model(model_size)
                result = model.transcribe(audio_path)
                st.session_state.transcription = result["text"]

                os.remove(audio_path)
            except Exception as e:
                st.error(f"Whisper error (FFmpeg?): {e}")

        # --- SUMMARIZATION ---
        if st.session_state.transcription:
            with st.spinner("Thinking (Llama 3 running locally)..."):
                try:
                    prompt = f"""
You are an expert academic note-taker.

Tasks:
1. Key concepts (bullets)
2. Important definitions
3. Deadlines or dates (if any)

Transcript:
{st.session_state.transcription}
"""

                    response = ollama.chat(
                        model="llama3",
                        messages=[{"role": "user", "content": prompt}]
                    )

                    st.session_state.notes = response["message"]["content"]
                except Exception as e:
                    st.error(f"Ollama error: {e}")

        # --- DISPLAY ---
        if st.session_state.notes:
            st.divider()
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📝 Notes")
                st.markdown(st.session_state.notes)

            with col2:
                st.subheader("🗣 Transcript")
                st.write(st.session_state.transcription)

            # --- PDF ---
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            safe_notes = st.session_state.notes.encode("latin-1", "ignore").decode("latin-1")
            safe_text = st.session_state.transcription.encode("latin-1", "ignore").decode("latin-1")

            pdf.multi_cell(0, 8, "NOTES\n\n" + safe_notes)
            pdf.add_page()
            pdf.multi_cell(0, 8, "TRANSCRIPT\n\n" + safe_text)

            pdf_bytes = pdf.output(dest="S").encode("latin-1")

            st.download_button(
                "📥 Download PDF",
                data=pdf_bytes,
                file_name="Lecture_Notes_Local.pdf",
                mime="application/pdf"
            )
