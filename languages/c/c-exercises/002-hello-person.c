/*
- Compile the code including the CS50 library:
gcc -Ilibs 002-hello-person.c libs/cs50/cs50.c -o 002-hello-person
*/


#include <cs50/cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");

    printf("Hello, %s!\n", answer);

    printf("Press any key to exit...");
    getchar();

    return 0;
}