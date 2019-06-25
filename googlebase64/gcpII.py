import requests
import json
from pprint import pprint

url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCK0BiYCf6maaMc43uicaD15t3Etkb37j4'
key_path = '/home/hdc/Downloads/project/py3cv4/jsonKey/lyshmily-457c5c843982.json'
base64_string = "test"
detection_type = "DOCUMENT_TEXT_DETECTION"
data = {
    "requests":
        {
            {"image":
                {"content": base64_string,}
            },
            {"features":
                 {"type": detection_type,}
             },
        },

}
with open("my.json", "w") as f:
    json.dump(data, f)
# data = json.loads(data)
# print(type(data))
# print(data.keys())
# print(type(json.dumps(data)))
# pprint(json.dumps(data))




