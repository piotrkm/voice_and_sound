# -*- coding: utf-8 -*-
"""voice and sound - spectrogram.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iaq28oC-jwaETxGG_8rNYkJNwdObCEC-
"""

from scipy.io import wavfile
from urllib.request import urlopen

samplerate, data = wavfile.read('./24789__ermine__061101_7-30_sparrow_chirp.wav')

duration = len(data)/samplerate

print(f'Sample rate: {samplerate} [Hz] \nNumbers of channels: {data.shape[1]}\nLength of the sound {duration:0.2f} [s]')

import matplotlib.pyplot as plt
import numpy as np

# plotting waves for two channels (L-ch.A, R-ch.B)

t = np.linspace(0,duration, data.shape[0])

fig, ax = plt.subplots(2, 1, figsize=(10,5), sharex=True)

ax[0].plot(t, data[:,0], label='channel A', c='green')
ax[0].grid(True)
ax[0].set_ylabel('Amplitude')
ax[0].legend()

ax[1].plot(t, data[:,1], label='channel B', c='red')
ax[1].grid(True)
ax[1].set_ylabel('Amplitude')
ax[1].legend()

plt.xlabel('Time [s]')

plt.savefig('waveplots.png')



# plotting spectrogram of the signal.
fig, ax = plt.subplots(2,1, sharex=True, figsize=(10,8))

ax[0].specgram(data[:,0], Fs=samplerate, cmap="jet")
ax[0].grid(True)
ax[0].set_ylabel('Frequency Hz')
ax[0].set_title('Sound spectrogram (channel A)')



ax[1].specgram(data[:,1], Fs=samplerate, cmap="jet")
ax[1].grid(True)
ax[1].set_title('Sound spectrogram (channel B)')
ax[1].set_xlabel('Time [s]')
ax[1].set_ylabel('Frequency Hz')

plt.savefig('spectrograms.png')


"""## Time spent:
2024-08-05   4h
"""


