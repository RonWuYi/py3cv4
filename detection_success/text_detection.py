import os
import re
import cv2
import pytesseract

from PIL import Image
from googlebase64 import gcpIII
from util.PyConstant import *
from db.PsyDb import Database

my_db = Database(database, user, password, host)


def img_show(start_x, start_y, end_x, end_y, orig, flag):
    if flag:
        cv2.rectangle(orig, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        cv2.imshow("origional", orig)
        cv2.waitKey(0)
    else:
        pass


def print_values(my_list, flag):
    if flag:
        for i in my_list:
            print(i)
    else:
        pass


def read_detection(file, box, debug=True, cv_config=psm3_config):
    new_value_list = []
    img = cv2.imread(file)
    orig = img.copy()
    for (startX, startY, endX, endY) in box:
        img_show(startX, startY, endX, endY, orig, debug)
        roi = orig[startY:endY, startX:endX]
        text = pytesseract.image_to_string(roi, config=cv_config)
        if debug:
            print(text)
            print(pytesseract.image_to_string(Image.fromarray(roi)))
        else:
            pass
        if box.index((startX, startY, endX, endY)) == 0:
            # cp = text
            cp = re.search(r'[0-9]*', text).group(0)
            new_value_list.append(cp)
        elif box.index((startX, startY, endX, endY)) == 1:
            name = re.search(r'[a-z.A-Z]*', text).group(0)
            new_value_list.append(name)
        elif box.index((startX, startY, endX, endY)) == 2:
            hp = re.search(r'[0-9]*', text).group(0)
            new_value_list.append(hp)
        else:
            dust = re.search(r'[0-9]*', text).group(0)
            new_value_list.append(dust)
    if len(new_value_list[0]) > 0 and len(new_value_list[1]) > 0 \
            and len(new_value_list[2]) > 0 and len(new_value_list[3]) > 0:
        pass
    elif len(new_value_list[0]) > 0 and len(new_value_list[1]) > 0 \
            and len(new_value_list[2]) > 0 and len(new_value_list[3]) > 0:
        value_list = gcpIII.detect_document(os.path.join(x, i))
        for idx, value in enumerate(new_value_list):
            if len(value) == 0 and idx == 0:
                if len(value_list[0]) >= 6:
                    cp = value_list[0][:3]
                else:
                    cp = value_list[0]
                new_value_list[0] = cp
            elif len(value) == 0 and idx == 1:
                name = value_list[1]
                new_value_list[1] = name
            elif len(value) == 0 and idx == 2:
                hp = value_list[2]
                new_value_list[2] = hp
            elif len(value) == 0 and idx == 0:
                if value_list[3] >= 5:
                    dust = value_list[3][1:4]
                else:
                    dust = value_list[3][1:3]
                new_value_list[3] = dust
    print_values(new_value_list, debug)
    my_db.execute(insert_into_bugs, (new_value_list[1], int(new_value_list[0]),
                                     int(new_value_list[2]), int(new_value_list[3])))
    return new_value_list


def walk_folder(path):
    file_list = []
    sub_list0 = []
    sub_list1 = []
    sub_list2 = []
    for x, _, z in os.walk(path):
        if len(z) > 0:
            for i in z:
                if x[-1:] == "2":
                    sub_list0.append(os.path.join(x, i))
                elif x[-1:] == "3":
                    sub_list1.append(os.path.join(x, i))
                else:
                    sub_list2.append(os.path.join(x, i))
    file_list.append(sub_list0)
    file_list.append(sub_list1)
    file_list.append(sub_list2)
    return file_list


if __name__ == '__main__':
    os.environ[GOOGLE_APPLICATION_CREDENTIALS] = key_path
    for i in walk_folder(root_folder):
        if len(i) > 0:
            if walk_folder(root_folder).index(i) == 0:
                for file in i:
                    read_detection(file, fix_box2)
            elif walk_folder(root_folder).index(i) == 1:
                for file in i:
                    read_detection(file, fix_box3)
            elif walk_folder(root_folder).index(i) == 1:
                for file in i:
                    read_detection(file, fix_box4)


