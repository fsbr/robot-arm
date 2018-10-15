# kinematics
# in this script i'll try to implement some simple kinematics

import numpy as np
import matplotlib.pyplot as plt

class SE3:
    # sets the SE3 group
    # the SE3 group has 4 segments
    #   ROTATION    3x1 zeros
    #    
    # 
    def __init__(self):
        T =  
    
if __name__ == "__main__":
    # typical matrix use cases
    A = np.matrix([[1,0],[0,1]])
    B = np.matrix([[1,2],[3,4]])
    C = A*B
    print(C)

    t = np.linspace(0,10, 1000)
    y = np.exp(0.4*t)
    plt.plot(t,y)
    plt.title('title')
    plt.xlabel('time (s)')
    plt.ylabel('value ($)')
    plt.show()

