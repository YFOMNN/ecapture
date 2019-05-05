# ecapture
## Image Capture Demo

First run the following command in a cmd window
~~~
pip install ecapture
~~~

Then, Create a new python script

Open the script

Import the module
~~~python
from ecapture import ecapture as ec
~~~ 
Capture using webcam
~~~python
(ec.capture(0,False,"img.jpg"))
~~~
The capture function takes three arguments:
  
  Camera index(first connected webcam will be of index 0. The next webcam will be of index 1)
  
  Window name (It can be a variable or a string. If you don't wish to see the window, type False)
   
   ~~~python
   ec.capture(0,False,"img.jpg")
   ~~~
  
  Save name (It can be a variable or a string. If you don't wish to save the image, type False)
  ~~~python
  ec.capture(0,"test",False)
  ~~~
The full code
~~~python
from ecapture import ecapture as ec

ec.capture(0,"test","img.jpg")
~~~
## Delayed Image Capture Demo
Create a new python script

Open the script

Import the module
~~~python
from ecapture import ecapture as ec
~~~ 
Capture the image using webcam
~~~python
ec.delay_imcapture(0,"Image","Demo.jpg",2)
~~~
The vidcapture function takes four arguments:
  
  Camera index(first connected webcam will be of index 0. The next webcam will be of index 1)
  
  Window name (It can be a variable or a string)
   
   ~~~python
   ec.delay_imcapture(0,"Video","Demo.jpg",2)
   ~~~
  
  Save name (It can be a variable or a string. If you don't wish to save the image, type False)
  ~~~python
  ec.delay_imcapture(0,"Video",False,2)
  ~~~
  
  The delay(The time till capturing the image)
  ~~~python
  ec.delay_imcapture(0,"Video","Demo.jpg",2)
  ~~~
The full code
~~~python
from ecapture import ecapture as ec

ec.delay_imcapture(0,"Video","Demo.jpg",2)
~~~
## Video Capture Demo
Create a new python script

Open the script

Import the module
~~~python
from ecapture import ecapture as ec
~~~ 
Capture the video using webcam
~~~python
ec.vidcapture(0,"Video","Demo.avi","q")
~~~
The vidcapture function takes four arguments:
  
  Camera index(first connected webcam will be of index 0. The next webcam will be of index 1)
  
  Window name (It can be a variable or a string)
   
   ~~~python
   ec.vidcapture(0,"Video","Demo.avi","q")
   ~~~
  
  Save name (It can be a variable or a string. If you don't wish to save the video, type False)
  ~~~python
  ec.vidcapture(0,"Video",False,"q")
  ~~~
  
  Exit key (The key you press to stop recording the video. It can be ("q", "x", "a" or any other letter))
  ~~~python
  ec.vidcapture(0,"Video","Demo.avi","x")
  ~~~
The full code
~~~python
from ecapture import ecapture as ec

ec.vidcapture(0,"Video","Demo.avi","q")
~~~
## Auto Video Capture Demo
Create a new python script

Open the script

Import the module
~~~python
from ecapture import ecapture as ec
~~~ 
Capture the video using webcam
~~~python
ec.auto_vidcapture(0,"Video","Demo.avi",5)
~~~
The vidcapture function takes four arguments:
  
  Camera index(first connected webcam will be of index 0. The next webcam will be of index 1)
  
  Window name (It can be a variable or a string)
   
   ~~~python
   ec.auto_vidcapture(0,"Vid","Demo.avi",5)
   ~~~
  
  Save name (It can be a variable or a string. If you don't wish to save the video, type False)
  ~~~python
  ec.auto_vidcapture(0,"Video",False,5)
  ~~~
  
  Exit time (The time until stopping recording of the video. It can be (5, 10, 15, 20 or any number of seconds in between)
  ~~~python
  ec.auto_vidcapture(0,"Video","Demo.avi",10)
  ~~~
The full code
~~~python
from ecapture import ecapture as ec

ec.auto_vidcapture(0,"Video","Demo.avi",5)
~~~
