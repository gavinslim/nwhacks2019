import requests
from datetime import datetime
from datetime import timedelta

url = 'http://localhost:8080/?'
url += 'from={}&to={}&age_from=36&age_to=67&'.format(datetime.utcnow() - timedelta(days=1), datetime.utcnow() + timedelta(days=1))
url += 'genders=["male"]&reactions=["positive","neutral"]&'
url += 'mustache=true&beard=false&hair_colors=["black","other","red"]&'
url += 'bald=false&glasses=true&eye_makeup=false&lip_makeup=true'
url += '&forehead_occlusion=false&eye_occlusion=false&mouth_occlusion=false'
res = requests.get(url=url)
print (res.text)