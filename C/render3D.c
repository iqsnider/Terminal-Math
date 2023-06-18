
#include<stdio.h>

float dot(float a[], float b[]){
    float result = 0;
    for (int i = 0; i < 3; i++)
        result += a[i]*b[i];
    return result;
}

float * add(float a[], float b[]){
    static float result[3];
    for (int i = 0; i < 3; i++){
        result[i] = a[i] + b[i];
    }

    return result;
}

// thing that makes the thing appear in the thing
void render_frame(int frame_height, int frame_width, int iter){
    
    for (int i = 0; i <= frame_height; i++){
        for (int j = 0; i <= frame_width; i++){
                // SIMPLE TEST CASE: define elementary vectors without using Euler angles
                float e_1[] = {1,0,0};
                float e_2[] = {0,0,1};
                float nhat[] = {0,1,0};

                // test vector
                float v[] = {1,3,5};

                //project the given vector onto the screen by defining vector u
                float u[3];
                

        }
    }
}


int main() {
    putchar('\n');


    int frame_height = 40;
    int frame_width = 100;

    float e_1[] = {1,0,0};
    float e_2[] = {0,0,1};            
    float nhat[] = {0,1,0};

    float v[] = {1,3,5};
    float *u;

    // ugh, I'm gonna just do the linear algebra by hand, and also switch to python
    // but I will be back
}