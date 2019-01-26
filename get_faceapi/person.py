import json
class Person:
    def __init__(self, json_str):
        self.json_str = json.loads(json_str)

        self.__CONF_THRESH__ = 0.7 #If scalar >__CONF_THRESH__, is true

        self.faceID = "str"
        self.age = 0
        self.gender = "string"
        self.headpose = {"pitch": 0.0,
                         "roll": 0.0,
                         "yaw": 0.0}
        self.accessories_glasses = 0.0
        self.occlusion_forehead = False
        self.occlusion_eye = False
        self.occlusion_mouth = False
        self.emotion = "string" #SOFTMAX INPUT
        self.makeup_eye = False
        self.makeup_lip = False
        self.moustache = False
        self.beard = False
        self.sideburns = False


    def get_if_looking(self):
        pass

    def toJSON(self):
        #TODO Return JSON of class
        pass

    def __str__(self):
        pass
