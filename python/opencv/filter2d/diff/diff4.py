#-*- coding:utf-8 -*-
import cv2
import numpy as np


def filter2d(src, kernel):
    # カーネルサイズ
    m, n = kernel.shape

    # 畳み込み演算をしない領域の幅
    d = int((m-1)/2)
    h, w = src.shape[0], src.shape[1]

    # 出力画像用の配列（要素は全て0）
    dst = np.zeros((h, w))

    for y in range(d, h - d):
        for x in range(d, w - d):
            # 畳み込み演算
            dst[y][x] = np.sum(src[y-d:y+d+1, x-d:x+d+1]*kernel)

    return dst


# 入力画像を読み込み
img = cv2.imread("C:/github/sample/python/opencv/filter2d/diff/input.jpg")

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# カーネル
kernel = np.array([[0, 0, 0],
                       [-1, 0, 1],
                       [0, 0, 0]])

dst1 = filter2d(gray, kernel)

# 結果を出力
cv2.imwrite("C:/github/sample/python/opencv/filter2d/diff/output1.jpg",
            np.uint8(np.abs(dst1)))
