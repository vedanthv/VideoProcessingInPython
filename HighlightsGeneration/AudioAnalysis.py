# Now, I have divided the audio into chunks of 10 seconds each, since we want to find out whether a particular audio chunk contains a rise in the audio voice or not. You can set time limit as per your choice, Try different time limits for different outputs. Also, we’ll play the audio chunk just for a check.

import librosa # for audio analysis
import IPython.display as ipd # for displaying audio file
import numpy as np

filename = "D:\Vedanth\VideoProcessingInPython\audio.wav"

# loading the file with a sampling rate. Sampling rate is nothing but size of the chunks of audio librosa takes. This is default at 22,500 but I have taken it at 16,000 for better quality and also because my video isn't long.
x, sr = librosa.load(filename, sr=16000)

# To get duration of the audio clip in minutes
int(librosa.get_duration(x, sr) / 60) 
# samples aren't actually in any time unit we convert it to minutes here, for convinience.

# Dividing into chunks of 10 seconds 
max_slice = 10 
window_length = max_slice * sr # final audio is here.This is the formula.

# Playing the audio chunk
a = x[21 * window_length:22 * window_length]
ipd.Audio(a, rate=sr)

# The energy or power of an audio signal refers to the loudness of the sound. It is computed by the sum of the square of the amplitude of an audio signal in the time domain. When energy is computed for a chunk of an entire audio signal, then it is known as Short Time Energy.

s_energy = np.array([sum(abs(x[i:i + window_length] ** 2)) for i in range(0, len(x), window_length)])
