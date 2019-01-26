import faceapi_utils

image_url = 'https://how-old.net/Images/faces2/main007.jpg'

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

faces = faceapi_utils.get_resp(image_url, params)
print(faceapi_utils.interp_json(faces))
faceapi_utils.annotate_image(image_url, faces)
# faces = faceapi_utils.get_resp(image_url, params)
# print(faces)
