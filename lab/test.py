import numpy as np
from signalp import signal
from spectral_feature import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

filename = "0100200101.wav"

test = signal(filename)
test._load_file()

# wav = test._read_stream()
# print(np.fromstring(wav, 'Int16'))
# test._save_file(wav)

# test._load_file()

print(len(test.data))
dat = test.data


# stream = np.fromstring(test.data, 'Int16')


ms = np.int(20*(test.FS/1000))  

for i in range(int(len(dat)/ms)):
    stream = dat[np.int(i*ms):np.int((i+1)*ms)]
    windowed = spectral_estimate(stream)
    lpc_data = lpc_spectrum(windowed)
    plt.plot(lpc_data)
    plt.show()