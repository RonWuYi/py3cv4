import collections
import requests
import base64
import urllib.request
import json
from pprint import pprint
detection_type = "DOCUMENT_TEXT_DETECTION"
URL = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCK0BiYCf6maaMc43uicaD15t3Etkb37j4'
file_folder = '/home/hdc/Downloads/project/py3cv4/png/2'
test_file = '/home/hdc/Downloads/project/py3cv4/png/2/IMG_5183.PNG'


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


with open(test_file, 'rb') as image_file:
    encode_string = base64.b64encode(image_file.read())

test_content = encode_string.decode("utf-8")


b1 = {"content": test_content}
b2 = {"type": detection_type}
dd = collections.defaultdict(dict)
dd["requests"]["image"] = b1
dd["requests"]["features"] = b2

# r = requests.post(URL, data=dd)
# print(r.text)

req = urllib.request.Request(URL, data=json.dumps(dd).encode('utf8'),
                             headers={'content-type': 'application/json'})

response = urllib.request.urlopen(req)

# print(type(req))
# pprint(response.read().decode('utf8'))

x = []
for page in response.full_text_annotation.text:
    x.append(page)
    # x.append(page.rstrip())
    # print()
print(''.join(x))

# data = json.loads(response.read().decode('utf8'), object_hook=JSONObject)
# print("#################################################################")
# print(data.responses.fullTextAnnotation.text())
# x = []
# for page in response.read().decode('utf8').full_text_annotation.text:
#     x.append(page)
#     # x.append(page.rstrip())
#     # print()
# print(''.join(x))