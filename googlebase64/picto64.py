import os
import base64

file_folder = '/home/hdc/Downloads/project/py3cv4/png/2'

test_file = '/home/hdc/Downloads/project/py3cv4/png/2/IMG_5183.PNG'
# for i in os.listdir(file_folder):
#     print(i)

# for i in os.listdir(file_folder):
#     with open(os.path.join(file_folder, i), 'rb') as image_file:
#         encode_string = base64.b64encode(image_file.read())
#         print("this is file {}".format(i))
#         print(encode_string)
#         print("################################")

with open(test_file, 'rb') as image_file:
    encode_string = base64.b64encode(image_file.read())
    print("this is file {}".format(image_file.name))
    print(encode_string)
    print("################################")
    print(type(encode_string))
    print(encode_string.decode("utf-8"))