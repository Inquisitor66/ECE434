#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_17", GPIO.OUT)
GPIO.setup("P8_11", GPIO.OUT)
GPIO.setup("P8_9", GPIO.OUT)
GPIO.setup("P8_7", GPIO.OUT)
GPIO.setup("P8_14", GPIO.IN)
GPIO.setup("P8_10", GPIO.IN)
GPIO.setup("P8_12", GPIO.IN)
GPIO.setup("P9_11", GPIO.IN)

def buttonEvent(button):
    if button == "P8_14":
        GPIO.output("P8_7",GPIO.input("P8_14"))
	print("Light\n")
    if button == "P8_10":
        GPIO.output("P8_9",GPIO.input("P8_10"))
    if button == "P8_12":
        GPIO.output("P8_11",GPIO.input("P8_12"))
    if button == "P9_11":
	print("Light\n")
        GPIO.output("P8_17",GPIO.input("P9_11"))

GPIO.add_event_detect("P8_14", GPIO.BOTH, callback = buttonEvent)
GPIO.add_event_detect("P8_10", GPIO.BOTH, callback = buttonEvent)
GPIO.add_event_detect("P8_12", GPIO.BOTH, callback = buttonEvent)
GPIO.add_event_detect("P9_11", GPIO.BOTH, callback = buttonEvent)


while True:
    continue
