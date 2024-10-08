    processor 6502

    seg code
    org $F000       ; Define the code origin at $F00

Start:              ; Labels are indented to the left
    sei             ; Disable interrupts
    cld             ; Disable the BCD decimal math mode
    ldx #$FF        ; Loads the X register with #$FF
    txs             ; Transfer the X register to the (S)tack pointer

; **************************************************************************
; Clear the Page Zero region ($00 to $FF).
; Meaning the entire RAM and also the entire TIA registers.
; **************************************************************************

    lda #0          ; A = 0. Load the A register with the literal (#) value 0
    ldx #$FF        ; X = #$FF. X will be the loop counter
    sta $FF         ; Make sure $FF is zeroed before the loop starts

MemLoop:
    dex             ; X--. Decrements from #$FF to #00
    sta $0,X        ; Store the value of A in memory position $0 + whatever is inside X
    bne MemLoop     ; If branch not equal (bne) to 0, go back, i.e. loop until X==0 (z-flag is set)

; **************************************************************************
; Fill the ROM size with exactly 4KB, by jumping to position $FFFC,
; writing 2 bytes (.word) with "Start" and another 2 bytes with "Start".
; The code below is a requirement for every Atari 2600 cartridge.
; **************************************************************************
    
    org $FFFC       ; Jump to the ROM $FFFC (the bottom of the Atari 2600 cartridge)
    .word Start     ; Reset vector at $FFFC (where the program starts)
    .word Start     ; Interrupt vector at $FFFE (unused in the VCS)