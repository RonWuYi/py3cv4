import re

myString="ce66"

x = re.search(r"(\d+)", myString)
# result =x.match(myString)
print(x.group(0))
print(type(x.group(0)))


# this is cp area for 3
startX, startY, endX, endY = 272, 63, 366, 140


##### this is name area ###################
startXn, startYn, endXn, endYn = 242, 513, 396, 570
# enlarge
startXn, startYn, endXn, endYn = 232, 513, 399, 570


# this is cp area for 3
startXc, startYc, endXc, endYc = 272, 63, 366, 140

#enlarge
startXc, startYc, endXc, endYc = 272, 63, 366, 132

# this is cp area for 4
startXc, startYc, endXc, endYc = 258, 63, 380, 132

fix_box3 = [(258, 63, 380, 132), (232, 513, 379, 570), (309, 593, 379, 620), (347, 905, 419, 940)]

# this is cp area for 2
startX, startY, endX, endY = 287, 63, 366, 132


# this is hp area
startXh, startYh, endXh, endYh = 309, 593, 399, 620


# this is dust area
startXd, startYd, endXd, endYd = 351, 905, 419, 940