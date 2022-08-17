import pyaudio
from math import pi
import numpy as np
import midi

CHUNK = 2**5
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


while True:
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=RATE, output=True, input=True, frames_per_buffer=CHUNK)
    event = midi.midiListener(port)
    wave = make_sinewave(500, 0.5)
    empty_wave = make_sinewave(0, 0)
    data = wave.astype(np.float32).tobytes()
    empty_data = empty_wave.astype(np.float32).tobytes()

    if midi.noteOn(event):
        while True:
            stream.write(data)
            if midi.noteOff(event):
                stream.stop_stream()
                break
            

    # if midi.noteOff(event):

 


