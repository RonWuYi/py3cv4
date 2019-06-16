import xml.etree.ElementTree as ET

# build a tree structure
root = ET.Element("html")

head = ET.SubElement(root, "head")

title = ET.SubElement(head, "title")
title.text = "Page Title"

cp = ET.SubElement(head, "cp")
cp.text = "cp area"
hp1 = ET.SubElement(head, "hp1")
hp1.text = "hp1 area"
dust = ET.SubElement(head, "dust")
dust.text = "dust area"
body = ET.SubElement(root, "body")
body.set("bgcolor", "#ffffff")

body.text = "Hello, World!"

hp = ET.SubElement(body, "hp")
hp.text = "hp area"

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)
tree.write("page.xhtml")