# -*- coding: utf-8 -*-

import cv2
import numpy as np
import glob
import os

#読み取り先のフォルダ名
files = glob.glob("../../images/raw_images/*")
#変換先のサイズ (768, 576)
reW = 640 #764 
reH = 480

#書き出し先フォルダ
try:
    os.mkdir("../../images/resized_images")
except FileExistsError:
    pass


#ファイルナンバリングの初期化
count = 0

for f in files:
    img = cv2.imread(f)
    #print(type(img))

    if type(img) is np.ndarray: #画像ファイル以外は弾く
        imgH, imgW = img.shape[:2]
        
        #縦横サイズが奇数であれば大きさを1減らして偶数にする
        if imgH % 2 == 1:
            img = img[0:imgH-1, 0:imgW]
            imgH, imgW = img.shape[:2]
        if imgW % 2 == 1:
            img = img[0:imgH, 0:imgW-1]
            imgH, imgW = img.shape[:2]
        
        #画像サイズがreW×reHより大きければ四隅をクリッピングする
        if imgH > reH and imgW > reW:
            #左上
            img1 = img[0:reH, 0:reW]
            f1 = "../../images/resized_images/" + str(count) + ".png"
            cv2.imshow("img",img1)
            cv2.waitKey(1)
            cv2.imwrite(f1,img1)
            count += 1
            #右上
            img2 = img[0:reH, imgW-reW:imgW]
            f1 = "../../images/resized_images/" + str(count) + ".png"
            cv2.imwrite(f1,img2)
            count += 1
            #左下
            img3 = img[imgH-reH:imgH, 0:reW]
            f1 = "../../images/resized_images/" + str(count) + ".png"
            cv2.imwrite(f1,img3)
            count += 1
            #右下
            img4 = img[imgH-reH:imgH, imgW-reW:imgW]
            f1 = "../../images/resized_images/" + str(count) + ".png"
            cv2.imwrite(f1,img4)
            count += 1

        else:  

            #テクいことしているから説明省略
            dst = np.tile(np.uint8([255,255,255]), (reH,reW,1))
            deW = int((imgW - reW) / 2)
            deH = int((imgH - reH) / 2)
            a = np.where(deW > 0, reW, imgW)
            b = np.where(deH > 0, reH, imgH)

            #print((reH-b)/2, (reH+b)/2, (imgH-b)/2, (imgH+b)/2)
            #print((reW-b)/2, (reW+b)/2, (imgW-b)/2, (imgW+b)/2)
            dst[int((reH-b)/2):int((reH+b)/2), int((reW-a)/2):int((reW+a)/2)] = img[int((imgH-b)/2):int((imgH+b)/2), int((imgW-a)/2):int((imgW+a)/2)]
            cv2.imshow("img",dst)
            cv2.waitKey(1)
            
            #書き込み先のフォルダ
            f1 = "../../images/resized_images/" + str(count) + ".png"
            cv2.imwrite(f1,dst)
            count += 1









cv2.destroyAllWindows()