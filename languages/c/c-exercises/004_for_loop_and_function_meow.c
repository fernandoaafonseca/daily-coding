#include <stdio.h>

void meow(void);

int main(void){
    for (int i = 0; i < 3; i++){
        meow();
    }
    int my_number = 1;

    getchar();
}

void meow(void) {
    printf("Meow!\n");
}