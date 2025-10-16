import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
eps = np.finfo(float).eps
from smstools.models import stft as st
from smstools.models import utilFunctions as UF

def extract_main_lobe(window, M, N):
    """Extract the main lobe of the magnitude spectrum of a window, given a window type and its length.

    Args:
        window (str): Window type to be used (either rectangular ('boxcar'), 'hamming' or 'blackmanharris')
        M (int): length of the window to be used
        N (int): size of FFT

    Results:
        np.array: an array containing the main lobe of the magnitude spectrum of the window in decibels (dB).
    """

    w = get_window(window, M)         # get the window

    fftbuffer = np.zeros(N)
    hM1 = int(np.floor((M+1)/2))
    hM2 = int(np.floor(M /2))
    fftbuffer[:hM1]= w[hM2:]
    fftbuffer[-hM2:] = w[:hM2]

    W = fft(fftbuffer)

    mW = 20*np.log10(np.abs(W)+np.finfo(float).eps)

    mW_shifted = fftshift(mW)

    peak_id =np.argmax(mW_shifted)

    left = peak_id
    while left > 0 and mW_shifted[left] >= mW_shifted[left-1]:
        left-=1
    
    right =peak_id
    while right <len(mW_shifted) and mW_shifted[right] >= mW_shifted[right+1]:
        right+=1
    
    main_lob = mW_shifted[left:right+1]

    return main_lob


test_cases = [
    ('blackmanharris', 100, 800),
    ('boxcar', 120, 960),
    ('hamming', 256, 2048)
]

plt.figure(figsize=(15, 10))

for i, (wtype, M, N) in enumerate(test_cases, 1):
    w = get_window(wtype, M)
    
    fftbuffer = np.zeros(N)
    hM1 = int(np.floor((M + 1) / 2))
    hM2 = int(np.floor(M / 2))
    fftbuffer[:hM1] = w[hM2:]
    fftbuffer[-hM2:] = w[:hM2]
    W = fft(fftbuffer)
    mW = 20 * np.log10(np.abs(fftshift(W)) + eps)

    main_lobe = extract_main_lobe(wtype, M, N)
    lobe_width = len(main_lobe)
    norm_lobe_width = lobe_width / (N / M)

    plt.subplot(3, 1, i)
    plt.plot(mW, label=f"{wtype} (M={M}, N={N})")
    center = len(mW) // 2
    plt.axvline(center - lobe_width // 2, color='r', linestyle='--', label="Lobe start")
    plt.axvline(center + lobe_width // 2, color='g', linestyle='--', label="Lobe end")
    plt.title(f"{wtype.upper()} — Main lobe width: {lobe_width} samples — Normalized: {norm_lobe_width:.2f}")
    plt.xlabel("FFT bins (centered)")
    plt.ylabel("Magnitude (dB)")
    plt.grid()
    plt.legend()

plt.tight_layout()
plt.show()
