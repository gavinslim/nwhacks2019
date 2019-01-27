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

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_frontal = faceCascade_frontal.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    faces_side = faceCascade_side.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
# http://answers.opencv.org/question/204685/why-it-cannot-detect-some-profile-face/
    flipped = cv2.flip(gray, 1)
    faces_other_side = faceCascade_side.detectMultiScale(
        flipped,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # Draw a rectangle around the faces
 #   if len(faces) > 0:
#    cv2.imwrite('detected_image{0}.jpg'.format(imageno),frame)
#             cv2.imwrite('detected_image.jpg',frame)
#    for (x, y, w, h) in faces_frontal:
 #       cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    for (x, y, w, h) in faces_other_side:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    imageno = imageno +1
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
