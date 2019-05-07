#!/usr/bin/env python
# -*- coding: utf-8 -*-

#func.pyのインポート
import func

def main():

    func.func()

    x = 5
    print(str(x) + "の2乗は" + str(func.pow(x)) + "です。")

    a, b = func.rand()
    print("2つの乱数は、" + str(a) + "と" +  str(b) + "です。")
    
    #以下のようにしてもよい
    #func.main()

#プログラム実行時に実行される部分
if __name__ == '__main__':
    main()
