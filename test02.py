import cv2
import pytesseract
import os

from PIL import Image
from xml.etree.ElementTree import ElementTree

tree = ElementTree()
tree.parse('/home/hdc/PycharmProjects/py3cv4/xml/result.xml')
tree.write("output.xml")

root_folder = '/home/hdc/PycharmProjects/py3cv4/png/'
folder2_path = '/home/hdc/PycharmProjects/py3cv4/png/2'
folder3_path = '/home/hdc/PycharmProjects/py3cv4/png/3'
folder4_path = '/home/hdc/PycharmProjects/py3cv4/png/4'

my_list = os.walk(root_folder)

for x, y, z in my_list:
    print(x, y, z)

# png_list = os.listdir(root_folder)
png_list = os.listdir(folder4_path)

# fix_box3 = [(258, 63, 380, 132)]

fix_box2 = [(287, 63, 366, 132), (232, 513, 379, 570), (309, 593, 379, 620), (347, 905, 419, 940)]

# 272, 63, 366, 140
fix_box3 = [(272, 63, 366, 132), (232, 513, 379, 570), (309, 593, 379, 620), (347, 905, 419, 940)]

fix_box4 = [(258, 63, 380, 132), (232, 513, 379, 570), (309, 593, 379, 620), (347, 905, 419, 940)]


for x, _, z in os.walk(root_folder):
    if len(z) > 0:
        for i in z:
            if x[-1:] == "2":
                img = cv2.imread(os.path.join(x, i))
                orig = img.copy()
                for (startX, startY, endX, endY) in fix_box2:
                    cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    cv2.imshow("origional", orig)
                    config = ("-l eng --oem 1 --psm 3")
                    roi = orig[startY:endY, startX:endX]
                    text = pytesseract.image_to_string(roi, config=config)
                    print(text)
                    print(pytesseract.image_to_string(Image.fromarray(roi)))
                    cv2.waitKey(0)

            elif x[-1:] == "3":
                img = cv2.imread(os.path.join(x, i))
                orig = img.copy()
                for (startX, startY, endX, endY) in fix_box3:
                    cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    cv2.imshow("origional", orig)
                    config = ("-l eng --oem 1 --psm 3")
                    roi = orig[startY:endY, startX:endX]
                    text = pytesseract.image_to_string(roi, config=config)
                    print(text)
                    print(pytesseract.image_to_string(Image.fromarray(roi)))
                    cv2.waitKey(0)
            else:
                img = cv2.imread(os.path.join(x, i))
                orig = img.copy()
                for (startX, startY, endX, endY) in fix_box4:
                    cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    cv2.imshow("origional", orig)
                    config = ("-l eng --oem 1 --psm 3")
                    roi = orig[startY:endY, startX:endX]
                    text = pytesseract.image_to_string(roi, config=config)
                    print(text)
                    print(pytesseract.image_to_string(Image.fromarray(roi)))
                    cv2.waitKey(0)