import numpy as np
import matplotlib
matplotlib.use("TkAgg")  
import matplotlib.pyplot as plt


def biquad_lowpass(fc, fs, Q=0.707):
    """
    Generate the coefficients for a biquad low-pass filter
    fc: cutoff frequency (Hz)
    fs: sampling frequency (Hz)
    Q: quality factor (0.707=Butterworth)
    """
    w0 = 2 * np.pi * fc / fs
    alpha = np.sin(w0) / (2 * Q)
    
    b0 = (1 - np.cos(w0)) / 2
    b1 = 1 - np.cos(w0)
    b2 = (1 - np.cos(w0)) / 2
    a0 = 1 + alpha
    a1 = -2 * np.cos(w0)
    a2 = 1 - alpha
    
    # Normalisation  a0
    return [b0/a0, b1/a0, b2/a0], [1, a1/a0, a2/a0]

def biquad_highpass(fc, fs, Q=0.707):
 
    w0 = 2 * np.pi * fc / fs
    alpha = np.sin(w0) / (2 * Q)
    
    b0 = (1 + np.cos(w0)) / 2
    b1 = -(1 + np.cos(w0))
    b2 = (1 + np.cos(w0)) / 2
    a0 = 1 + alpha
    a1 = -2 * np.cos(w0)
    a2 = 1 - alpha
    
    return [b0/a0, b1/a0, b2/a0], [1, a1/a0, a2/a0]

def biquad_bandpass(fc, fs, Q=1.0):
 
    w0 = 2 * np.pi * fc / fs
    alpha = np.sin(w0) / (2 * Q)
    
    b0 = alpha
    b1 = 0
    b2 = -alpha
    a0 = 1 + alpha
    a1 = -2 * np.cos(w0)
    a2 = 1 - alpha
    
    return [b0/a0, b1/a0, b2/a0], [1, a1/a0, a2/a0]

def biquad_notch(fc, fs, Q=1.0):

    w0 = 2 * np.pi * fc / fs
    alpha = np.sin(w0) / (2 * Q)
    
    b0 = 1
    b1 = -2 * np.cos(w0)
    b2 = 1
    a0 = 1 + alpha
    a1 = -2 * np.cos(w0)
    a2 = 1 - alpha
    
    return [b0/a0, b1/a0, b2/a0], [1, a1/a0, a2/a0]

def biquad_peaking(fc, fs, Q=1.0, gain_db=6):
  
    w0 = 2 * np.pi * fc / fs
    A = 10**(gain_db / 40)
    alpha = np.sin(w0) / (2 * Q)
    
    b0 = 1 + alpha * A
    b1 = -2 * np.cos(w0)
    b2 = 1 - alpha * A
    a0 = 1 + alpha / A
    a1 = -2 * np.cos(w0)
    a2 = 1 - alpha / A
    
    return [b0/a0, b1/a0, b2/a0], [1, a1/a0, a2/a0]

def plot_frequency_response(b, a, fs):

    from scipy import signal
    
    w, h = signal.freqz(b, a, worN=8000, fs=fs)
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(w, 20 * np.log10(abs(h)))
    plt.title('Réponse en amplitude')
    plt.xlabel('Fréquence (Hz)')
    plt.ylabel('Amplitude (dB)')
    plt.grid(True)
    plt.xscale('log')
    
    plt.subplot(1, 2, 2)
    plt.plot(w, np.angle(h))
    plt.title('Réponse en phase')
    plt.xlabel('Fréquence (Hz)')
    plt.ylabel('Phase (radians)')
    plt.grid(True)
    plt.xscale('log')
    
    plt.tight_layout()
    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    fs = 44100  # sampling frequency
    fc = 1000   # cut-off frequency
    Q = 0.707   # quality factor
    
    # Generating Coefficients for a Low-Pass Filter
    b, a = biquad_lowpass(fc, fs, Q)
    
    print("lowpass coef:")
    print(f"b (numerator): {b}")
    print(f"a (denominator): {a}")
    
    # show frequency response
    plot_frequency_response(b, a, fs)
