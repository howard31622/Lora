{\rtf1\ansi\ansicpg950\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww22580\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #!/usr/bin/env python\
import time, serial, subprocess, sys, csv, hashlib\
import wiringpi as wpi\
import json\
import time\
\
from os import popen\
from urllib import request\
from subprocess import Popen\
\
\
\
counter = 1\
\
wpi.wiringPiSetup()\
ser = serial.Serial(\
        port='/dev/serial0',\
        baudrate = 57600,\
        #baudrate = 115200,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS\
)\
\
\
wpi.pinMode(8, 1) # 1 for OUTPUT\
wpi.digitalWrite(8, 1);\
wpi.delay(600)\
print(ser.name)\
\
\
\
\
\
def sentData(Device_ID, RFIDid, temperature):\
    print(\'93sent data to server\'94)\
	\
\
#initial lora setup \
cmd = "source ~/Desktop/lorasetup.sh"\
retcode = subprocess.Popen(cmd, shell=True,executable='/bin/bash')\
\
\
# Always wait the data which sent from arduino\
###This place need to try catch\
while True:\
    rec_data = ser.read()\
    wpi.delay(100)\
    data_left = ser.inWaiting()\
    if data_left==0:\
        print ("data_lef=0", rec_data)\
    else:\
        rec_data += ser.read(data_left)\
        print("data to be processed", len(rec_data), rec_data)\
        if (len(rec_data)>20):\
            dataAll = rec_data.decode()\
            dataArr = dataAll.split(",")\
            dataDeviceID = dataArr[2]\
            dataRFIDid = dataArr[3]\
            dataTemperature = dataArr[4]\
            #print("before",dataArr,dataDeviceID,dataRFIDid,dataTemperature)\
            \
            print(counter)\
            global counter\
            counter+=1\
            \
            sentData(dataDeviceID, dataRFIDid, dataTemperature)\
            print(time.strftime("%Y/%m/%d~%H:%M:%S",time.localtime()))\
            print("")\
\
\
\
\
\
}