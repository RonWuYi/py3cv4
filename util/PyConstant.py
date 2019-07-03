GOOGLE_APPLICATION_CREDENTIALS = 'GOOGLE_APPLICATION_CREDENTIALS'
my_xml = '/home/hdc/Downloads/project/py3cv4/xml/result.xml'

key_path = '/home/hdc/Downloads/project/py3cv4/jsonKey/lyshmily-457c5c843982.json'
root_folder = '/home/hdc/Downloads/project/py3cv4/png'
root_home = '/home/hdc/PycharmProjects/py3cv4/png'
psm3_config = "-l eng --oem 1 --psm 3"
psm8_config = "-l eng --oem 1 --psm 8"

psm_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
osm_list = [1, 2]

psm_oem_number = '-l eng --psm {} --oem {} -c tessedit_char_whitelist=0123456789'
psm_config_words = '-l eng --psm {} --oem {} -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# psm_oem_number = '--psm {} --oem {} -c tessedit_char_whitelist=0123456789'
# psm_config_words = '--psm {} --oem {} -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
# psm0_oem1_number = '--psm 0 --oem 3 -c tessedit_char_whitelist=0123456789'
psm1_config_number = '--psm 1 --oem 3 -c tessedit_char_whitelist=0123456789'
psm2_config_number = '--psm 2 --oem 3 -c tessedit_char_whitelist=0123456789'
psm3_config_number = '--psm 3 --oem 3 -c tessedit_char_whitelist=0123456789'
psm4_config_number = '--psm 4 --oem 3 -c tessedit_char_whitelist=0123456789'
psm5_config_number = '--psm 5 --oem 3 -c tessedit_char_whitelist=0123456789'
psm6_config_number = '--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
psm7_config_number = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789'


psm7_oem1_number = '--psm 7 --oem 1 -c tessedit_char_whitelist=0123456789'
psm7_oem1_config_words = '--psm 7 --oem 1 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

psm8_config_number = '--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789'
psm9_config_number = '--psm 9 --oem 3 -c tessedit_char_whitelist=0123456789'
psm10_config_number = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
psm11_config_number = '--psm 11 --oem 3 -c tessedit_char_whitelist=0123456789'
psm12_config_number = '--psm 12 --oem 3 -c tessedit_char_whitelist=0123456789'
psm13_config_number = '--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789'


psm7_config_words = '--psm 7 --oem 3 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
psm8_config_words2 = '-l eng --psm 13 --oem 1'
# startX, startY, endX, endY
# fix_box2 = [(289, 65, 366, 129), (220, 513, 406, 570), (259, 593, 298, 620), (353, 905, 419, 940)]
fix_box2 = [(289, 65, 352, 129), (200, 513, 416, 570), (259, 593, 298, 620), (347, 905, 405, 940)]
fix_box3 = [(272, 63, 366, 132), (200, 513, 416, 570), (259, 593, 296, 620), (346, 905, 419, 940)]
fix_box4 = [(258, 63, 380, 132), (200, 513, 416, 570), (259, 593, 298, 620), (343, 905, 419, 940)]

true_flag = True
false_flag = False

name, cp, hp, dust = None, None, None, None
data_sum = 0


database = "testdb"
user = "postgres"
password = "postgres"
host = "172.16.66.244"

insert_into_bugs = "INSERT INTO bugs (name, cp, hp, dust) VALUES (%s, %s, %s, %s)"

filename = "My_test.PNG"
