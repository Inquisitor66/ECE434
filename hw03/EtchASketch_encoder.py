#!/usr/bin/env python3
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
import sys

GPIO.cleanup()
bus = smbus.SMBus(1)
matrix = 0x70
encoderXPos = RotaryEncoder(eQEP1)
encoderYPos = RotaryEncoder(eQEP2)
encoderXPos.setAbsolute()
encoderXPos.enable()
encoderYPos.setAbsolute()
encoderYPos.enable()
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)
GPIO.setup("P8_18", GPIO.IN)
GPIO.setup("P8_16", GPIO.IN)

xEncoderPrev = encoderXPos.position
yEncoderPrev = encoderYPos.position

grid = [0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00]

bus.write_i2c_block_data(matrix, 0, grid)

xPos = 1
yPos = 8

def main():
	global xEncoderPrev
	global yEncoderPrev
	while True:
		if encoderXPos.position > xEncoderPrev:
			moveRight()
			xEncoderPrev = encoderXPos.position
		elif encoderXPos.position < xEncoderPrev:
			moveLeft()
			xEncoderPrev = encoderXPos.position
		if encoderYPos.position > yEncoderPrev:
			moveUp()
			yEncoderPrev = encoderYPos.position
		elif encoderYPos.position < yEncoderPrev:
			moveDown()
			yEncoderPrev = encoderYPos.position

def clearScreen(button):
	global grid
	grid = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00]
	bus.write_i2c_block_data(matrix, 0, grid)

def quitGame(button):
	clearScreen(button)
	GPIO.cleanup()
	sys.exit()

def updateGrid():
	global xPos
	global yPos
	global grid
	global matrix
	grid[2*(xPos-1)] = grid[2*(xPos-1)] | (1<<(yPos-1))
	bus.write_i2c_block_data(matrix, 0, grid)
	time.sleep(.1)

def moveRight():
	global xPos
	global matrix
	global grid
	if xPos == 8:
		updateGrid()
	else:
		xPos = xPos + 1
		updateGrid()

def moveLeft():
	global xPos
	global matrix
	global grid
	if xPos == 1:
		updateGrid()
	else:
		xPos = xPos - 1
		updateGrid()

def moveDown():
	global yPos
	global matrix
	global grid
	if yPos == 8:
		updateGrid()
	else:
		yPos = yPos + 1
		updateGrid()

def moveUp():
	global yPos
	global matrix
	global grid
	if yPos == 1:
		updateGrid()
	else:
		yPos = yPos - 1
		updateGrid()

GPIO.add_event_detect("P8_18", GPIO.RISING, callback = clearScreen, bouncetime = 100)
GPIO.add_event_detect("P8_16", GPIO.RISING, callback = quitGame, bouncetime = 100)

main()
