import os

key_path = "/home/hdc/Downloads/project/py3cv4/jsonKey/lyshmily-457c5c843982.json"
os.system('export GOOGLE_APPLICATION_CREDENTIALS={}'.format(key_path))

print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS '))