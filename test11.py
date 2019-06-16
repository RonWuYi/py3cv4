import xml.etree.ElementTree as ET

my_xml = '/home/hdc/PycharmProjects/py3cv4/xml/result.xml'
three = ET.parse(my_xml)

root = three.getroot()

for i in range(6):
    bug = ET.SubElement(root, 'bug')

    name = ET.SubElement(bug, 'name{}'.format(i))
    name.text = "name area {}".format(i)

    cp = ET.SubElement(bug, 'cp{}'.format(i))
    cp.text = "cp area {}".format(i)

    hp = ET.SubElement(bug, 'hp{}'.format(i))
    hp.text = "hp area {}".format(i)

    dust = ET.SubElement(bug, 'dust{}'.format(i))
    dust.text = "dust area {}".format(i)

tree = ET.ElementTree(root)
tree.write("page5.xml")
