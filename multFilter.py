import numpy as np
from scipy.io.wavfile import write

def applyAndSave(file: np.ndarray):
    write('modified.wav', 44100, np.multiply(file, [500000]))