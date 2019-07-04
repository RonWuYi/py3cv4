from util.func import *
from util.PyConstant import name, cp, dust
from db.PsyDb import Database
from selenium import webdriver

if __name__ == '__main__':
    os.environ[GOOGLE_APPLICATION_CREDENTIALS] = key_path
    my_db = Database(database, user, password, host)

    # for i in walk_folder(root_folder):
    #     if len(i) > 0:
    #         if walk_folder(root_folder).index(i) == 0:
    #             for file1 in i:
    #                 read_detection(db=my_db, input_file=file1, box=fix_box2, cp_len=2, debug=false_flag,
    #                                ocr_cfg1=psm7_oem1_number, ocr_cfg2=psm7_oem1_config_words, file_name=file1[-12:])
    #         elif walk_folder(root_folder).index(i) == 1:
    #             for file2 in i:
    #                 read_detection(db=my_db, input_file=file2, box=fix_box3, cp_len=3, debug=false_flag,
    #                                ocr_cfg1=psm7_oem1_number, ocr_cfg2=psm7_oem1_config_words, file_name=file2[-12:])
    #         elif walk_folder(root_folder).index(i) == 2:
    #             for file3 in i:
    #                 read_detection(db=my_db, input_file=file3, box=fix_box4, cp_len=4, debug=false_flag,
    #                                ocr_cfg1=psm7_oem1_number, ocr_cfg2=psm7_oem1_config_words, file_name=file3[-12:])
    #
    driver = webdriver.Firefox(executable_path='/home/hdc/Downloads/project/py3cv4/geckodriver/geckodriver')
    driver.maximize_window()
    driver.get("https://pokeassistant.com/main/ivcalculator")
    # driver.minimize_window()
    cook_accept(driver)
    my_db.execute(select_bugs)
    for i in my_db.fetchall():
        # print(i)
        if false_flag:
            print(i)
            print(type(i[1]))
        if i[0] == name and int(i[1]) <= cp and int(i[2]) >= dust:
            my_db.execute(update_useless_bug, ("true", i[5]))
            my_db.commit()
        elif i[0] == name and int(i[1]) <= cp and int(i[2]) <= dust:
            if do_calculation(driver, name_changed=False, name=i[0],
                              cp=str(i[1]), hp=str(i[2]), dust=str(i[3]), debug=false_flag):
                bug_result = check_results(driver)
                if false_flag:
                    print(bug_result)
                if len(bug_result) == 3:
                    my_db.execute(insert_into_results, (i[0], int(i[1]), int(i[3]), float(bug_result[0]),
                                                        float(bug_result[1]), float(bug_result[2]), i[5]))
                    my_db.execute(update_checked_bug, ("true", i[5]))
                    my_db.commit()
            else:
                print("check {} failed!".format(i[5]))
        elif i[0] != name:
            if do_calculation(driver, name_changed=True, name=i[0],
                              cp=str(i[1]), hp=str(i[2]), dust=str(i[3]), debug=false_flag):
                bug_result = check_results(driver)
                if false_flag:
                    print(bug_result)
                if len(bug_result) == 3:
                    my_db.execute(insert_into_results, (i[0], int(i[1]), int(i[3]), float(bug_result[0]),
                                                        float(bug_result[1]), float(bug_result[2]), i[5]))
                    my_db.execute(update_checked_bug, ("true", i[5]))

                    my_db.commit()
            else:
                print("check {} failed!".format(i[5]))
        name, cp, dust = i[0], int(i[1]), int(i[3])
    driver.quit()
    my_db.exit()
