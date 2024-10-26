; ==========================================================================
; The screen is 32x32 pixels in size.
; Each pixel is represented by one byte, which determines its color.
; ==========================================================================
; The available colors are:
;   $00: Black
;   $01: White
;   $02: Red
;   $03: Cyan
;   $04: Purple
;   $05: Green
;   $06: Blue
;   $07: Yellow
;   $08: Orange
;   $09: Brown
;   $0a: Light red
;   $0b: Dark gray
;   $0c: Grey
;   $0d: Light green
;   $0e: Light blue
;   $0f: Light gray
; ==========================================================================
;
; GPU Memory locations:
;   $0200 to $05ff
;   (1032 locations in total) map to screen pixels.
; It is divided into 4 pages, with 8 strips of 32 "pixels" in each.
; Each page has its own most significant byte and contains 256 bytes
; ($00 to $FF).

; Source: https://gist.github.com/kjayawar/94c1341cc1409b572259e641ea4d6e79
; Source: https://github.com/skilldrick/easy6502/tree/gh-pages
; ==========================================================================

; ==========================================================================
; First line containing all 16 available colors in order ($00 to $0F),
; filling the first 16 pixels of the screen from top-left to top-middle
; ($200 to $20F).
; ==========================================================================
FillFirstLineWith16Colors:
    LDA #$00
    STA $200
    LDA #$01
    STA $201
    LDA #$02
    STA $202
    LDA #$03
    STA $203
    LDA #$04
    STA $204
    LDA #$05
    STA $205
    LDA #$06
    STA $206
    LDA #$07
    STA $207
    LDA #$08
    STA $208
    LDA #$09
    STA $209
    LDA #$0a
    STA $20a
    LDA #$0b
    STA $20b
    LDA #$0c
    STA $20c
    LDA #$0d
    STA $20d
    LDA #$0e
    STA $20e
    LDA #$0f
    STA $20f

; ==========================================================================  
; Beginning at the third line, a "drawing" of my first name in red color ($02).
; Well, I gave up as I was tired at the 5th letter hard coding de pixels. XD
; Anyway, it was a fun exercise to get my brain used to the hexadecimal system.
; ==========================================================================  
DrawMyNameInRed:
    LDA #$02
    DrawLetterF:
        STA $0241
        STA $0242
        STA $0243

        STA $0261

        STA $0281
        STA $0282

        STA $02a1

        STA $02c1
    
    DrawLetterE:
        STA $0245
        STA $0246
        STA $0247
        
        STA $0265

        STA $0285
        STA $0286

        STA $02a5

        STA $02c5	
        STA $02c6
        STA $02c7

    DrawLetterR:
        STA $0249
        STA $024a
        STA $024b
        
        STA $0269

        STA $026c

        STA $0289
        STA $028a
        STA $028b

        STA $02a9
        STA $02ab

        STA $02c9	
        STA $02cc

    DrawLetterN:
        STA $0349
        STA $034c
        
        STA $0369
        STA $036a
        STA $036c

        STA $0389

        STA $038a
        STA $038b
        STA $038c

        STA $03a9
        STA $03ab
        STA $03ac

        STA $03c9	
        STA $03cc

    DrawLetterA:
        STA $034f
        STA $0350
        
        STA $036e
        STA $0371

        STA $038e
        STA $038f
        STA $0390
        STA $0391

        STA $03ae
        STA $03b1

        STA $03ce
        STA $03d1
