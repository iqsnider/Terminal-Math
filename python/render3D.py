import numpy as np
import math as m
import time

# define elementary vectors without using Euler angles
e_1 = np.array([0,1,0])
e_2 = np.array([0,0,1])
nhat = np.array([1,0,0]) # vector normal to the screen


# ray tracing?
def ray_trace():
    pass
        
# find luminance
def luminance(r, scale, zbuffer,rpos):
    # L = np.sqrt(r.dot(r))
    
    L = np.dot(r, nhat)

    luminance_index = int(L*scale)

    return ".,-~:;=!*#$@"[luminance_index]



def decimal_range(start, stop, increment):
    while start < stop: # and not math.isclose(start, stop): Py>3.5
        yield start
        start += increment

# makes a rotation matrix from given Euler angles
def make_rotation(phi, thta, psi):
    
    # consolidated rotation matrix
    cosphi = m.cos(phi)
    sinphi = m.sin(phi)

    costhta = m.cos(thta)
    sinthta = m.sin(thta)

    cospsi = m.cos(psi)
    sinpsi = m.sin(psi)

    rotation_m = np.array([[costhta*cospsi, cospsi*sinthta*sinphi - sinpsi*cosphi, cospsi*sinthta*cosphi + sinpsi*sinphi],
                          [sinpsi*costhta, sinpsi*sinthta*sinphi + cospsi*cosphi, sinpsi*sinthta*cosphi - cospsi*sinphi],
                          [-sinthta, costhta*sinphi, costhta*cosphi]])


    # rotation_m = np.matmul(r_3, r_2)
    # rotation_m = np.matmul(rotation_m, r_1)

    return rotation_m


# render the graph in the terminal
def render_frame(frame_height, frame_width, rotation_m, step, show_axes):

    # define x scale (basically: how much zoom? set to frame sizes for 1x zoom):
    e_1_scale = frame_width
    # define y scale:
    e_2_scale = frame_height

    # define graph tick mark scale (range of values shown on screen):
    e_1tick_scale = 20
    e_2tick_scale = 17

    # defines calcuation scales
    graph_height = frame_height/(e_2_scale/(e_2tick_scale))
    graph_width = frame_width/(e_1_scale/(e_1tick_scale))

    # define origin as the center of the graph
    origin = graph_width/2

    # output matrix
    output = [ [' ']*frame_width for i in range(frame_height)]

    # for luminance calculation (Thank you Andy Sloane!)
    zbuffer = [ [0]*frame_width for i in range(frame_height)]
    

    # define elementary vectors without using Euler angles
    e_1 = np.array([0,1,0])
    e_2 = np.array([0,0,1])
    nhat = np.array([1,0,0]) # vector normal to the screen



    if show_axes == True:
        # show coordinate axis
        x_axis = np.dot(rotation_m, nhat)
        y_axis = np.dot(rotation_m, e_1)
        z_axis = np.dot(rotation_m, e_2)
        # define origin as center of the screen
        output[round(frame_height/2)][round(frame_width/2)] = "+"


    ####################### A Function to Graph ######################

    # --------> trefoil knot
    R = 3.5
    for t in decimal_range(-4, 4, 0.01):
        x = R*(m.sin(t) + 2*m.sin(2*t)) 
        y = R*(m.cos(t) - 2*m.cos(2*t))
        z =-R*m.sin(3*t)

        v = np.array([x,y,z])
        r = np.dot(rotation_m, v)


        rpos = [int(frame_width/2 + r[1]/graph_width * frame_width),
            int(frame_height/2 - r[2]/graph_height * frame_height)]
        
        if rpos[0] < frame_width and rpos[1] < frame_height and rpos[0] >=0 and rpos[1] >= 0:
            output[rpos[1]][rpos[0]] = "#" #luminance(r,0.5, zbuffer, rpos)

    #################### Make the coordinate axes ####################
    if show_axes == True:
        
        alb, aub, ainc = -graph_height/2,graph_height/2, 0.2

        # x_axis
        for t in decimal_range(alb, aub, ainc):
            r = x_axis*t

            # needs work
            rpos = [int(frame_width/2 + r[1]/graph_width * frame_width),
                    int(frame_height/2 - r[2]/graph_height * frame_height)]

            if rpos[0] < frame_width and rpos[1] < frame_height and rpos[0] >=0 and rpos[1] >= 0:
                output[rpos[1]][rpos[0]] = "x"

        # y_axis
        for t in decimal_range(alb, aub, ainc):
            r = y_axis*t

            # needs work
            rpos = [int(frame_width/2 + r[1]/graph_width * frame_width),
                    int(frame_height/2 - r[2]/graph_height * frame_height)]

            if rpos[0] < frame_width and rpos[1] < frame_height and rpos[0] >=0 and rpos[1] >= 0:
                output[rpos[1]][rpos[0]] = "y"

        # z_axis
        for t in decimal_range(alb, aub, ainc):
            r = z_axis*t

            # needs work
            rpos = [int(frame_width/2 + r[1]/graph_width * frame_width),
                    int(frame_height/2 - r[2]/graph_height * frame_height)]

            if rpos[0] < frame_width and rpos[1] < frame_height and rpos[0] >=0 and rpos[1] >= 0:
                output[rpos[1]][rpos[0]] = "z"
        
        



    #################### ######################## ####################
    
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
    step = 0.2

    if propogate == True:
        while True:

            psi += 0.05
            # phi += 0.1
            # thta += -0.075
            
            rotation_m = make_rotation(phi, thta, psi)

            render_frame(frame_height, frame_width, rotation_m, step, show_axes)
            print("\x1b["+ str(frame_height+1) +"A")
            usleep(50000)
            


    else:
        rotation_m = make_rotation(phi, thta, psi)

        render_frame(frame_height, frame_width, rotation_m, step, show_axes)
