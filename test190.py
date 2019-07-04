import time
import datetime

from db.PsyDb import Database
from util import PyConstant


test_db = Database(PyConstant.database, PyConstant.user, PyConstant.password, PyConstant.host)

# intsert_file = "insert into files VALUES (%s, %s)"
# test_db.execute(intsert_file, ("test_file2", str(datetime.datetime.now())[:19]))
# test_db.execute(intsert_file, ("test_file3", datetime.datetime.now().isoformat(timespec='seconds')))
# time.sleep(60)
try:
    test_db.execute("select file_name from files;")
    # print(test_db.fetchall())
    print([x[0] for x in test_db.fetchall()])
except Exception as e:
    print(e)
# test_db.commit()
test_db.exit()
# print(str(datetime.datetime.now())[:19])
# print(type(datetime.datetime.now()))
