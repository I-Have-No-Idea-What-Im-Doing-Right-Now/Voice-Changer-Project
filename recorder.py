import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
print(sd.query_devices())
def recAndPlayback():

    fs = 44100 # Sampling frequency
    duration = 2  # seconds

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    sd.stop()
    write('test.wav', fs, myrecording)
    #sd.play(myrecording, samplerate=fs, blocking=True)
    #sd.stop()
           