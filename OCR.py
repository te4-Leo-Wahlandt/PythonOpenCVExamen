import numpy as np
import cv2
import pytesseract
from PIL import Image
import re
import os
import urllib.request
#import RPi.GPIO as GPIO
import time


cap = cv2.VideoCapture(0)
try: 
    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print('Error Creating directory of data')

currentFrame = 0

#The LED response
#GPIO.setmode(GPIO.BCM)
#Green light
#GPIO.setup(26, GPIO.OUT)
#red light
#GPIO.setup(6, GPIO.OUT)





#This code will be able to load in the source code for the biluppgifter homepage
def CheckifPolice(result):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = "https://biluppgifter.se/fordon/OYC087"
    
    headers={'User-Agent':user_agent,} 
    
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)

    data = response.read().decode('UTF-8') # The data u need

    print(data)

    #Refactor the data so it won't fetch all data. Only need a specific div

    regex = re.findall(r'POLIS', str(data))
    PoliceInstance = len(regex)
    print(PoliceInstance)

    if(PoliceInstance >= 1):
        #GPIO.setup(6, True)
        time.sleep(5)
        #GPIO.setup(6, False)
        print("Kan vara polis")
    else:
       #GPIO.setup(26, True)
        time.sleep(5)
       # GPIO.setup(26, False)

    

#Run program: python3 OCR.py
while(True): 
    ret, video = cap.read()
    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    #cv2.imshow('video', video)

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

