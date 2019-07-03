import os
import re
import cv2
import pytesseract

from googlebase64 import gcpIII
from util.PyConstant import *
from db.PsyDb import Database
from pathlib import Path


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
        else:
            pass
    else:
        pass


def read_detection(db, input_file, box, debug=True, tesseract_config1=None, tesseract_config2=None):
    new_value_list = []
    img = cv2.imread(input_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filename, gray)
    new_image = cv2.imread(os.path.join(str(Path.cwd()), filename))
    orig = new_image.copy()
    for (startX, startY, endX, endY) in box:
        img_show(startX, startY, endX, endY, orig, debug)
        roi = orig[startY:endY, startX:endX]
        if box.index((startX, startY, endX, endY)) == 0:
            text = pytesseract.image_to_string(roi, config=tesseract_config1)
            print(text)
            bug_cp = re.search(r'[0-9]*', text).group(0)
            new_value_list.append(bug_cp)
        elif box.index((startX, startY, endX, endY)) == 1:
            text = pytesseract.image_to_string(roi, config=tesseract_config2)
            print(text)
            bug_name = re.search(r'[a-z.A-Z]*', text).group(0)
            new_value_list.append(bug_name)
        elif box.index((startX, startY, endX, endY)) == 2:
            text = pytesseract.image_to_string(roi, config=tesseract_config1)
            print(text)
            bug_hp = re.search(r'[0-9]*', text).group(0)
            new_value_list.append(bug_hp)
        else:
            text = pytesseract.image_to_string(roi, config=tesseract_config1)
            print(text)
            bug_dust = text.replace(',', '')
            new_value_list.append(bug_dust)
        if debug:
            print(new_value_list)
    if len(new_value_list[0]) > 0 and len(new_value_list[1]) > 0 \
            and len(new_value_list[2]) > 0 and len(new_value_list[3]) > 0:
        pass
    elif '' in new_value_list:
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
    try:
        db.execute(insert_into_bugs, (new_value_list[1], int(new_value_list[0]),
                                      int(new_value_list[2]), int(new_value_list[3])))
    except Exception as e:
        print(e)
    os.remove(os.path.join(str(Path.cwd()), filename))
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
    my_db = Database(database, user, password, host)
    for i in walk_folder(root_folder):
        if len(i) > 0:
            if walk_folder(root_folder).index(i) == 0:
                for file in i:
                    read_detection(db=my_db, input_file=file, box=fix_box2, debug=false_flag,
                                   tesseract_config1=psm7_oem1_number, tesseract_config2=psm7_oem1_config_words)
                my_db.commit()
            elif walk_folder(root_folder).index(i) == 1:
                for file in i:
                    read_detection(db=my_db, input_file=file, box=fix_box3, debug=false_flag,
                                   tesseract_config1=psm7_oem1_number, tesseract_config2=psm7_oem1_config_words)
                my_db.commit()
            elif walk_folder(root_folder).index(i) == 1:
                for file in i:
                    read_detection(db=my_db, input_file=file, box=fix_box4, debug=false_flag,
                                   tesseract_config1=psm7_oem1_number, tesseract_config2=psm7_oem1_config_words)
                my_db.commit()
    my_db.exit()
