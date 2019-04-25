#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
#print(cv2.__version__)


if __name__ == '__main__':

    #ウィンドウの定義
    cv2.namedWindow("stream", cv2.WINDOW_NORMAL)
    cv2.namedWindow("canny", cv2.WINDOW_NORMAL)

    #以下のようにすると、接続されているカメラデバイスを開く
    src = cv2.VideoCapture(0)

    #ビデオデバイスが見つからなければ終了
    if not src.isOpened():
        print("No Stream.")
        import sys
        sys.exit()

    #解像度を設定
    src.set(3, 640)
    src.set(4, 480)


    while True:
        ret, frame = src.read()

        #輪郭抽出
        canny_img = cv2.Canny(frame, 20, 110)

        #フレームをウィンドウに表示
        cv2.imshow("stream", frame)
        cv2.imshow('canny', canny_img)

        key = cv2.waitKey(33)
        #Escキーが押されたら終了
        if key == 27:
            break

        #1フレーム分待つ
        #time.sleep(0.33)

    #すべてのウィンドウを破棄
    cv2.destroyAllWindows()
src.release()
