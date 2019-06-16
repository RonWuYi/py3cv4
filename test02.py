import cv2
import pytesseract
import os

import xml.etree.ElementTree as ET

my_xml = '/home/hdc/PycharmProjects/py3cv4/xml/result.xml'
three = ET.parse(my_xml)
root = three.getroot()

root_folder = '/home/hdc/PycharmProjects/py3cv4/png/'

fix_box2 = [(289, 65, 366, 129), (232, 513, 393, 570), (259, 593, 298, 620), (353, 905, 419, 940)]
fix_box3 = [(272, 63, 366, 132), (232, 513, 384, 570), (259, 593, 298, 620), (353, 905, 419, 940)]
fix_box4 = [(258, 63, 380, 132), (232, 513, 379, 570), (259, 593, 298, 620), (352, 905, 419, 940)]

name, cp, hp, dust = None, None, None, None

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
                    if fix_box2.index((startX, startY, endX, endY)) == 0:
                        cp = text
                    elif fix_box2.index((startX, startY, endX, endY)) == 1:
                        name = text
                    elif fix_box2.index((startX, startY, endX, endY)) == 2:
                        hp = text
                    else:
                        dust = text
                bug = ET.SubElement(root, 'bug')
                bug_name = ET.SubElement(bug, 'name')
                bug_name.text = name
                bug_cp = ET.SubElement(bug, 'cp')
                bug_cp.text = cp
                bug_hp = ET.SubElement(bug, 'hp')
                bug_hp.text = hp
                bug_dust = ET.SubElement(bug, 'dust')
                bug_dust.text = dust
            elif x[-1:] == "3":
                img = cv2.imread(os.path.join(x, i))
                orig = img.copy()
                for (startX, startY, endX, endY) in fix_box3:
                    # cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    # cv2.imshow("origional", orig)
                    config = ("-l eng --oem 1 --psm 3")
                    roi = orig[startY:endY, startX:endX]
                    text = pytesseract.image_to_string(roi, config=config)
                    print(text)
                    if fix_box3.index((startX, startY, endX, endY)) == 0:
                        cp = text
                    elif fix_box3.index((startX, startY, endX, endY)) == 1:
                        name = text
                    elif fix_box3.index((startX, startY, endX, endY)) == 2:
                        hp = text
                    else:
                        dust = text
                    # cv2.waitKey(0)
                bug = ET.SubElement(root, 'bug')
                bug_name = ET.SubElement(bug, 'name')
                bug_name.text = name
                bug_cp = ET.SubElement(bug, 'cp')
                bug_cp.text = cp
                bug_hp = ET.SubElement(bug, 'hp')
                bug_hp.text = hp
                bug_dust = ET.SubElement(bug, 'dust')
                bug_dust.text = dust
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
                    if fix_box4.index((startX, startY, endX, endY)) == 0:
                        cp = text
                    elif fix_box4.index((startX, startY, endX, endY)) == 1:
                        name = text
                    elif fix_box4.index((startX, startY, endX, endY)) == 2:
                        hp = text
                    else:
                        dust = text
                    # cv2.waitKey(0)
                bug = ET.SubElement(root, 'bug')
                bug_name = ET.SubElement(bug, 'name')
                bug_name.text = name
                bug_cp = ET.SubElement(bug, 'cp')
                bug_cp.text = cp
                bug_hp = ET.SubElement(bug, 'hp')
                bug_hp.text = hp
                bug_dust = ET.SubElement(bug, 'dust')
                bug_dust.text = dust

tree = ET.ElementTree(root)
tree.write("output.xml")
