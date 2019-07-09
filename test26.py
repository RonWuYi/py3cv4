import shutil
import os


path = '/home/hdc/Downloads/project/py3cv4'



def clean_up(path):
    shutil.rmtree(path=path)


for x, y, z in os.walk(path):
    print(x)
    print(y)
    print(z)
    print('#########################################')