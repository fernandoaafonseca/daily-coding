    LDA #$01
    STA $0200
    LDA #$05
    STA $0201
    LDA #$08
    STA $0202

    ; 3rd line
    LDA #$04
    STA $0240
    LDA #$04
    STA $0241
    LDA #$04
    STA $0242

    LDA #$04
    STA $024f
    LDA #$04
    STA $025f

    ; 4th line
    LDA #$06
    STA $0260
    LDA #$06
    STA $026f
    LDA #$06
    STA $027f

    ; 5th line
    LDA #$07
    STA $0280
    LDA #$07
    STA $0281

    LDA #$07
    STA $028f
    LDA #$07
    STA $029f

    ; 6th line
    LDA #$08
    STA $02a0
    LDA #$08
    STA $02af
    LDA #$08
    STA $02bf

    ; 7th line
    LDA #$09
    STA $02c0
    LDA #$09
    STA $02cf
    LDA #$09
    STA $02df

    ; 3rd last line
    LDA #$0b
    STA $05a0
    LDA #$0b
    STA $05af
    LDA #$0b
    STA $05bf

    ; 2nd last line
    LDA #$0c
    STA $05c0
    LDA #$0c
    STA $05cf
    LDA #$0c
    STA $05df

    ; Last line
    LDA #$0d
    STA $05e0
    LDA #$0d
    STA $05ef
    LDA #$0d
    STA $05ff
