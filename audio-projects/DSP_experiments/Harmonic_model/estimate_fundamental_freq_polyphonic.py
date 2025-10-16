import numpy as np
import math
from scipy.signal import get_window
import matplotlib.pyplot as plt
import IPython.display as ipd

from smstools.models import utilFunctions as UF
from smstools.models import harmonicModel as HM
from smstools.models import sineModel as SM
from smstools.models import stft
from smstools.models import dftModel as DFT

eps = np.finfo(float).eps

# E6 - 1.1: 
# Set the analysis parameters of f0Detection() to perform the best f0 dectection of the melody
# present in cello-double-2.wav. Explain the results.

input_file = 'cello-double-2.wav'

### Change these analysis parameter values marked as XX

window = 'blackmanharris'
M = 2047
N = 4096*2
f0et = 5
t = -60
minf0 = 100
maxf0 = 400


# No need to modify the code below, just understand it
H = 256
fs, x = UF.wavread(input_file)
w  = get_window(window, M)
f0 = HM.f0Detection(x, fs, w, N, H, t, minf0, maxf0, f0et)
y = UF.sinewaveSynth(f0, 0.8, H, fs)

ipd.display(ipd.Audio(data=x, rate=fs))
ipd.display(ipd.Audio(data=y, rate=fs))
UF.wavwrite(y,fs,'outputVio2.wav')
# Code for plotting the f0 contour on top of the spectrogram
maxplotfreq = 500.0
fig = plt.figure(figsize=(15, 9))

mX, pX = stft.stftAnal(x, w, N, H)
mX = np.transpose(mX[:,:int(N*(maxplotfreq/fs))+1])

timeStamps = np.arange(mX.shape[1])*H/float(fs)
binFreqs = np.arange(mX.shape[0])*fs/float(N)

plt.pcolormesh(timeStamps, binFreqs, mX, shading='auto')
plt.plot(timeStamps, f0, color = 'k', linewidth=1.5)

plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.legend(('f0',))
plt.show()
