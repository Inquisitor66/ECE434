#!/bin/sh

while :
do
	i2cget -y 1 0x48
	i2cget -y 1 0x49
	sleep 1s
done
