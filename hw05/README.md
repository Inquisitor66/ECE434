The purpose of this assignment is to create a makefile, install a kernel source, do some cross compiling, and go through 3 kernel module examples.

For the Makefile, simply change into the 'make' directly and run:  
>make all  

and to run the program, use:  
>./app.arm  

and to clean up the directory:
>make clean  

The kernel source is installed into the bb-kernel directory. The cross-compiling needs crossCompileEnv.sh and helloWorld.c. Finally, the outputs to the kernel modules are as below.

Host computer helloWorld.c output:
>Hello, World? Main is executing at 0x55e081fe96aa  
>This address (0x7ffef7b5b1c0) is in our stack frame  
>This address (0x55e0821ea018) is in our bss section  
>This address (0x55e0821ea010) is in our data section  

Bone computer helloWorld.c output:
>Hello, World! Main is executing at 0x1040c  
>This address (0xbebbcc54) is in our stack frame  
>This address (0x21030) is in our bss section  
>This address (0x21028) is in our data section  

## Kernel Installation:  
Part 1 insmod output of the hello.ko function:  
>[Oct22 22:28] EBB: Hello world from the BBB LKM!  

Part 1 rmmod output of the hello.ko function:  
>[Oct22 22:28] EBB: Hello world from the BBB LKM!  
>[Oct22 22:29] EBB: Goodbye world from the BBB LKM!  

Part 1 named insmod output of the hello.ko function:  
>[  +0.006569] EBB: Hello Dalton from the BBB LKM!  

Part 1 named rmmod output of the hello.ko function:  
>[  +0.006569] EBB: Hello Dalton from the BBB LKM!
>[ +23.211250] EBB: Goodbye Dalton from the BBB LKM!

Part 2 insmod ebbchar.c terminal outputs:  
>[Oct22 22:46] EBBChar: Initializing the EBBChar LKM  
>[  +0.000039] EBBChar: registered correctly with major number 240  
>[  +0.000121] EBBChar: device class registered correctly  
>[  +0.000336] EBBChar: device class created correctly

Part 2 test ebbchar.c terminal outputs:  
Type in a short string to send to the kernel module:
This is a Test!
Writing message to the device [This is a Test!].
Press ENTER to read back from the device...

Reading from the device...
The received message is: [This is a Test!]
End of the program  

Part 2 rmmod ebbchar.c terminal outputs:  
>[Oct22 22:46] EBBChar: Initializing the EBBChar LKM  
>[  +0.000039] EBBChar: registered correctly with major number 240  
>[  +0.000121] EBBChar: device class registered correctly  
>[  +0.000336] EBBChar: device class created correctly  
>[Oct22 22:48] EBBChar: Device has been opened 1 time(s)  
>[  +7.185136] EBBChar: Received 15 characters from the user  
>[  +1.436145] EBBChar: Sent 15 characters to the user  
>[  +0.000545] EBBChar: Device successfully closed

## Prof. Yoder's comments

Got it.

Late:  -2
Grade:  8/10
