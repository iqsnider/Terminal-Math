#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

#include <unistd.h>
#include <math.h>

//TODO args parser in C

#define PI 3.14159265

void sine_frame(int frame_height, int frame_width, float iter){

    for (int i = 0; i <= frame_height; i++){
        for (float j = 0; j <= frame_width; j++){

            // start interpolation maths
            float rel_x = ((j-iter)/frame_width)*2*PI;

            // print values for debugging
            // printf("%f%s",rel_x,"\n");

            float y = sin(rel_x);

            // find position on grid
            int xp = j;
            int yp =  round(frame_height/2 - y*frame_height/2);

            // print values for debugging
            // printf("%d%s%d%s",xp," ",yp,"\n");
            // end interpolation maths

            // plot the sine wave
            if (i == yp){
                putchar(' ');
            }

            else{
                putchar('#');
            }
        }
        putchar('\n');
    }
}

int main(){
    
    putchar('\n');

    // char next_frame[] = "\x1b[";
    // int frame_height = 10;
    // for (int k = 0; k <70; k++){
    //     for (int j = 0; j < 10; j++){
    //         for (int i = 0; i < 10; i++){
    //             putchar(k+'0');
    //         }
    //         putchar('\n');
            
    //     }
    //     usleep(60000);

    //     printf("%s%d%s",next_frame, frame_height, "A");
    // }

    int frame_height = 40;
    int frame_width = 80;

    // float y = sin(1);

    // int yp = (int) (frame_height/2 + y*frame_height/2);

    // printf("%d",yp);


    // sine_frame(frame_height,frame_width,1);
    float k = 0;
    for (;;){

        sine_frame(frame_height,frame_width,k);

        usleep(10000);
        printf("%s%d%s","\x1b[",frame_height+1,"A");
        k++;
    }
    
}