import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    """Compute the DFT of a signal.
    
    Args:
        x (numpy array): input sequence of length N
        
    Returns:
        np.array: N point DFT of the input sequence x
    """
    X=np.array([])
    for k in range(len(x)) :
        s = np.exp(1j*2*np.pi*k/len(x)*np.arange(len(x)))
        X = np.append(X,sum(x*np.conjugate(s)))
    return X
x=np.array([1,2,3,4])
print(dft(x))

plt.plot(np.arange(len(x)),abs(dft(x)))
plt.show()
