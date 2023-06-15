# print("\x12[23A")

import time

x = 1
for i in range(30):
    ''' 
    First part of print command sends cursor to start, middle prints images, 
    end clears screen and repositions cursor.
    '''
    print("\x1b[H\n\n","\n----"+str(x)+"----\n----"+str(x)+"----\n----"+str(x)+"----\n","\x1b[H")
    # print("---------\n----"+str(x)+"----\n---------\n")
    
    time.sleep(0.25)

    x+=1
    
