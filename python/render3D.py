import numpy as np
import math as m
import time

'''
TODO:
1. algebraically define a range for the value, t.
2. render 3D surfaces
3. Add condition for t: if upos is outside of frame, don't add upos data to output
4. luminance calculation
5. runtime optimizations (it's real bad, gamers)
6. Clean code
7. Write a program for argument parsing a 3D function into a parametric system of equations for x, y, and z
8. Make a new github repo called 3D graphing calculator
'''

# define elementary vectors without using Euler angles
e_1 = np.array([0,1,0])
e_2 = np.array([0,0,1])
nhat = np.array([1,0,0]) # vector normal to the screen


# find luminance
def luminance(r):
    # L = np.sqrt(r.dot(r))
    L = np.dot(r, nhat)

    luminance_index = int(L/1.7)

    return ".,-~:;=!*#$@"[luminance_index]



def decimal_range(start, stop, increment):
    while start < stop: # and not math.isclose(start, stop): Py>3.5
        yield start
        start += increment

# makes a rotation matrix from given Euler angles
def make_rotation(phi, thta, psi):

    # Euler rotation (convenient... sometimes.)
    # # rotation about z-axis
    # r_1 = np.array([[m.cos(phi), m.sin(phi), 0],
    #                [-m.sin(phi), m.cos(phi), 0],
    #                [0, 0, 1]])

    # # rotation about new x-axis
    # r_2 = np.array([[1, 0, 0],
    #                [0, m.cos(thta), m.sin(thta)],
    #                [0, -m.sin(thta), m.cos(thta)]])
     
    # # rotation about newest z-axis
    # r_3 = np.array([[m.cos(psi), m.sin(psi), 0],
    #                [-m.sin(psi), m.cos(psi), 0],
    #                [0, 0, 1]])

    # TAIT-BRYAN rotation (easier to visualize lol)
    r_1 = np.array([[1,0,0],
                    [0,m.cos(phi),-m.sin(phi)],
                    [0,m.sin(phi),m.cos(phi)]])
    
    r_2 = np.array([[m.cos(thta),0,m.sin(thta)],
                    [0,1,0],
                    [-m.sin(thta),0,m.cos(thta)]])
    
    r_3 = np.array([[m.cos(psi),-m.sin(psi),0],
                    [m.sin(psi),m.cos(psi),0],
                    [0,0,1]])


    rotation_m = np.matmul(r_3, r_2)
    rotation_m = np.matmul(rotation_m, r_1)

    return rotation_m


# render the graph in the terminal
def render_frame(frame_height, frame_width, rotation_m, step, show_axes):

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
    output = [ [' ']*frame_width for i in range(frame_height)]
    

    # define elementary vectors without using Euler angles
    e_1 = np.array([0,1,0])
    e_2 = np.array([0,0,1])
    nhat = np.array([1,0,0]) # vector normal to the screen


    # show coordinate axis
    x_axis = np.dot(rotation_m, nhat)
    y_axis = np.dot(rotation_m, e_1)
    z_axis = np.dot(rotation_m, e_2)

    #################### Make the coordinate axes ####################
    if show_axes == True:

        xlb, xub, xinc = -19, 19, 0.2
        ylb, yub, yinc = -19, 19, 0.2
        zlb, zub, zinc = -18, 18, 0.2

        # x_axis
        for t in decimal_range(xlb, xub, xinc):
            r = x_axis*t

            # needs work
            rpos = [int(frame_width/2 + r[1]/graph_width * frame_width),
                    int(frame_height/2 - r[2]/graph_height * frame_height)]

            # print(upos, t)
            output[rpos[1]][rpos[0]] = "x"

        # y_axis
        for t in decimal_range(ylb, yub, yinc):
            r = y_axis*t

            # needs work
            rpos = [int(frame_width/2 + r[1]/graph_width * frame_width),
                    int(frame_height/2 - r[2]/graph_height * frame_height)]

            # print(upos, t)
            output[rpos[1]][rpos[0]] = "y"

        # z_axis
        for t in decimal_range(zlb, zub, zinc):
            r = z_axis*t

            # needs work
            rpos = [int(frame_width/2 + r[1]/graph_width * frame_width),
                    int(frame_height/2 - r[2]/graph_height * frame_height)]

            # print(upos, t)
            output[rpos[1]][rpos[0]] = "z"
        
        # define origin as center of the screen
        output[round(frame_height/2)][round(frame_width/2)] = "+"



    #################### ######################## ####################

    ####################### A Function to Graph ######################

    '''The commented out stuff are functions that work, I just don't run them
    all at the same time for obvious reasons.'''

    # --------> cone
    # for theta in decimal_range(0, 2*np.pi, 0.02):
    #     for r in decimal_range(0, m.sqrt(9), 0.02):
            
    #         x = r*m.cos(theta)
    #         y = r*m.sin(theta)
    #         z = m.sqrt(9 - r*r)

    #         v = np.array([x,y,z])
    #         r = np.dot(rotation_m, v)


    #         rpos = [round(frame_width/2 + r[1]/graph_width * frame_width),
    #             round(frame_height/2 - r[2]/graph_height * frame_height)]

    #         output[rpos[1]][rpos[0]] = luminance(r)

    # -------> Torus
    # R1 = 10
    # R2 = 5

    # for theta in decimal_range(0, 2*np.pi, step):
    #     for phi in decimal_range(0, 2*np.pi, step):
            
    #         x = (R1 + R2*m.cos(phi))*m.cos(theta)
    #         y = (R1 + R2*m.cos(phi))*m.sin(theta)
    #         z = R2*m.sin(phi)

    #         v = np.array([x,y,z])
    #         r = np.dot(rotation_m, v)

    #         rpos = [int(frame_width/2 + r[1]/graph_width * frame_width),
    #             int((frame_height/2 - r[2]/graph_height * frame_height))]
    
    #         # output[rpos[1]][rpos[0]] = "#"
    #         output[rpos[1]][rpos[0]] = luminance(r)



    # --------> cube
    # for t_x in decimal_range(-7, 7, step):
    #     for t_y in decimal_range(-7,7, step):
    #         for t_z in decimal_range(-7,7,step):
            
    #             x = t_x
    #             y = t_y
    #             z = t_z

    #             v = np.array([x,y,z])
    #             r = np.dot(rotation_m, v)


    #             rpos = [round(frame_width/2 + r[1]/graph_width * frame_width),
    #                 round(frame_height/2 - r[2]/graph_height * frame_height)]

    #             output[rpos[1]][rpos[0]] = luminance(r)

    # --------->  plane
    # for t_1 in decimal_range(-7, 7, 0.2):
    #     for t_2 in decimal_range(-7,7, 0.2):
            
    #             x = 0
    #             y = t_1
    #             z = t_2

    #             v = np.array([x,y,z])
    #             r = np.dot(rotation_m, v)


    #             rpos = [round(frame_width/2 + r[1]/graph_width * frame_width),
    #                 round(frame_height/2 - r[2]/graph_height * frame_height)]

    #             output[rpos[1]][rpos[0]] = luminance(r)

    # ---------> a function
    for t_1 in decimal_range(-12, 12, 0.2):
        for t_2 in decimal_range(-12, 12, 0.2):
            x = t_1
            y = t_2
            z = t_1*t_2/10

            v = np.array([x,y,z])
            r = np.dot(rotation_m, v)


            rpos = [int(frame_width/2 + r[1]/graph_width * frame_width),
                int(frame_height/2 - r[2]/graph_height * frame_height)]
            
            output[rpos[1]][rpos[0]] = luminance(r)






    #################### TEST ####################

    # test line:
    # lb = -15
    # ub = 15
    # increment = 0.02

    # # draw line (add line position data to output matrix)
    # for t in decimal_range(lb, ub, increment):

    #     v = np.array([t,6*m.cos(t),6*m.sin(t)])
    #     r = np.dot(rotation_m, v)

    #     # needs work
    #     rpos = [round(frame_width/2 + r[1]/graph_width * frame_width),
    #             round(frame_height/2 - r[2]/graph_height * frame_height)]

    #     output[rpos[1]][rpos[0]] = '#'

    ################### END TEST ###################
    
    # make frame
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
    phi = -0.05
    thta = -0.3
    psi = 0.3
    # phi = 0
    # thta = 0
    # psi = 0

    propogate = True
    show_axes = True
    step = 0.5

    if propogate == True:
        while True:

            psi += 0.05
            # phi += 0.1
            # thta += -0.075
            
            rotation_m = make_rotation(phi, thta, psi)

            render_frame(frame_height, frame_width, rotation_m, step, show_axes)
            print("\x1b[41A")
            usleep(50000)
            


    else:
        rotation_m = make_rotation(phi, thta, psi)

        render_frame(frame_height, frame_width, rotation_m, step, show_axes)



    # speed check
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print(elapsed_time)