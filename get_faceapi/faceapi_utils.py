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
        plt.text(origin[0], origin[1], "%s"%(face.get_if_looking()), \
                 fontsize=20, weight="bold", va="bottom", color=(1,1,1))
    plt.axis("off")
    plt.show()

def get_resp(path, params):
    __subscription_key = "30c9191c099b4dc5b8cf3ebe1cf06310"
    assert __subscription_key
    __face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

    headers = { 'Content-Type': 'application/octet-stream',
                'Ocp-Apim-Subscription-Key': __subscription_key }

    data = open(path, "rb")

    response = requests.post(__face_api_url, params=params, headers=headers, data=data)
    faces = response.json()
    return faces
