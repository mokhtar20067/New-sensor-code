import time
import os
import sys
import RPi.GPIO as GPIO

import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred,{
'databaseURL' : "https://raspberrypi-11104-default-rtdb.firebaseio.com/"
})
ref = db.reference('Fan State')

FAN_PIN = 20

#def GPIOsetup():
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.setwarnings(False)
    
def fanON():
    GPIO.output(FAN_PIN, 0)
    print ("fan on")
    return()
    sleep(4)
def fanOFF():
    GPIO.output(FAN_PIN, 1)
    print ("fan off")
    return()
fanON()
ref . push({
    "Fan State" : "ON"
    })
print( "Fan State Pushed" )
time.sleep(5)
fanOFF()
ref . push({
    "Fan State" : "OFF "
    })
print( "Fan State Pushed" )