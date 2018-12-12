import numpy as np
import scipy.io.wavfile as wf
import pyaudio
import matplotlib.pyplot as plt
from audiolazy import lazy_lpc as lpc

# Parameter for recording
DEVICE = 0 #record device
BYTES: int = 4
CHUNK: int = 8**BYTES 
FS: int = 44100 #frame rate(frame per sec)
FORMAT = pyaudio.paInt16
CHANNELS = 1
WINDOW = np.hamming(CHUNK)

# Parameter for signal preprocessing
ORDER = 12
NFFT = CHUNK*2

# Voice activity detection process


def est_predictor_gain(x, a):
    cor = np.correlate(x, x, mode='full')
    rr = cor[np.int(len(cor)/2): np.int(len(cor)/2+ORDER+1)]
    g = np.sqrt(np.sum(a*rr))
    return g


def lpc_spectrum(data):
    a = lpc.lpc.autocor(data, ORDER)
    g = est_predictor_gain(data, a.numerator)
    spectral_lpc = np.fft.fft([xx/g for xx in a.numerator], NFFT)
    S = -20*np.log10(np.abs(spectral_lpc)**2)
    return S[0:np.int(NFFT/2)]


def spectral_estimate(data):
    spectral = np.fft.fft(data, NFFT)
    S = 20*np.log10(np.abs(spectral)**2)
    return S[0:np.int(NFFT/2)]

def spectral_centroid(data):
    magnitudes = np.abs(np.fft.rfft(data)) # magnitudes of positive frequencies
    length = len(data)
    freqs = np.abs(np.fft.fftfreq(length, 1.0/FS)[:length//2+1]) # positive frequencies
    return np.sum(magnitudes*freqs) / np.sum(magnitudes) # return weighted mean

def frame_energy():
    pass

def spectral_flatness():
    pass
