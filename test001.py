import re

myString="ce66"

x = re.search(r"(\d+)", myString)
# result =x.match(myString)
print(x.group(0))
print(type(x.group(0)))