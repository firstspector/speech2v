import pyaudio
import wave
import sys
import scipy.io.wavfile as wav
import numpy as np

def startrec(d):
	byteList = np.fromstring(d,dtype='int16')
	#print(byteList)
	#print(len(byteList))
	if max(np.abs(byteList)) > 25000:
		return 1

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SEC = 2

if len(sys.argv) < 2:
	print("record a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
	sys.exit(-1)

wf = wave.open(sys.argv[1], 'wb')

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

print("recording...")
frames = []

i = 0
st = np.arange(0,1024)
#plt.ion()
#plt.show()
while i !=1:
	data = stream.read(CHUNK)
	#mn = np.fromstring(data,dtype=('float32'))
	#plt.plot(st,mn)
	#plt.draw()
	#st += 1024
	#plt.pause(.001)
	i = startrec(data)

frames.append(data)
for i in range(0,int(RATE/CHUNK*RECORD_SEC)):
	data = stream.read(CHUNK)
	frames.append(data)

print("finish :)")


stream.stop_stream()
stream.close()

wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

wf = wave.open(sys.argv[1], 'rb')

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=RATE,output=True)

data = wf.readframes(CHUNK)

while data != '':
	stream.write(data)
	data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()