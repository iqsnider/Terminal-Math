#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h> 

#include <unistd.h>
#include <math.h>

//TODO args parser in C

void render_frame(int frame_height, int frame_width, int iter, bool propogation){

    for (int i = 0; i <= frame_height; i++){
        for (int j = 0; j <= frame_width; j++){

            // start interpolation maths

            // define x scale (basically: how much zoom? set to frame sizes for 1x zoom):
            int x_scale = frame_width;
            // define y scale:
            int y_scale = frame_height;

            // define graph tick mark scale:
            float xtick_scale = 2*M_PI;
            float ytick_scale = 5;


            // defines calcuation scales
            float graph_height = frame_height/(y_scale/(ytick_scale));
            float graph_length = frame_width/(x_scale/(xtick_scale));

            // define origin as center of graph
            float origin = (float) graph_length/2;

            float x;
            // if you want propogation:
            if (propogation == true){
                x = (((float)j-iter)/frame_width)*graph_length - origin;
            }

            // no propogation
            if (propogation == false){
                x = (((float)j)/frame_width)*graph_length - origin;
            }

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
            // places characters and makes axes (ez for 2d)
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


    int frame_height = 40;
    int frame_width = 100;
    bool propogate = true;

    for (int i = 0;;i++){

        render_frame(frame_height, frame_width, i, propogate);

        usleep(50000);
        printf("%s%d%s","\x1b[",frame_height+1,"A");
    }
    
}