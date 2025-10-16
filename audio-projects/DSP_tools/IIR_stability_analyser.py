import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Example: IIR filter coefficients (Direct Form)
b = [0.2929, 0.5858, 0.2929] # numerator
a = [1.0, 0.0, 0.1716]       # denominator

# Calculate poles and zeros
z, p, k = signal.tf2zpk(b, a)

# Check for stability
stable = np.all(np.abs(p) < 1)
print("Poles:", p)
print("Is the filter stable?", stable)

# Visualization of the Z-plane
plt.figure(figsize=(5,5))
plt.scatter(np.real(p), np.imag(p), color='r', label='Poles')
plt.scatter(np.real(z), np.imag(z), color='b', label='Zeros')
circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
plt.gca().add_artist(circle)
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.axis('equal')
plt.grid()
plt.legend()
plt.title('Pole-Zero Diagram')
plt.show()
