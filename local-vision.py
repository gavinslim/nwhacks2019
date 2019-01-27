# This code will identify if a person is present in the video stream and send it upstream if there is
# https://realpython.com/face-detection-in-python-using-a-webcam/
# run code using python local-vision.py haarcascade_frontalface_default.xml
import cv2
import sys

cascPath_frontal = sys.argv[1]
cascPath_side = sys.argv[2]
faceCascade_frontal = cv2.CascadeClassifier(cascPath_frontal)
faceCascade_side = cv2.CascadeClassifier(cascPath_side)

video_capture = cv2.VideoCapture(0)
imageno = 5
count_right = 0
count_left = 0
count_front = 0

front_filter = 1
left_filter = 0
right_filter = 0

take_pic = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_side = faceCascade_side.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if len(faces_side) > 0:
        #cv2.imwrite('detected_image_right{0}.jpg'.format(count_right),frame)
        #count_right = count_right + 1

        for (x, y, w, h) in faces_side:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2) #Green

    # http://answers.opencv.org/question/204685/why-it-cannot-detect-some-profile-face/
    else:
        flipped = cv2.flip(gray, 1)
        faces_other_side = faceCascade_side.detectMultiScale(
            flipped,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if len(faces_other_side) > 0:
            #cv2.imwrite('detected_image_left{0}.jpg'.format(count_left),frame)
            #count_left = count_left + 1
            for (x, y, w, h) in faces_other_side:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2) #Red
        else:
            faces_frontal = faceCascade_frontal.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            if len(faces_frontal) > 0:
                #cv2.imwrite('detected_image_front{0}.jpg'.format(count_front),frame)
                #count_front = count_front + 1
                for (x, y, w, h) in faces_frontal:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2) #Blue


    # Drawing rectangle
    # for (x, y, w, h) in faces_frontal:
    #    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #imageno = imageno +1
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
