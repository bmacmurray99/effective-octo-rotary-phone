#!/usr/bin/python
import Adafruit_DHT
import requests, math, time,subprocess, datetime
from random import *
import RPi.GPIO as GPIO

timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
# Get readings from DHT22 sensor on BCM pin #2 in % humidity and Celsius 
hum, temp =  Adafruit_DHT.read_retry(22,2)

#Define POST request parameters
payload = {
	#'user':'razbox',
	#'password':'password',snake
	'temp':temp,
	'hum':hum,
	'time': str(timestamp),
	'lights': 1,
	'fans':0
}
#Define BCM Channels
channels = [24,25]
#send request


sendData = requests.post('http://flyingtoastersunlimited.pythonanywhere.com/update',
data = payload)
sendData.raise_for_status()
#confirm request is good, build error logging later. 
print(sendData.status_code)
print(timestamp,hum,temp)
#Set Pinout Mode as BCM 


GPIO.setmode(GPIO.BCM)
if int(temp) > 25 or int(hum) > 80 and GPIO.function() != 'GPIO.OUT':
	GPIO.setup(channels, GPIO.OUT)
	#Set Pinout Mode as BCM 
elif int(temp) <= 25 or int(hum) <= 80 and GPIO.function() != 'GPIO.IN':
	GPIO.setup(channels, GPIO.IN)
	GPIO.cleanup() 





#Generates 24 hours of fake data

	"""

def fake_data():
	hour = 0
	pload = {
	'temp':20,
	'hum':90,
	'time':'',
	'lights': 1,
	'fans':0
}

	for i in range(0,24):
		fake_time = '2017-12-29 '+str(hour)+':11:11'
		pload['time'] = fake_time
	
		postData = requests.post('http://flyingtoastersunlimited.pythonanywhere.com/update',
data = pload)
		postData.raise_for_status()
		pload['temp'] = pload['temp']+1
		pload['hum'] = pload['hum']-1
		hour = hour + 1
		


	


fake_data()

"""
