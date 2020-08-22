import numpy as np
import cv2
import os
import time
import sys
from datetime import datetime

class VisualDSBuilder:
    def __init__(self, frequency, dsfolder, videopath, size, colorspace):
        self.frequency = frequency
        self.dsfolder = dsfolder
        self.imgNo = 0
        self.size = size
        self.colorspace = colorspace
        if colorspace == None:
            self.colorspace = 'BGR'
        else:
            self.colorspace = colorspace.upper()


        if not os.path.exists(dsfolder):
            os.mkdir(dsfolder)
        if videopath:
            if not os.path.isfile(videopath):
                print("[INFO] - Input video file *", videopath, "* doesn't exist")
                exit()
            self.cap = cv2.VideoCapture(videopath)
        else:
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def run(self):
        if self.cap.isOpened() == False: 
            exit()
        start = time.time() 
        while(self.cap.isOpened()):
            hasFrame, frame = self.cap.read()
            
            if not hasFrame:
                break

            if not self.frequency:
                label = 'Manual Mode, press SPACEBAR to capture'
            else:
                label = 'Automatic Mode, saving at %s Hertz (%s seconds)' % (self.frequency, 1/self.frequency)
            infoframe = frame.copy()
            cv2.putText(infoframe, label, (10, 15), 1, 1, (255,0,0), 1, cv2.LINE_AA)
            cv2.putText(infoframe, 'Press ESC to Exit', (10, 30), 1, 1, (255,0,0), 1, cv2.LINE_AA)            
            k = cv2.waitKey(1)
            if k == 27:
                break                
            if not self.frequency:
                if k == 32:
                    self._saveImg(frame, self.size, self.colorspace)
            else:
                timeout = 1/self.frequency
                t = time.time() - start                                
                if t > timeout:
                    start = time.time()
                    self._saveImg(frame, self.size, self.colorspace)                
            cv2.imshow("Video Output", infoframe)
        self.cap.release()
        cv2.destroyAllWindows()

    def _saveImg(self, img, size, colorspace):
        now = datetime.now()
        label = str(self.imgNo) + '-' + now.strftime("%m%d%Y_%H%M%S%f") + '.png'
        fnpath = os.path.join(self.dsfolder, label)

        if colorspace == 'YCRCB':
            colorspace = cv2.COLOR_BGR2YCrCb
        if colorspace == 'HSV':
            colorspace = cv2.COLOR_BGR2HSV
        if colorspace == 'LAB':
            colorspace = cv2.COLOR_BGR2LAB
        if colorspace == 'GRAY':
            colorspace = cv2.COLOR_BGR2GRAY
        if colorspace == 'RGB':
            colorspace = cv2.COLOR_BGR2RGB

        if not colorspace == 'BGR':
            img = cv2.cvtColor(img, colorspace)
        img = cv2.resize(img, size)

        cv2.imwrite(fnpath, img)
        self.imgNo += 1