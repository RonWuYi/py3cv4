from xml.etree.ElementTree import ElementTree

tree =ElementTree()
tree.parse('/home/hdc/PycharmProjects/py3cv4/xml/result.xml')

root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
# element = root.find()
# tree.write("output.xml")