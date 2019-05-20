#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import time
import datetime
# print(cv2.__version__)

#=============================================================================#

# Webカメラの映像がストリーミング配信されているRaspberry PiサーバのURL
# 以下のように記述すると、Basic認証がかけられているサイトにパスワードの入力なしでアクセスできる
URL = "http://pi:raspberry@192.168.0.100:9000/?action=stream&ignored.mjpg"

# 画像撮影間隔（秒）
INTERVAL = 1

# 撮影した画像の保存先のディレクトリ
SAVE_DIR = "/home/pi/timelapse/"

#=============================================================================#


def main():

    # 前回静止画を撮影した時刻
    # 初めはプログラム開始時の時刻を入れておく
    last_shoot = datetime.datetime.now()

    # ネットワーク上のストリーミング映像を開く
    # src = cv2.VideoCapture(URL)

    # 接続されているカメラデバイスを開く
    src = cv2.VideoCapture(0)

    # キャプチャソースが使用可能になるまで少し待機
    time.sleep(1)

    # ビデオデバイスが見つからなければ終了
    if not src.isOpened():
        print("No Stream.")
        import sys
        sys.exit()

    # 解像度を設定
    src.set(3, 640)
    src.set(4, 480)

    while True:

        # フレーム読み込み
        img = src.read()

        # 検知された時点の時刻を取得
        now = datetime.datetime.now()

        # 画像を撮影した直近の時刻と現在時刻との差分をとる
        delta = now - last_shoot

        # 差分を秒単位に直してキャスト
        delta = int(delta.total_seconds())
        # print(delta)

        # 前回の撮影からINTERVAL秒以上経過しているならば
        if (delta >= INTERVAL):

            # 今回撮影した時刻を、直近の撮影時刻として保存
            last_shoot = now
            # print(now.strftime('%Y-%m-%d %H:%M:%S') + "\t" + "took a picture")

            # 画像を保存
            filename = SAVE_DIR + now.strftime('%Y%m%d_%H%M%S') + ".jpg"
            cv2.imwrite(filename, img[1])

    # すべてのウィンドウを破棄
    cv2.destroyAllWindows()
    src.release()


#=============================================================================#

if __name__ == '__main__':
    main()
