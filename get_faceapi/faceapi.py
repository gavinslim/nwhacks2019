import faceapi_utils
import person
import glob
import time
from datetime import datetime

local_imgglob = glob.glob("small_test/*.jpg")

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories',
}

people = {}
faceapi_utils.post_largefacelist()

for im in local_imgglob:
    faces = faceapi_utils.get_resp(im, params) #Array of all faces in frame
    for p in faces:
        newPerson = person.Person(p)
        if faceapi_utils.post_findsimilars(p.faceID)[1] > 0.7 and len(people.values >= 0): #Check confidence threshold and if db isn't empty
            #update
            pass
        else:
            target = str(newPerson.rect['left']) + ',' + str(newPerson.rect['top']) + ',' +str(newPerson.rect['width']) + ',' +str(newPerson.rect['height'])
            newPerson.faceID = faceapi_utils.post_newPerson(im, target) # Set persistant ID
            people[newPerson.faceID] = newPerson


    faceapi_utils.annotate_image(im, people)
    print(len(people), len(faces))
    print(im)
    print('_____________')
    time.sleep(3)

for PeopleID in people.keys():
    print(people[PeopleID].timeline)
