import string
import random
import json
import requests

def rand_int():
    return random.randint(0, 99)

def rand_str():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def rand_item(arr):
    return arr[random.randint(0, len(arr)-1)]

def rand_bool():
    return rand_item([True, False])

def rand_data():
    return {
        "faceID": rand_str(),
        "age": rand_int(),
        "gender": 'male' if rand_int() % 2 == 0 else 'female',
        "start_reaction": rand_item(['anger', 'contempt', 'disgust', 'fear', 'sadness', 'happiness', 'surprise']),
        "end_reaction": rand_item(['anger', 'contempt', 'disgust', 'fear', 'sadness', 'happiness', 'surprise']),
        "face_attributes": {
            "hair": {
                "color": rand_item(['brown', 'black', 'red', 'gray', 'blonde', 'other']),
                "bald": rand_bool(),
            },
            "facial_hair": {
                "beard": rand_bool(),
                "moustache": rand_bool(),
            }
        },
        "accessories": {
            "glasses": rand_bool(),
            "makeup": {
                "eyeMakeup": rand_bool(),
                "lipMakeup": rand_bool(),
                "eyeMakeup": rand_bool()
            }
        },
        "occlusion": {
            "foreheadOccluded": rand_bool(),
            "eyeOccluded": rand_bool(),
            "mouthOccluded": rand_bool()
        }
    }


for i in range (0, 99):
    # res = requests.post(url='http://localhost:8080/', json=rand_data())
    print (rand_data())

