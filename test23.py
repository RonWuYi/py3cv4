import os
import re
import cv2
import pytesseract

from pathlib import Path
from PIL import Image

files = '/home/hdc/Downloads/project/py3cv4/png/2/IMG_5185.PNG'
image = cv2.imread(files)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filename = "My_test.PNG"
cv2.imwrite(filename, gray)

new_image = cv2.imread(os.path.join(str(Path.cwd()), filename))
cv2.imshow("changed", new_image)
cv2.waitKey()
