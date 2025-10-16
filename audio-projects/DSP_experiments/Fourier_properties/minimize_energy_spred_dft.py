from scipy.fftpack import fft, fftshift
import numpy as np
from math import gcd, ceil, floor
from smstools.models.dftModel import dftAnal, dftSynth
from scipy.signal import get_window
import matplotlib.pyplot as plt


def lcm(a,b):
    return abs(a*b)//gcd(a,b)

def minimize_energy_spread_dft(x, fs, f1, f2):
    """ From a signal with two sinusoids compute its magnitude spectrum having only two non-zero value.

    Args:
        x (np.array): input signal
        fs (float): sampling frequency in Hz
        f1 (float): frequency of first sinusoid component in Hz
        f2 (float): frequency of second sinusoid component in Hz

    Returns:
        np.array: positive half of magnitude spectrum (in dB)

    """
    T1 = int(fs /f1)
    T2 = int(fs/f2)
    M= lcm(T1,T2)
    x_win=x[:M]
    X=fft(x_win)
    mag= np.abs(X[:M//2 +1])
    mag[mag<1e-6]= 1e-6
    mX = 20 * np.log10(mag)
    return mX

#tests :

fs = 10000
f1 = 80
f2 = 200
t = np.arange(0, 1, 1/fs)
x = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

mX = minimize_energy_spread_dft(x, fs, f1, f2)

plt.figure()
plt.plot(t[:250], x[:250])
plt.title("Signal case 1")
plt.xlabel("Frequency bin")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.plot(mX)
plt.title("Spectre (dB) - Test Case 1")
plt.xlabel("Index DFT")
plt.ylabel("Magnitude (dB)")
plt.grid()

plt.show()
