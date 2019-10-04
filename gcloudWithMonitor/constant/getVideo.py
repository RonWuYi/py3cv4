import cv2

#######################################################################################
VIDEO_OUTPUT_FILENAME = "output.mp4"
#######################################################################################


def getVideo(duration, file_name):
    formatted_Time = duration
    print("Recording video for %.3f seconds" % formatted_Time)
    cap = cv2.VideoCapture(0)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

    # fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    ############################################ TODO fix!!
    # fourcc = cv2.CV_FOURCC('X', '2', '6', '4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    #############################################
    out = cv2.VideoWriter(file_name, fourcc, 30.0, (width, height))
    i=0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            # frame = cv2.flip(frame, 0)
            out.write(frame)
            #cv2.imshow('frame', frame)
            if (i*60.0/3600.0) == formatted_Time:
                break
        else:
            print("Could not read capture!")
            break
        i = i+1
    cap.release()
    out.release()


if __name__ == '__main__':
    getVideo()
