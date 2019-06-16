import xml.etree.ElementTree as ET

root = ET.Element("html")

head = ET.SubElement(root, "head")
title = ET.SubElement(head, "title")
title.text =  "page title"

three = ET.ElementTree(root)
three.write('output3.xml')