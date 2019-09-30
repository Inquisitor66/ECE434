This homework is split into two parts, Reading 2 Temperature Sensors and
porting the etch-A-Sketch onto an 8x8 LED Matrix.

Firstly, the included setup.sh file should be run to configure all the pins
correctly.

To read values correctly when readTemp.sh is run, both temperature sensors
should be hooked up to the I2C 1 bus. Then the address port on one should be 
left open, and the other should be grounded. Then when running readTemp.sh,
the values should be displayed.

To run the LED Etch-A-Sketch, the Matrix should also be hooked up to the I2C 1
bus. Then 2 Rotary Encoders need to be hooked up. One on eQEP1 port on pins 
P8_33 and P8_35. Then the second on eQEP2 port using P8_11 and P8_12, which uses
the alternate "b" positioning.
