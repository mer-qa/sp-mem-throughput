/*
 *  linux/arch/arm/lib/memchr.S
 *
 *  Copyright (C) 1995-2000 Russell King
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation.
 *
 *  ASM optimised string functions
 */
#include "linux-linkage.h"
#include "arm-asm-assembler.h"

	.text
	.align	5
ENTRY(linux_arm_memchr)
1:	subs	r2, r2, #1
	bmi	2f
	ldrb	r3, [r0], #1
	teq	r3, r1
	bne	1b
	sub	r0, r0, #1
2:	movne	r0, #0
	mov	pc, lr
ENDPROC(linux_arm_memchr)

#if defined(__linux__) && defined(__ELF__)
.section .note.GNU-stack,"",%progbits
#endif
