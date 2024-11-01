import sounddevice as sd
import numpy as np

def recAndPlayback():

    fs = 44100 # Sampling frequency
    duration = 2  # seconds

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print(myrecording)
    sd.play(data=myrecording, samplerate=fs)
    sd.wait()
    sd.stop()
                               