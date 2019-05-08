#!/usr/bin/python
#coding:utf-8

import cv2

#URL = "http://pi:raspberry@10.159.13.13:9000/?action=stream"
#URL = "http://10.159.13.14:9000/?action=stream"
#src = cv2.VideoCapture(URL)
src = cv2.VideoCapture(0)

while(True):

    ret, frame = src.read()
    #gray_img = cv2.imread(frame, cv2.IMREAD_GRAYSCALE)
    canny_img = cv2.Canny(frame, 20, 110)
    cv2.imshow('frame', canny_img)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
