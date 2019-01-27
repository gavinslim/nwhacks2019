# This code will identify if a person is present in the video stream and send it upstream if there is
# https://realpython.com/face-detection-in-python-using-a-webcam/
# run code using python local-vision.py haarcascade_frontalface_default.xml

import cv2
import sys
import datetime
import time
import os
import subprocess

print('python3 get_faceapi/faceapi.py')
subprocess.Popen(['python3' ,'get_faceapi/faceapi.py'])

# cascPath_frontal = sys.argv[1]
#cascPath_side = sys.argv[1]
faceCascade_frontal = cv2.CascadeClassifier(os.path.join(os.getcwd(),'haarcascade_frontalface_default.xml'))
faceCascade_side = cv2.CascadeClassifier(os.path.join(os.getcwd(),'haarcascade_profileface.xml'))

# flags
take_pic = 0
draw_front = 0
draw_left = 0
draw_right = 0
count = 0
__INTERVAL__ = 0.5

# initialize video capture
video_capture = cv2.VideoCapture(0)

def get_image():
    ret, frame = video_capture.read()
    return frame

start = datetime.datetime.now()

while 1==1:
    take_pic = 0
    curr = datetime.datetime.now()
    offset = curr-start

    if offset.seconds + offset.microseconds/1e6 > __INTERVAL__:
        start = datetime.datetime.now()

        frame = get_image()
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces_right = faceCascade_side.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(60, 60),
           #flags=cv2.CASCADE_SCALE_IMAGE
        )
        if len(faces_right) > 0:
            draw_right = 1
            take_pic = 1
        else:
            flipped = cv2.flip(gray, 1)
            faces_left = faceCascade_side.detectMultiScale(
                flipped,
                scaleFactor=1.1,
                minNeighbors=10,
                minSize=(60, 60),
               #flags=cv2.CASCADE_SCALE_IMAGE
            )

            if len(faces_left) > 0:
                draw_left = 1
                take_pic = 1
            else:
                faces_frontal = faceCascade_frontal.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=10,
                    minSize=(60, 60),
                   #flags=cv2.CASCADE_SCALE_IMAGE
                )
                if len(faces_frontal) > 0:
                    draw_front = 1
                    take_pic = 1

        if take_pic == 1:
            timestr = datetime.datetime.now().strftime("%m_%d_%H_%M_%S.%f")[:-5] #month_day_hour_second_millisecond 1dp
            cv2.imwrite('{0}.jpg'.format(timestr),frame)
            count = count + 1
            print(count)
            print((offset.seconds + offset.microseconds/1e6) - __INTERVAL__)
            print('____________')

    # Draw rectangle
    # if draw_right == 1:
    #     for (x, y, w, h) in faces_right:
    #         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) #Green
    #         cv2.putText(frame, 'Right!', (x, y-5), 1, 2, (0, 255, 0), 2, cv2.LINE_AA)
    #         draw_right = 0
    # elif draw_left == 1:
    #     for (x, y, w, h) in faces_left:
    #         cv2.rectangle(frame, (512-x, y), (512-x+w, y+h), (255, 0, 0), 2) #Red
    #         cv2.putText(frame, 'Left!', (512-x, y), 1, 2, (255, 0, 0), 2, cv2.LINE_AA)
    #         draw_left = 0
    # elif draw_front == 1:
    #     for (x, y, w, h) in faces_frontal:
    #         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2) #Red
    #         cv2.putText(frame, 'Front!', (x, y-5), 1, 2, (0, 0, 255), 2, cv2.LINE_AA)
    #         draw_front = 0

    # Display the resulting frame
    #cv2.imshow('Video', frame)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# When everything is done, release the capture
