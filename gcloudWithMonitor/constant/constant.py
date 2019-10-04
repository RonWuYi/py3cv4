import os
import cv2
import datetime
import string
# from datetime import datetime
from pathlib import Path
# print(datetime.now())
# print('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
key_path = 'C:\\Work\\test project\\github\\mysite\\private\\bugs-14332e1a3777.json'

videoinpath = "C:\\Work\\media\\in"
videooutpath = "C:\\Work\\media\\out"
# time_string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

storage_name = 'bugs-246912.appspot.com'

# temp = []


# for i in range(len(time_string)-1):
#     if time_string[i] not in string.digits:
#         temp.append('_')
#     else:
#         temp.append(time_string[i])
        # temp[i] = time_string[i]

def time_string():
    cur_string = datetime.datetime.now().isoformat(timespec='seconds')
    return cur_string.replace(':', '')


def cur_folder() :
    return os.getcwd()

def cur_path():
    return str(Path.cwd())

cap = cv2.VideoCapture(0)

# define the codec and create VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
outtest = os.path.join(os.getcwd(),"media",'output{}.avi'.format(time_string()))

if __name__ == '__main__':
    # Imports the Google Cloud client library
    from google.cloud import storage

    # Instantiates a client
    storage_client = storage.Client()

    # The name for the new bucket
    bucket_name = 'my-new-bucket'

    # Creates the new bucket
    bucket = storage_client.create_bucket(bucket_name)

    print('Bucket {} created.'.format(bucket.name))
    # while True:
    #     print(datetime.datetime.now())
    #     print(time_string())