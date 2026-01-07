import ollama

def ask_question(transcript, question, model_name="llama3.2"):
    """
    The Tutor: Answers user questions based ONLY on the transcript.
    """
    prompt = f"""
    You are a helpful tutor.
    Answer the student's question based strictly on the lecture transcript below.
    If the answer is not in the transcript, say:
    "The professor didn't mention that."

    TRANSCRIPT:
    {transcript}

    STUDENT QUESTION:
    {question}
    """

    try:
        response = ollama.chat(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
