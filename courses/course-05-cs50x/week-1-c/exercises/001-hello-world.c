/*
    - Using cs50.dev:
        - Create a file:
            code hello.c
    
        - Compile a code:
            make hello
    
        - Run the compiled file:
            ./hello
    
    - Documentation:
    manual.cs50.io
*/

#include <stdio.h>

int main(void) {
    printf("Hello, world!\n");

    printf("Press any key to exit...");
    getchar();
}