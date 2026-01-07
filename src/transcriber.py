import whisper

def transcribe_audio(file_path, model_size="base"):
    """
    The Ears: Listens to audio and returns raw text.
    """
    try:
        model = whisper.load_model(model_size)
        result = model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        return f"Error: {str(e)}"
