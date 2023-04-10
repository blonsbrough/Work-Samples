# A script to fix corrupted RGB images

import sys
import numpy as np
import interpol_starter_code as interpol
import matplotlib.pyplot as plt

def _main(filename):

    print("alo world")

    # Load corrupted image from file    
    I = plt.imread(filename)

    # Show the original, corrupted image on the screen
    plt.imshow(I)
    plt.show(block=True)

    bad_px = [] #create list of bad pixels
    M = I.shape[0]  #Define bounds of picture in y pixels
    N = I.shape[1]  #Define bounds of picture in x pixels
   
    for m in range(M): #find bad pixels and add them to bad pixel list
        for n in range(N):
            if I[m,n,0] == 1:
              
                bad_px.append((m,n))
    
    # Send the corrupted image and list of bad pixels to be fixed
    I = pixelfix(I, bad_px)

    # Save the fixed image and show it on screen
    plt.imshow(I)
    plt.savefig(f"fixed_{filename}")
    plt.show(block=True)
def pixelfix(I, pxq, copy=True):
    """Use bilinear interpolation to replace pixels in image.

    Parameters
    ----------
    I : ndarray, M-by-N-by-3
        A color image array to fix, in RGB format.
    pxq : ndarray, P-by-2
        List of pixel indices to replace.
    copy : bool, optional
        If True (default), return a copy of the image with replaced pixels;
        otherwise fix pixles in-place.
    
    Returns
    -------
    Iq : ndarray, same shape as I
        Copy of image with fixed pixels; only if copy==True.
    """
    for n in range(len(pxq)):
        x = pxq[n][1]  #delegates x coordinate of flawed pixel
        y = pxq[n][0]  #delegates y coordinate of flawed pixel
        I1R = 0
        I2R = 0
        I3R = 0
        I4R = 0
        I1G = 0
        I2G = 0
        I3G = 0
        I4G = 0
        I1B = 0
        I2B = 0
        I3B = 0
        I4B = 0
        C1 = 0
        C2 = 0
        C3 = 0
        C4 = 0
        try: 
            if I[y,x+1,0] < 1: #if reference pixel is not completely red, include it.
                I1R = I[y,x+1,0]
                I1G = I[y,x+1,1]
                I1B = I[y,x+1,2]
                C1 = 1
        except: 
            pass
        try: 
            if I[y,x-1,0] < 1:
                I2R = I[y,x-1,0]
                I2G = I[y,x-1,1]
                I2B = I[y,x-1,2]
                C2 = 1
        except:  
            pass
        try: 
            if I[y+1,x,0] < 1:
                I3R = I[y+1,x,0]
                I3G = I[y+1,x,1]
                I3B = I[y+1,x,2]
                C3 = 1
        except:
            pass
        try: 
            if I[y-1,x,0] < 1:
                I4R = I[y-1,x,0]
                I4G = I[y-1,x,1]
                I4B = I[y-1,x,2]
                C4 = 1
        except:
            pass
        try: #tries to replace flawed pixel by interpolating the average value of each color value from the 4 adjacent pixels.
            I[y,x,0] = (I1R+I2R+I3R+I4R)/(C1+C2+C3+C4) #replace red values
        except:
            pass #if pixels' color cannot be interpolated, say when it is on an edge, it is left as is.
        try:   
            I[y,x,1] = (I1G+I2G+I3G+I4G)/(C1+C2+C3+C4) #replace green values
        except:
            pass
        try:  
            I[y,x,2] = (I1B+I2B+I3B+I4B)/(C1+C2+C3+C4) #replace blue values
        except:
            pass
    return(I)

if __name__ == '__main__':
    _main(sys.argv[1])