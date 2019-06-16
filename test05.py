from xml.etree.ElementTree import ElementTree

tree = ElementTree()
tree.parse('/home/hdc/PycharmProjects/py3cv4/xml/result.xml')

root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    # print(child.cp)

# print(root[0][2].text)
for bug in root.findall('bug'):
    cp = bug.find('cp').text
    name = bug.get('name')
    print(name, cp)
# element = root.find()
# tree.write("output.xml")

for bug in root.iter('bug'):
    print(bug.attrib)

# tree.append()