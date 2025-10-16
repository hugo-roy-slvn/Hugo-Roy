import numpy as np
import matplotlib.pyplot as plt

X=np.array([1,1,1,1])

def idft(X):
    """Compute the inverse-DFT of a spectrum.
    
    Args:
        X (np.array): frequency spectrum (length N)
        
    Returns:
        np.array: N point IDFT of the frequency spectrum X
        
    """
    y=np.array([])
    for n in range(len(X)):
        s= np.exp(1j*2*np.pi*n/len(X)*np.arange(len(X)))
        y = np.append(y,1/len(X)*sum(X*s))
    return y

print(idft(X))
plt.plot(np.arange(len(X)),idft(X).real)

plt.show()
