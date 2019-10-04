import numpy as np
import cv2

cap = cv2.VideoCapture('C:\\Work\\test project\\github\\mysite\\output2019_09_30_13_01_4.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret ==True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()