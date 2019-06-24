import os
import subprocess

key_path = "/home/hdc/Downloads/project/py3cv4/jsonKey/lyshmily-457c5c843982.json"


# os.system('export GOOGLE_APPLICATION_CREDENTIALS={}'.format(key_path))

subprocess.run(["export GOOGLE_APPLICATION_CREDENTIALS={}".format(key_path)], stdout=subprocess.PIPE)
# print(stdout)
print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS '))