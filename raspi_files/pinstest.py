
import RPi.GPIO as GPIO
import time 
#Define Which BCM channels to use
channels = [17,18]
#Set Pinout Mode as BCM 
GPIO.setmode(GPIO.BCM)
GPIO.setup(channels, GPIO.IN)
#Activate Relays
time.sleep(1)
GPIO.setup(channels, GPIO.OUT)
time.sleep(1)
GPIO.setup(channels, GPIO.IN)
time.sleep(1)
GPIO.setup(channels, GPIO.OUT)
time.sleep(1)
GPIO.setup(channels, GPIO.IN)
time.sleep(1)
GPIO.setup(channels, GPIO.OUT)
time.sleep(1)
GPIO.setup(channels, GPIO.IN)
time.sleep(1)
GPIO.setup(channels, GPIO.OUT)
time.sleep(1)
GPIO.setup(channels, GPIO.IN)
time.sleep(1)
GPIO.setup(channels, GPIO.OUT)
time.sleep(1)
GPIO.setup(channels, GPIO.IN)
time.sleep(1)
GPIO.setup(channels, GPIO.OUT)
time.sleep(1)
GPIO.setup(channels, GPIO.IN)





