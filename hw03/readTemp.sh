#!/bin/bash

while :
do
	echo $(($(i2cget -y 1 0x48) *9/5+32))
	echo $(($(i2cget -y 1 0x49)*9/5+32))
	sleep 1s
done
