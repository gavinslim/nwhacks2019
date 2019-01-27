import faceapi_utils
import person
import glob
from datetime import datetime
__TIME__ = datetime.utcnow()

local_imgglob = glob.glob("test_imgs/*.jpg")

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories',
}

people = {}

for im in local_imgglob:
    faces = faceapi_utils.get_resp(im, params) #Array of all faces in frame
    for p in faces:
        if len(people.values()) == 0:
            newPerson = person.Person(p, __TIME__)
            people[newPerson.faceID] = newPerson
        else:
            for k in people.values():
                if faceapi_utils.get_similar(p['faceId'], k.faceID):
                    #Handle new values
                    pass
                else:
                    newPerson = person.Person(p, __TIME__)
                    people[newPerson.faceID] = newPerson

    #faceapi_utils.annotate_image(im, people)
