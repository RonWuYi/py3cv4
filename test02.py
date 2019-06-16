import cv2
import pytesseract
import os

from PIL import Image
from xml.etree.ElementTree import ElementTree

tree = ElementTree()
# tree.parse('/home/hdc/PycharmProjects/py3cv4/xml/result.xml')

root_folder = '/home/hdc/PycharmProjects/py3cv4/png/'

fix_box2 = [(289, 65, 366, 129), (232, 513, 393, 570), (259, 593, 298, 620), (353, 905, 419, 940)]
fix_box3 = [(272, 63, 366, 132), (232, 513, 384, 570), (259, 593, 298, 620), (353, 905, 419, 940)]
fix_box4 = [(258, 63, 380, 132), (232, 513, 379, 570), (259, 593, 298, 620), (353, 905, 419, 940)]


for x, _, z in os.walk(root_folder):
    if len(z) > 0:
        for i in z:
            if x[-1:] == "2":
                img = cv2.imread(os.path.join(x, i))
                orig = img.copy()
                for (startX, startY, endX, endY) in fix_box2:
                    # cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    # cv2.imshow("origional", orig)
                    config = ("-l eng --oem 1 --psm 3")
                    roi = orig[startY:endY, startX:endX]
                    text = pytesseract.image_to_string(roi, config=config)
                    print(text)
                    # print(pytesseract.image_to_string(Image.fromarray(roi)))
                    # cv2.waitKey(0)

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
                    cv2.waitKey(0)
            else:
                img = cv2.imread(os.path.join(x, i))
                orig = img.copy()
                for (startX, startY, endX, endY) in fix_box4:
                    # cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    # cv2.imshow("origional", orig)
                    config = ("-l eng --oem 1 --psm 3")
                    roi = orig[startY:endY, startX:endX]
                    text = pytesseract.image_to_string(roi, config=config)
                    print(text)
                    # print(pytesseract.image_to_string(Image.fromarray(roi)))
                    # cv2.waitKey(0)

# tree.write("output.xml")