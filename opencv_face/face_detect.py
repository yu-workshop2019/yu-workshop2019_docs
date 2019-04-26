# -*- coding: utf-8 -*-

import cv2
import time
import datetime
import numpy as np
#from pythonosc import osc_message_builder, udp_client

#print(cv2.__version__)

def main():
    #ウィンドウの定義
    cv2.namedWindow("stream", cv2.WINDOW_NORMAL)

    #顔認識のデータが入ったカスケード分類器の定義
    HAAR_FILE = './haarcascade_frontalface_default.xml'

    #カスケード分類器の読み込み
    cascade = cv2.CascadeClassifier(HAAR_FILE)

    #カスケード分類器のファイルが見つからないなら終了
    if cascade.empty():
        print("No Cascade File.")
        import sys
        sys.exit()

    #ビデオデバイスを開く
    src = cv2.VideoCapture(0)

    #ビデオデバイスが見つからなければ終了
    if not src.isOpened():
        print("No Stream.")
        import sys
        sys.exit()

    """
    #初期フレーム取得
    retval, frame = src.read()

    #フレームの形状取得
    height, width, channels = frame.shape
    """

    #画面の横幅と高さを設定
    w = 320
    h = 240
    src.set(3, w) #width
    src.set(4, h) #height
    #FPSを設定
    src.set(5, 15) #fps

    #FPSカウント用に現在時刻取得
    start = datetime.datetime.now()

    while True:
        #ビデオデバイスからフレームを取得
        retval, frame = src.read()
        if frame is None:
            break

        #顔検出
        objects = cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3, flags=cv2.CASCADE_SCALE_IMAGE, minSize=(30, 30), maxSize=(100, 100))

        #顔部分にフレームを描画（検出された顔の数だけ繰り返す）
        for x, y, w, h in objects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 200, 0), 2 , 0)

        #FPS計算と表示の設定
        stop = datetime.datetime.now()
        delta = stop - start
        fps = 1.0 / (delta.microseconds * 0.000001)
        #print("{0:2.2f}".format(fps) + "FPS")
        text = "{0:2.2f}".format(fps) + " fps"
        font = cv2.FONT_HERSHEY_DUPLEX
        font_size = 0.6
        cv2.putText(frame,text,(10, 25),font, font_size,(0,200,0))

        #カウントをリセット
        start = datetime.datetime.now()

        #フレームをウィンドウに表示
        cv2.imshow("stream", frame)

        #キー入力を33ms待つ
        key = cv2.waitKey(33)

        #Escキーが押されたら終了
        if key == 27:
            break

    #すべてのウィンドウを破棄
    cv2.destroyAllWindows()
    src.release()

if __name__ == '__main__':
    main()
