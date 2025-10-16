from scipy.fftpack import fft, fftshift
import numpy as np
from math import gcd, ceil, floor
from smstools.models.dftModel import dftAnal, dftSynth
from scipy.signal import get_window
import matplotlib.pyplot as plt

def test_real_even(x):
    """check if x is real and even using the symmetry properties of its DFT.
    Args:
        x (np.array): input signal of length M (M is odd)

    Returns:
        tuple including:
        isRealEven (boolean): True if input x is real and even, and False otherwise
        dftbuffer (np.array): M point zero phase windowed version of x
        X (np.array): M point DFT of dftbuffer

    """
    M = len(x)
    
    hM1 = floor((M + 1) / 2)
    hM2 = floor(M / 2)
    dftbuffer = np.zeros(M)
    dftbuffer[:hM1] = x[hM2:]
    dftbuffer[-hM2:] = x[:hM2]

    # DFT
    X = fft(dftbuffer)

    isRealEven = np.all(np.abs(np.imag(X)) < 1e-6)

    return isRealEven, dftbuffer, X

x1 = np.array([2, 3, 4, 3, 2])
isEven1, dftbuffer1, X1 = test_real_even(x1)
print("Test Case 1 — Est pair et réel ?", isEven1)
print("dftbuffer :", dftbuffer1)
print("X :", np.round(X1, 4))

x2 = np.array([1, 2, 3, 4, 1, 2, 3])
isEven2, dftbuffer2, X2 = test_real_even(x2)
print("Test Case 2 — Est pair et réel ?", isEven2)
print("dftbuffer :", dftbuffer2)
print("X :", np.round(X2, 4))

x3 = get_window('hann', 51, fftbins=False)
isEven3, dftbuffer3, X3 = test_real_even(x3)

plt.figure()
plt.plot(x3)
plt.title("Signal d'entrée (fenêtre Hanning)")
plt.xlabel("Échantillons")
plt.ylabel("Amplitude")

plt.figure()
plt.plot(np.real(X3), label="Partie réelle")
plt.plot(np.imag(X3), label="Partie imaginaire")
plt.title("DFT de la fenêtre Hanning")
plt.xlabel("Indice DFT")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
