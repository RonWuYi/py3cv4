import os
import re
import cv2
import psycopg2
import pytesseract
import xml.etree.ElementTree as ET

from googlebase64 import gcpIII
# from base64.google_picto64II import detect_document

my_xml = '/home/hdc/Downloads/project/py3cv4/xml/result.xml'

three = ET.parse(my_xml)
root = three.getroot()

key_path = '/home/hdc/Downloads/project/py3cv4/jsonKey/lyshmily-457c5c843982.json'
root_folder = '/home/hdc/Downloads/project/py3cv4/png'
config = "-l eng --oem 1 --psm 3"

fix_box2 = [(289, 65, 366, 129), (220, 513, 406, 570), (259, 593, 298, 620), (353, 905, 419, 940)]
fix_box3 = [(272, 63, 366, 132), (220, 513, 406, 570), (259, 593, 298, 620), (353, 905, 419, 940)]
fix_box4 = [(258, 63, 380, 132), (220, 513, 406, 570), (259, 593, 298, 620), (350, 905, 419, 940)]

name, cp, hp, dust = None, None, None, None
global sum

for x, _, z in os.walk(root_folder):
    if len(z) > 0:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
        conn = psycopg2.connect(database="testdb", user="postgres", password="postgres", host="172.16.66.244")
        cur = conn.cursor()
        sum = 0
        for i in z:
            sum += 1
            print("start handle {}".format(os.path.join(x, i)))
            if x[-1:] == "2":
                # pass
                img = cv2.imread(os.path.join(x, i))
                orig = img.copy()
                for (startX, startY, endX, endY) in fix_box2:
                    # cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    # cv2.imshow("origional", orig)
                    roi = orig[startY:endY, startX:endX]
                    text = pytesseract.image_to_string(roi, config=config)
                    # print(text)
                    # print(pytesseract.image_to_string(Image.fromarray(roi)))
                    # cv2.waitKey(0)
                    if fix_box2.index((startX, startY, endX, endY)) == 0:
                        # cp = text
                        cp = re.search(r'[0-9]*', text).group(0)
                    elif fix_box2.index((startX, startY, endX, endY)) == 1:
                        name = re.search(r'[a-z.A-Z]*', text).group(0)
                    elif fix_box2.index((startX, startY, endX, endY)) == 2:
                        hp = re.search(r'[0-9]*', text).group(0)
                    else:
                        dust = re.search(r'[0-9]*', text).group(0)
                new_value_list = [cp, name, hp, dust]
                if len(cp) > 0 and len(name) > 0 and len(hp) > 0 and len(dust) > 0:
                    bug = ET.SubElement(root, 'bug')
                    bug_name = ET.SubElement(bug, 'name')
                    bug_name.text = name
                    bug_cp = ET.SubElement(bug, 'cp')
                    bug_cp.text = cp
                    bug_hp = ET.SubElement(bug, 'hp')
                    bug_hp.text = hp
                    bug_dust = ET.SubElement(bug, 'dust')
                    bug_dust.text = dust
                elif len(cp) == 0 or len(name) == 0 or len(hp) == 0 or len(dust) == 0:
                    value_list = gcpIII.detect_document(os.path.join(x, i))
                    for idx, value in enumerate(new_value_list):
                        if len(value) == 0 and idx == 0:
                            if len(value_list[0]) >= 6:
                                cp = value_list[0][:3]
                            else:
                                cp = value_list[0]
                        elif len(value) == 0 and idx == 1:
                            name = value_list[1]
                        elif len(value) == 0 and idx == 2:
                            hp = value_list[2]
                        elif len(value) == 0 and idx == 0:
                            if value_list[3] >= 5:
                                dust = value_list[3][1:4]
                            else:
                                dust = value_list[3][1:3]
                    bug = ET.SubElement(root, 'bug')
                    bug_name = ET.SubElement(bug, 'name')
                    bug_name.text = name
                    bug_cp = ET.SubElement(bug, 'cp')
                    bug_cp.text = cp
                    bug_hp = ET.SubElement(bug, 'hp')
                    bug_hp.text = hp
                    bug_dust = ET.SubElement(bug, 'dust')
                    bug_dust.text = dust
                print(cp, name, hp, dust)
                try:
                    cur.execute("INSERT INTO bugs (name, cp, hp, dust) VALUES (%s, %s, %s, %s)",
                                (name, int(cp), int(hp), int(dust)))
                except ValueError as e:
                    print(e)
                    continue
            elif x[-1:] == "3":
                # pass
                img = cv2.imread(os.path.join(x, i))
                orig = img.copy()
                for (startX, startY, endX, endY) in fix_box3:
                    # cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    # cv2.imshow("origional", orig)
                    roi = orig[startY:endY, startX:endX]
                    text = pytesseract.image_to_string(roi, config=config)
                    # print(text)
                    if fix_box3.index((startX, startY, endX, endY)) == 0:
                        # cp = text
                        cp = re.search(r'[0-9]*', text).group(0)
                    elif fix_box3.index((startX, startY, endX, endY)) == 1:
                        name = re.search(r'[a-z.A-Z]*', text).group(0)
                    elif fix_box3.index((startX, startY, endX, endY)) == 2:
                        hp = re.search(r'[0-9]*', text).group(0)
                    else:
                        # dust = re.search(r'[0-9]*', text).group(0)
                        dust = text.replace(',', '')
                # if all(v is not None for v in [cp, name, hp, dust]):
                new_value_list = [cp, name, hp, dust]
                if len(cp) > 0 and len(name) > 0 and len(hp) > 0 and len(dust) > 0:
                    bug = ET.SubElement(root, 'bug')
                    bug_name = ET.SubElement(bug, 'name')
                    bug_name.text = name
                    bug_cp = ET.SubElement(bug, 'cp')
                    bug_cp.text = cp
                    bug_hp = ET.SubElement(bug, 'hp')
                    bug_hp.text = hp
                    bug_dust = ET.SubElement(bug, 'dust')
                    bug_dust.text = dust
                elif len(cp) == 0 or len(name) == 0 or len(hp) == 0 or len(dust) == 0:
                    value_list = gcpIII.detect_document(os.path.join(x, i))
                    for idx, value in enumerate(new_value_list):
                        if len(value) == 0 and idx == 0:
                            if len(value_list[0]) >= 6:
                                cp = value_list[0][:3]
                            else:
                                cp = value_list[0]
                        elif len(value) == 0 and idx == 1:
                            name = value_list[1]
                        elif len(value) == 0 and idx == 2:
                            hp = value_list[2]
                        elif len(value) == 0 and idx == 0:
                            if value_list[3] > 5:
                                dust = value_list[3][1:5]
                            else:
                                dust = value_list[3][1:4]
                        bug = ET.SubElement(root, 'bug')
                        bug_name = ET.SubElement(bug, 'name')
                        bug_name.text = name
                        bug_cp = ET.SubElement(bug, 'cp')
                        bug_cp.text = cp
                        bug_hp = ET.SubElement(bug, 'hp')
                        bug_hp.text = hp
                        bug_dust = ET.SubElement(bug, 'dust')
                        bug_dust.text = dust
                print("cp  = {}".format(cp))
                print("lenght and type is {} and {}".format(len(cp), type(cp)))
                print("name  = {}".format(name))
                print("lenght and type is {} and {}".format(len(name), type(name)))
                print("hp  = {}".format(hp))
                print("lenght and type is {} and {}".format(len(hp), type(hp)))
                print("dust  = {}".format(dust))
                print("lenght and type is {} and {}".format(len(dust), type(dust)))
                # print(cp, name, hp, dust)
                try:
                    cur.execute("INSERT INTO bugs (name, cp, hp, dust) VALUES (%s, %s, %s, %s)",
                                (name, int(cp), int(hp), int(dust)))
                except ValueError as e:
                    print(e)
                    continue
            else:
                img = cv2.imread(os.path.join(x, i))
                orig = img.copy()
                for (startX, startY, endX, endY) in fix_box4:
                    # cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    # cv2.imshow("origional", orig)
                    roi = orig[startY:endY, startX:endX]
                    text = pytesseract.image_to_string(roi, config=config)
                    # print(text)
                    if fix_box4.index((startX, startY, endX, endY)) == 0:
                        # cp = text
                        cp = re.search(r'[0-9]*', text).group(0)
                    elif fix_box4.index((startX, startY, endX, endY)) == 1:
                        name = re.search(r'[a-z.A-Z]*', text).group(0)
                    elif fix_box4.index((startX, startY, endX, endY)) == 2:
                        hp = re.search(r'[0-9]*', text).group(0)
                    else:
                        dust = text.replace(',', '')
                    # cv2.waitKey(0)
                new_value_list = [cp, name, hp, dust]
                if len(cp) > 0 and len(name) > 0 and len(hp) > 0 and len(dust) > 0:

                    bug = ET.SubElement(root, 'bug')
                    bug_name = ET.SubElement(bug, 'name')
                    bug_name.text = name
                    bug_cp = ET.SubElement(bug, 'cp')
                    bug_cp.text = cp
                    bug_hp = ET.SubElement(bug, 'hp')
                    bug_hp.text = hp
                    bug_dust = ET.SubElement(bug, 'dust')
                    bug_dust.text = dust

                elif len(cp) == 0 or len(name) == 0 or len(hp) == 0 or len(dust) == 0:
                    value_list = gcpIII.detect_document(os.path.join(x, i))
                    for idx, value in enumerate(new_value_list):
                        if len(value) == 0 and idx == 0:
                            if len(value_list[0]) >= 6:
                                cp = value_list[0][:3]
                            else:
                                cp = value_list[0]
                        elif len(value) == 0 and idx == 1:
                            name = value_list[1]
                        elif len(value) == 0 and idx == 2:
                            hp = value_list[2]
                        elif len(value) == 0 and idx == 0:
                            if value_list[3] > 5:
                                dust = value_list[3][1:5]
                            else:
                                dust = value_list[3][1:4]
                    bug = ET.SubElement(root, 'bug')
                    bug_name = ET.SubElement(bug, 'name')
                    bug_name.text = name
                    bug_cp = ET.SubElement(bug, 'cp')
                    bug_cp.text = cp
                    bug_hp = ET.SubElement(bug, 'hp')
                    bug_hp.text = hp
                    bug_dust = ET.SubElement(bug, 'dust')
                    bug_dust.text = dust
                print(cp, name, hp, dust)
                try:
                    cur.execute("INSERT INTO bugs (name, cp, hp, dust) VALUES (%s, %s, %s, %s)",
                                (name, int(cp), int(hp), int(dust)))
                except ValueError as e:
                    print(e)
                    continue
        conn.commit()
        conn.close()
    print("handle {} files".format(sum))

tree = ET.ElementTree(root)
tree.write("output.xml")
print("Done!")
