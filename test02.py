import cv2

img = cv2.imread(r'/home/hdc/PycharmProjects/py3cv4/png/IMG_4156.PNG')

print(type(img))
try:
    from PIL import Image

except ImportError:
    import Image

import pytesseract

tessdata_dir_config = r'--tessdata-dir "/home/hdc/PycharmProjects/py3cv4/data"'
# pytesseract.image_to_string(img, lang='en', config=tessdata_dir_config)

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(img))