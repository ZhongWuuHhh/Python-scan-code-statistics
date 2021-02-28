#首先导入本次所需要的库，最后一个csv是Python自带的csv表格操作库，这里我们需要把我们扫到的二维码信息都存入csv表格里。
import cv2
from pyzbar import pyzbar
import csv


#声明一个空字典dicttoday
dicttoday = {}

#打开文本文件
file = open('list.txt','r')

#遍历文件
for line in file.readlines():
    line = line.strip()
    k = line.split('	')[0]
    v = line.split('	')[1]
    dicttoday[k] = v

#关闭文件
file.close()

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
 
  #循环
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
  cv2.imshow('Test',frame)
  
  #键入q停止
  if cv2.waitKey(1) == ord('q'):
    cv2.destroyWindow('Test')
    break

#打印剩余值
print ("未上交:",list(dicttoday.values()))

#创建并打开文本文件
file = open('dicttoday.txt', 'w')

#字典输出
for k,v in sorted(dicttoday.items()):
  file.write(str(v)+'\n')
  #file.write(str(k)+' '+str(v)+'\n')
file.close()

exit
