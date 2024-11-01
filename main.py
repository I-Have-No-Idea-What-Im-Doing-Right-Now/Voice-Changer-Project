#Sources:
#https://pypi.org/project/pvrecorder/
#https://github.com/jiaaro/pydub
import pydub as pd
from pvrecorder import PvRecorder
from time import time
import wave
import struct

SAVE_PATH = "sigma.wav"

recorder = PvRecorder(device_index=-1, frame_length=512)
recorder.start()

sTime = time()
frames=[]
while time() < sTime + 1:
    frame = recorder.read()
    frames.append(frame)

recorder.stop()

with wave.open(SAVE_PATH, 'w') as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack("h" * len(frames), *frames))
