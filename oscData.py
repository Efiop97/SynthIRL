import numpy as np
import services as sv
import scipy.io.wavfile as wav
from scipy import signal

sample_rate = 44100
f = 440
t = 3
WT_len = 64
WT = np.zeros((WT_len,))

def sine(x):
    return np.sin(x)

def sawtooth(x):
    return (x + np.pi) / np.pi % 2 - 1

def squarewave(x):
    return signal.square(x)

wave_Type =[]



def main():
    

    waveform = sine

    for n in range(WT_len):
        WT[n] = waveform(2 * np.pi * n / WT_len)

    output = np.zeros((t * sample_rate,))

    index = 0
    indexInc = f * WT_len / sample_rate

    for n in range(output.shape[0]):
        output[n] = sv.Lin_interpolation(WT, index)
        index += indexInc
        index %= WT_len

    gain = -20
    amplitude = 10 ** (gain / 20)

    wav.write('sine440Hz2.wav', sample_rate, output.astype(np.float32))


    


