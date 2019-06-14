from imutils.object_detection import non_max_suppression
import numpy as np
import pytesseract
import argparse
import cv2
import time
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
	help="path to input image")
ap.add_argument("-east", "--east", type=str,
	help="path to input EAST text detector")
ap.add_argument("-c", "--min-confidence", type=float, default=0.5,
	help="minimum probability required to inspect a region")
ap.add_argument("-w", "--width", type=int, default=320,
	help="nearest multiple of 32 for resized width")
ap.add_argument("-e", "--height", type=int, default=320,
	help="nearest multiple of 32 for resized height")
ap.add_argument("-p", "--padding", type=float, default=0.0,
	help="amount of padding to add to each border of ROI")
args = vars(ap.parse_args())
path = "/home/hdc/PycharmProjects/py3cv4/png"
file_path = '/home/hdc/PycharmProjects/py3cv4/png/IMG_4158.PNG'
# hasimage = True
# while hasimage:

results = []
real_results = []

for i in os.listdir(path):
	if os.path.isfile(os.path.join(path, i)):
		current_image = os.path.join(path, i)
	# if
		image = cv2.imread(current_image)
		orig = image.copy()
		(origH, origW) = image.shape[:2]

		# set the new width and height and then determine the ratio in change
		# for both the width and height
		(newW, newH) = (args["width"], args["height"])
		rW = origW / float(newW)
		rH = origH / float(newH)

		# resize the image and grab the new image dimensions
		image = cv2.resize(image, (newW, newH))
		(H, W) = image.shape[:2]

		fake_box = [(244, 63, 366, 120), (234, 507, 426, 560), (304, 590, 396, 620), (350, 898, 436, 940)]
		# loop over the bounding boxes
		for (startX, startY, endX, endY) in fake_box:
			roi = orig[startY:endY, startX:endX]
			config = ("-l eng --oem 1 --psm 3")
			text = pytesseract.image_to_string(roi, config=config)

			# add the bounding box coordinates and OCR'd text to the list
			# of results
			results.append(((startX, startY, endX, endY), text))
			real_results.append(text)
		# sort the results bounding box coordinates from top to bottom
		results = sorted(results, key=lambda r:r[0][1])


# print(results)
print(real_results)
print(len(real_results)/4)
# loop over the results


# for ((startX, startY, endX, endY), text) in results:
# display the text OCR'd by Tesseract
print("OCR TEXT")
print("========")
print("{}\n".format(text))

# strip out non-ASCII text so we can draw the text on the image
# using OpenCV, then draw the text and a bounding box surrounding
# the text region of the input image
text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
output = orig.copy()
cv2.rectangle(output, (startX, startY), (endX, endY),
	(0, 0, 255), 2)
cv2.putText(output, text, (startX, startY - 20),
	cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
print("we are in startX-{}, startY-{}, endX-{}, endY-{}".format(startX, startY, endX, endY))
# show the output image
cv2.imshow("Text Detection", output)
time.sleep(1)
# cv2.waitKey(0)