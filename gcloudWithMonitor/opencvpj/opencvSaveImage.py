import os
import cv2

from constant import constant

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if ret == True:
        cv2.imshow("test", frame)
    k = cv2.waitKey(1)

    if k%256 == 27:
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        img_name = "frame_{}.png".format(img_counter)
        cv2.imwrite(os.path.join(constant.cur_folder(), "media", img_name), frame)
        print("{} written".format(img_name))
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
