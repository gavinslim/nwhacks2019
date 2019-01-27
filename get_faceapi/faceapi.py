import faceapi_utils
import person

local0 = "test_imgs/0.jpg"
local1 = "test_imgs/1.jpg"
local2 = "test_imgs/2.jpg"

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories',
}

faces = faceapi_utils.get_resp(local2, params) #Array of all faces
people = {}

for p in faces:
    newPerson = person.Person(p)
    people[newPerson.faceID] = newPerson
    print(newPerson)

faceapi_utils.annotate_image(local2, people)
