import json

def dump(people):
    for person in people:
        data = {
            "faceID": person.faceID,
            "age": person.age,
            "gender": person.gender,
            "start_reaction": person.emotion_i, #note to get this value from the emotion object not the smile.
            "end_reaction": person.emotion,
            "timeline": person.timeline, #Where 0 represents not looking and 1 represents looking
            "face_attributes": {
                "hair": {
                    "color": person.hair_color,
                    "bald": person.hair_bald # boolean
                },
                "facial_hair": {
                    "beard": person.beard, # boolean
                    "moustache": person.moustache # boolean
                },
                "accessories": {
                    person.accessories
                },
                "makeup": {
                    "eyeMakeup": person.makeup_eye,
                    "lipMakeup": person.makeup_lip
                },
                "occlusion": {
                    "foreheadOccluded": person.occlusion_forehead,
                    "eyeOccluded": person.occlusion_eye,
                    "mouthOccluded": person.occlusion_mouth
                  }
            }
        }
        return data
