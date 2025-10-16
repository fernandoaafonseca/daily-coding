; ************************************************************************************* ;
; Exercise 3:																			;
;																						;
; This exercise is about transferring values from registers to other registers.			;
; ************************************************************************************* ;

.segment "HEADER"
.org $7FF0
.byte $4E,$45,$53,$1A,$02,$01,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00

.segment "CODE"
.org $8000

Reset:					; TO-DO:
	lda #15				; Load the A register with the literal decimal value 15

	tax					; Transfer the value from A to X
	tay					; Transfer the value from A to Y
	txa					; Transfer the value from X to A
	tya					; Transfer the value from Y to A

 	;; There is no TXY or TXY
 	;; Therefore, we can't transfer directly X to Y or Y to X.
 	;; If we wish to do so, we must go through the A register.

	ldx #6				; Load X with the decimal value 6
	txa					; Transfer the value from X to Y
	tay

	jmp Reset			; Jump to the Reset label to force an infinite loop

NMI:
	rti

IRQ:
	rti

.segment "VECTORS"
.org $FFFA
.word NMI
.word Reset
.word IRQ