import numpy as np
from scipy import signal

def low_pass_filter(wave, rate):
    N = 5
    cutoff_freq = 20
    sos = signal.butter(N, cutoff_freq, analog=True,btype='highpass', output='sos')
    filtered_signal = signal.sosfilt(sos, wave)
    return filtered_signal

