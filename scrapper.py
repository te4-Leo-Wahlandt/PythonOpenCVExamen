import requests
import re
from bs4 import BeautifulSoup
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
         #GPIO.setup(26, True)
    