from util.func import *
from db.PsyDb import Database
from selenium import webdriver

if __name__ == '__main__':
    os.environ[GOOGLE_APPLICATION_CREDENTIALS] = key_path
    my_db = Database(database, user, password, host)
    # for i in walk_folder(root_folder):
    #     if len(i) > 0:
    #         for file1 in i:
    #             print(file1[-12:])

    for i in walk_folder(root_folder):
        if len(i) > 0:
            if walk_folder(root_folder).index(i) == 0:
                for file1 in i:
                    read_detection(db=my_db, input_file=file1, box=fix_box2, cp_len=2, debug=false_flag,
                                   ocr_cfg1=psm7_oem1_number, ocr_cfg2=psm7_oem1_config_words, file_name=file1[-12:])
            elif walk_folder(root_folder).index(i) == 1:
                for file2 in i:
                    read_detection(db=my_db, input_file=file2, box=fix_box3, cp_len=3, debug=false_flag,
                                   ocr_cfg1=psm7_oem1_number, ocr_cfg2=psm7_oem1_config_words, file_name=file2[-12:])
            elif walk_folder(root_folder).index(i) == 2:
                for file3 in i:
                    read_detection(db=my_db, input_file=file3, box=fix_box4, cp_len=4, debug=false_flag,
                                   ocr_cfg1=psm7_oem1_number, ocr_cfg2=psm7_oem1_config_words, file_name=file3[-12:])

    # my_db.execute(select_bugs)
    # cook_accept()
    # test_driver = webdriver.Firefox(executable_path='/home/hdc/Downloads/project/py3cv4/geckodriver/geckodriver')
    # test_driver.maximize_window()
    # test_driver.get("https://pokeassistant.com/main/ivcalculator")
    # for i in my_db.fetchall():
    #     print(i)
    #     print(type(i[1]))
    #     if i[0] == name and i[1] <= cp and i[2] >= dust:
    #         continue
    #     elif i[0] == name and i[1] <= cp and i[2] < dust:
    #         do_calculation(i[0], str(i[1]), str(i[2]), str(i[3]))
    #         my_value = driver.find_element_by_id("possibleCombinationsStringmax")
    #         print(my_value.text)
    #         max_rate = my_value.text[my_value.text.index(":") + 2:]
    #         print(my_value.text[my_value.text.index(":") + 2:])
    #         print(type(my_value.text[my_value.text.index(":") + 2:]))
    #         new_max_rate = float(max_rate.strip('%')) / 100.0
    #         name, cp, hp, dust = i[0], str(i[1]), str(i[2]), str(i[3])
    #         my_db.execute(insert_into_results, (name, cp, dust, new_max_rate))
    my_db.exit()
