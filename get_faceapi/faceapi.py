import faceapi_utils
import person
import glob
import time
import dump_to_json
from datetime import datetime
import os

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories',
}

people = {}
faceapi_utils.post_facelist()

while True:
    print("Awaiting images")
    while len(glob.glob("*.jpg")) == 0:
        time.sleep(0.1)
    print("Images found!")

    local_imgglob = glob.glob("*.jpg")
    local_imgglob.sort(key=os.path.getmtime)

    for im in local_imgglob:
        faces = faceapi_utils.get_resp(im, params) #Array of all faces in frame
        updated_faces = []
        for p in faces:
            newPerson = person.Person(p)
            if len(people.values()) <= 0:
                target = str(newPerson.rect['left']) + ',' + str(newPerson.rect['top']) + ',' +str(newPerson.rect['width']) + ',' +str(newPerson.rect['height'])
                newPerson.faceID = faceapi_utils.post_newPerson(im, target) # Set persistant ID
                people[newPerson.faceID] = newPerson
                updated_faces.append(newPerson.faceID)
            else:
                sim_results = faceapi_utils.post_findsimilars(newPerson.faceID)
                if sim_results is not None: #Check confidence threshold
                    people[sim_results].update_vals(p)
                    updated_faces.append(sim_results)
                else:
                    target = str(newPerson.rect['left']) + ',' + str(newPerson.rect['top']) + ',' +str(newPerson.rect['width']) + ',' +str(newPerson.rect['height'])
                    newPerson.faceID = faceapi_utils.post_newPerson(im, target) # Set persistant ID
                    people[newPerson.faceID] = newPerson
                    updated_faces.append(newPerson.faceID)

        for x in people.keys():
            if not x in updated_faces:
                people[x].elim_inactive()

        #faceapi_utils.annotate_image(im, people)
        print(len(people), len(faces))
        print('_____________')

        os.remove(im)

    longest = 0
    for PeopleID in people.keys():
        if len(people[PeopleID].timeline) > longest:
            longest = len(people[PeopleID].timeline)

    for PeopleID in people.keys():
        people[PeopleID].timeline = "0" * (longest - len(people[PeopleID].timeline)) + people[PeopleID].timeline
        print(people[PeopleID].timeline)

#y = dump_to_json.dump(people)
