import moviepy.editor as mp

clip = mp.VideoFileClip("./videofile.mp4").subclip(1, 1380) # feed in our video file, subclip specifies the time limit for the video for which we need the audio data
clip.audio.write_audiofile("./audio.wav")