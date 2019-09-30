#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <signal.h>

#define GPIO1_START_ADDR 0x4804C000
#define GPIO1_END_ADDR   0x4804e000
#define GPIO1_SIZE (GPIO1_END_ADDR - GPIO1_START_ADDR)

#define GPIO_SETDATAOUT 0x194
#define GPIO_CLEARDATAOUT 0x190
#define GPIO_OE 0x134
#define GPIO_DATAIN 0x138
#define USR3 (1<<24)
#define USR1 (1<<22)
#define BTN1 (1<<12)
#define BTN2 (1<<14)

int main(int argc, char *argv[]) {
	volatile void *gpio_addr;
	volatile unsigned int *gpio_oe_addr;
	volatile unsigned int *gpio_datain;
	volatile unsigned int *gpio_setdataout_addr;
	volatile unsigned int *gpio_cleardataout_addr;
	unsigned int reg;

	int fd = open("/dev/mem", O_RDWR);
	gpio_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd,
			GPIO1_START_ADDR);
	gpio_oe_addr = gpio_addr + GPIO_OE;
	gpio_datain = gpio_addr + GPIO_DATAIN;
	gpio_setdataout_addr = gpio_addr + GPIO_SETDATAOUT;
	gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;

	reg = *gpio_oe_addr;
	reg &= ~USR3;
	reg &= ~USR1;
	*gpio_oe_addr = reg;
	
	while(1) {
		if(*gpio_datain & BTN1) {
			*gpio_setdataout_addr = USR3;
		} else {
			*gpio_cleardataout_addr = USR3;
		}
		if(*gpio_datain & BTN2) {
			*gpio_setdataout_addr = USR1;
		} else {
			*gpio_cleardataout_addr = USR1;
		}
		usleep(1000);
	}
	munmap((void *)gpio_addr, GPIO1_SIZE);
	close(fd);
	return 0;
}
