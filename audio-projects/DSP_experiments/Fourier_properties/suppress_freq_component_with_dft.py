from scipy.fftpack import fft, fftshift
import numpy as np
from math import gcd, ceil, floor
from smstools.models.dftModel import dftAnal, dftSynth
from scipy.signal import get_window
import matplotlib.pyplot as plt

def suppress_freq_dft_model(x, fs, N):
    """
    Args:
        x (np.array): input signal of length M (odd size)
        fs (float): sampling frequency (Hz)
        N (int): FFT size

    Returns:
       np.array: output signal with filtering (N samples long)
    """
    M = len(x)
    w = get_window('hamming', M)
    outputScaleFactor = sum(w)

    mX, pX = dftAnal(x,w,N)
    cut_bin= int(np.ceil(70*N)/fs)
    mX[:cut_bin+1]=-120

    y = dftSynth(mX,pX,M)*outputScaleFactor

    return y

#test :

fs = 10000
N=1024
t = np.arange(N)/fs

frqs1=[40,100,200,1000]
x1=sum(np.sin(2*np.pi*f*t)for f in frqs1)
y1=suppress_freq_dft_model(x1,fs,N)
print(y1)

frqs2=[23,36,230,900,2300]
x2=sum(np.sin(2*np.pi*f*t)for f in frqs2)
y2=suppress_freq_dft_model(x2,fs,N)
print(y2)

def plot_spectra(x, y, fs, N, title):
    w = get_window('hamming', len(x))
    mX_x, _ = dftAnal(x, w, N)
    mX_y, _ = dftAnal(y, w, N)

    freqs = np.linspace(0, fs/2, N//2 + 1)

    plt.figure(figsize=(10,4))
    plt.plot(freqs, mX_x, label="Avant filtrage")
    plt.plot(freqs, mX_y, label="Après filtrage")
    plt.title(title)
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()

plot_spectra(x1, y1, fs, N, "Test Case 1 - fs=10kHz")
plot_spectra(x2, y2, fs, N, "Test Case 2 - fs=48kHz")
