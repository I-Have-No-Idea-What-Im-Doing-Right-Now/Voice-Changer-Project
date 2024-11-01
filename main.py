import sounddevice as sd

fs = 44100 # Sampling frequency

duration = 10.5  # seconds
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
