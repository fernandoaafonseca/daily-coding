; ************************************************************************************* ;
; Exercise 2:																			;
;																						;
; Your goal here is to just store some values into zero-page memory positions.			;
; ************************************************************************************* ;

.segment "HEADER"
.org $7FF0
.byte $4E,$45,$53,$1A,$02,$01,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00

.segment "CODE"
.org $8000

Reset:					; TO-DO:
	lda #$A				; Load the A register with the literal hexadecimal value $A
	lda #%11111111		; Load the X register with the decimal value %11111111
	sta $80				; Store the value in the A register into memory address $80
	stx $81				; Store the value in the X register into memory address $81

NMI:
	rti

IRQ:
	rti

.segment "VECTORS"
.org $FFFA
.word NMI
.word Reset
.word IRQ