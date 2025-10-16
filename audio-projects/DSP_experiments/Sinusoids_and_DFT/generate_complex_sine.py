import numpy as np
import matplotlib.pyplot as plt

def gen_complex_sine(k, N):
    """Generate one of the complex sinusoids used in the DFT from its frequency index and the DFT lenght.
    
    Args:
        k (integer): frequency index of the complex sinusoid of the DFT
        N (integer) = length of complex sinusoid, DFT length, in samples
        
    Returns:
        np.array: array with generated complex sinusoid (length N)
        
    """
    n=np.arange(N)
    return np.exp(1j * 2 * np.pi * k * n /N)

print(gen_complex_sine(1,5))

N=5
k=1
n=np.arange(N)
plt.plot(n, np.real(gen_complex_sine(k,N)))
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.title("complex Sinewave")
plt.grid()
plt.show()
