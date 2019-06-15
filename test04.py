import cv2
import pytesseract
# import time
from PIL import Image
import os

folder_path = '/home/hdc/PycharmProjects/py3cv4/png'
png_list = os.listdir(folder_path)

image_file = '/home/hdc/PycharmProjects/py3cv4/png/2/IMG_4167.PNG'
# for i in png_list:
img = cv2.imread(image_file)
orig = img.copy()

# this is cp area
startX, startY, endX, endY = 287, 63, 366, 132
# for (startX, startY, endX, endY) in [(244, 63, 366, 120)]):
cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
cv2.imshow("origional", orig)
config = ("-l eng --oem 1 --psm 3")
roi = orig[startY:endY, startX:endX]
text = pytesseract.image_to_string(roi, config=config)
print(text)
print(pytesseract.image_to_string(Image.fromarray(roi)))
# print(Image.fromarray(roi))
cv2.waitKey(0)
