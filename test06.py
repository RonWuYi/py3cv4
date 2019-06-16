# from xml.etree.ElementTree import ElementTree as ET
# from xml.etree import ElementTree as ET

import xml.etree.ElementTree as ET
import xml.sax

three = ET()
three.parse('/home/hdc/PycharmProjects/py3cv4/xml/example.xml')
root = three.getroot()


a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(b, 'c')
c.text = 'text3'

print(ET.tostring(root))