import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

print(sd.query_devices())


def recAndPlayback():

    fs = 44100 # Sampling frequency
    duration = 2  # seconds

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="float32")
    sd.wait()
    sd.stop()

    write('test.wav', fs, recording)

    sd.play(recording, samplerate=fs, blocking=True)
    
    print(recording.shape)
    print(recording)
    
    return recording
    