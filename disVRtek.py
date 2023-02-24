import os
import time
import Record
import whisperdeneme
import Speak_and_text


Record.recording()
time.sleep(4)
whisperdeneme.sestotext2()
# os.remove("output.mp3")
