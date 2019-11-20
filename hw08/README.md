The purpose of this assignment was to go over some PRU cookbook examples.

The first example was to run example 2. Example 2 starts running by running
'make' and it can be stopped at any time by running 'make stop'. Then we switch the output from USR3 to P9_31. The configuration of P9_31 has to be set to gpio and out for this to work. An LED was attached to make sure that it was toggling. A scope was used to measure how fast the pin can be toggled, which is about every 80 ns. There isn't a jitter, but it is very unstable. The figure for this measurement is "2.6BlinkingLED.png".  

Next, I started on example 5 and using the PRU GPIO. To use all of the following examples, this must be run first:  
>export PRUN=0  

I used:  
>export TARGET=pwm1  

to start the first of the examples. The scope capture "5.3pwmgenerator.png" is the 50 MHz waveform from this example when "make" is run. The waveform is not stable at all, but it doesn't have any jitter. When it comes to standard deviation, I am unsure about what to do this between, so I chose the regular GPIO and PRU GPIO, which has a std deviation of 42.43.  

Next, pwm4 was set as the target. It runs a PWM output on pins P9_31, P9_30, P9_28, and P9_28 by using the first 4 bits on __R30. The fastest times can be seen in "5.4fastest4channel.png". The highest frequency on a single channel is about 50 MHz, so split between 4, the fastest is only about 12.5 MHz. There is jitter in waveforms, but they are stable. pwm-test.c does not work to change the times in my experience.

Finally, input1 was set as the target and a function generator was hooked up and a square wave was inserted into P9_25 and set as an input using __R31. In "5.9readinganinput.png" it can be seen that there is about a 35 ns delay between reading from __R31 and being able to write to __R30.

I could not get sine1.c to go through a low pass filter and output a good looking waveform, so I have not completed this section.

## Prof. Yoder's comments

Your plot look mostly good, tough the section 2.6 plot has too much decay in it.

Grade:  10/10
