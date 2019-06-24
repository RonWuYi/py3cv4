import os
import base64
from google.cloud import vision

client = vision.ImageAnnotatorClient()
image_path = '/home/hdc/Downloads/project/py3cv4/png/2/IMG_5184.PNG'

with open(image_path, 'rb') as image:
    content = image.read()
    response = client.annotate_image({'image': {'content': content},
                                      'features': [{'type': vision.enums.Feature.Type.DOCUMENT_TEXT_DETECTION}], })
    print(response)
    # response = client.annotate_image({'image': {'content': content}})
