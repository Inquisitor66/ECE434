#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import argparse
import curses
import sys
from curses import wrapper

stdscr = None
GPIO.cleanup()
LOOP = True
parser = argparse.ArgumentParser()
parser.add_argument("xDim", help = "The Width of the Etch A Sketch board", type = int)
parser.add_argument("yDim", help = "The Height of the Etch A Sketch board", type = int)
args = parser.parse_args()

GPIO.setup("P8_18", GPIO.IN)
GPIO.setup("P8_16", GPIO.IN)
GPIO.setup("P8_12", GPIO.IN)
GPIO.setup("P8_10", GPIO.IN)
GPIO.setup("P8_14", GPIO.IN)
GPIO.setup("P9_11", GPIO.IN)
xPos = 1
yPos = 1

def resetScreen(stdscr):
    for i in range (1, args.xDim+1):
        stdscr.addstr(0,2*i+1,'{} '.format(i))
    for i in range (1, args.yDim+1):
        stdscr.addstr(i,0,'{}:'.format(i))

def buttonPress(button):
    global xPos
    global yPos
    global LOOP
    if button == "P8_18":
        GPIO.cleanup()
        print(chr(27) + "[2J")
        LOOP = False
    elif button == "P8_16":
        stdscr.clear()
        resetScreen(stdscr)
    elif button == "P9_11":
        if xPos == args.xDim:
            stdscr.refresh()
        else:
            xPos = xPos + 1
            stdscr.addstr(yPos,2*xPos+1,'X')
    elif button == "P8_12":
        if yPos == args.yDim:
            stdscr.refresh()
        else:
            yPos = yPos + 1
            stdscr.addstr(yPos,2*xPos+1,'X')
    elif button == "P8_10":
        if yPos == 1:
            stdscr.refresh()
        else:
            yPos = yPos - 1
            stdscr.addstr(yPos,2*xPos+1,'X')
    elif button == "P8_14":
        if xPos == 1:
            stdscr.refresh()
        else:
            xPos = xPos - 1
            stdscr.addstr(yPos,2*xPos+1,'X')


GPIO.add_event_detect("P8_18", GPIO.RISING, callback = buttonPress, bouncetime = 100)
GPIO.add_event_detect("P8_16", GPIO.RISING, callback = buttonPress, bouncetime = 100)
GPIO.add_event_detect("P8_12", GPIO.RISING, callback = buttonPress, bouncetime = 100)
GPIO.add_event_detect("P8_10", GPIO.RISING, callback = buttonPress, bouncetime = 100)
GPIO.add_event_detect("P8_14", GPIO.RISING, callback = buttonPress, bouncetime = 100)
GPIO.add_event_detect("P9_11", GPIO.RISING, callback = buttonPress, bouncetime = 100)



def main(stdscr_temp):
    global stdscr
    global LOOP
    stdscr = stdscr_temp
    resetScreen(stdscr)
    stdscr.addstr(1,3,'X')
    while LOOP:
        stdscr.refresh()

wrapper(main)
