import io
import json
import os

from google.cloud import vision
from google.cloud.vision import types
from pprint import pprint

path = '/home/hdc/Downloads/project/py3cv4/png/2/IMG_5183.PNG'

key_path = '/home/hdc/Downloads/project/py3cv4/jsonKey/lyshmily-457c5c843982.json'


def method():
    client = vision.ImageAnnotatorClient()
    file_name = '/home/hdc/Downloads/project/py3cv4/png/2/IMG_5183.PNG'
    # file_name = os.path.join()
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.document_text_detection(image=image)
    labels = response.full_text_annotation
    print('texts:')
    for text in labels:
        print(text.description)


def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    x = []
    for page in response.full_text_annotation.text:
        x.append(page)
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
    print("#######################################################################################")    
    print(''.join(x))
    print("#######################################################################################")
    # pprint(str(response))
    # # data = json.loads(str(response))
    # with open(os.path.join('/home/hdc/Downloads/project/py3cv4/jsonData', 'data2.json'), 'w') as f:
    #     json.dump(json.load(str(response)), f)

    # with open(os.path.join('/home/hdc/Downloads/project/py3cv4/jsonData', 'testdata.txt'), 'w') as f:
    #     f.write(str(response))
    # for k, v in json.loads(str(response)):
    #     if k == "fullTextAnnotation":
    #         print(v)


if __name__ == '__main__':
    # print(os.environ)
    # os.putenv('GOOGLE_APPLICATION_CREDENTIALS', key_path)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
    # os.system('echo $GOOGLE_APPLICATION_CREDENTIALS')
    # print(os.environ)
    detect_document(path)
