#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import argparse
import curses
import sys
from curses import wrapper

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

parser = argparse.ArgumentParser()
parser.add_argument("xDim", help = "The Width of the Etch A Sketch board", type = int)
parser.add_argument("yDim", help = "The Height of the Etch A Sketch board", type = int)
args = parser.parse_args()

GPIO.setup("P8_26", GPIO.IN)
GPIO.setup("P8_24", GPIO.IN)
GPIO.setup("P8_24", GPIO.IN)
GPIO.setup("P8_23", GPIO.IN)
GPIO.setup("P8_22", GPIO.IN)
GPIO.setup("P8_21", GPIO.IN)
xPos = 1
yPos = 1

def resetScreen(stdscr):
    for i in range (1, args.xDim+1):
        stdscr.addstr(0,2*i+1,'{} '.format(i))
    for i in range (1, args.yDim+1):
        stdscr.addstr(i,0,'{}:'.format(i))

def buttonPress(button,stdscr):
    if button == "P8_26":
        sys.exit(0)
    elif button == "P8_25":
        stdscr.clear()
        resetScreen(stdscr)
    elif button == "P8_24":
        if xPos == args.xDim:
            stdscr.refresh()
        else:
            xPos = xPos + 1
            stdscr.addstr(yPos,2*xPos+1,'X')
    elif button == "P8_23":
        if yPos == args.yDim:
            stdscr.refresh()
        else:
            yPos = yPos + 1
            stdscr.addstr(yPos,2*xPos+1,'X')
    elif button == "P8_22":
        if yPos == 1:
            stdscr.refresh()
        else:
            yPos = yPos - 1
            stdscr.addstr(yPos,2*xPos+1,'X')
    elif button == "P8_21":
        if xPos == 1:
            stdscr.refresh()
        else:
            xPos = xPos - 1
            stdscr.addstr(yPos,2*xPos+1,'X')


GPIO.add_event_detect("P8_26", GPIO.RISING, callback = buttonPress(stdscr))
GPIO.add_event_detect("P8_25", GPIO.RISING, callback = buttonPress(stdscr))
GPIO.add_event_detect("P8_24", GPIO.RISING, callback = buttonPress(stdscr))
GPIO.add_event_detect("P8_23", GPIO.RISING, callback = buttonPress(stdscr))
GPIO.add_event_detect("P8_22", GPIO.RISING, callback = buttonPress(stdscr))
GPIO.add_event_detect("P8_21", GPIO.RISING, callback = buttonPress(stdscr))



def main(stdscr):
    resetScreen(stdscr)
    stdscr.addstr(1,3,'X')
    while True:
        stdscr.refresh()

main()
