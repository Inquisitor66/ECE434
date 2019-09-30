#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import argparse
import time

GPIO.cleanup()
parser = argparse.ArgumentParser()
parser.add_argument("delay", help = "The number of seconds you would like to delay", type = float)
args = parser.parse_args()

GPIO.setup("P9_12", GPIO.OUT)

while True:
	GPIO.output("P9_12", GPIO.HIGH)
	time.sleep(args.delay)
	GPIO.output("P9_12", GPIO.LOW)
	time.sleep(args.delay)
