import urllib.request
import re
#import RPi.GPIO as GPIO

#The LED response
#GPIO.setmode(GPIO.BCM)
#Green light
#GPIO.setup(26, GPIO.OUT)
#red light
#GPIO.setup(6, GPIO.OUT)


def CheckifPolice(result):
    #reset the GPIO
    #GPIO.setup(6, False)
    #GPIO.setup(26, False)

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
        print("Kan vara polis")
        #GPIO.setup(6, True)
    else:
        print("Är inte polis")
        #GPIO.setup(26, True)
