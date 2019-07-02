GOOGLE_APPLICATION_CREDENTIALS = 'GOOGLE_APPLICATION_CREDENTIALS'
my_xml = '/home/hdc/Downloads/project/py3cv4/xml/result.xml'

key_path = '/home/hdc/Downloads/project/py3cv4/jsonKey/lyshmily-457c5c843982.json'
root_folder = '/home/hdc/Downloads/project/py3cv4/png'
psm3_config = "-l eng --oem 1 --psm 3"
psm8_config = "-l eng --oem 1 --psm 8"

# fix_box2 = [(289, 65, 366, 129), (220, 513, 406, 570), (259, 593, 298, 620), (353, 905, 419, 940)]
fix_box2 = [(289, 65, 366, 129), (220, 513, 406, 570), (259, 593, 298, 620), (347, 905, 419, 940)]
fix_box3 = [(272, 63, 366, 132), (220, 513, 406, 570), (259, 593, 298, 620), (353, 905, 419, 940)]
fix_box4 = [(258, 63, 380, 132), (220, 513, 406, 570), (259, 593, 298, 620), (350, 905, 419, 940)]

true_flag = True
false_flag = False

name, cp, hp, dust = None, None, None, None
data_sum = 0


database = "testdb"
user = "postgres"
password = "postgres"
host = "172.16.66.244"

insert_into_bugs = "INSERT INTO bugs (name, cp, hp, dust) VALUES (%s, %s, %s, %s)"
