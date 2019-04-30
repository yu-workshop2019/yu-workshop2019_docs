# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np
from PIL import Image
#print(cv2.__version__)

#取得した映像から顔を認識する関数
def face_detect(src, pure_image, cascade):


    while True:

        #ビデオデバイスからフレームを取得
        retval, frame = src.read()

        if frame is None:
            break

        #顔検出
        objects = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=3, flags=cv2.CASCADE_SCALE_IMAGE, minSize=(30, 30), maxSize=(100, 100))

        #顔が検出されたならば
        if len(objects) > 0:

            #検出された顔の左上の座標(x、y)および大きさ(w、h)を取得
            for rect in objects:
                x = rect[0]
                y = rect[1]
                w = rect[2]
                h = rect[3]

                #顔の形状に合わせ、画像が顔全体を覆うように範囲を調整
                x = x - w / 4
                y = y - h / 2.2
                w = w * 1.4
                h = h * 1.6

                #整数値にするため丸める
                x = int(round(x))
                y = int(round(y))
                w = int(round(w))
                h = int(round(h))

                #mainから渡された画像をそのまま繰り返し加工するとどんどん劣化するので、
                #オリジナルには手を加えず毎回コピーを加工する
                image = pure_image

                #以上より得られた顔の範囲にフィットするように、合成する画像をリサイズ
                image = cv2.resize(image, (w, h))

                #顔部分に画像を合成する関数を呼び出し
                frame = over_lay(frame, image, x, y)

                #以下の記述を有効化すると顔部分にモザイク処理ができる
                #dst = frame[y:y+h, x:x+w]
                #blur = cv2.blur(dst, (50, 50))
                #frame[y:y+h, x:x+w] = blur
                
                
        #ウィンドウの定義
        cv2.namedWindow("face_mask", cv2.WINDOW_NORMAL)
        
        #合成した映像をウィンドウに出力
        cv2.imshow("face_mask", frame)

        #キー入力を33ms待つ
        key = cv2.waitKey(33)

        #Escキーが押されたら終了
        if key == 27:
            break

    #すべてのウィンドウを破棄
    cv2.destroyAllWindows()
    src.release()


#映像の顔部分に画像を合成する関数
def over_lay(frame, image, x, y):

    #合成する画像の高さおよび横幅を取得
    height, width = image.shape[:2]

    #以下、openCVのデータをPILのデータへと変換
    #BGRからRGBへ変換
    #layer_1 はビデオデバイスより取得したストリーム映像
    #layer_2 は顔部分に合成する画像
    layer_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    layer_2 = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)

    #PILのデータへと変換
    layer_1 = Image.fromarray(layer_1)
    layer_2 = Image.fromarray(layer_2)

    #アルファチャンネルを付加
    layer_1 = layer_1.convert('RGBA')
    layer_2 = layer_2.convert('RGBA')

    #ビデオデバイスと同じ大きさを持つ透過レイヤを準備
    tmp = Image.new('RGBA', layer_1.size, (255, 255, 255, 0))

    #先ほど準備したレイヤに、顔部分に合成する画像を貼り付け
    tmp.paste(layer_2, (x, y), layer_2)

    #ビデオデバイスより取得したストリーム映像と、画像を貼り付けた透過レイヤとを合成
    result = Image.alpha_composite(layer_1, tmp)

    #アルファチャンネルを除去し、GBRへと変換したものを返す
    return cv2.cvtColor(np.asarray(result), cv2.COLOR_RGBA2BGR)


if __name__=='__main__':

    #顔部分に合成する画像を開く
    pure_image = cv2.imread("image.png", cv2.IMREAD_UNCHANGED)
    #pure_image = cv2.imread("stig_helmet.png", cv2.IMREAD_UNCHANGED)

    #画像が見つからなければ終了
    if pure_image is None:
        print("No Image.")
        sys.exit()

    #ビデオデバイスを開く
    src = cv2.VideoCapture(0)

    #ビデオデバイスが見つからなければ終了
    if not src.isOpened():
        print("No Stream.")
        sys.exit()

    #ビデオデバイスから取得する映像の解像度を設定
    #src.set(3,  640)
    #src.set(4, 480)

    src.set(3,  320)    #width
    src.set(4, 240)     #height
    src.set(5, 10)      #FPS


    #顔認識のデータが入ったカスケード分類器の定義
    HAAR_FILE = 'haarcascade_frontalface_default.xml'

    #カスケード分類器の読み込み
    cascade = cv2.CascadeClassifier(HAAR_FILE)

    #カスケード分類器のファイルが見つからないなら終了
    if cascade.empty():
        print("No Cascade File.")
        sys.exit()

    #顔検出をする関数を呼び出し
    face_detect(src, pure_image, cascade)
