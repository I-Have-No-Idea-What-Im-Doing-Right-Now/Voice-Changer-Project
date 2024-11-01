import sounddevice as sd
import numpy as np

def recAndPlayback():

    fs = 44100 # Sampling frequency
    duration = 2  # seconds

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    sd.stop()
    print(myrecording)
    sd.play(myrecording, samplerate=fs, blocking=True)
    sd.stop()
           