import time
import pyautogui
import psycopg2

from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import TimeoutException


driver = webdriver.Firefox()
driver.maximize_window()

# driver.get("https://www.google.com")
driver.get("https://pokeassistant.com/main/ivcalculator")

print(driver.title)

# global name, cp, hp, dust
insert_into_results = "INSERT INTO results (name, cp, hp, max_rat) VALUES (%s, %s, %s, %s)"


def cook_accept():
    # time.sleep(1)

    gdpr_cookie_accept_button = driver.find_element_by_id("gdpr-cookie-accept")
    gdpr_cookie_accept_button.click()


def do_calculation(name="Buneary", cp="503", hp="80", dust="1600"):
    # input_element = driver.find_element_by_name("q")
    pokemon_name = driver.find_element_by_name("search_pokemon_name")

    pokemon_name.send_keys(name)

    time.sleep(1)
    # pokemon_name = driver.find_element_by_name("search_pokemon_name")
    #
    # pokemon_name.send_keys("503")

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

    # search_dust = driver.find_element_by_name("search_dust")

    search_dust.select_by_value(dust)

    time.sleep(1)
    # search_dust = driver.find_element_by_name("search_dust")
    #
    # search_dust.send_keys("1600")
    #
    # search_dust = driver.find_element_by_name("search_dust")
    #
    # search_dust.send_keys("1600")
    #
    # pyautogui.click()
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
    # time.sleep(1)
    # input_element.submit()
    time.sleep(1)


conn = psycopg2.connect(database="testdb", user="postgres", password="postgres", host="172.16.66.244")
cur = conn.cursor()
cur.execute("SELECT * from bugs where checked = FALSE order by (name, cp) desc;")
# print(cur.fetchone())

# try:
#     WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
#     print(driver.title)
#
# finally:
#     driver.quit()

# driver.quit()


cook_accept()
# do_calculation()

name, cp, hp, dust = None, None, None, None

for i in cur.fetchall():
    print(i)
    print(type(i[1]))

    if i[0] == name and i[1] <= cp and i[2] >= dust:
        continue
    elif i[0] == name and i[1] <= cp and i[2] < dust:
        do_calculation(i[0], str(i[1]), str(i[2]), str(i[3]))
        # do_calculation("Squirtle", "390", "70", "1900")

        my_value = driver.find_element_by_id("possibleCombinationsStringmax")

        print(my_value.text)
        # for elem in my_value:
        #     print(elem.text)

        max_rate = my_value.text[my_value.text.index(":")+2:]
        print(my_value.text[my_value.text.index(":")+2:])
        print(type(my_value.text[my_value.text.index(":")+2:]))

        # print(int(my_value.text[my_value.text.index(":")+2:]))

        new_max_rate = float(max_rate.strip('%'))/100.0
        name, cp, hp, dust = i[0], str(i[1]), str(i[2]), str(i[3])

        cur.execute(insert_into_results, (name, cp, dust, new_max_rate))
        # cur.commite

        if new_max_rate > 0.89:
            print(new_max_rate)
        else:
            pass

