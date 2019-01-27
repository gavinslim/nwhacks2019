import faceapi_utils
import person
import glob
from datetime import datetime
__TIME__ = datetime.utcnow()

local0 = "test_imgs/0.jpg"
local1 = "test_imgs/1.jpg"
local2 = "test_imgs/2.jpg"

local_imgglob = glob.glob("test_imgs/*.jpg")
print(local_imgglob)

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories',
}

for im in local_imgglob:
    faces = faceapi_utils.get_resp(im, params) #Array of all faces
    people = {}

    for p in faces:
        newPerson = person.Person(p, __TIME__)
        people[newPerson.faceID] = newPerson
        print(newPerson)

    #faceapi_utils.annotate_image(im, people)
