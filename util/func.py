import os
import cv2
import time
import shutil
import pyautogui
import pytesseract

from pathlib import Path
from util.PyConstant import *
from datetime import datetime
from googlebase64 import gcpIII
from selenium.webdriver.support.ui import Select


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'PNG'}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def img_show(start_x, start_y, end_x, end_y, orig, flag):
    if flag:
        cv2.rectangle(orig, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        cv2.imshow("origional", orig)
        cv2.waitKey(0)
    else:
        pass


def img_show_block(orig, flag):
    if flag:
        cv2.imshow("origional", orig)
        cv2.waitKey(0)


def print_values(my_list, flag):
    if flag:
        if len(my_list) > 0:
            print(input_file for input_file in my_list)
        else:
            pass
    else:
        pass


def read_detection(db, input_file, box, cp_len, file_name, debug=True,
                   ocr_cfg1=None, ocr_cfg2=None):
    new_value_list = []
    img = cv2.imread(input_file)
    if debug:
        print("handle file {}".format(input_file))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(fixed_test_name, gray)
    new_image = cv2.imread(os.path.join(str(Path.cwd()), fixed_test_name))
    orig = new_image.copy()
    for (startX, startY, endX, endY) in box:
        img_show(startX, startY, endX, endY, orig, debug)
        roi = orig[startY:endY, startX:endX]
        img_show_block(roi, debug)
        if box.index((startX, startY, endX, endY)) == 0:
            value_list = gcpIII.cp_detect(input_file, cp_len)
            bug_cp = value_list
            if debug:
                print(bug_cp)
            new_value_list.append(bug_cp)
        elif box.index((startX, startY, endX, endY)) == 1:
            tmp_list1 = []
            tmp_list2 = []
            text = pytesseract.image_to_string(roi, config=ocr_cfg2)
            for i in text:
                if i.isalpha():
                    tmp_list1.append(i)
            bug_name = ''.join(tmp_list1)
            if len(bug_name) > 0:
                if debug:
                    print(bug_name)
                new_value_list.append(bug_name)
            else:
                cv2.imwrite(tmp_filename, roi)
                value_list = gcpIII.single_detect(os.path.join(str(Path.cwd()), tmp_filename))
                os.remove(os.path.join(str(Path.cwd()), tmp_filename))
                for i in value_list:
                    if i.isalpha():
                        tmp_list2.append(i)
                bug_name = ''.join(tmp_list2)
                new_value_list.append(bug_name)
                if debug:
                    print(bug_name)
        elif box.index((startX, startY, endX, endY)) == 2:
            tmp_list1 = []
            tmp_list2 = []
            text = pytesseract.image_to_string(roi, config=ocr_cfg1)
            for i in text:
                if i.isnumeric():
                    tmp_list1.append(i)
            bug_hp = ''.join(tmp_list1)
            if len(bug_hp) > 0:
                if debug:
                    print(bug_hp)
                new_value_list.append(bug_hp)
            else:
                cv2.imwrite(tmp_filename, roi)
                value_list = gcpIII.single_detect(os.path.join(str(Path.cwd()), tmp_filename))
                os.remove(os.path.join(str(Path.cwd()), tmp_filename))
                for i in value_list:
                    if i.isnumeric():
                        tmp_list2.append(i)
                bug_hp = ''.join(tmp_list2)
                new_value_list.append(bug_hp)
                if debug:
                    print(bug_hp)
        else:
            tmp_list1 = []
            tmp_list2 = []
            text = pytesseract.image_to_string(roi, config=ocr_cfg1)
            for i in text:
                if i.isnumeric():
                    tmp_list1.append(i)
            bug_dust = ''.join(tmp_list1)

            if len(bug_dust) > 0:
                if debug:
                    print(bug_dust)
                new_value_list.append(bug_dust)
            else:
                cv2.imwrite(tmp_filename, roi)
                value_list = gcpIII.single_detect(os.path.join(str(Path.cwd()), tmp_filename))
                os.remove(os.path.join(str(Path.cwd()), tmp_filename))
                for i in value_list:
                    if i.isnumeric():
                        tmp_list2.append(i)
                bug_dust = ''.join(tmp_list2)
                new_value_list.append(bug_dust)
                if debug:
                    print(bug_dust)

        if debug:
            print(new_value_list)
            print("####################################################################################")
    try:
        db.execute(insert_into_files, (file_name, datetime.now().isoformat(timespec='seconds')))
        db.execute(insert_into_bugs, (new_value_list[1], int(new_value_list[0]),
                                      int(new_value_list[2]), int(new_value_list[3]), file_name))
    except Exception as e:
        print(e)
    db.commit()
    os.remove(os.path.join(str(Path.cwd()), fixed_test_name))
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
                elif x[-1:] == "4":
                    sub_list2.append(os.path.join(x, input_file))
    file_list.append(sub_list0)
    file_list.append(sub_list1)
    file_list.append(sub_list2)
    return file_list


def check_results(test_driver, debug=false_flag):
    try:
        my_value_max = test_driver.find_element_by_id("possibleCombinationsStringmax")
        my_value_avg = test_driver.find_element_by_id("possibleCombinationsStringavg")
        my_value_min = test_driver.find_element_by_id("possibleCombinationsStringmin")

        max_rate = my_value_max.text[my_value_max.text.index(":") + 2:]
        if debug:
            print(my_value_max.text[my_value_max.text.index(":") + 2:])
            print(type(my_value_max.text[my_value_max.text.index(":") + 2:]))

        new_max_rate = float(max_rate.strip('%')) / 100.0

        avg_rate = my_value_avg.text[my_value_avg.text.index(":") + 2:]
        if debug:
            print(my_value_avg.text[my_value_avg.text.index(":") + 2:])
            print(type(my_value_avg.text[my_value_avg.text.index(":") + 2:]))

        new_avg_rate = float(avg_rate.strip('%')) / 100.0

        min_rate = my_value_min.text[my_value_min.text.index(":") + 2:]
        if debug:
            print(my_value_min.text[my_value_min.text.index(":") + 2:])
            print(type(my_value_min.text[my_value_min.text.index(":") + 2:]))
        new_min_rate = float(min_rate.strip('%')) / 100.0
        return [new_max_rate, new_avg_rate, new_min_rate]
    except Exception as e:
        print(e)
        return []


def cook_accept(test_driver):
    gdpr_cookie_accept_button = test_driver.find_element_by_id("gdpr-cookie-accept")
    gdpr_cookie_accept_button.click()


def do_calculation(test_driver, name_changed=True, name="Buneary", cp="503", hp="80", dust="1600", debug=false_flag):
    time.sleep(0.5)
    try:
        pokemon_name = test_driver.find_element_by_name("search_pokemon_name")
        search_cp = test_driver.find_element_by_name("search_cp")
        search_hp = test_driver.find_element_by_name("search_hp")
        search_dust = Select(test_driver.find_element_by_name("search_dust"))
    except Exception as e:
        print(e)
        return false_flag
    xy = pokemon_name.location
    x, y = xy['x'], xy['y']
    if name_changed:
        time.sleep(0.5)
        pokemon_name.send_keys(name)
        time.sleep(1)
        search_cp.send_keys(cp)
        time.sleep(1)
        if debug:
            print(xy.keys())
            print(xy.values())
            print(xy['x'])
            print(type(xy['x']))
            print(xy['y'])
            print(type(xy['y']))
        search_hp.send_keys(hp)
        time.sleep(1)
        try:
            search_dust.select_by_value(dust)
        except Exception as e:
            print(e)
            return false_flag
        time.sleep(1)
        input_element = None
        try:
            input_element = test_driver.find_element_by_id("calculatebtn")
        except Exception as e:
            print(e)
            return false_flag
        time.sleep(1)
        pyautogui.click(x + 75, y + 91)
        time.sleep(1)
        pyautogui.moveTo(x + 126, y + 185, 0.5)
        time.sleep(0.5)
        pyautogui.click(x + 126, y + 182)
        time.sleep(1)
        input_element.click()
        time.sleep(1)
    else:
        time.sleep(0.5)
        search_cp.send_keys(cp)
        time.sleep(1)
        if debug:
            print(xy.keys())
            print(xy.values())
            print(xy['x'])
            print(type(xy['x']))
            print(xy['y'])
            print(type(xy['y']))
        search_hp.send_keys(hp)
        time.sleep(1)
        try:
            search_dust.select_by_value(dust)
        except Exception as e:
            print(e)
            return false_flag
        time.sleep(1)
        input_element = None
        try:
            input_element = test_driver.find_element_by_id("calculatebtn")
        except Exception as e:
            print(e)
            return false_flag
        # time.sleep(1)
        # pyautogui.click(x + 75, y + 91)
        # time.sleep(1)
        # pyautogui.moveTo(x + 126, y + 182, 0.5)
        # time.sleep(0.5)
        # pyautogui.click(x + 126, y + 182)
        time.sleep(1)
        input_element.click()
        time.sleep(1)
    try:
        test_driver.find_element_by_link_text("No combinations found. Are you sure you have not powered-up before?")
        flag = false_flag
    except Exception as e:
        flag = true_flag
        if debug:
            print(e)
    return flag


def clean_up(path):
    shutil.rmtree(path=path)
