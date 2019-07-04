import datetime
from datetime import date
# for i in datetime.datetime.now():
#     print(i)

print(datetime.datetime.now())
print(type(datetime.datetime.now().isoformat(timespec='seconds')))