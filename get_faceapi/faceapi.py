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
        if len(people.values()) <= 0:
            newPerson = person.Person(p)
            people[newPerson.faceID] = newPerson
        else:
            for PeopleID in people.keys():
                print(people.keys())
                matches = 0
                match = faceapi_utils.get_similar(p['faceId'], PeopleID)
                print('Match', match)
                if match:
                    people[PeopleID].update_vals(p)
                    matches += 1
            if matches == 0:
                newPerson = person.Person(p)
                people[newPerson.faceID] = newPerson

    faceapi_utils.annotate_image(im, people)
    print(len(people), len(faces))
    print(im)
    print('_____________')
    time.sleep(3)

for PeopleID in people.keys():
    print(people[PeopleID].timeline)
