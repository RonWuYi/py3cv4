import xml.etree.ElementTree as ET

my_xml = '/home/hdc/PycharmProjects/py3cv4/output3.xml'
three = ET.parse(my_xml)

root = three.getroot()

for i in range(6):
    bug = ET.SubElement(root, 'bug')

    name = ET.SubElement(bug, 'name')
    name.text = "name area"

    cp = ET.SubElement(bug, 'cp')
    cp.text = "cp area"

    hp = ET.SubElement(bug, 'hp')
    hp.text = "hp area"

    dust = ET.SubElement(bug, 'dust')
    dust.text = "dust area"

tree = ET.ElementTree(root)
tree.write("page4.xml")
