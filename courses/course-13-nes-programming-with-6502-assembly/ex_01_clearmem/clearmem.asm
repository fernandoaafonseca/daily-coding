; **************************************************************************
; The iNES header (contains a total of 16 bytes with the flags at $7F00).
; **************************************************************************

; **************************************************************************
; Source:
; https://www.nesdev.org/wiki/INES
; **************************************************************************

; **************************************************************************
; -> The format of the header is as follows:
;
; Bytes		Description
;
; 0-3		Constant $4E $45 $53 $1A (ASCII "NES" followed by MS-DOS end-of-file)
; 4			Size of PRG ROM in 16 KB units
; 5			Size of CHR ROM in 8 KB units (value 0 means the board uses CHR RAM)
; 6			Flags 6 – Mapper, mirroring, battery, trainer
; 7			Flags 7 – Mapper, VS/Playchoice, NES 2.0
; 8			Flags 8 – PRG-RAM size (rarely used extension)
; 9			Flags 9 – TV system (rarely used extension)
; 10		Flags 10 – TV system, PRG-RAM presence (unofficial, rarely used extension)
; 11-15		Unused padding (should be filled with zero, but some rippers put their name across bytes 7-15)
; **************************************************************************

.segment "HEADER"
.org $7FF0						; Location of the iNES header in the cartridge

; **************************************************************************
; Bytes 0-3 - Constant $4E $45 $53 $1A (ASCII "NES" followed by MS-DOS end-of-file)
;
; It could use only one line like this:
; .byte $43,$45,$53,$1A		; 4 bytes with the chars 'N', 'E', 'S', '\n'
; **************************************************************************
.byte $4E						; Add the byte "N"
.byte $45						; Add the byte "E"
.byte $53						; Add the byte "S"
.byte $1A						; Add the byte "break line" (in MS-DOS format)

; **************************************************************************
; Byte 4 - Size of PRG ROM in 16 KB units
; **************************************************************************
.byte $02						; 2x 16 KB of PRG ROM we'll use (= 32 KB -> NROM)

; **************************************************************************
; Byte 5 - Size of CHR ROM in 8 KB units (value 0 means the board uses CHR RAM)
; **************************************************************************
.byte $01						; 1x 8 KB of CHR ROM we'll use (= 8 KB)

; **************************************************************************
; Flags 6 – Mapper, mirroring, battery, trainer
;
; 76543210
; ||||||||
; |||||||+- Nametable arrangement: 0: vertical arrangement ("horizontal mirrored") (CIRAM A10 = PPU A11)
; |||||||                          1: horizontal arrangement ("vertically mirrored") (CIRAM A10 = PPU A10)
; ||||||+-- 1: Cartridge contains battery-backed PRG RAM ($6000-7FFF) or other persistent memory
; |||||+--- 1: 512-byte trainer at $7000-$71FF (stored before PRG data)
; ||||+---- 1: Alternative nametable layout
; ++++----- Lower nybble of mapper number
; **************************************************************************
.byte %0000000					; Horizontal mirroring, no battery, mapper 0

; **************************************************************************
; Flags 7 – Mapper, VS/Playchoice, NES 2.0
;
; 76543210
; ||||||||
; |||||||+- VS Unisystem
; ||||||+-- PlayChoice-10 (8 KB of Hint Screen data stored after CHR data)
; ||||++--- If equal to 2, flags 8-15 are in NES 2.0 format
; ++++----- Upper nybble of mapper number
; **************************************************************************
.byte %0000000					; Mapper 0, playchoice, no NES 2.0

; **************************************************************************
; Flags 8 – PRG-RAM size (rarely used extension)
;
; 76543210
; ||||||||
; ++++++++- PRG RAM size
; **************************************************************************
.byte $00						; No PRG-RAM

; **************************************************************************
; Flags 9 – TV system (rarely used extension)
;
; 76543210
; ||||||||
; |||||||+- TV system (0: NTSC; 1: PAL)
; +++++++-- Reserved, set to zero
; **************************************************************************
.byte $00						; NTSC TV format

; **************************************************************************
; Flags 10 – TV system, PRG-RAM presence (unofficial, rarely used extension)
;
; 76543210
; ||  ||
; ||  ++- TV system (0: NTSC; 2: PAL; 1/3: dual compatible)
; |+----- PRG RAM ($6000-$7FFF) (0: present; 1: not present)
; +------ 0: Board has no bus conflicts; 1: Board has bus conflicts
; **************************************************************************
.byte $00						; No PRG-RAM

; **************************************************************************
; Flags 11-15 - Unused padding (should be filled with zero, but some rippers put their name across bytes 7-15)
; **************************************************************************
.byte $00,$00,$00,$00,$00	; Unused padding to complete 16 bytes of header


; **************************************************************************
; PRG-ROM code located at $8000.
; **************************************************************************
.segment "CODE"
.org $8000

; **************************************************************************
; It will be executed every time the CPU powers on or resets.
; **************************************************************************
RESET:
	sei							; Disable all IRQ interrupts
	; **************************************************************************
	; The BCD (Binary-Code Decimal) Flag is unsupported by the NES CPU
	; **************************************************************************
	cld							; Clear the Decimal Mode Flag
	lda #$FF					; Load X with literal hexadecimal "FF"
	; **************************************************************************
	; Transfer the value of X to the Stack Pointer
	; "FF" is the bottom of the Stack Pointer -> empty stack
	; **************************************************************************
	txs							; Initialize the Stack Pointer at the end ($01FF)


; **************************************************************************
; Loop all memory positions from $00 to $FF clearing them out.
; **************************************************************************
	lda #0						; Load A with literal decimal "0"
	ldx #$FF					; X = $FF
MemLoop:
	; **************************************************************************
	; Store the value of A (which is always "0") at the memory position
	; "$0,x" (="$0 + the value of X").
	;
	; So:
	; Store the value "0" at "$0 + $FF" (=$FF).
	; Decrement X by 1.
	; Then:
	; Store the value "0" at "$0 + $FE" (=$FE).
	; And so on.
	; **************************************************************************
	sta $0,x					; Store the value of A (zero) into $0+X
	dex							; X-- (Decrement X by 1)
	; **************************************************************************
	; bne: Branch on not equal to zero
	; Z == 0
	; Z Flag (Zero Flag) -> 0 = Result not zero, 1 = Result zero
	; **************************************************************************
	bne MemLoop					; If X is not 0 (Z Flag == 0), loop back to MemLoop

; **************************************************************************
; It will be executed every time we have an NMI interrupt, if we have some.
; **************************************************************************
NMI:
	rti							; Return from interrupt (don't do anything)

; **************************************************************************
; It will be executed every time we have an IRQ interrupt, if we have some.
; **************************************************************************
IRQ:
	rti							; Return from interrupt (don't do anything)


; **************************************************************************
; Points to the label addresses of the interrupt handlers.
; It begins at the "beginning of the end" of the cartridge at "$FFFA",
; then adds 16 bits for every ".word", ending at the address "$FFFF".
; **************************************************************************
.segment "VECTORS"
.org $FFFA						; Address of the end of the cartridge

; **************************************************************************
; ".word" means 2 bytes.
; **************************************************************************
.word NMI						; Address of the NMI (Non-Maskable Iterrupt) handler
.word RESET						; Address of the RESET handler
.word IRQ						; Address of IRQ (Interrupt Request) handler


; **************************************************************************
; -> How to assemble the code
;
; Source code (one or multiple ".asm" files)
;	-> ASSEMBLER -> Object file (one or multiple ".o" files)
;		-> LINKER -> Cartridge (one final ".nes" executable)
;
; Generate an intermediate ".o" (object) file with the ASSEMBLER ("ca65"):
; ca65 clearmem.asm -o clearmem.o
;
; No outputs means "no errors".
;
; The LINKER ("ld65") needs a configuration file (".cfg").
; ld65 -C nes.cfg clearmem.o -o clearmem.nes
;
; To view the raw opcode:
; hexdump clearmem.nes
;
; To run the ROM with the FCEUX emulator:
; fceux clearmem.nes
; **************************************************************************