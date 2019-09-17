#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_30", GPIO.OUT)
GPIO.setup("P8_29", GPIO.OUT)
GPIO.setup("P8_28", GPIO.OUT)
GPIO.setup("P8_27", GPIO.OUT)
GPIO.setup("P8_24", GPIO.IN)
GPIO.setup("P8_23", GPIO.IN)
GPIO.setup("P8_22", GPIO.IN)
GPIO.setup("P8_21", GPIO.IN)

def buttonEvent(button):
    if button == "P8_24":
        GPIO.output("P8_30",GPIO.input("P8_24"))
    if button == "P8_23":
        GPIO.output("P8_29",GPIO.input("P8_23"))
    if button == "P8_22":
        GPIO.output("P8_28",GPIO.input("P8_22"))
    if button == "P8_21":
        GPIO.output("P8_27",GPIO.input("P8_21"))

GPIO.add_event_detect("P8_24", GPIO.BOTH, callback = buttonEvent)
GPIO.add_event_detect("P8_23", GPIO.BOTH, callback = buttonEvent)
GPIO.add_event_detect("P8_22", GPIO.BOTH, callback = buttonEvent)
GPIO.add_event_detect("P8_21", GPIO.BOTH, callback = buttonEvent)


while True:
    continue
