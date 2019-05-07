#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func():
    print("funcを実行しました。")

def pow(x):
    print("powを実行しました。")
    return(x * x)

def rand():
    import random
    print("randを実行しました。")
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    return (a, b)

def main():
    print("mainを実行しました。")

    #funcの実行
    func()

    #powの実行
    x = 5
    print(str(x) + "の2乗は" + str(pow(x)) + "です。")

    #randの実行
    a, b = rand()
    print("2つの乱数は、" + str(a) + "と" +  str(b) + "です。")

#プログラム実行時に実行される部分
if __name__ == '__main__':
    print("まずここが実行されます。")
    main()
