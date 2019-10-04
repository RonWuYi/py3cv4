import time

from threading import Thread

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T1-minus', n)
            n -= 1
            time.sleep(5)

class CountdownTask2:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T2-minus', n)
            n -= 1
            time.sleep(5)
tar = []
c1 = CountdownTask()
t1 = Thread(target=c1.run, args=(100,))


c2 = CountdownTask2()
t2 = Thread(target=c2.run, args=(100,))
t1.start()
t2.start()
tar.append(t1)
tar.append(t2)

for tt in tar:
    tt.join()
# c1.terminate() # Signal termination
# c2.terminate() # Signal termination
# t1.join()      # Wait for actual termination (if needed)