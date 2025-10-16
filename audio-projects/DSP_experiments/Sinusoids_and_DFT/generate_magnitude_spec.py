import numpy as np
import matplotlib.pyplot as plt

x=np.array([1, 2, 3, 4])
x=np.cos(2*np.pi*200.0*np.arange(512)/1000)
def gen_mag_spec(x):
    """Compute magnitude spectrum of a signal.
    
    Args:
        x (np.array): input sequence of length N
        
    Returns:
        np.array: magnitude spectrum of the input sequence x (length N)
        
    """
    N = len(x)
    mag_spec = []

    for k in range(N):
        n = np.arange(N)
        W = np.exp(-1j * 2 * np.pi * k * n / N)  # Base DFT
        X_k = np.sum(x * W)                      # Coefficient DFT à la fréquence k
        mag_spec.append(np.abs(X_k))             # Magnitude

    return np.array(mag_spec)
print(gen_mag_spec(x))
plt.stem(np.arange(len(x)), gen_mag_spec(x))
plt.title("Spectre de magnitude (DFT manuelle)")
plt.xlabel("Index fréquentiel k")
plt.ylabel("Magnitude")
plt.grid()
plt.show()
