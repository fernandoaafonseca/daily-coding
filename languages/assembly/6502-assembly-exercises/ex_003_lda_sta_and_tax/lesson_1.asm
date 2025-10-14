; **************************************************************************
; Lesson 1 - Basic 6502 program
; Loads a value into the accumulator and stores it in memory
; **************************************************************************

; **************************************************************************
;   .org $8000        ; Starting address (generic)
; Start:
;   LDA #$05          ; Load immediate value 5 into A
;   STA $0200         ; Store it at memory address $0200
;   BRK               ; Stop execution
;
;   .org $FFFC        ; Reset vector (for completeness)
;   .word Start
; **************************************************************************

; **************************************************************************
; EXERCISE INSTRUCTIONS
; Modify the program to:
; - Load #$0A (decimal 10) into the accumulator.
; - Store it in $0201.
; - Transfer A to X using TAX.
; - Increment X twice (INX two times).
; - Stop execution with BRK.
;
; Then, try to predict the final values of A, X, and the memory positions
; $0200 and $0201.
; (Hint: A and X will be different.)
; **************************************************************************


    processor 6502


    .org $8000          ; Starting address (generic)
Start:
    LDA #$05            ; Load immediate value 5 into A
    STA $0200           ; Store it at memory address $0200
    LDA #10             ; A = 10
    STA $0201           ; Store A at memory address $0201
    TAX                 ; Copy A into X
    INX                 ; Increment X
    INX                 ; Increment X
    BRK                 ; Stop execution

    .org $FFFC        ; Reset vector (for completeness)
    .word Start

; **************************************************************************
; -> ChatGPT:
; Agora, instrução por instrução:
;
; LDA #$05
; A = 5
; Flags: Z=0 (não é zero), N=0 (positivo)
;
; STA $0200
; Mem[$0200] = 5
;
; LDA #10
; A = 10 (em decimal, ou $0A em hexadecimal)
;
; STA $0201
; Mem[$0201] = 10
;
; TAX
; X = A → portanto, X = 10
;
; INX
; X = 11
;
; INX
; X = 12
;
; BRK
; Execução para.
; **************************************************************************

; **************************************************************************
;
; Estado final do processador e da memória
; Elemento      Valor final         Explicação
; A             $0A (10 decimal)    O acumulador nunca mais foi modificado depois do LDA #10.
; X             $0C (12 decimal)    Iniciou em 10, incrementou duas vezes.
; $0200         $05                 Gravado no início, não foi alterado.
; $0201         $0A                 Gravado com o valor do acumulador antes de TAX.
;
; ✅ Suas previsões estavam corretíssimas — você entendeu o comportamento fundamental do registrador A (ele mantém o último valor até ser sobrescrito).
; **************************************************************************


; **************************************************************************
; -> How to compile with DASM:
; dasm lesson_1.asm -f3 -olesson_1.bin
; **************************************************************************