import cv2
from pyzbar.pyzbar import decode
import csv
import time
import threading
import tkinter

originaldict = {}
stopcontrol = 'continue'


def readdict():
    file = open('1.txt','r')
    
    for line in file.readlines():
        line = line.strip()
        k = line.split('	')[0]
        v = line.split('	')[1]
        originaldict[k] = v

    file.close()

    print('ok')


def decodevideo():
    found = set()

    capture = cv2.VideoCapture(0)
    
    while(1):
        ret,frame = capture.read()

        barcode = decode(frame, symbols=None)

        for tests in barcode:
            testdate = tests.data.decode('utf-8')
            testtype = tests.type
            printout = '{} ({})'.format(testdate, testtype)

            if testdate not in found:
                print('[INFO] Found {} barcode: {}'.format(testtype, testdate))
                del originaldict[testdate]
                found.add(testdate)

        if stopcontrol == 'stop':
            break


def writedict():
    print ("未上交:",list(originaldict.values()))

    file = open('dicttoday.txt', 'w')

    for k,v in sorted(originaldict.items()):
        file.write(str(v)+'\n')
        #file.write(str(k)+' '+str(v)+'\n')

    file.close()

    print('ok')


def guicontrol():
    root = tkinter.Tk()
    root.title('统计')

    lb1 = tkinter.Button(root,text='开始',command=start)
    lb1.place(relx=0.0,rely=0.5,relheight=0.5,relwidth=0.5)

    lb2 = tkinter.Button(root,text='停止',command=stop)
    lb2.place(relx=0.5,rely=0.5,relheight=0.5,relwidth=0.5)

    lb3 = tkinter.Button(root,text='1',command=choose)
    lb3.place(relx=0.0,rely=0.0,relheight=0.5,relwidth=1.0)


def choose():
    t1.start()


def start():
    t2.start()


def stop():
    stopcontrol = 'stop'
    time.sleep(2)
    t3.start()
    

t1 = threading.Thread(target=readdict, name='readdict')
t2 = threading.Thread(target=decodevideo, name='decodevideo')
t3 = threading.Thread(target=writedict, name='writedict')

guicontrol()

