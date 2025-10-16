import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
eps = np.finfo(float).eps
from smstools.models import stft as st
from smstools.models import utilFunctions as UF

def compute_snr(input_file, window, M, N, H):
    """Measure the amount of distortion introduced during the analysis and synthesis of a signal using the STFT model.

    Args:
        input_file (str): wav file name including the path
        window (str): analysis window type (rectangular, triangular, hanning, hamming, blackman, or blackmanharris)
        M (int): analysis window length (odd positive integer)
        N (int): fft size (power of two, > M)
        H (int): hop size for the stft computation

    Result:
        tuple with the signal to noise ratio over the whole sound and of the sound without the begining and end.
    """
    (fs, x)=UF.wavread(input_file)
    w = get_window(window,M)

    y = st.stft(x,w,N,H)

    min_len = min(len(x), len(y))
    x = x[:min_len]
    y = y[:min_len]

    E1s = np.sum(np.square(x))
    E2s = np.sum(np.square(x-y))


    SNR1= 10*np.log10(E1s/(E2s+np.finfo(float).eps))

    x2=x[M:-M]
    y2 = y[M:-M]

    E1s2= np.sum(np.square(x2))
    E2s2= np.sum(np.square(x2-y2))

    SNR2 = 10*np.log10(E1s2/(E2s2+np.finfo(float).eps))

    return(SNR1, SNR2)

print(compute_snr("sounds_piano.wav",'blackman',513,2048,128))
print(compute_snr("sax-phrase-short.wav",'hamming',512,1024,64))
print(compute_snr("rain.wav",'hann',1024,2048,128))
