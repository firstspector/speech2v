import numpy as np
import pyaudio as pa
import scipy.io.wavfile as wf
import wave
import os
import sys

# Parameter for recording
DEVICE = 0 #record device
BYTES: int = 4
CHUNK: int = 8**BYTES 
FS: int = 44100 #frame rate(frame per sec)
FORMAT = pa.paInt16
CHANNELS = 1

p = pa.PyAudio()
print("Checking compatability with input parameters:")
print("\tAudio Device:", DEVICE)
print("\tRate:", FS)
print("\tChannels:", CHANNELS)
print("\tFormat:", FORMAT)

isSupported = p.is_format_supported(input_format=FORMAT,
                            input_channels=CHANNELS,
                            rate=FS,
                            input_device=DEVICE)
if isSupported:
    print("\nThese settings are supported on device %i!\n" % (DEVICE))
else:
    sys.exit("\nUh oh, these settings aren't",
            " supported on device %i.\n" % (DEVICE))

stream = p.open(format=FORMAT,
            channels=CHANNELS,
            rate=FS,
            input=True,
            frames_per_buffer=CHUNK)

class signal():
    """ signal preparation """

    def __init__(self,filename:str):
        self.DEVICE = 0 #record device
        self.BYTES: int = 4
        self.CHUNK: int = 8**self.BYTES 
        self.FS: int = 44100 #frame rate(frame per sec)
        self.FORMAT = pa.paInt16
        self.CHANNELS = 1
        self.filename = filename
        self.data = np.array([])

    def _load_file(self):
        filepath = os.path.join("./data",self.filename)
        self.FS, self.data = wf.read(filepath)

    def _save_file(self, raw_data):
        filepath = os.path.join("./data",self.filename)
        w = wave.open(filepath, 'wb')
        w.setnchannels(self.CHANNELS)
        w.setsampwidth(p.get_sample_size(self.FORMAT))
        w.setframerate(self.FS)
        w.writeframes(b''.join(raw_data))
        w.close()

    def _read_stream(self):
        frames = []
        for i in range(20):
            frames.append(stream.read(self.CHUNK))

        return b''.join(frames)

    
