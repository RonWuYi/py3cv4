import os
import cv2
import time

from pathlib import Path
from func import opencvSave
from threading import Thread
from constant import constant, google

google.set_env()
keyFlag = True

my_save = opencvSave.Cv2Video(constant.cap, constant.fourcc)

t1 = Thread(target=my_save.Create, args=())
t2 = Thread(target=my_save.Upload, args=(constant.videooutpath, ))

t1.start()
t2.start()

t1.join()
t2.join()

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        my_save.Createterminate()
        my_save.Uploadterminate()
        break



