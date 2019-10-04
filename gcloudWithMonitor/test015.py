import time

from constant import constant
from threading import Thread

class Test:
    def run(self):
        # start_time = constant.time_string()
        while True:
            print(constant.time_string())
            time.sleep(3)


c = Test()
t = Thread(target=c.run, args=())
t.start()

