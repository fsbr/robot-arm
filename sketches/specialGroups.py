# this script contains libraries to do se(3) and one day it will also
# include so(3), etc.
# tckf
# fall 2019

# imports
import numpy as np
import matplotlib.pyplot as plt

def SE2(tht1, xt,yt):
    """
    performs a rotation by tht1 radians
    then a translation by xt and yt
    """
    nextFrame = np.matrix([[np.cos(tht1), -np.sin(tht1), xt],
                [np.sin(tht1), np.cos(tht1), yt],
                [0, 0, 1]])
    return nextFrame 

if __name__ == "__main__":
    
    # so basically i make a column vector
    # [[x],[y],[1]]
    # and then i manpiulate it with SE2
    A = np.matrix([[1],[1],[1]])
    print(A)
    B = SE2(0, 4, -1)*A 
    print(B)
    
