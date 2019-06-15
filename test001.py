import re

myString="ce66"

x = re.search(r"(\d+)", myString)
# result =x.match(myString)
print(x.group(0))
print(type(x.group(0)))

##### this is name area ###################
startX, startY, endX, endY = 242, 513, 396, 570


# this is cp area
startX, startY, endX, endY = 272, 63, 366, 140