import numpy as np
from scipy.io.wavfile import write

def apply(file: np.ndarray, amm):
    return np.multiply(file, [amm])

def applyAndSave(file: np.ndarray, amm):
    write('modified.wav', 44100, apply(file, amm))