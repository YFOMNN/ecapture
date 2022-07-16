# ecapture
[![Downloads](https://pepy.tech/badge/ecapture)](https://pepy.tech/project/ecapture)    [![Downloads](https://pepy.tech/badge/ecapture/month)](https://pepy.tech/project/ecapture/month)    [![Downloads](https://pepy.tech/badge/ecapture/week)](https://pepy.tech/project/ecapture/week)
## Image Capture Demo
# Capture
Function: Capture photos
Number of Arguments: 3

~~~python
import ecapture as ec
ec.capture(0,"frame", "frame.png")
~~~

## Arguments:
### Camera Index
Input the index of the webcam that you choose to use. Index 0 will be first webcam, Index 1 will be the second webcam, and so on and so forth.

### Window Name
Input False if a window with the captured image should not be displayed. A window name input as a string will show a window with the captured image

### Save Name
Input False if the captured image should not be saved. A save name input as a string will save the captured image with the desired name.


# Video Capture
Function: Record videos
Number of Arguments: 4

~~~python
import ecapture as ec
ec.vidCapture(0, "frame", "frame.avi", "x")
~~~

## Arguments:
### Camera Index
Input the index of the webcam that you choose to use. Index 0 will be first webcam, Index 1 will be the second webcam, and so on and so forth.

### Window Name
Input False if a window with the captured image should not be displayed. A window name input as a string will show a window with the current frame.

### Save Name
Input False if the captured image should not be saved. A save name input as a string will save the recorded video with the desired name.

### Exit Key
The key that has to be pressed to end the recording.
# Timed Video Capture
Function: Record videos for a specified duration
Number of Arguments: 4

~~~python
import ecapture as ec
ec.vidCapture(0, "frame", "frame.avi", 5)
~~~

## Arguments:
### Camera Index
Input the index of the webcam that you choose to use. Index 0 will be first webcam, Index 1 will be the second webcam, and so on and so forth.

### Window Name
Input False if a window with the captured image should not be displayed. A window name input as a string will show a window with the current frame.

### Save Name
Input False if the captured image should not be saved. A save name input as a string will save the recorded video with the desired name.

### Timer
The time after which the video recording terminates.
