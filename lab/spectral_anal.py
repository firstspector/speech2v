import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp, convolve
import scipy.io.wavfile as wav
from scipy.signal.windows import chebwin

rate, data = wav.read("test01.wav")

analytic_signal = hilbert(data)
amplitude_env = np.abs(analytic_signal)
win = chebwin(441,at=1,sym=False)
conv_signal = convolve(data,data,mode='same')


# plt.plot(data[(20*np.int(rate*0.01)):25*(np.int(rate*0.01))],label='signal')

plt.plot(conv_signal,label='env')

plt.show()