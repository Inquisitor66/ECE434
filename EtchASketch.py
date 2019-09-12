#!/usr/bin/env python3
import argparse
import curses
from curses import wrapper


parser = argparse.ArgumentParser()
parser.add_argument("xDim", help = "The Width of the Etch A Sketch board", type = int)
parser.add_argument("yDim", help = "The Height of the Etch A Sketch board", type = int)
args = parser.parse_args()

def main(stdscr):
    xPos = 1
    yPos = 1
    for i in range (1, args.xDim+1):
        stdscr.addstr(0,2*i+1,'{} '.format(i))
    for i in range (1, args.yDim+1):
        stdscr.addstr(i,0,'{}:'.format(i))
    while True:
        stdscr.refresh()
        input = stdscr.getch()
        if input == ord('w'):
            if yPos == 1:
                stdscr.refresh()
            else:
                yPos = yPos - 1
                stdscr.addstr(yPos,2*xPos,'X')
        elif input == ord('d'):
            if xPos == args.xDim + 1:
                stdscr.refresh()
            else:
                xPos = xPos + 1
                stdscr.addstr(yPos,2*xPos,'X')
        elif input == ord('s'):
            if yPos == args.yDim:
                stdscr.refresh()
            else:
                yPos = yPos + 1
                stdscr.addstr(yPos,2*xPos,'X')
        elif input == ord('a'):
            if xPos == 1:
                stdscr.refresh()
            else:
                xPos = xPos - 1
                stdscr.addstr(yPos,2*xPos,'X')
        elif input == ord('q'):
            break
        elif input == ord('e'):
            stdscr.clear()
            for i in range (1, args.xDim+1):
                stdscr.addstr(0,2*i+1,'{} '.format(i))
            for i in range (1, args.yDim+1):
                stdscr.addstr(i,0,'{}:'.format(i))

wrapper(main)
