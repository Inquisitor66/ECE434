#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

#define PRUN 1_1

volatile register uint32_t __R30;
volatile register uint32_t __R31;

void main(void)
{
		// Select which pin to toggle.;
        uint32_t gpio2 = P9_31;
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	while (1) {
				// Set the GPIO pin to 1
		__R30 |= gpio2;
                __delay_cycles(1);
		
                __R30 &= ~gpio2;		// Clearn the GPIO pin
		__delay_cycles(0);
	}
}

