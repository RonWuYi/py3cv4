import os
from googlebase64 import gcp

key_path = '/home/hdc/Downloads/project/py3cv4/jsonKey/lyshmily-457c5c843982.json'
file = '/home/hdc/Downloads/project/py3cv4/png/3/IMG_5176.PNG'


if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
    # gcp.method(file)
    gcp.detect_document(file)