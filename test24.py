import os
import re
import cv2
import pytesseract

from googlebase64 import gcpIII
from util.PyConstant import *
from db.PsyDb import Database
from pathlib import Path


input_file = '/home/hdc/Downloads/project/py3cv4/detection_success/My_test.PNG'


img = cv2.imread(input_file)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
orig = img.copy()
flag = 0
for startX, startY, endX, endY in fix_box2:
    flag += 1
    roi = orig[startY:endY, startX:endX]
    cv2.imwrite(tmp_filename.format(flag), roi)
    new_image = cv2.imread(os.path.join(str(Path.cwd()), tmp_filename.format(flag)))
    print(gcpIII.single_detect(os.path.join(str(Path.cwd()), tmp_filename.format(flag))))
# cv2.

# new_image = cv2.imread(os.path.join(str(Path.cwd()), filename))
    cv2.imshow("changed", new_image)
    cv2.waitKey()
    os.remove(os.path.join(str(Path.cwd()), tmp_filename.format(flag)))