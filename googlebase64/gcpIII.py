import io
import os
import string

from google.cloud import vision
from google.cloud.vision import types

root_path = '/home/hdc/Downloads/project/py3cv4/png'
path = '/home/hdc/Downloads/project/py3cv4/png/2/IMG_5183.PNG'
key_path = '/home/hdc/Downloads/project/py3cv4/jsonKey/lyshmily-457c5c843982.json'


def method(file_name):
    client = vision.ImageAnnotatorClient()
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.document_text_detection(image=image)
    my_list = []
    for page in response.full_text_annotation.text:
        my_list.append(page)
    print(my_list)


def single_detect(path):
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)
    # cp = []
    # name = []
    # hp = []
    # dust = []
    my_list = []

    for page in response.full_text_annotation.text:
        my_list.append(page)
    new_list = [x for x in my_list if x in string.ascii_letters or x in string.octdigits or x == '/']
    return new_list


def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)
    cp = []
    name = []
    hp = []
    dust = []
    my_list = []

    for page in response.full_text_annotation.text:
        my_list.append(page)
    new_list = [x for x in my_list if x in string.ascii_letters or x in string.octdigits or x == '/']
    # print(new_list)
    for idx, val in enumerate(new_list):
        if val == 'C' and new_list[idx + 1] == 'P':
            for idx1, val1 in enumerate(new_list[idx + 2:]):
                if val1.isdigit():
                    cp.append(val1)
                # elif len(cp)
                elif len(name) == 0:
                    for idx2, val2 in enumerate(new_list[idx + idx1 + 2:]):
                        if val2.isalpha():
                            name.append(val2)
                        elif val2.isdigit() and len(dust) == 0:
                            continue
                        elif val2.isdigit() and len(dust) > 0:
                            break
                        else:
                            for idx33, val33 in enumerate(new_list[idx + idx1 + idx2 + 2 + 1:]):
                                if val33.isdigit():
                                    hp.append(val33)
                                else:
                                    last_list = new_list[idx + idx1 + idx2 + idx33 + 3:]
                                    for idx3, val3 in enumerate(last_list):
                                        if val3 == 'U' and last_list[idx3 + 1] == 'P':
                                            for idx4, val4 in enumerate(last_list[idx3 + 2:]):
                                                if val4.isdigit():
                                                    dust.append(val4)
                                                else:
                                                    break
                                        elif len(dust) == 0:
                                            continue
                                        elif len(dust) > 0:
                                            break
                                    break
                elif len(name) > 0:
                    break
        elif len(cp) == 0 or len(name) == 0 or len(hp) == 0 or len(dust) == 0:
            continue
        elif len(cp) > 0 and len(name) > 0 and len(hp) > 0 and len(dust) > 0:
            break

    # print("***************************************************************************************")
    # print(''.join(cp))
    # print(''.join(name))
    # print(''.join(hp))
    # print(''.join(dust))
    # print("#######################################################################################")

    return [''.join(cp), ''.join(name), ''.join(hp), ''.join(dust)]


def cp_detect(path, cpleng):
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)
    cp = []
    # name = []
    # hp = []
    # dust = []
    my_list = []

    for page in response.full_text_annotation.text:
        my_list.append(page)
    # new_list = [x for x in my_list if x in string.ascii_letters or x in string.octdigits]
    if False:
        print(my_list)
    for idx, val in enumerate(my_list):
        # if val.isdigit()
        if (val == 'C' or val == 'c') and (my_list[idx + 1] == 'P' or my_list[idx + 1] == 'p'):
            for idx1, val1 in enumerate(my_list[idx + 2:]):
                if val1.isdigit() and len(cp) < cpleng:
                    cp.append(val1)
                elif len(cp) == cpleng:
                    break
        elif len(cp) == cpleng:
            break

            # if len(cp) == cpleng:
            #     break
                # elif len(cp)
        #         elif len(name) == 0:
        #             for idx2, val2 in enumerate(new_list[idx + idx1 + 2:]):
        #                 if val2.isalpha():
        #                     name.append(val2)
        #                 elif val2.isdigit() and len(dust) == 0:
        #                     continue
        #                 elif val2.isdigit() and len(dust) > 0:
        #                     break
        #                 else:
        #                     for idx33, val33 in enumerate(new_list[idx + idx1 + idx2 + 2 + 1:]):
        #                         if val33.isdigit():
        #                             hp.append(val33)
        #                         else:
        #                             last_list = new_list[idx + idx1 + idx2 + idx33 + 3:]
        #                             for idx3, val3 in enumerate(last_list):
        #                                 if val3 == 'U' and last_list[idx3 + 1] == 'P':
        #                                     for idx4, val4 in enumerate(last_list[idx3 + 2:]):
        #                                         if val4.isdigit():
        #                                             dust.append(val4)
        #                                         else:
        #                                             break
        #                                 elif len(dust) == 0:
        #                                     continue
        #                                 elif len(dust) > 0:
        #                                     break
        #                             break
        #         elif len(name) > 0:
        #             break
        # elif len(cp) == 0 or len(name) == 0 or len(hp) == 0 or len(dust) == 0:
        #     continue
        # elif len(cp) > 0 and len(name) > 0 and len(hp) > 0 and len(dust) > 0:
        #     break

    # print("***************************************************************************************")
    # print(''.join(cp))
    # print(''.join(name))
    # print(''.join(hp))
    # print(''.join(dust))
    # print("#######################################################################################")

    return ''.join(cp)


if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
    for x, _, z in os.walk(root_path):
        if len(z) > 0:
            for i in z:
                print("we are working on {}".format(os.path.join(x, i)))
                detect_document(os.path.join(x, i))
