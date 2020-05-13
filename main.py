import numpy as np
import cv2
import pytesseract
from PIL import Image
import os
import re
from scrapper import CheckifPolice


import time


cap = cv2.VideoCapture(0)
try: 
    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print('Error Creating directory of data')

currentFrame = 0

#This code will be able to load in the source code for the biluppgifter homepage
#new branch
#Run program: python3 OCR.py
while(True): 
    ret, video = cap.read()
    cv2.imshow('video', video)

    videoText = pytesseract.image_to_string(video, lang ='eng')
    videoReg = re.findall("[A-Z]{3} [0-9]{2}[(0-9)|(A-Z)]{1}", videoText)
   
    print(videoReg)
    
    if (videoReg):
        result = "".join(videoReg)
        name = './data/frame' + str(currentFrame) + '.png'
        cv2.imwrite(name, video)
        print('creating...' + name)
        imgText = pytesseract.image_to_string(name, lang ='eng')
        imgReg = re.findall("[A-Z]{3} [0-9]{2}[(0-9)|(A-Z)]{1}", imgText)
        resultImg = "".join(imgReg)
        if (result == resultImg):
            CheckifPolice(result)
        else:
            print("different values, video: " + result + " Result img: " + resultImg)
        currentFrame += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

