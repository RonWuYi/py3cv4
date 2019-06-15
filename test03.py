import cv2
import pytesseract
# import time
from PIL import Image
import os

folder_path = '/home/hdc/PycharmProjects/py3cv4/png'
png_list = os.listdir(folder_path)


for i in png_list:
    print(i)