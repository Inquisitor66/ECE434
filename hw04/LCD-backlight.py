#!/usr/bin/env python3
import Adafruit_BBIO.PWM as PWM
import sys

LED = "P9_16"

duty = 100
if(len(sys.argv) > 1):
	duty = float(sys.argv[1])

print("duty: " + str(duty))
PWM.start(LED, duty)
