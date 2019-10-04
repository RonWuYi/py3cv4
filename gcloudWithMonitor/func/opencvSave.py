import os 
import cv2
import time
import numpy as np

from pathlib import Path
from datetime import datetime
from constant import constant, google


class Cv2Video:
    def __init__(self, cap, fourcc):
        self.cap = cap
        self.fourcc = fourcc
        self.fileName = 'out{}.avi'.format(constant.time_string())
        # self.out = cv2.VideoWriter(os.path.join(str(Path.cwd()), 'media', self.fileName), self.fourcc, 20.0, (640, 480))
        self.out = cv2.VideoWriter(os.path.join(constant.videoinpath, self.fileName), self.fourcc, 20.0, (640, 480))
        self.start_time = time.time()
        self._Createrunning = True
        self._Uploadrunning = True
        self.upload_count = 0
        self.upload_file_list = []
        self.upload_save_file = []
        self.encrypted_save_file = []

    def Createterminate(self):
        self._Createrunning = False
        # self._running = False

    def Uploadterminate(self):
        self._Uploadrunning = False

    def Create(self):
        frame_count = 120

        while(self.cap.isOpened() and self._Createrunning == True):

            # ret, frame = cv2.VideoCapture(0).read()
            ret, frame = self.cap.read()
            # Our operations on the freame come here
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

            # Display the resulting frame
            cv2.imshow('WebCamera', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if ret == True and (frame_count) > 0:
                save_frame = cv2.flip(frame, 0)
                self.out.write(save_frame)

                frame_count -= 1
            else:
                os.system("ffmpeg.exe -i " + os.path.join(constant.videoinpath, self.fileName) + " -vcodec copy -acodec copy -encryption_scheme cenc-aes-ctr -encryption_key 76a6c65c5ea762046bd749a2e632ccbb -encryption_kid a7e61c373e219033c21091fa607bf3b8 " + os.path.join(constant.videooutpath, "encrypted{}.mp4".format(self.fileName[-20:-4])))
                self.upload_save_file.append(self.fileName)
                self.encrypted_save_file.append("encrypted{}.mp4".format(self.fileName[-20:-4]))
                self.fileName = 'out{}.avi'.format(constant.time_string())
                frame_count = 120
                # self.out=cv2.VideoWriter(os.path.join(str(Path.cwd()), 'media', self.fileName), self.fourcc, 20.0, (640, 480))
                self.out=cv2.VideoWriter(os.path.join(constant.videoinpath, self.fileName), self.fourcc, 20.0, (640, 480))
                # break
    
    def Upload(self, folder):
        # upload_file = []
        # upload_time = 0
        while self._Uploadrunning:
            # for i in os.listdir(os.path.join(folder, 'media')):
            for i in os.listdir(folder):
                # if i.endswith('mp4') and len(os.listdir(folder)) > self.upload_count and i in self.upload_save_file:
                if i.endswith('mp4') and len(os.listdir(folder)) > self.upload_count and i in self.encrypted_save_file:
                    if i not in self.upload_file_list:
                        # pass
                        google.upload_blob(constant.storage_name, os.path.join(folder, i), 'test{}'.format(i))
                        self.upload_file_list.append(i)
                        self.upload_count += 1
                        # upload_time += 1

    def fileEncryption(self):
        print ("Awaiting for a file to encrypt")
        var = 1
        while var:
            if (len([name for name in os.listdir(constant.videoinpath) if os.path.isfile(os.path.join(constant.videoinpath, name))])) > 0:
                with os.scandir(constant.videoinpath) as entries:
                    for entry in entries:
                        if entry.is_file():
                            print(entry.name)
                            os.system("ffmpeg.exe -i " + constant.videoinpath + entry.name + " -vcodec copy -acodec copy -encryption_scheme cenc-aes-ctr -encryption_key 76a6c65c5ea762046bd749a2e632ccbb -encryption_kid a7e61c373e219033c21091fa607bf3b8 " + constant.videooutpath + entry.name + "encrypted.mp4")
                            os.remove(constant.videoinpath + entry.name)

    def ReleaseObj(self):
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()
