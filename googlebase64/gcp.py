import io
import json
import os

from google.cloud import vision
from google.cloud.vision import types
from pprint import pprint
root_path = '/home/hdc/Downloads/project/py3cv4/png'
path = '/home/hdc/Downloads/project/py3cv4/png/2/IMG_5183.PNG'

key_path = '/home/hdc/Downloads/project/py3cv4/jsonKey/lyshmily-457c5c843982.json'


def method(file_name):
    client = vision.ImageAnnotatorClient()
    # file_name = '/home/hdc/Downloads/project/py3cv4/png/2/IMG_5183.PNG'
    # file_name = os.path.join()
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.document_text_detection(image=image)
    labels = response.full_text_annotation
    # print('texts:')
    # for text in labels:
    #     print(text.description)
    my_list = []
    for page in response.full_text_annotation.text:
        my_list.append(page)
    print(my_list)


def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    my_list = []
    for page in response.full_text_annotation.text:
        my_list.append(page)
        # print(page.text)

        # for block in page.blocks:
        #     # print(block.)
        #     # print(block.text)
        #     print('\nBlock confidence: {}\n'.format(block.confidence))
        #
        #     for paragraph in block.paragraphs:
        #         print('Paragraph confidence: {}'.format(
        #             paragraph.confidence))
        #
        #         for word in paragraph.words:
        #             word_text = ''.join([
        #                 symbol.text for symbol in word.symbols
        #             ])
        #             print('Word text: {} (confidence: {})'.format(
        #                 word_text, word.confidence))
        #
        #             for symbol in word.symbols:
        #                 print('\tSymbol: {} (confidence: {})'.format(
        #                     symbol.text, symbol.confidence))

    # print(my_list)
    # print("#######################################################################################")
    # print(''.join(my_list))

    cp = []
    name = []
    hp = []
    dust = []
    # number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # for idx, val in enumerate(my_list):
    #     if val == 'C' and my_list[idx + 1] == 'P':
    #         for idx1, val1 in enumerate(my_list[idx + 2:]):
    #             if val1 != '\n':
    #                 cp.append(val1)
    #             else:
    #                 flag = 0
    #                 for idx2, val2 in enumerate(my_list[idx + idx1 + 2:]):
    #                     if val2 != '\n':
    #                         name.append(val2)
    #                     else:
    #                         flag += 1
    #                         if flag == 2:
    #                             for idx3, val3 in enumerate(my_list[idx + idx1 + idx2 + 3:]):
    #                                 if val3 != '\n' and val3 != ' ' and val3 != '/':
    #                                     hp.append(val3)
    #                                 elif val3 == ' ' and my_list[idx + idx1 + idx2 + idx3 + 2] == '/':
    #                                     break
    #                             break
    #                         else:
    #                             continue
    #                 break
    #
    #         break

    for idx, val in enumerate(my_list):
        if val == 'C' and my_list[idx + 1] == 'P':
            for idx1, val1 in enumerate(my_list[idx + 2:]):
                if val1.isdigit():
                    cp.append(val1)
                else:
                    flag = 0
                    for idx2, val2 in enumerate(my_list[idx + idx1 + 2:]):
                        if val2.isalpha():
                            name.append(val2)
                        else:
                            flag += 1
                            if flag == 2:
                                for idx3, val3 in enumerate(my_list[idx + idx1 + idx2 + 3:]):
                                    # if val3 != '\n' and val3 != ' ' and val3 != '/':
                                    if val3.isdigit():
                                        hp.append(val3)
                                    elif val3 == ' ' and my_list[idx + idx1 + idx2 + idx3 + 2] == '/':
                                        new_lsit = my_list[idx + idx1 + idx2 + idx3 + 3:]
                                        for idx4, val4 in enumerate(my_list[idx + idx1 + idx2 + idx3 + 3:]):
                                            if val4 == ' ' and new_lsit[idx4 + 1] == 'U' and new_lsit[idx4 + 2] == 'P':
                                                flagI = 0
                                                for idx5, val5 in enumerate(my_list[idx + idx1 +
                                                                                    idx2 + idx3 + idx4 + 3 + 2 + 1:]):
                                                    # if val5 != '\n' and val5 != ',':
                                                    if val5.isdigit():
                                                        dust.append(val5)
                                                    else:
                                                        flagI += 1
                                                        if flagI >= 3:
                                                            break
                                                        else:
                                                            continue
                                                # pass]
                                                # break
                                                break
                                        break
                                break
                            else:
                                continue
                    break

            break
    print("#######################################################################################")
    if len(cp) == 0 or len(name) == 0 or len(hp) == 0 or len(dust) == 0:
        print(my_list)
    print("***************************************************************************************")
    print(''.join(cp))
    print(''.join(name))
    print(''.join(hp))
    print(''.join(dust))
    # print(len(x))
    print("#######################################################################################")
    # # pprint(str(response))
    # # # data = json.loads(str(response))
    # # with open(os.path.join('/home/hdc/Downloads/project/py3cv4/jsonData', 'data2.json'), 'w') as f:
    # #     json.dump(json.load(str(response)), f)
    #
    # # with open(os.path.join('/home/hdc/Downloads/project/py3cv4/jsonData', 'testdata.txt'), 'w') as f:
    # #     f.write(str(response))
    # # for k, v in json.loads(str(response)):
    # #     if k == "fullTextAnnotation":
    # #         print(v)


if __name__ == '__main__':
    # print(os.environ)
    # os.putenv('GOOGLE_APPLICATION_CREDENTIALS', key_path)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
    # os.system('echo $GOOGLE_APPLICATION_CREDENTIALS')
    # print(os.environ)
    for x, _, z in os.walk(root_path):
        if len(z) > 0:
            for i in z:
                print("we are working on {}".format(os.path.join(x, i)))
                detect_document(os.path.join(x, i))
