import pyaudio
import wave
import numpy as np
import time
import Speak_and_text
import text_to_speak


def recording():
    # Kaydedilecek dosyanın adı ve kayıt süresi
    filename = "output.mp3"
    duration = 10000  # saniye cinsinden

    # PyAudio öğesi oluşturma
    audio = pyaudio.PyAudio()

    # Ses kaydı için ayarlar
    format = pyaudio.paInt16
    channels = 1
    rate = 44100
    frames_per_buffer = 1024

    # Stream başlatma ve kayıt yapma
    stream = audio.open(format=format, channels=channels, rate=rate,
                        input=True, frames_per_buffer=frames_per_buffer)
    frames = []
    silent_count = 0 # ardışık sessiz frame sayısı
    
    time.sleep(1)

    # Speak_and_text.speak("konuşmaya başla")
    
    text_to_speak.konus("konusmaya basla")

    print("Ses kaydı başladı.")

    for i in range(int(rate / frames_per_buffer * duration)):
        data = stream.read(frames_per_buffer)
        frames.append(data)
        
        # Ses seviyesini hesaplama
        audio_data = np.frombuffer(data, dtype=np.int16)
        audio_level = np.abs(audio_data).mean()
        
        # Eşik seviyesi
        threshold = 50
        
        # Eğer ses seviyesi eşik seviyesinin altındaysa, sessiz frame sayısını artırın.
        if audio_level < threshold:
            silent_count += 1
        else:
            silent_count = 0
            
        # Ardışık sessiz frame sayısı, belirli bir sürenin üzerine çıkarsa kaydı durdurun.
        max_silent_frames = int(rate / frames_per_buffer * 3)  # 3 saniye
        if silent_count > max_silent_frames:
            
            print("Kayıt durduruldu.")
            break

    # Stream ve PyAudio öğesini kapatma
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Ses dosyasını kaydetme
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Ses kaydı dosyası {}'ye kaydedildi.".format(filename))
    print("metin çıktısı bekleniyor.....")

if __name__=='__main__':
    recording()
