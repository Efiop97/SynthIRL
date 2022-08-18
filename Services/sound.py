import pyaudio
from math import pi
import numpy as np
import midi
import math
import itertools


CHUNK = 256
RATE = 48000
NOTE_AMP = 0.1

port = midi.midiConnect(0)
p = pyaudio.PyAudio()

def make_sin(frequency, length, sample_rate=RATE):
    length = int(length * sample_rate)
    factor = float(frequency) * (pi * 2) / sample_rate
    waveform = np.sin(np.arange(length) * factor)

    return waveform


def make_sinewave(freq=440, amp=1, sample_rate=RATE):
    increment = (2 * math.pi * freq)/ sample_rate
    return (math.sin(v) * amp * NOTE_AMP \
            for v in itertools.count(start=0, step=increment))
        
def playSound():
    return

def get_samples(notes_dict, num_samples=CHUNK):
    return [sum([int(next(osc) * 32767) \
            for _, osc in notes_dict.items()]) \
            for _ in range(num_samples)]

stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, output=True,  frames_per_buffer=CHUNK)

try: 
    print("Starting...")
    notes_dict = {}
    while True:
        if notes_dict:
            # Play the notes
            samples = get_samples(notes_dict)
            samples = np.int16(samples).tobytes()
            stream.write(samples)
            
        if midi.checkMidiConnection(port):
            # Add or remove notes from notes_dict
            for event in midi.midiListener(port):
                (status, channel, note, vel, time) = event
                if midi.noteOn and note not in notes_dict:
                    freq = midi.noteToFreq(note) / 2
                    print(freq)
                    notes_dict[note] = make_sinewave(freq=freq, amp=vel/127)
                elif midi.noteOff and note in notes_dict:
                    print("note is off")
                    del notes_dict[note]
                    
except KeyboardInterrupt as err:
    print("Stopping...")


# while True:
#     stream = p.open(format=pyaudio.paFloat32, channels=1, rate=RATE, output=True,  frames_per_buffer=CHUNK)
#     event = midi.midiListener(port)
#     wave = make_sinewave
#     data = wave.astype(np.float32).tobytes()

#     while midi.noteOn(event):
#             event = midi.midiListener(port)
#             stream.write(data,)

#             if not midi.noteOn(event):
#                 stream.stop_stream()
#                 stream.close()
#                 break


        



 


