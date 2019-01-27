# Team Submission for nwHacks 2019

### Proposal
* Determine success of a advertisement based on number of people and duration it is looked at
* Have an interface to easily access demographic data and statistics
* Change advertisement based on demographic for virtual advertisement

### Software
1. Microsoft Azure APIs Face API
  - Can use Face Verification to get ID: [Link](https://azure.microsoft.com/en-gb/services/cognitive-services/face/#verification)
    - If Face ID is in pose where looking at camera for more than a designated period of time, count impression
    - Uses RESTful API: [Link](https://docs.microsoft.com/en-gb/azure/cognitive-services/face/QuickStarts/Python)
    - Get demographics
      - returnFaceAttributes
      - Age, gender, headPose
    - Face API .ipynb example: [Link](https://hub.mybinder.org/user/microsoft-cogni-vices-notebooks-yyu0i5ow/notebooks/FaceAPI.ipynb)
2.
  - Break down demographics of each ad per hour
    - Web display
  - Google Dialogue Flow?

### Hardware
##### Cameras
1. Jevois Camera: [Link](http://jevois.org/) - Open-source machine vision. OpenCV, TensorFlow
2. Point Grey CM3-U3-13S2M-CS: [Link](https://www.ptgrey.com/chameleon3-13-mp-mono-usb3-vision) - Mono (BW)
3. RPi Camera v2: [Link](https://www.raspberrypi.org/products/camera-module-v2/)


### References
1. OpenCV 3.0 installation on RPi Stretch: [Link](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/)