import pyaudio
from math import pi
import numpy as np
import midi


CHUNK = 1024
RATE = 44100
LEN = 10

port = midi.midiConnect(2)
p = pyaudio.PyAudio()



def make_sinewave(frequency, length, sample_rate=RATE):
    length = int(length * sample_rate)
    factor = float(frequency) * (pi * 2) / sample_rate
    waveform = np.sin(np.arange(length) * factor)

    return waveform

def playSound():
    return

event = midi.midiListener(port)
for e in event:
    if midi.noteOn(event):
        print("on")



# while True:
#     stream = p.open(format=pyaudio.paFloat32, channels=1, rate=RATE, output=True,  frames_per_buffer=CHUNK)
#     event = midi.midiListener(port)
#     wave = make_sinewave(500, 1)
#     data = wave.astype(np.float32).tobytes()

#     while midi.noteOn(event):
#             event = midi.midiListener(port)
#             stream.write(data,)
#             if not midi.noteOn(event):
#                 stream.stop_stream()
#                 stream.close()
#                 break


        



 


