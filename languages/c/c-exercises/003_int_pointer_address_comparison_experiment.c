/*
- Some Shell commands:
    - ls -> list files and folders
    - cd -> change directory
    - cd.. -> change to the parent directory
    - mkdir -> make directory
    - mv -> move or rename file or folder
        - To move:
            mv file-name.c folder-name
            - To move to the parent directory:
                mv file-name.c ..
        - To rename:
            mv old-name.c new-name.c
    - cp -> copy file
        cp file-name.c backup-name.c
    - rm -> remove file
    - rm dir -> remove directory
    - ./file-name -> run the binary file


- Data types and format codes:
    - bool
    - char
        - %c
    - string
        - %s
    - int
        - %i
    - long
        - $li
    - double
    - float
        - %f

- CS50 library to get inputs:
    - get_char()
    - get_string()
    - get_int()
    - get_long()
    - get_double()
    - get_float()
*/


/**
 * This code was written to explore a specific hypothesis:
 * "What happens if I compare an integer variable to the memory address of a string (char *) in C?"
 * 
 * In C, char * (a string or character pointer) is actually just a memory address — a number representing
 * where in memory the string begins. An int is also just a number. The user was wondering:
 * 
 * - If I assign an int x with the value of the address of y (a char *), and then compare x and y, will they be equal?
 * - Does C block this kind of comparison because they're different types?
 * - Could the int and the address match purely by coincidence?
 * 
 * The conclusion is:
 * - C allows this comparison (it gives a compiler warning, but still compiles and runs).
 * - The comparison will return true if the integer x holds the same numeric value as the address stored in y.
 * - C doesn't care about type safety at runtime for this; it just compares the bits.
 * - This is generally a bad idea unless you really intend to compare a number with an address.
 * 
 * The program prints whether x holds the same value as the address of y.
 * It pauses at the end so the output can be read before the console closes.
 */

#include <stdio.h>
#include <stdint.h>

int main(void)
{
    char *y = "hello";
    int x = (int)(uintptr_t)y;  // Forcing x to hold the numeric value of y's memory address

    if (x == (int)(uintptr_t)y)
    {
        printf("The values are equal (x holds the same number as y's address)\n");
    }
    else
    {
        printf("The values are different\n");
    }
    
    getchar();  // Wait for the user to press Enter before closing

    return 0;
}