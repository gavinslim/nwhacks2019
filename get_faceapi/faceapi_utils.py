import matplotlib.pyplot as plt
import requests
import io
from matplotlib import patches
from PIL import Image

def annotate_image(image_url, people):

    image_file = open(image_url, "rb")
    image = Image.open(image_file)

    plt.figure(figsize=(8,8))
    ax = plt.imshow(image, alpha=1.0)
    for face in people.itervalues():
        fr = face.rect
        origin = (fr["left"], fr["top"])
        p = patches.Rectangle(origin, fr["width"], \
                              fr["height"], fill=False, linewidth=2, color='b')
        ax.axes.add_patch(p)
        plt.text(origin[0], origin[1], "%s"%(face.faceID[:6]), \
                 fontsize=20, weight="bold", va="bottom", color=(1,1,1))
    plt.axis("off")
    plt.show()

def get_resp(path, params):
    print('API CALL 1')
    __subscription_key = "61246efcaeac473fa675ffd8446b8110"
    __face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

    headers = { 'Content-Type': 'application/octet-stream',
                'Ocp-Apim-Subscription-Key': __subscription_key }

    data = open(path, "rb")

    response = requests.post(__face_api_url, params=params, headers=headers, data=data)
    faces = response.json()
    return faces

def get_similar(faceID1, faceID2):
    print('API CALL 2')
    __subscription_key = "61246efcaeac473fa675ffd8446b8110"
    __face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/verify'

    headers = {'Content-Type': 'application/json',
               'Ocp-Apim-Subscription-Key': __subscription_key}

    response = requests.post(__face_api_url, headers=headers, json={"faceId1": faceID1, "faceId2": faceID2})
    response = response.json()
    print(response, faceID1, faceID2)
    if response["isIdentical"] and response["confidence"] >= 0.7:
        return True
    else:
        return False

def post_newPerson(path, target):
    __subscription_key = "61246efcaeac473fa675ffd8446b8110"
    __face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/largefacelists/nwhacksfacelist/persistedfaces?NA&targetFace='+target

    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': __subscription_key}

    data = open(path, "rb")

    response = requests.post(__face_api_url, headers=headers, data = data)
    response = response.json()

    return response["persistedFaceId"]

def post_largefacelist():
    __subscription_key = "61246efcaeac473fa675ffd8446b8110"
    __face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/largefacelists/nwhacksfacelist'

    headers = {'Content-Type': 'application/json',
               'Ocp-Apim-Subscription-Key': __subscription_key}

    response = requests.delete(__face_api_url, headers=headers, json={"name": "nwhacksfacelist"})
    response = requests.put(__face_api_url, headers=headers, json={"name": "nwhacksfacelist"})

def post_findsimilars(faceId):
    __subscription_key = "61246efcaeac473fa675ffd8446b8110"
    __face_api_url = 'https://westcentralus.apiapi.cognitive.microsoft.com/face/v1.0/findsimilars'

    headers = {'Content-Type': 'application/json',
               'Ocp-Apim-Subscription-Key': __subscription_key}

    response = requests.post(__face_api_url, headers=headers, json={"faceId": faceId,
                                                                    "largeFaceListId": "nwhacksfacelist"})

    response = response.json()

    return response["persistedFaceId"], response["confidence"]
