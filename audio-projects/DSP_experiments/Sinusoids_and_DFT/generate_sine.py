import numpy as np
import matplotlib.pyplot as plt


def gen_sine(A, f, phi, fs, t):
    """Generate a real sinusoid given its amplitude, frequency, initial phase, sampling rate, and duration.
    
    Args:
        A (float):  amplitude of the sinusoid
        f (float): frequency of the sinusoid in Hz
        phi (float): initial phase of the sinusoid in radians
        fs (float): sampling frequency of the sinusoid in Hz
        t (float): duration of the sinusoid (is second)
        
    Returns:
        np.array: array containing generated sinusoid
        
    """
    t=np.arange(-t,t,1/fs)
    return A* np.cos(2*np.pi * f * t + phi)

print(gen_sine(1,10,1,50,0.1))
t=0.5
A=1
f=440
phi=1
fs=5000
t2=np.arange(-t,t,1/fs)

plt.plot(t2, gen_sine(A,f,phi,fs,t))
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.title("Sinewavv")
plt.grid()
plt.show()
