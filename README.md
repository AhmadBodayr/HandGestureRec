# HandGestureRec
# Short Summary:
The library is an open source dynamic hand gesture recognition built using python with a Tkinter GUI and ML. using Tensorflow, Keras Api for TF, OpneCV for camera access and MediaPipe for hand landmarks detection https://github.com/AhmadBodayr/HandGestureRec
## Implementation: 
The library uses the webcam as the sensor and it gives the user access to the webcam using opencv, then the handlandmarks are collected using MediaPipe.
## GUI:
The GUI is the main way for the user to interact with the toolkit. It is written in Tkinter for python wich is the default GUI library for Python. The GUI is simple and easy to use.
## The Backend:
It is comprised of:
### Data Collection:
 The data collection is done using OpenCV and MediaPipe, each gesture is composed of 80 videos each is 30 frames, with each frame containing the 42 landmarks for each hand. Each landmark is an X, Y,  Z  tupple which describes the location of that specific landmark.
### Data Storage Strategy:
No DBMS was used instead a folder tree which is composed of 3 submodules was built. The first submodule is  a  gestures folder that contains all the gestures defined by the user, the second is a datasets submodule which contains all the datasets created by the user. A single dataset is a non null subset of the gestures.
### The machine learning algorithm:
The ML. model used is an LSTM model  which was built using Tensorflow 2.X  and the Keras ApI. for tensorFlow.
# How to use:
install the library from $ pip using pip install HandGestureRec and in your python project write in the terminal 'execHandGestureRec' 
* 1)   The user define one or more gesture using the GUI. One gesture is to be defined at a time. The gesture is defined by giving it a name and pressing create gesture then OpenCV will  give the user access to the webcam, 80 videos will be taken each is 30 frames in length so the user needs to do the gesture for 80 times. The starting time of each try of the 80 will be shown on the screen.
* 2) After the user defines 1 or more gestures, he can then use the datasets submodule to create a dataset which will then serve as an input to the ML. model. To create a dataset the user have to give it a name and choose a subset of the gestures he defiend before hand then press create dataset.
* 3)  After having one or more datasets the user can then can to the models submodule to crerate a model to a specific dataset. There is a 1:1 relation between the datasets and the models meaning that every dataset can only contribute to only one model.
* 4)  After creating one or more models the user can test his models using the testing submodule.

