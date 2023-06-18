import numpy as np
import time



def render_frame(frame_height, frame_width):
    
    for k in range(0, frame_height):
        for j in range(0, frame_width):

            # SIMPLE TEST CASE: define elementary vectors without using Euler angles
            e_1 = np.array([0,1,0])
            e_2 = np.array([0,0,1])
            nhat = np.array([1,0,0])

            # show coordinate axis
            # x_axis = np.multiply(rotation_m, nhat)
            # y_axis = np.multiply(rotation_m, e_1)
            # z_axis = np.multiply(rotation_m, e_2)

            # test vector
            v = np.array([1,3,5])

            # project the given vector onto the screen by defining vector u
            u = np.dot(v, e_1)*e_1 + np.dot(v, e_2)*e_2
            
            ######-----> start interpolation maths

            # define x scale (basically: how much zoom? set to frame sizes for 1x zoom):
            e_1_scale = frame_width
            # define y scale:
            e_2_scale = frame_height

            # define graph tick mark scale (range of values shown on screen):
            e_1tick_scale = frame_width
            e_2tick_scale = frame_height

            # defines calcuation scales
            graph_height = frame_height/(e_2_scale/(e_2tick_scale))
            graph_width = frame_width/(e_1_scale/(e_1tick_scale))

            # define origin as the center of the graph
            origin = graph_width/2

            # find position on grid
            upos = [round(frame_width/2 + u[1]/graph_width * frame_width),
                    round(frame_height/2 - u[2]/graph_height * frame_height)]


            if [j,k] == [upos[0],upos[1]]:
                print("#", end="")

            elif [k,j] == [frame_height/2,frame_width/2]:
                print("+",end="")

            else: print(".", end="")
        
        print("")

            

if __name__ == '__main__':

    # start_time = time.time()

    usleep = lambda x: time.sleep(x/1000000.0)

    frame_height = 40
    frame_width = 100

    render_frame(frame_height, frame_width)

    print("\n")
    # while True:

    #     render_frame(frame_height, frame_width)

    #     print("\x1b[",frame_height+1,"A")
    #     usleep(50000)



    # speed check
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print(elapsed_time)