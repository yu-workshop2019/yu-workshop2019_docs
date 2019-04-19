#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
#print(cv2.__version__)

#=============================================================================#

#Webカメラの映像がストリーミング配信されているRaspberry PiサーバのURL
#以下のように記述すると、Basic認証がかけられているサイトにパスワードの入力なしでアクセスできる
#URL = "http://pi:raspberry@10.159.13.13:9000/?action=stream/"
URL = "http://10.159.13.14:9000/?action=stream/"

#動体と認知する最小サイズの定義
#これより小さな動体は無視される
#MINSIZE = 100
MINSIZE = 40

#動体と認知する最大サイズの定義
#これより大きな動体は無視される
MAXSIZE = 400

#差分を検出するときの閾値の定義
THRESHOLD = 3
#5

#ゴマ塩雑音を除去するための値の定義
BLUR = 9
#7

#日没-翌日の日の出までの夜間（暗いとき）には撮影を停止するための閾値
BLIGHTNESS = 80

#写真に四角形を描画するかどうか
RECT = True
#=============================================================================#

#直近3フレーム間の差分を検出する関数
#img:フレーム間の差分を取るための3枚の画像
def frame_diff(img1, img2, img3):

    #3枚の画像の差分を2枚ずつ取る(画素の差の絶対値を計算)
    diff_a = cv2.absdiff(img3, img2)
    diff_b = cv2.absdiff(img2, img1)

    #先ほど取った2枚の差分画像の論理積を取る
    #黒画素でないところのみが表示される
    diff = cv2.bitwise_and(diff_a, diff_b)

    #差分が閾値THRESHOLDより小さい場合はTrue
    mask = diff < THRESHOLD

    #背景画像と同じサイズの配列を生成
    img_mask = np.empty((img1.shape[0], img1.shape[1]), np.uint8 )

    #全画素を白に
    img_mask[:][:] = 255

    #Trueの部分（閾値未満の背景部分、つまり、動いていない部分）は黒く塗りつぶす
    img_mask[mask] = 0

    #ゴマ塩雑音を除去
    img_mask = cv2.medianBlur(img_mask, BLUR)

    #動体部分のみが白く表示された二値画像を返す
    return img_mask


#=============================================================================#



if __name__ == '__main__':

    #ウィンドウの定義
    cv2.namedWindow("motion_detection", cv2.WINDOW_NORMAL)
    #cv2.namedWindow("motion_detection_binary")

    #ネットワーク上のストリーミング映像を開く
    src = cv2.VideoCapture(URL)

    #以下のようにすると、接続されているカメラデバイスを開く
    #src = cv2.VideoCapture(0)

    #ビデオデバイスが見つからなければ終了
    if not src.isOpened():
        print("No Stream.")
        import sys
        sys.exit()

    #解像度を設定
    src.set(3, 640)
    src.set(4, 480)


    #最初の3フレームを読み込み、各々グレースケールに変換
    color_img1 = src.read()
    color_img2 = src.read()
    color_img3 = src.read()

    img1 = cv2.cvtColor(color_img1[1], cv2.COLOR_RGB2GRAY)
    img2 = cv2.cvtColor(color_img2[1], cv2.COLOR_RGB2GRAY)
    img3 = cv2.cvtColor(color_img3[1], cv2.COLOR_RGB2GRAY)


    while True:

        #撮影環境の明るさを算出（全画素値の平均）
        blightness = img2.mean()
        #print(blightness)

        #フレーム間の差分を計算する関数を呼び出し、
        #img_frame_subに、動体部分のみが白く表示された二値画像を格納
        img_frame_sub = frame_diff(img1, img2, img3)

        #閾値上の動体が検知されたかを表すフラグ
        moving_object = False

        #動体部分のみが白く表示された二値画像から輪郭を抽出
        contours = cv2.findContours(img_frame_sub, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]

        #openCV2系では以下を使用
        #contours, retval = cv2.findContours(img_frame_sub, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #動体の数だけ繰り返す
        for pt in contours:

            #動体部分の大きさを取得
            x, y, w, h = cv2.boundingRect(pt)

            #小さな物体を除外
            if w < MINSIZE:
                continue

            #大きな物体を除外
            if w > MAXSIZE:
                continue

            if (RECT == True):
                #動体部分に四角形を描画
                cv2.rectangle(color_img2[1], (x, y), (x + w, y + h), (0, 255, 0), 3 )

            #動体が検知されたならフラグをTrueに
            moving_object = True

        #フレームをウィンドウに表示
        cv2.imshow("motion_detection", color_img2[1])
        #cv2.imshow("motion_detection_binary", img_frame_sub)


        key = cv2.waitKey(33)
        #Escキーが押されたら終了
        if key == 27:
            break

        #1フレーム分待つ
        #time.sleep(0.33)

        #新しいフレームを1つ読み込み、以前のフレームを前倒しする
        color_img2 = color_img3
        color_img3 = src.read()

        img1 = img2
        img2 = img3
        img3 = cv2.cvtColor(color_img3[1], cv2.COLOR_RGB2GRAY)

    #すべてのウィンドウを破棄
    cv2.destroyAllWindows()
    src.release()
