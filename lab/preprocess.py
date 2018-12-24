import numpy as np
from scipy import signal

def high_pass_filter(wave, rate, cutoff_freq=200):
    length = len(wave)/rate

    Nyquist_freq = rate/2
    cutoff_wn = cutoff_freq/Nyquist_freq
    N = 5

    sos = signal.butter(5, cutoff_wn, 'hp', output='sos')
    filtered = signal.sosfilt(sos, wave)
    return filtered

def low_pass_filter(wave, rate, cutoff_freq=6000):
    length = len(wave)/rate

    Nyquist_freq = rate/2
    cutoff_wn = cutoff_freq/Nyquist_freq
    N = 5

    sos = signal.butter(5, cutoff_wn, 'lp', output='sos')
    filtered = signal.sosfilt(sos, wave)
    return filtered
