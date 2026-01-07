import ollama

def generate_notes(transcript, model_name="llama3.2"):
    """
    The Brain: Reads transcript and creates structured notes.
    """
    prompt = f"""
    You are an expert academic note-taker.
    Analyze the following transcript and create professional study notes.

    Structure:
    1. 📌 Executive Summary (2–3 sentences)
    2. 🔑 Key Concepts (Bullet points with definitions)
    3. 📅 Deadlines & Action Items (If any)

    TRANSCRIPT:
    {transcript}
    """

    try:
        response = ollama.chat(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error connecting to Ollama: {str(e)}"
