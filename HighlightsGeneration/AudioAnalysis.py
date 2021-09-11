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

energy = np.array([sum(abs(x[i:i + window_length] ** 2)) for i in range(0, len(x), window_length)])

# Classify every chunk of audio as excitement or not

# Create a df for energy data
df = pd.DataFrame(columns=['energy', 'start', 'end']) # df for energy data
thresh = 180 # above this value, the audio is excitement class.
row_index = 0
for i in range(len(energy)):
    value = energy[i] # take 'value' value from the energy dataframe
    if value >= thresh:
        i = np.where(energy == value)[0]
        df.loc[row_index, 'energy'] = value # if value >= thresh then set the 'energy' column value as the value
        df.loc[row_index, 'start'] = i[0] * 10 # start time of audio sequence of the excitement chunk
        df.loc[row_index, 'end'] = (i[0] + 1) * 10 # stop time of the audio sequence of the excitement chunk
        row_index = row_index + 1 # go to the next row of the dataframe

# merging all consequtive audio clips into one

temp = [] # only temporary for storing the clips together
i = 0
j = 0
n = len(df) - 2
m = len(df) - 1
while (i <= n):
    j = i + 1
    while (j <= m):
        if (df['end'][i] == df['start'][j]):
            df.loc[i, 'end'] = df.loc[j, 'end']
            temp.append(j)
            j = j + 1
        else:
            i = j
            break
df.drop(temp, axis=0, inplace=True)
print(df) # this data frame only has start and end time of the audio clips that exceed or equal the threshold

# Now each of the clips is in audio format. But our final goal is to make it video highlights. So we are going to glue together all the excite-clips and make the video highlights for the chunks that

# This code will generate the highlights from each of the chunk based on the amplitude and then it will save these final highlights in your system.

start=np.array(df['start'])
end=np.array(df['end'])
for i in range(len(df)):
 if(i!=0):
  start_lim = start[i] - 10
 else:
  start_lim = start[i] 
 end_lim   = end[i]   
 filename="highlight" + str(i+1) + ".mp4"
 ffmpeg_extract_subclip("./highlights.mp4",start_lim,end_lim,targetname=filename)
