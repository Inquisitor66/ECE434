#!/bin/bash

cd /sys/class/gpio
echo 12 > export
echo 14 > export
echo in > gpio12/direction
echo in > gpio14/direction

export LED=51
export RESET=12
export DC=13
export CS=5
export BUS=1
sudo bash << EOF
if lsmod | grep -q 'fbtft_device' ; then rmmod fbtft_device; fi
if lsmod | grep -q 'fb_ili9341 ' ; then rmmod --force fb_ili9341; fi
if lsmod | grep -q 'fbtft ' ; then rmmod --force fbtft; fi
config-pin P9_19 gpio
config-pin P9_20 gpio
config-pin P9_18 spi
config-pin P9_21 spi
config-pin P9_22 spi_sclk
config-pin P9_17 spi_cs
sleep 0.1
modprobe fbtft_device name=adafruit28 busnum=$BUS rotate=180 gpios=reset:$RESET,dc:$DC cs=0
while [ ! -e /dev/fb0 ]
do
	echo Waiting for /dev/fb0
	sleep2
done
export FRAMEBUFFER=/dev/fb0
EOF
