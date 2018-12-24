import numpy as np
from preprocess import *
import matplotlib.pyplot as plt
from scipy import signal 
import scipy.io.wavfile as wav

# t = np.linspace(0, 1, 1000, False)  
# sig = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*30*t)

# plt.plot(t,sig)
# plt.show()

# z = low_pass_filter(sig,1000)

# plt.plot(t,z)
# plt.show()
fs, sig = wav.read("data/0100200101.wav")
print(fs)
sig = sig/30000
# fs = 44100
length = len(sig)/fs
t = np.linspace(0, length, len(sig), False)  # 1 second
# sig = np.sin(2*np.pi*100*t) + np.sin(2*np.pi*500*t)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(t, sig)
ax1.set_title('10 Hz and 20 Hz sinusoids')
ax1.axis([0, length, -1, 1])

cutoff_freq = 200
Nyquist_freq = fs/2
cutoff_wn = cutoff_freq/Nyquist_freq
sos = signal.butter(5, cutoff_wn, 'hp', output='sos')
filtered = signal.sosfilt(sos, sig)
ax2.plot(t, filtered)
ax2.set_title('After 15 Hz high-pass filter')
ax2.axis([0, length, -1, 1])
ax2.set_xlabel('Time [seconds]')
plt.tight_layout()
plt.show()

wav.write("data/0100200101_filtered.wav",fs,filtered)