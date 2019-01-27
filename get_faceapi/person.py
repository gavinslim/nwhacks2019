import json

class Person:

    def softmax(self, val):
        if val > self.__CONF_THRESH__:
            return True
        else:
            return False

    def softmax_emotions(self, d):
         v = list(d.values())
         k = list(d.keys())
         return k[v.index(max(v))]

    def __init__(self, json_str, time):

        self.__CONF_THRESH__ = 0.7 #If scalar >__CONF_THRESH__, is true
        self.__INTERVAL__ = 0.1 #Refresh interval in seconds
        self.__YAWBOUND__ = 10 # +/- in degrees from center
        self.___TIME__ = time

        self.timeline = "" #00001110011 Where 0 represents not looking and 1 represents looking
        self.faceID = json_str["faceId"]
        self.rect = json_str["faceRectangle"]
        self.attr = json_str["faceAttributes"]
        self.age = self.attr["age"]
        self.gender = self.attr["gender"]
        self.headpose_roll = self.attr["headPose"]["roll"]
        self.headpose_yaw = self.attr["headPose"]["yaw"]
        self.accessories = []

        if not self.attr["glasses"] == "NullGlasses":
            self.accessories.append(self.attr["glasses"])
        for acc in self.attr["accessories"]:
            if self.softmax(acc["confidence"]) and not acc["type"] == "glasses":
                self.accessories.append(acc["type"])

        self.occlusion_forehead = self.attr["occlusion"]["foreheadOccluded"]
        self.occlusion_eye = self.attr["occlusion"]["eyeOccluded"]
        self.occlusion_mouth = self.attr["occlusion"]["mouthOccluded"]
        self.emotion = self.softmax_emotions(self.attr["emotion"]) #SOFTMAX INPUT
        self.makeup_eye = self.attr["makeup"]["eyeMakeup"]
        self.makeup_lip = self.attr["makeup"]["lipMakeup"]
        self.moustache = self.softmax(self.attr["facialHair"]["moustache"])
        self.beard = self.softmax(self.attr["facialHair"]["beard"])
        self.sideburns = self.softmax(self.attr["facialHair"]["sideburns"])

        self.total_time = 0.0

    def get_if_looking(self):
        if abs(self.headpose_yaw) > self.__YAWBOUND__:
            return False
        else:
            return True

    def toJSON(self):
        #TODO Return JSON of class
        pass

    def __str__(self):
        return "ID: " + str(self.faceID) + \
        "\nAge: " + str(self.age) + \
        "\nGender: " + str(self.gender) + \
        "\nRoll: " + str(self.headpose_roll) + \
        "\nYaw: " + str(self.headpose_yaw) + \
        "\nAccessories: " + ''.join(self.accessories) + \
        "\nEmotion: " + str(self.emotion) + \
        "\n_____"
