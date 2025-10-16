; *****************************************************************************	;
; Exercise 1:																	;
;																				;
; Your goal here is simply load the processor registers A, X and Y with			;
; some values.																	;
; *****************************************************************************	;

.segment "HEADER"
.org $7FF0
.byte $4E,$45,$53,$1A,$02,$01,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00

.segment "CODE"
.org $8000

Reset:			; TO-DO:
	lda #$82	; Load the A register with the literal hexadecimal value $82
	ldx #82		; Load the X register with the literal decimal value 82
	ldy $82		; Load the Y register with the value that is inside memory position $82

NMI:
	rti

IRQ:
	rti

.segment "VECTORS"
.org $FFFA
.word NMI
.word Reset
.word IRQ


; ca65 warmup_01.asm -o warmup_01.o
; d65 -C nes.cfg warmup_01.o -o warmup_01.nes