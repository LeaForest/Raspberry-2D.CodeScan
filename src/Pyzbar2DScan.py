#!/usr/bin/python 是告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器。
#!/usr/bin/env python 会去环境设置寻找 python 目录，再调用对应路径下的解释器程序完成操作。推荐写法。
# 有这句的，加上执行权限后，可以直接用 ./test.py 执行，只对 Linux/Unix 用户适用
# -*- coding: UTF-8 -*- 或者 # coding=utf-8 即可支持中文编码而不报错
import cv2
import pyzbar.pyzbar as pyzbar
 
 
def decodeDisplay(image):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
 
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 0, 125), 2)

        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    return image
 
 
def detect():
    camera = cv2.VideoCapture\
	(0)                   #使用"多行连接符"斜杠（ \）可以将一行的语句分为多行显示
 
    while True:

        ret, frame = camera.read() # 返回两个元组分别给变量ret,frame

        gray = cv2.cvtColor(frame,  #语句中包含 [], {} 或 () 括号就不需要使用多行连接符
		cv2.COLOR_BGR2GRAY)
		
        im = decodeDisplay(gray)
 
        cv2.waitKey(5)
        cv2.imshow("camera", im)
 
    camera.release()
    cv2.destroyAllWindows()
 
 
if __name__ == '__main__':
    detect()