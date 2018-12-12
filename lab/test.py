import numpy as np
from signalp import signal
from spectral_feature import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

filename = "test.wav"

test = signal(filename)

wav = test._read_stream()
print(np.fromstring(wav, 'Int16'))
# test._save_file(wav)

# test._load_file()

print(len(test.data))
dat = wav

fig = plt.figure(facecolor='white') 
axFreq = fig.add_axes([.1, .1, .8, 0.4*(2)])
axFreq.plot(range(np.int((8*1024)/2)), [0]*(np.int(8*1024/2)))


# stream = np.fromstring(test.data, 'Int16')
def update(i):
    stream = dat[(i+1)*1:(i+1)*441]
    windowed = spectral_estimate(stream)
    return lpc_spectrum(windowed)
    


for i in range(100):
    plt.show()
    axFreq.plot(update(i))
    