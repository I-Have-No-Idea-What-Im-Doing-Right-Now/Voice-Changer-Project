import numpy as np
from scipy.io.wavfile import write

def apply(file: np.ndarray):
    import multFilter # Only needed in the function

    out = file

    for i in range(out.__len__()):
        if i % 10 != 0:
            out[i][0] = 0.0

    return multFilter.apply(out, 3)

def applyAndSave(file: np.ndarray):

    write('modified.wav', 44100, apply(file))