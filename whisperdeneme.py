import whisper

def sestotext():
    
    model = whisper.load_model("base")
    result = model.transcribe("output.mp3")
    
    print(result["text"])


