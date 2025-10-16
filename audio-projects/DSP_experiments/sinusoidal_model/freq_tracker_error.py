import numpy as np
from scipy.signal import get_window
import math
from smstools.models import dftModel as DFT
from smstools.models import utilFunctions as UF
from smstools.models import stft
from smstools.models import sineModel as SM
import matplotlib.pyplot as plt

def gen_time_stamps(xlen, M, fs, H):
    """Generate frame time stamps for a given signal length and sampling rate.

    Args:
        xlen (int): duration of signal in samples
        M (int): window size
        fs (int): sampling rate
        H (int): hop size

    Result:
        np.array: time stamps

    """
    hM1 = int(np.floor((M+1)/2))
    hM2 = int(np.floor(M/2))
    xlen = xlen + 2*hM2
    pin = hM1
    pend = xlen - hM1
    tStamps = np.arange(pin,pend,H)/float(fs)
    return tStamps

def gen_true_freq_tracks_chirp_150_190(tStamps):
    """Generate the frequency values present in file "../sounds/chirp-150-190-linear.wav"

    Args:
        tStamps (np.array): time stamps

    Result:
        np.array: time stamps and frequency values of predefined chirp

    """
    fTrack = np.zeros((len(tStamps),2))
    fTrack[:,0] = np.transpose(np.linspace(190, 190+1250, len(tStamps)))
    fTrack[:,1] = np.transpose(np.linspace(150, 150+1250, len(tStamps)))
    return fTrack

def gen_true_freq_tracks_440_602(tStamps):
    """Generate the frequency values present in file "../sounds/sines-440-602-hRange.wav"

    Args:
        tStamps (np.array): time stamps

    Result:
        np.array: time stamps and frequency values of predefined chirp

    """
    fTrack = np.zeros((len(tStamps),2))
    fTrack[:,0] = np.transpose(440*np.ones((len(tStamps),1)))
    fTrack[:,1] = np.transpose(602*np.ones((len(tStamps),1)))
    return fTrack

def freq_tracker_error(input_file, fTrackTrue, window, t, H, M):
    """Estimate sinusoidal values of a sound

    Args:
        input_file (str): wav file including the path
        fTrackTrue (np.array): array of true frequency values, one row per time frame, one column per component
        window (str): window type used for analysis
        t (float): peak picking threshold (negative dB)
        H (int): hop size in samples
        M (int): window size in samples

   Result:
           float: mean estimation error
           np.array: estimated frequency values, one row per time frame, one column per component

    """

    N = int(pow(2, np.ceil(np.log2(M))))        # FFT Size, power of 2 larger than M
    maxnSines = 2                               # Maximum number of sinusoids at any time frame
    minSineDur = 0.0                            # minimum duration set to zero to not do tracking
    freqDevOffset = 30                          # minimum frequency deviation at 0Hz
    freqDevSlope = 0.001                        # slope increase of minimum frequency deviation

    fs, x = UF.wavread(input_file)              # read input sound
    w = get_window(window, M)                   # Compute analysis window
    # analyze the sound with the sinusoidal model
    fTrackEst, mTrackEst, pTrackEst = SM.sineModelAnal(x, fs, w, N, H, t, maxnSines, minSineDur, freqDevOffset, freqDevSlope)
    tailF = 20
    # Compute mean estimation error. 20 frames at the beginning and end not used to compute error
    meanErr = np.mean(np.abs(fTrackTrue[tailF:-tailF,:] - fTrackEst[tailF:-tailF,:]),axis=0)

    return (meanErr, fTrackEst)



# === Paramètres généraux ===
input_file = 'chirp-150-190-linear.wav'
window = 'blackman'
t = -30    # seuil en dB pour la détection de pics
H = 128    # hop size
fs, x = UF.wavread(input_file)

# === Génération de la vérité terrain ===
# Choix initial de la taille de fenêtre M
M = 1023  # à ajuster pour minimiser l'erreur
tStamps = gen_time_stamps(len(x), M, fs, H)
fTrackTrue = gen_true_freq_tracks_chirp_150_190(tStamps)

# === Analyse par le modèle sinusoïdal ===
meanErr, fTrackEst = freq_tracker_error(input_file, fTrackTrue, window, t, H, M)

print(f"Taille de fenêtre M = {M}")
print(f"Erreur moyenne d'estimation (en Hz) : {meanErr}")

input_file = 'chirp-150-190-linear.wav'
H = 128
t = -80
window = 'blackman'
fs, x = UF.wavread(input_file)

#  Test initial avec mauvaise valeur de M (pour comparaison)
M_bad = 1023
tStamps = gen_time_stamps(len(x), M_bad, fs, H)
fTrackTrue = gen_true_freq_tracks_chirp_150_190(tStamps)
err_bad, fEst_bad = freq_tracker_error(input_file, fTrackTrue, window, t, H, M_bad)

#  Test optima
# l avec bonne valeur de M (minimiser erreur < 2Hz)
M_good =  5000
tStamps_good = gen_time_stamps(len(x), M_good, fs, H)
fTrackTrue_good = gen_true_freq_tracks_chirp_150_190(tStamps_good)
err_good, fEst_good = freq_tracker_error(input_file, fTrackTrue_good, window, t, H, M_good)

print(f"Taille de fenêtre M = {M_good}")
print(f"Erreur moyenne d'estimation (en Hz) : {err_good}")
plt.figure(figsize=(12, 6))

# 1. Mauvaise estimation
plt.subplot(2, 1, 1)
plt.plot(tStamps, fTrackTrue[:, 0], 'g', label='True Track 1')
plt.plot(tStamps, fTrackTrue[:, 1], 'b', label='True Track 2')
plt.plot(tStamps, fEst_bad[:, 0], 'r--', label='Estimated Track 1')
plt.plot(tStamps, fEst_bad[:, 1], 'm--', label='Estimated Track 2')
plt.title(f'X Estimation avec M = {M_bad}, Erreurs: {err_bad}')
plt.xlabel("Temps (s)")
plt.ylabel("Fréquence (Hz)")
plt.legend()
plt.grid()

# 2. Bonne estimation
plt.subplot(2, 1, 2)
plt.plot(tStamps_good, fTrackTrue_good[:, 0], 'g', label='True Track 1')
plt.plot(tStamps_good, fTrackTrue_good[:, 1], 'b', label='True Track 2')
plt.plot(tStamps_good, fEst_good[:, 0], 'r--', label='Estimated Track 1')
plt.plot(tStamps_good, fEst_good[:, 1], 'm--', label='Estimated Track 2')
plt.title(f'V Bonne estimation avec M = {M_good}, Erreurs: {err_good}')
plt.xlabel("Temps (s)")
plt.ylabel("Fréquence (Hz)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
