# 🚀Video Processing In Python
In this project my team tackles some real world problems involving video processing that can be solved with Python and Data Science.

### 📍 Team Members
- Vedanth V Baliga
- Nandini Hazarika
- Adithya Challa

<hr>

## 🏏Sports Match Highlights Generation

### ❓ Problem being Tackled : 
The task of generating highlights for any sport is quite tedious and difficult. It involves a lot of tech and other software, hardware needs. You also need to invest in a lot of time to do it. If you’re into such a video company or department then it is okay, but if you’re a normal user just like me, you wouldn’t want to do it that way. 

We are going to use pure Python and some useful libraries to generate **high quality** highlights of a particular sport.

### ⚡ Our Solution
We will be using speech analysis for this task. Machine Learning and Deep Learning is also a solution but it will be added on in later iterations.
When something exciting happens during a game, there is a rise in the commentator’s voice. Let’s take cricket for example. Whenever a batsman hits a boundary or a bowler takes a wicket, there is a rise in the commentator’s voice. Both the audience and the commentators have high pitch during that event. We can use these changes in audio to capture interesting moments from a video.

### 💡 Approach
▶ Input the video file <br><br>
▶ Extract the audio<br><br>
▶ Break the audio into chunks that can be analysed without excess compute power<br><br>
▶ Compute energy of every chunk of every chunk<br><br>
▶ Classify every chunk as excitement clip or not based on the sampling rate and threshold value<br><br>
▶ Merge all the clips to form the video highlights<br><br>
▶ Generate the final video highlights<br><br>

### 📷 Video Footage for the Project
The [video footage](https://drive.google.com/file/d/18uSa-F8JMJHuE53FlKSuaQs1R2LWVvqg/view?usp=sharing) we are using is a 23 minutes clip of the cricket match between India and West Indies.<br>
In **Step 2** we are extracting the audio. Find the extracted `.wav` audio file [here](https://drive.google.com/file/d/1820vX4kGLHhaKxVCUysPtmFUd8QCR7N7/view?usp=sharing)

### 👩‍💻 Codebase!
- To extract the audio file, here is the [code](https://github.com/vedanthv/VideoProcessingInPython/blob/main/HighlightsGeneration/AudioExtract.py)
- To divide the audio into chunks, classify as excitement and join all chunks here is the [code](https://github.com/vedanthv/VideoProcessingInPython/blob/main/HighlightsGeneration/AudioAnalysis.py) 

### 🏆Demo
This [match](https://drive.google.com/file/d/18uSa-F8JMJHuE53FlKSuaQs1R2LWVvqg/view?usp=sharing) between India and West Indies of 25 minutes converted to this [highlights](https://drive.google.com/file/d/1gAU-iXOG1u-W8r1M8xr5QW55M9oXjrEN/view?usp=sharing) of 5 minutes.
