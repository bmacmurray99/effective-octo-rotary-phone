
import RPi.GPIO as GPIO
import time 
#Define Which BCM channels to use
channels = [17,18]
#Set Pinout Mode as BCM 
GPIO.setmode(GPIO.BCM)
GPIO.setup(channels, GPIO.IN)
#Activate Relays
i = 30
while i> 0 :
  time.sleep(.5)
  GPIO.setup(channels, GPIO.OUT)
  time.sleep(.5)
  GPIO.setup(channels, GPIO.IN)
  i-=1






