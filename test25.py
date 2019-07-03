
from googlebase64 import gcpIII


error_list = ['/home/hdc/Downloads/project/py3cv4/png/3/IMG_5179.PNG',
              '/home/hdc/Downloads/project/py3cv4/png/4/IMG_5150.PNG']

flg = 1

for i in error_list:
    flg += 1
    gcpIII.cp_detect(i, flg)
