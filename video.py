#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import numpy as np
import cv2

#video width, height and fps
WIDTH = 640
HEIGHT = 480
FPS = 30.0

cap = cv2.VideoCapture(0)

#set video resolution
cap.set(3, WIDTH)
cap.set(4, HEIGHT)
cap.set(5, FPS)

filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".avi"

# Define the codec and create VideoWriter object
#XVID version
#fourcc = cv2.cv.CV_FOURCC(*'XVID')

#MPEG version
fourcc = cv2.cv.CV_FOURCC('M', 'P', 'E', 'G')

#print(cap.get(3))
#print(cap.get(4))
#print(cap.get(5))

#fps and resolution
out = cv2.VideoWriter(filename,fourcc, float(FPS), (int(cap.get(3)), int(cap.get(4))))

while(cap.isOpened()):
    frame = cap.read()
    # write the frame
    out.write(frame[1])

    #the "Esc" key
    #if (cv2.waitKey(1) == 27):
    #    break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
