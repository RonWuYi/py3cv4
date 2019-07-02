import os
import re
import cv2
import pytesseract

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
        if len(my_list) > 0:
            print(input_file for input_file in my_list)
            # for i in my_list:
            #     print(i)
        else:
            pass
    else:
        pass


def read_detection(input_file, box, debug=True, cv_config=psm3_config):
    new_value_list = []
    img = cv2.imread(input_file)
    orig = img.copy()
    for (startX, startY, endX, endY) in box:
        img_show(startX, startY, endX, endY, orig, debug)
        roi = orig[startY:endY, startX:endX]
        text = pytesseract.image_to_string(roi, config=cv_config)
        if debug:
            print(text)
        else:
            pass
        if box.index((startX, startY, endX, endY)) == 0:
            bug_cp = re.search(r'[0-9]*', text).group(0)
            if len(bug_cp) > 0:
                new_value_list.append(bug_cp)
            else:
                new_value_list.append('0')
        elif box.index((startX, startY, endX, endY)) == 1:
            bug_name = re.search(r'[a-z.A-Z]*', text).group(0)
            if len(bug_name) > 0:
                new_value_list.append(bug_name)
            else:
                new_value_list.append('empty')
        elif box.index((startX, startY, endX, endY)) == 2:
            bug_hp = re.search(r'[0-9]*', text).group(0)
            if len(bug_hp) > 0:
                new_value_list.append(bug_hp)
            else:
                new_value_list.append('0')
        else:
            bug_dust = re.search(r'[0-9]*', text).group(0)
            if len(bug_dust) > 0:
                new_value_list.append(bug_dust)
            else:
                new_value_list.append('0')
    if len(new_value_list[0]) > 0 and len(new_value_list[1]) > 0 \
            and len(new_value_list[2]) > 0 and len(new_value_list[3]) > 0:
        pass
    elif len(new_value_list[0]) == 0 or len(new_value_list[1]) == 0 \
            or len(new_value_list[2]) == 0 or len(new_value_list[3]) == 0:
        value_list = gcpIII.detect_document(input_file)
        for idx, value in enumerate(new_value_list):
            if len(value) == 0 and idx == 0:
                if len(value_list[0]) >= 6:
                    bug_cp = value_list[0][:3]
                else:
                    bug_cp = value_list[0]
                if len(bug_cp) > 0:
                    new_value_list[0] = bug_cp
            elif len(value) == 0 and idx == 1:
                bug_name = value_list[1]
                if len(bug_name) > 0:
                    new_value_list[1] = bug_name
            elif len(value) == 0 and idx == 2:
                bug_hp = value_list[2]
                if len(bug_hp) > 0:
                    new_value_list[2] = bug_hp
            elif len(value) == 0 and idx == 0:
                if value_list[3] >= 5:
                    bug_dust = value_list[3][1:4]
                else:
                    bug_dust = value_list[3][1:3]
                if len(bug_dust) > 0:
                    new_value_list[3] = bug_dust
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
            for input_file in z:
                if x[-1:] == "2":
                    sub_list0.append(os.path.join(x, input_file))
                elif x[-1:] == "3":
                    sub_list1.append(os.path.join(x, input_file))
                else:
                    sub_list2.append(os.path.join(x, input_file))
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
                    read_detection(file, fix_box2, debug=false_flag)
            elif walk_folder(root_folder).index(i) == 1:
                for file in i:
                    read_detection(file, fix_box3)
            elif walk_folder(root_folder).index(i) == 1:
                for file in i:
                    read_detection(file, fix_box4, debug=false_flag)
