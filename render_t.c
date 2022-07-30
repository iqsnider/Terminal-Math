#include <stdlib.h>
#include <stdio.h>

#include <unistd.h>
#include <math.h>

//TODO fix data types and type conversions
//TODO args parser in C

#define PI 3.14159265

void trig_frame(int frame_height, int frame_width, float iter,int amplitude){

    for (int i = 0; i <= frame_height; i++){
        for (int j = 0; j <= frame_width; j++){

            // start interpolation maths
            float rel_x = ((j-iter)/frame_width)*2*PI;

            // print values for debugging
            // printf("%f%s",rel_x,"\n");

            float y = sin(rel_x);

            // find position on grid
            // int yp =  round(frame_height/2 - y*frame_height/2);
            int yp =  round(frame_height/2 - y*amplitude);

            // print values for debugging
            // printf("%d%s%d%s",xp," ",yp,"\n");
            // end interpolation maths

            // plot the sine wave

            
            // place characters (ez for 2d)
            // makes an x and y axis
            if (i == yp){
                putchar('#');
            }

            else if (i == frame_height/2){
                putchar('-');
            }

            else{
                if (j == frame_width/2){
                    putchar('|');
                }
                else{
                    putchar(' ');
                }
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

    int frame_height = 30;
    int frame_width = 60;

    // float y = sin(1);

    // int yp = (int) (frame_height/2 + y*frame_height/2);

    // printf("%d",yp);


    // sine_frame(frame_height,frame_width,1);
    float k = 0;
    int amplitude = 6;
    for (;;){

        trig_frame(frame_height,frame_width,k, amplitude);

        usleep(50000);
        printf("%s%d%s","\x1b[",frame_height+1,"A");
        k++;
    }
    
}