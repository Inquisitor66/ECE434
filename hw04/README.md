The purpose of this homework was to interface with an LCD screen to display images,
rotate those images, add text to those images, play a movie, rotate that movie,
and display text onto the LCD screen.

To start, setup.sh needs to be run using:
>./setup.sh

Then, the LCD screen needs to be hooked up correctly:  

- MISO to P9_21  
- LED to P9_16
- SCK to P9_22
- MOSI to P9_18
- D/C to P9_19
- RESET to P9_20
- CS to P9_17
- GND to P9_2
- VCC to P9_4

After the LCD is correctly hooked up, the backlight needs to be set up:  
>./LCD-backlight.py  

to display boris on the screen:  
>fbi -noverbose -T 1 -a boris.png  

to display boris rotated:
>./rotateBoris.sh  

to display boris with a caption:
>./magickImage.sh  

to display text onto the LCD:
>./myName.sh  

to play the hubble movie:  
>mplayer hst_1.mpg  

to play the hubble movie rotated 90 degrees:  
>mplayer -vf rotate=1 hst_1.mpg  

Beyond this, another aspect of this assignment was to use mmap to control an LED. Firstly, the board must be setup correctly which entails:  
- A button hooked up to GPIO1_12 which is P8_12
- A button hooked up to GPIO1_14 which is P8_16  

Once hooked up, the mmapGPIO.c file needs to be compiled using:  
>gcc mmapGPIO.c mmapGPIO  

then the program is begun using:
>./mmapGPIO  

at which point pressing either of the buttons will turn on either the USR1 or USR3 LEDs on the Beaglebone. Below we also have the Memory map table:  

|   AM335S  | Memory Map  |
|-----------|-------------|
|0x4000_0000|   Boot ROM  |
|0x402F_0400|SRAM Internal|
|0x8000_0000| EMIF0 SDRAM |
|0x44E0_7000|    GPIO0    |
|0x44E0_9000|    UART0    |
|0x4802_2000|    UART1    |
|0x4802_4000|    UART2    |
|0x4804_C000|    GPIO1    |
|0x481A_6000|    UART3    |
|0x481A_8000|    UART4    |
|0x481A_A000|    UART5    |
|0x481A_C000|    GPIO2    |
|0x481A_E000|    GPIO3    |

## Prof. Yoder's comments

README missing.  LCD was demoed.

Grade:  2/10

## Prof. Yoder's new comments
Much more complete.  Photo's of LCD are missing.

Late:  -3
Grade:  5/10