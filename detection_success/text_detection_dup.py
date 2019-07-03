import os
import cv2
import pytesseract

from googlebase64 import gcpIII
from util.PyConstant import *
from db.PsyDb import Database
from pathlib import Path

import time
import pyautogui

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://pokeassistant.com/main/ivcalculator")
insert_into_results = "INSERT INTO results (name, cp, hp, max_rat) VALUES (%s, %s, %s, %s)"


def img_show(start_x, start_y, end_x, end_y, orig, flag):
    if flag:
        cv2.rectangle(orig, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        cv2.imshow("origional", orig)
        cv2.waitKey(0)
    else:
        pass


def img_show_block(orig, flag):
    if flag:
        # cv2.rectangle(orig, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
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


def read_detection(db, input_file, box, cpleng, debug=True, tesseract_config1=None, tesseract_config2=None):
    new_value_list = []
    img = cv2.imread(input_file)
    # old_orig = img.copy()
    print("handle file {}".format(input_file))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filename, gray)
    new_image = cv2.imread(os.path.join(str(Path.cwd()), filename))
    orig = new_image.copy()
    for (startX, startY, endX, endY) in box:
        img_show(startX, startY, endX, endY, orig, debug)
        roi = orig[startY:endY, startX:endX]
        img_show_block(roi, debug)
        if box.index((startX, startY, endX, endY)) == 0:
            # test
            value_list = gcpIII.cp_detect(input_file, cpleng)
            bug_cp = value_list
            print(bug_cp)
            new_value_list.append(bug_cp)

        elif box.index((startX, startY, endX, endY)) == 1:

            tmp_list1 = []
            tmp_list2 = []
            text = pytesseract.image_to_string(roi, config=tesseract_config2)
            for i in text:
                if i.isalpha():
                    tmp_list1.append(i)
            bug_name = ''.join(tmp_list1)

            if len(bug_name) > 0:
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
                print(bug_name)

        elif box.index((startX, startY, endX, endY)) == 2:

            tmp_list1 = []
            tmp_list2 = []
            text = pytesseract.image_to_string(roi, config=tesseract_config1)
            for i in text:
                if i.isnumeric():
                    tmp_list1.append(i)
            bug_hp = ''.join(tmp_list1)

            # bug_cp = re.search(r'[0-9]*', text).group(0)

            if len(bug_hp) > 0:
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
                print(bug_hp)

        else:

            tmp_list1 = []
            tmp_list2 = []
            text = pytesseract.image_to_string(roi, config=tesseract_config1)
            for i in text:
                if i.isnumeric():
                    tmp_list1.append(i)
            bug_dust = ''.join(tmp_list1)

            if len(bug_dust) > 0:
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
                print(bug_dust)

        if debug:
            print(new_value_list)
    print("####################################################################################")
    try:
        db.execute(insert_into_bugs, (new_value_list[1], int(new_value_list[0]),
                                      int(new_value_list[2]), int(new_value_list[3])))
    except Exception as e:
        print(e)
    db.commit()
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
                elif x[-1:] == "4":
                    sub_list2.append(os.path.join(x, input_file))
    file_list.append(sub_list0)
    file_list.append(sub_list1)
    file_list.append(sub_list2)
    return file_list


def check_results():
    my_value_max = driver.find_element_by_id("possibleCombinationsStringmax")
    my_value_avg = driver.find_element_by_id("possibleCombinationsStringavg")
    my_value_min = driver.find_element_by_id("possibleCombinationsStringmin")
    # print(my_value.text)
    # for elem in my_value:
    #     print(elem.text)
    max_rate = my_value_max.text[my_value_max.text.index(":") + 2:]
    print(my_value_max.text[my_value_max.text.index(":") + 2:])
    print(type(my_value_max.text[my_value_max.text.index(":") + 2:]))
    # print(int(my_value.text[my_value.text.index(":")+2:]))
    new_max_rate = float(max_rate.strip('%')) / 100.0

    avg_rate = my_value_avg.text[my_value_avg.text.index(":") + 2:]
    print(my_value_avg.text[my_value_avg.text.index(":") + 2:])
    print(type(my_value_avg.text[my_value_avg.text.index(":") + 2:]))
    # print(int(my_value.text[my_value.text.index(":")+2:]))
    new_avg_rate = float(avg_rate.strip('%')) / 100.0

    min_rate = my_value_min.text[my_value_min.text.index(":") + 2:]
    print(my_value_min.text[my_value_min.text.index(":") + 2:])
    print(type(my_value_min.text[my_value_min.text.index(":") + 2:]))
    # print(int(my_value.text[my_value.text.index(":")+2:]))
    new_min_rate = float(min_rate.strip('%')) / 100.0

    return [new_max_rate, new_avg_rate, new_min_rate]


def cook_accept():
    gdpr_cookie_accept_button = driver.find_element_by_id("gdpr-cookie-accept")
    gdpr_cookie_accept_button.click()


def do_calculation(name="Buneary", cp="503", hp="80", dust="1600"):
    pokemon_name = driver.find_element_by_name("search_pokemon_name")
    pokemon_name.send_keys(name)
    time.sleep(1)
    search_cp = driver.find_element_by_name("search_cp")
    search_cp.send_keys(cp)
    time.sleep(1)
    search_hp = driver.find_element_by_name("search_hp")
    xy = pokemon_name.location
    print(xy.keys())
    print(xy.values())
    print(xy['x'])
    print(type(xy['x']))
    print(xy['y'])
    print(type(xy['y']))
    x, y = xy['x'], xy['y']
    search_hp.send_keys(hp)
    time.sleep(1)
    search_dust = Select(driver.find_element_by_name("search_dust"))
    search_dust.select_by_value(dust)
    time.sleep(1)
    input_element = None
    try:
        input_element = driver.find_element_by_id("calculatebtn")
    except Exception as e:
        print(e)
    time.sleep(1)
    pyautogui.click(x + 75, y + 91)
    time.sleep(1)
    pyautogui.moveTo(x + 126, y + 182, 0.5)
    time.sleep(0.5)
    pyautogui.click(x + 126, y + 182)
    time.sleep(1)
    input_element.click()
    time.sleep(1)
    new_rate = check_results()
    return new_rate


if __name__ == '__main__':
    os.environ[GOOGLE_APPLICATION_CREDENTIALS] = key_path
    my_db = Database(database, user, password, host)
    for i in walk_folder(root_folder):
        if len(i) > 0:
            if walk_folder(root_folder).index(i) == 0:
                for file1 in i:
                    read_detection(db=my_db, input_file=file1, box=fix_box2, cpleng=2, debug=false_flag,
                                   tesseract_config1=psm7_oem1_number, tesseract_config2=psm7_oem1_config_words)
                # my_db.commit()
            elif walk_folder(root_folder).index(i) == 1:
                for file2 in i:
                    read_detection(db=my_db, input_file=file2, box=fix_box3, cpleng=3, debug=false_flag,
                                   tesseract_config1=psm7_oem1_number, tesseract_config2=psm7_oem1_config_words)
                # my_db.commit()
            elif walk_folder(root_folder).index(i) == 2:
                for file3 in i:
                    read_detection(db=my_db, input_file=file3, box=fix_box4, cpleng=4, debug=false_flag,
                                   tesseract_config1=psm7_oem1_number, tesseract_config2=psm7_oem1_config_words)

    my_db.execute("SELECT * from bugs where checked = FALSE order by (name, cp) desc;")
    cook_accept()
    name, cp, hp, dust = None, None, None, None

    for i in my_db.fetchall():
        print(i)
        print(type(i[1]))

        if i[0] == name and i[1] <= cp and i[2] >= dust:
            continue
        elif i[0] == name and i[1] <= cp and i[2] < dust:
            do_calculation(i[0], str(i[1]), str(i[2]), str(i[3]))
            my_value = driver.find_element_by_id("possibleCombinationsStringmax")

            print(my_value.text)
            # for elem in my_value:
            #     print(elem.text)

            max_rate = my_value.text[my_value.text.index(":") + 2:]
            print(my_value.text[my_value.text.index(":") + 2:])
            print(type(my_value.text[my_value.text.index(":") + 2:]))

            # print(int(my_value.text[my_value.text.index(":")+2:]))

            new_max_rate = float(max_rate.strip('%')) / 100.0
            name, cp, hp, dust = i[0], str(i[1]), str(i[2]), str(i[3])

            my_db.execute(insert_into_results, (name, cp, dust, new_max_rate))
    my_db.exit()
