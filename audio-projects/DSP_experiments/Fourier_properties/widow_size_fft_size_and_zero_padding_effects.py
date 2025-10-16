from scipy.fftpack import fft, fftshift
import numpy as np
from math import gcd, ceil, floor
from smstools.models.dftModel import dftAnal, dftSynth
from scipy.signal import get_window
import matplotlib.pyplot as plt

def zp_fft_size_expt(x, window_size=[256, 512, 256], FFT_size=[256, 512, 512]):
    """compute magnitude spectra of x with different window sizes and FFT sizes.

    Args:
        x (np.array): input signal (512 samples long)

    Returns:
        list with magnitude spectra (np.array)
    """
    spectra=[]
    for M,N in zip(window_size,FFT_size):
        w = get_window('hamm',M)
        mX, _ =dftAnal(x[:M],w,N)
        spectra.append(mX)

    return spectra

fs = 1000
N=512
n=np.arange(N)/fs
x= .2*np.cos(2*np.pi*200*n)+.2*np.cos(2*np.pi*400*n)
plt.figure()
plt.plot(x)
plt.xlabel("amplitude")
plt.ylabel("time")
plt.show()
mags=zp_fft_size_expt(x)
plt.figure()
for i, mX in enumerate(mags):
    plt.plot(mX, label=f"Cas {i+1}")
plt.xlabel("Bin")
plt.ylabel("Magnitude (dB)")
plt.legend()
plt.title("Effets de la taille de fenêtre et du zero-padding")
plt.grid()

plt.show()
