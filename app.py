import streamlit as st
from fpdf import FPDF
import tempfile
import os

from src.transcriber import transcribe_audio
from src.summarizer import generate_notes
from src.chat import ask_question

# --- PAGE CONFIG ---
st.set_page_config(page_title="Local Lecture Agent", layout="centered")
st.title("🎓 Local Lecture Agent (Free & Private)")
st.write("Runs 100% locally. No API keys. No internet.")

# --- SESSION STATE ---
if "transcription" not in st.session_state:
    st.session_state.transcription = None
if "notes" not in st.session_state:
    st.session_state.notes = None

# --- SIDEBAR SETTINGS ---
st.sidebar.header("Agent Settings")
whisper_model_size = st.sidebar.selectbox("Whisper Accuracy", ["base", "small", "medium"], index=0)
ollama_model = st.sidebar.text_input("Ollama Model Name", value="llama3")
st.sidebar.info("Tip: base is fast | medium is more accurate but slower")

# --- AUDIO INPUT ---
audio = st.audio_input("🎙️ Record Lecture")

if audio:
    st.success("Audio captured.")

    if st.button("▶ Start Agent"):
        # 1) SAVE TEMP AUDIO
        tmp_file_path = None
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                tmp_file.write(audio.getvalue())
                tmp_file_path = tmp_file.name
        except Exception as e:
            st.error(f"Could not save audio: {e}")

        # 2) TRANSCRIBE
        if tmp_file_path:
            with st.spinner(f"Listening (Whisper '{whisper_model_size}' running locally)..."):
                transcript = transcribe_audio(tmp_file_path, model_size=whisper_model_size)

            # cleanup temp file
            try:
                os.remove(tmp_file_path)
            except Exception:
                pass

            # If transcriber returned an error string
            if transcript.startswith("Error:"):
                st.error(transcript)
            else:
                st.session_state.transcription = transcript

        # 3) NOTES
        if st.session_state.transcription:
            with st.spinner(f"Thinking (Ollama '{ollama_model}' running locally)..."):
                notes = generate_notes(st.session_state.transcription, model_name=ollama_model)

            if notes.startswith("Error"):
                st.error(notes)
            else:
                st.session_state.notes = notes

# --- DISPLAY RESULTS ---
if st.session_state.transcription:
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📝 Professional Notes")
        if st.session_state.notes:
            st.markdown(st.session_state.notes)
        else:
            st.info("Notes not generated yet. Click ▶ Start Agent after recording.")

    with col2:
        st.subheader("🗣 Raw Transcript")
        st.write(st.session_state.transcription)

# --- Q&A AGENT ---
if st.session_state.transcription:
    st.divider()
    st.subheader("❓ Q&A Agent (Grounded in Transcript)")
    question = st.text_input("Ask a question about the lecture")

    if st.button("Ask"):
        if not question.strip():
            st.warning("Type a question first.")
        else:
            with st.spinner("Answering from transcript only..."):
                answer = ask_question(st.session_state.transcription, question.strip(), model_name=ollama_model)
            st.write(answer)

# --- PDF DOWNLOAD ---
if st.session_state.notes and st.session_state.transcription:
    st.divider()
    st.subheader("📄 Export")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    safe_notes = st.session_state.notes.encode("latin-1", "ignore").decode("latin-1")
    safe_trans = st.session_state.transcription.encode("latin-1", "ignore").decode("latin-1")

    pdf.multi_cell(0, 8, "NOTES\n\n" + safe_notes)
    pdf.add_page()
    pdf.multi_cell(0, 8, "TRANSCRIPT\n\n" + safe_trans)

    pdf_bytes = pdf.output(dest="S").encode("latin-1")

    st.download_button(
        "📥 Download PDF",
        data=pdf_bytes,
        file_name="Lecture_Notes_Local.pdf",
        mime="application/pdf"
    )
