import numpy as np
import math as m
import time


# makes a rotation matrix from given Euler angles
def make_rotation(phi, thta, psi):

    # rotation about z-axis
    r_1 = np.array([[m.cos(phi), m.sin(phi), 0],
                   [-m.sin(phi), m.cos(phi), 0],
                   [0, 0, 1]])

    # rotation about new x-axis
    r_2 = np.array([[1, 0, 0],
                   [0, m.cos(thta), m.sin(thta)],
                   [0, -m.sin(thta), m.cos(thta)]])
     
    # rotation about newest z-axis
    r_3 = np.array([[m.cos(psi), m.sin(psi), 0],
                   [-m.sin(psi), m.cos(psi), 0],
                   [0, 0, 1]])

    rotation_m = np.multiply(r_3, r_1, r_2) 

    return rotation_m


# render the graph in the terminal
def render_frame(frame_height, frame_width, rotation_m):

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


    # output matrix
    output = [ ['.']*frame_width for i in range(frame_height)]

    # for k in range(0, frame_height):
    #     for j in range(0, frame_width):

    #         # SIMPLE TEST CASE: define elementary vectors without using Euler angles
    #         e_1 = np.array([0,1,0])
    #         e_2 = np.array([0,0,1])
    #         # vector normal to the screen (only used for internal calculation purposes)
    #         nhat = np.array([1,0,0])

    #         # show coordinate axis
    #         x_axis = np.dot(rotation_m, nhat)
    #         y_axis = np.dot(rotation_m, e_1)
    #         z_axis = np.dot(rotation_m, e_2)



    #         # test vector to be projected
    #         v = np.array([1,3,5])

    #         t = j*graph_width - origin

    #         # project the given vector onto the screen by defining vector u
    #         u = (np.dot(v, e_1)*e_1 + np.dot(v, e_2)*e_2)*t

    #         # find position on grid
    #         upos = [round(frame_width/2 + u[1]/graph_width * frame_width),
    #                 round(frame_height/2 - u[2]/graph_height * frame_height)]

    # basically you have to make a for loop for each object that you render

    e_1 = np.array([0,1,0])
    e_2 = np.array([0,0,1])
    # vector normal to the screen (only used for internal calculation purposes)
    nhat = np.array([1,0,0])


    # show coordinate axis
    x_axis = np.dot(rotation_m, nhat)
    y_axis = np.dot(rotation_m, e_1)
    z_axis = np.dot(rotation_m, e_2)

    # test vector to be projected
    v = np.array([1,3,5])

    # test line:
    for t in range(-3, 3):
        u = (np.dot(v, e_1)*e_1 + np.dot(v, e_2)*e_2)*t

        # needs work
        upos = [round(frame_width/2 + u[1]/graph_width * frame_width),
                round(frame_height/2 - u[2]/graph_height * frame_height)]

        # print(upos, t)
        output[upos[1]][upos[0]] = "#"


    output[round(frame_height/2)][round(frame_width/2)] = "+" # this is for debugging
    
    # dump output to screen
    for k in range(0, frame_height):
        for j in range(0, frame_width):
            print(output[k][j], end="")
        print("") 


if __name__ == '__main__':

    # start_time = time.time()

    usleep = lambda x: time.sleep(x/1000000.0)

    frame_height = 40
    frame_width = 100

    # define Euler angles
    phi = 0
    thta = 0
    psi = 0

    rotation_m = make_rotation(phi, thta, psi)

    render_frame(frame_height, frame_width, rotation_m)

    print("\n")
    # while True:

    #     render_frame(frame_height, frame_width)

    #     print("\x1b[",frame_height+1,"A")
    #     usleep(50000)



    # speed check
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print(elapsed_time)

    # check rotation matrix
    print(rotation_m)