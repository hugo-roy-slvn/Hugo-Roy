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

def segment_stable_frequency_regions(f0, stdThsld, minNoteDur, winStable):
    """Segment the stable regions of a fundamental frequency track.

    Args:
        f0 (np.array): f0 values of a sound
        stdThsld (float): threshold for detecting stable regions in the f0 contour (in cents)
        minNoteDur (float): minimum allowed segment length (note duration)
        winStable (int): number of samples used for computing standard deviation

    Result:
        segments (np.array): starting and ending frame indexes of every segment

    """

    # convert f0 values from Hz to Cents (as described in pdf document)
    f0Cents = 1200*np.log2((f0+eps)/55.0)

    # create an array containing standard deviation of last winStable samples
    stdArr = 10000000000*np.ones(f0.shape)
    for ii in range(winStable-1, len(f0)):
        stdArr[ii] = np.std(f0Cents[ii-winStable+1:ii+1])

    # apply threshold on standard deviation values to find indexes of the stable points in melody
    indFlat = np.where(stdArr<=stdThsld)[0]
    flatArr = np.zeros(f0.shape)
    flatArr[indFlat] = 1

    # create segments of continuous stable points such that consecutive stable points belong to same segment
    onset = np.where((flatArr[1:]-flatArr[:-1])==1)[0]+1
    offset = np.where((flatArr[1:]-flatArr[:-1])==-1)[0]

    # remove any offset before onset (to sync them)
    indRem = np.where(offset<onset[0])[0]
    offset = np.delete(offset, indRem)

    minN = min(onset.size, offset.size)
    segments = np.transpose(np.vstack((onset[:minN], offset[:minN])))

    # apply segment filtering, i.e. remove segments with are < minNoteDur in length
    minNoteSamples = int(np.ceil(minNoteDur*fs/H))
    diff = segments[:,1] - segments[:,0]
    indDel = np.where(diff<minNoteSamples)
    segments = np.delete(segments,indDel, axis=0)

    return segments

# E6 - 2.1: 
# Compute the fundamental frequency of sax-phrase-short.wav, call segment_stable_frequency_regions(), and
# plot spectrogram, f0, and segments. Make your own choices of parameters to make the best
# possible note segmentation (best as a possible step for a note transcription), the ones
# in the test cases above might not the best ones. Synthesize the f0 segments and compare
# with the original sound. Explain the results.


### parameters to change

input_file = 'cello-phrase.wav'
stdThsld = 20
minNoteDur = 0.2
winStable = 3
window = 'blackman'
M = 1025
N = 2048
H = 256
f0et = 5.0
t = -90
minf0 = 310
maxf0 = 500

# compute f0 and segments
fs, x = UF.wavread(input_file)
w  = get_window(window, M)
f0 = HM.f0Detection(x, fs, w, N, H, t, minf0, maxf0, f0et)
segments = segment_stable_frequency_regions(f0,stdThsld, minNoteDur,winStable)
print(len(segments))
# plot spectrogram, f0, and segments
maxplotfreq = 1000.0

plt.figure(figsize=(15, 9))

mX, pX = stft.stftAnal(x, w, N, H)
mX = np.transpose(mX[:,:int(N*(maxplotfreq/fs))+1])

timeStamps = np.arange(mX.shape[1])*H/float(fs)
binFreqs = np.arange(mX.shape[0])*fs/float(N)

plt.pcolormesh(timeStamps, binFreqs, mX, shading='auto')
plt.plot(timeStamps, f0, color = 'k', linewidth=5)

for i in range(segments.shape[0]):
    plt.plot(timeStamps[segments[i,0]:segments[i,1]], f0[segments[i,0]:segments[i,1]], color = '#A9E2F3', linewidth=1.5)
plt.ylabel('Frequency (Hz)', fontsize = 12)
plt.xlabel('Time (s)', fontsize = 12)
plt.legend(('f0','segments'))

plt.show()
### Explanation
"""


"""
