#首先导入本次所需要的库，最后一个csv是Python自带的csv表格操作库，这里我们需要把我们扫到的二维码信息都存入csv表格里。
import cv2
from pyzbar import pyzbar
import csv


#生成字典dicttoday
dicttoday = {'01':'a', '02':'b','03':'c','04':'d'}
#设置变量防重复
#调用opencv实例化摄像头
found = set()
capture = cv2.VideoCapture(0)
#循环采集条码，
while(1):
  #采集实时图像
  ret,frame = capture.read()
  #解码
  test = pyzbar.decode(frame)
 
  #循环检测的条形码
  for tests in test:
    #转成字符串
    testdate = tests.data.decode('utf-8')
    testtype = tests.type
 
    #绘出条形码数据，条形码类型
    printout = "{} ({})".format(testdate, testtype)
 
    if testdate not in found:
    #打印条形码数据，条形码类型
      print("[INFO] Found {} barcode: {}".format(testtype, testdate))
    #从字典中删除对应值
    if testdate not in found:
      del dicttoday[testdate]
      found.add(testdate)
  #键入q停止
  cv2.imshow('Test',frame)
  if cv2.waitKey(1) == ord('q'):
    break
#打印剩余值
print(dicttoday)