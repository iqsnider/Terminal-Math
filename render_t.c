#include <stdlib.h>
#include <stdio.h>

#include <unistd.h>
#include <math.h>

//TODO fix data types and type conversions
//TODO args parser in C

#define PI 3.14159265

void render_frame(int frame_height, int frame_width, int iter){

    for (int i = 0; i <= frame_height; i++){
        for (int j = 0; j <= frame_width; j++){

            // start interpolation maths

            // define x scale (basically: how much zoom? set to frame sizes for 1x zoom):
            int x_scale = frame_width;
            // define y scale:
            int y_scale = frame_height;

            // define graph tick mark scale:
            float xtick_scale = 2*PI;
            float ytick_scale = 5;


            // defines calcuation scales
            float graph_height = frame_height/(y_scale/(ytick_scale));
            float graph_length = frame_width/(x_scale/(xtick_scale));

            // define origin as center of graph
            float origin = (float) graph_length/2;
            // float x = (((float)j)/frame_width)*graph_length - origin;
            // if you want propogation:
            float x = (((float)j-iter)/frame_width)*graph_length - origin;

            // print values for debugging
            // printf("%f%s",rel_x,"\n");

            float y = sin(x);
            // float y = x*x;

            // find position on grid
            // int yp =  round(frame_height/2 - y*amplitude);
            int yp =  round(frame_height/2 - (y/graph_height)*frame_height);

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
    int k = 0;
    for (;;){

        render_frame(frame_height, frame_width, k);

        usleep(50000);
        printf("%s%d%s","\x1b[",frame_height+1,"A");
        k++;
    }
    
}