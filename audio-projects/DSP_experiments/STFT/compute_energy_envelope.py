import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
eps = np.finfo(float).eps
from smstools.models import stft as st
from smstools.models import utilFunctions as UF

def compute_eng_env(input_file, window, M, N, H):
    """Compute band-wise energy envelopes of a given audio signal using the STFT.

    Args:
        input_file (string): input sound file (monophonic with sampling rate of 44100)
        window (string): analysis window type (choice of rectangular, triangular, hanning,
                hamming, blackman, blackmanharris)
        M (integer): analysis window size (odd positive integer)
        N (integer): FFT size (power of 2, such that N > M)
        H (integer): hop size for the stft computation

    Result:
        np.array: magnitude spectra of sound (2D array)
        np.array: 2D numpy array with energy envelope of band 0 < f < 3000 Hz (in dB) in first column, [:,0]
        np.array: energy envelope of band 3000 < f < 10000 Hz (in dB) in second column [:,1]
    """

    fs, x = UF.wavread(input_file)
    w=get_window(window,M)

    xmX,xpX=st.stftAnal(x,w,N,H)

    bin_freqs = np.arange(N//2 + 1) * fs / N

    low_band_bins = np.where((bin_freqs > 0) & (bin_freqs < 3000))[0]
    high_band_bins = np.where((bin_freqs > 3000) & (bin_freqs < 10000))[0]
    print(low_band_bins)
    print(high_band_bins)
    nb_frame= xmX.shape[0]
    energy_env=np.zeros((nb_frame,2))

    for i in range(nb_frame):
        low_energy = np.sum(np.square(xmX[i, low_band_bins]))
        high_energy = np.sum(np.square(xmX[i, high_band_bins]))

        energy_env[i, 0] = 10 * np.log10(low_energy + np.finfo(float).eps)
        energy_env[i, 1] = 10 * np.log10(high_energy + np.finfo(float).eps)

    return xmX, energy_env

input_file = "sax-phrase-short.wav"
window = "hamming"
M = 513
N = 4096
H = 128

xmX, energy_env = compute_eng_env(input_file, window, M, N, H)

# Récupération des dimensions et axes
fs, x = UF.wavread(input_file)
nb_frames = xmX.shape[0]
time = np.arange(nb_frames) * H / fs
freq_axis = np.arange(N//2 + 1) * fs / N

# --- Affichage ---
plt.figure(figsize=(14, 8))

# 1. Spectrogramme
plt.subplot(2, 1, 1)
plt.pcolormesh(time, freq_axis, xmX.T, shading='gouraud')
plt.title("Spectrogramme du signal")
plt.xlabel("Temps (s)")
plt.ylabel("Fréquence (Hz)")
plt.colorbar(label="Amplitude (dB)")

# 2. Enveloppes d’énergie
plt.subplot(2, 1, 2)
plt.plot(time, energy_env[:, 0], label="Énergie 0–3kHz (basse)")
plt.plot(time, energy_env[:, 1], label="Énergie 3–10kHz (haute)")
plt.title("Enveloppes d’énergie par bande")
plt.xlabel("Temps (s)")
plt.ylabel("Énergie (dB)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
