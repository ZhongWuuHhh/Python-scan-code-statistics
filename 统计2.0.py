#首先导入本次所需要的库，最后一个csv是Python自带的csv表格操作库，这里我们需要把我们扫到的二维码信息都存入csv表格里。
import cv2
from pyzbar import pyzbar
import csv
import tkinter

root = tkinter.Tk()
root.title('统计')

dicttoday = {}

def run1():
    run3()

def run3():

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
    while (1) :
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
                del dicttoday[testdate]
                found.add(testdate)
          
      
def run2():
    #创建并打开文本文件
    file = open('dicttoday.txt', 'w')

    #字典输出
    for k,v in sorted(dicttoday.items()):
        file.write(str(v)+'\n')
        #file.write(str(k)+' '+str(v)+'\n')
    file.close()

lb1 = tkinter.Button(root,text='开始',command=run1)
lb1.place(relx=0.0,rely=0.0,relheight=1.0,relwidth=0.5)
lb2 = tkinter.Button(root,text='停止',command=run2)
lb2.place(relx=0.5,rely=0.0,relheight=1.0,relwidth=0.5)

root.mainloop()
