![Adsight](Resources/logo_alpha.png)

# AdSight - Team Submission for nwHacks 2019
Contributors: Jacky Zhao, Gavin Lim, Viral Galaiya, Rishab Manocha

### Problem
Physical ads are becoming more and more disadvantaged as more tools are being created for tracking impressions, demographics, and statistics for web traffic and adverstisements. The problem is because it is nearly impossible to measure the effectiveness of a physical ad. How can we measure and display these normally 'web-based' metrics for physical ads?

### Proposal
* Determine success of a advertisement based on number of people and duration it is looked at
* Have an interface to easily access demographic data and statistics
* Change advertisement based on demographic for virtual advertisement

### Solution
Our solution comes in two main parts: software and hardware. We can describe out data flow as follows:
1. *Hardware - Raspberry Pi running Raspbian*
  - Get images using OpenCV 2
  - Running Haar-based Cascade filter with a pretrained dataset to check if people are in frame
  - Uses two filters (side and front) to get more yaw coverage
  - If a face is detected, begin saving images from camera to local at set intervals (500ms)
  - Go to 2.
2. *Software - Azure API*
  - Glob all images in local
  - Grab head poses of all faces in image by submitting a POST request to MS Azure's Face Detect
  - Check if unique face by running it against MS Azure Face List with FindSimilars
    - If unique, append faceID to Face List
    - Else update existing faceID entry in Face List
  - Update attention timelines according to headpose
  - Form person class to .JSON format
  - POST .JSON to webservice (Go to 3.)
3. *Software - Front End*
  - Add POSTed .JSON to SQLAlchemy DB
  - Filter entries based on user-selected filters (age, gender, etc.)

### Challenges we ran into
 * Frame-rate and detection accuracy of the Cascade Network
 * Initial configuration of RPi with OpenCV and Raspbian Stretch
 * Optimizing processing speed of RPi when running detection algorithm


### Accomplishments that we're proud of


### What we learned


### What's next for AdSight


# Rough Details
### Software
1. Microsoft Azure APIs Face API
  - Can use Face Verification to get ID: [Link](https://azure.microsoft.com/en-gb/services/cognitive-services/face/#verification)
    - If Face ID is in pose where looking at camera for more than a designated period of time, count impression
    - Uses RESTful API: [Link](https://docs.microsoft.com/en-gb/azure/cognitive-services/face/QuickStarts/Python)
    - Get demographics
      - returnFaceAttributes
    - Face API .ipynb example: [Link](https://hub.mybinder.org/user/microsoft-cogni-vices-notebooks-yyu0i5ow/notebooks/FaceAPI.ipynb)
2. Web App
  - Break down demographics of each ad per hour
    - Web display
  - Google Dialogue Flow?

### Hardware
1. RPi Camera v2: [Link](https://www.raspberrypi.org/products/camera-module-v2/)
2. RPi Model 2B+
