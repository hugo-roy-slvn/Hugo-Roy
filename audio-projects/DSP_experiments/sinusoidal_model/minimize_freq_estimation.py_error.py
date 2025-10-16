import numpy as np
from scipy.signal import get_window
import math
from smstools.models import dftModel as DFT
from smstools.models import utilFunctions as UF
from smstools.models import stft
from smstools.models import sineModel as SM
import matplotlib.pyplot as plt

# E5 - 1.1: Complete the function min_freq_est_err()

def min_freq_est_err(input_file, f):
    """Best estimate the frequency of a sinusoid by iterating over different sizes of analysis window.

    Args:
            input_file (str): wav file
            f (float): frequency of the sinusoid present in the input audio signal (Hz)

    Result:
            f_est (float): estimated frequency of the sinusoid (Hz)
            M (int): Window size
            N (int): FFT size

    """
    # analysis parameters:
    window = 'blackman'
    t = -40
    fs, x = UF.wavread(input_file)
    center_sample = int(0.5 * fs)

    k = 1
    while True:
        M = 100 * k + 1
        N = 2 ** int(np.ceil(np.log2(M)))

        start = center_sample - M // 2
        end = center_sample + M // 2 + 1
        x_frame = x[start:end]

        w = get_window(window, M)
        mX, pX = DFT.dftAnal(x_frame, w, N)

        ploc = UF.peakDetection(mX, t)
        iploc, _mag, _phase = UF.peakInterp(mX, pX, ploc)

        if len(iploc) == 0:
            k += 1
            continue

        f_est = iploc[0] * fs / N
        error = abs(f_est - f)

        if error < 0.05:
            return f_est, M, N

        k += 1

print(min_freq_est_err("sine-490.wav",490))
print(min_freq_est_err("sine-1000.wav",1000))
print(min_freq_est_err("sine-200.wav",200))
