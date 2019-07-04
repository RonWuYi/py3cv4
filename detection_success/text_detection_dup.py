from util.func import *
from util.PyConstant import name, cp, dust
from db.PsyDb import Database
from selenium import webdriver


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://pokeassistant.com/main/ivcalculator")


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

    my_db.execute(select_bugs)
    cook_accept()

    for i in my_db.fetchall():
        print(i)
        print(type(i[1]))

        if i[0] == name and i[1] <= cp and i[2] >= dust:
            continue
        elif i[0] == name and i[1] <= cp and i[2] < dust:
            do_calculation(i[0], str(i[1]), str(i[2]), str(i[3]))
            my_value = driver.find_element_by_id("possibleCombinationsStringmax")
            print(my_value.text)
            max_rate = my_value.text[my_value.text.index(":") + 2:]
            print(my_value.text[my_value.text.index(":") + 2:])
            print(type(my_value.text[my_value.text.index(":") + 2:]))
            new_max_rate = float(max_rate.strip('%')) / 100.0
            name, cp, hp, dust = i[0], str(i[1]), str(i[2]), str(i[3])

            my_db.execute(insert_into_results, (name, cp, dust, new_max_rate))
    my_db.exit()
