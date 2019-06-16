import os

folder_path = '/home/hdc/PycharmProjects/py3cv4/png'


for x, _, z in os.walk(folder_path):
    if len(z) > 0:
        if x[-1:] == "2":
            print("in 2")
            print(z)
            print("###################")

        elif x[-1:] == "3":
            print("in 3")
            print(z)
            print("###################")
        else:
            print("in 4")
            print(z)
            print("###################")




