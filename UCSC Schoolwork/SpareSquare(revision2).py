# This program demonstrates the misconception that the amount of toilet paper left is linearly
# related to the radius of the remaining roll in plot form.

import numpy as np
import matplotlib.pyplot as plt



def remaining_roll(r, R=2.5):
    """This module takes an input radius r and total radius R of a toilet paper roll,
       and returns the remaining length of roll
    -----------------------------------------------------------
    R = max radius of role, given in terms of inner radius r0
    RR = Remaining roll in terms of length (l/L)
       """
    assert(r <= R), "radius cannot be more than total radius"
    assert(r >= 1), "radius cannot be less than inner radius"   #makes sure radius is acceptable
    assert(R >= 1), "Total radius cannot be less than inner radius"
    RR = (r**2-1)/(R**2-1)  #calculates remaining roll
    return(RR)
    
def visible_roll (r, R=2.5):
    """This module takes an input radius r and a total radius R 
       and outputs the fraction of the roll based on radius"
    ------------------------------------------------------------
    r = current radius of roll
    R = max radius of roll, given in terms of the inner radius r0
    VR = percieved amount of roll remaining (r/r0)
    """
    assert(r <= R), "radius cannot be more than total radius"
    assert(r >= 1), "radius cannot be less than inner radius"  #makes sure radius is acceptable
    assert(R >= 1), "Total radius cannot be less than inner radius"
    VR = (r-1)/(R-1)  #calculates visible roll in terms of fraction of R
    return(VR)
    
    
def dif_plot(R0=2.5, n=100, N=3):
    """this module takes an input total radius and number of steps, and plots the difference
    in expected roll remaining based on what you can see, and what is actually left.
    ----------------------------------------------------------------------------------
    N = number of lines to graph, done in intervals of 1r0
    R0 = initial max radius divided by inner radius, default 2.5 times inner radius
    R = max radius
    n = number of steps to include, default 1
    Rx = list of x coordinates in r/r0
    Ry = list of Remaining roll coordinates based on actual length, in l/L.
    
    """

    assert(N <= 15), "The graph gets cluttered with more than 15 graphs, please reduce"
    assert(N >= 1), "cannot have negative number of graphs"
    assert(R0 > 1), "Total radius cannot be less than inner radius"
    plt.close('all') #closes figures
    fh = plt.figure(figsize=(8,6)) #creates new plot space
    
    for k in range(N): #creates N lines spaced 1r0 apart in max radius R
        Rx = []  #defines lists of data to plot
        Ry = []
        R = R0+2*k  #add 1 to original max R for each new plot
        for i in range(n):  #loop which creates the data points based on the equations
            Ry.append(remaining_roll(1+(i/n)*(R-1), R)) #appends new y component coordinates
            Rx.append(visible_roll(1+(i/n)*(R-1), R))  #appends new x coordinate components
        plt.plot(Rx, Ry, '-',label = f"R/r0={R}")  #plot current set
    
    plt.xlabel('Percieved radius remaining, r/r0')    #axis markers
    plt.ylabel('Actual length remaining, l/L')
   
    plt.legend()  #show labels
    plt.show(block=False)
    
    
    
    
    
    
    
    
    
    
