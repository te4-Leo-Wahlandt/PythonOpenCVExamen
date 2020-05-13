import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import unquote
#import RPi.GPIO as GPIO

baseURL = 'https://biluppgifter.se/fordon/'
def CheckifPolice(result):
    r = requests.get(baseURL+result)
    soup = BeautifulSoup(r.text, 'html.parser')
    if(soup.find_all('div', {'class': 'alert alert-danger text-center'})):
        print("Polis")
         #GPIO.setup(6, True)
    else:
        print("Ingen Polis")
        getInfo = soup.find('a', {'class': 'gtm-merinfo'})
        href = getInfo['href']
        getDriver(href)
        #GPIO.setup(26, True)
    

def getDriver(getInfo):
    splitURL = getInfo.split('/')
    if(splitURL[3] == 'foretag'):
        print("Ägs av företaget: " + splitURL[4])
    else:
        nameAndYear = splitURL[5].split('-')
        fullName = ""
        for name in nameAndYear[0:-1]:
            fullName += name + " "

        year = nameAndYear[-1]
        print(fullName)
        print(year)
CheckifPolice('AAS23A')