import os
import io

key_path = "/home/hdc/Downloads/project/py3cv4/jsonKey/lyshmily-457c5c843982.json"


def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)


def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.txt for symbol in word.symbols
                    ])

                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))


if __name__ == '__main__':
    if os.path.isfile(key_path):
        print('pass')
    else:
        print('fail')
    # os.system('export GOOGLE_APPLICATION_CREDENTIALS={}'.format(key_path))
    # implicit()
    # detect_document('/home/hdc/Downloads/project/py3cv4/png/2/IMG_5184.PNG')
