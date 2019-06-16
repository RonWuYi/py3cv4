from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

three = ElementTree()

top = Element('top')

child = SubElement(top, 'child')

child.text = 'test child'


print(tostring(top))

three.write('output1.xml')