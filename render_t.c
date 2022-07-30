#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

#include <unistd.h>

#include <time.h>

int main(){

    putchar('\n');
    for (int k = 0; k < 5; k++){
        for (int j = 0; j < 10; j++){
            for (int i = 0; i < 10; i++){
                
                putchar(j+'0');
                usleep(15000);
            }
            putchar('\n');
            
        }
        usleep(200000);
        printf("\x1b[10A");
    }
    
}