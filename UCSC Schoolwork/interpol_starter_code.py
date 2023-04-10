# This module contains some educational interpolation routines. The
# implementations are focused on illustrating the mathematical algorithm, rather
# than on efficiency or robustness, and therefore their performance on large
# data sets may be poor.

import numpy as np
import matplotlib.pyplot as plt

def linear(xq, xp, yp):
    """Piecewise-linear interpolation of one-dimensional data.

    Parameters
    ----------
    xq : scalar or ndarray vector
        The x-coordinates at which to evaluate the inteprolated values.
    xp : ndarray vector
        The x-coordinates of the data points; must be increasing.
    yp : ndarray vector
        The y-coordinates of the data points; must be same length as xp.

    Returns
    -------
    yq : scalar or ndarray vector
        The interpolated value(s); same shape as xq.
    """

    # Input control
    xq = np.array(xq, ndmin=1) # now it's ndarray vector for sure
    xp, yp = np.array(xp), np.array(yp) # now they are ndarray for sure
    assert len(xp.shape) == 1, "Data x- and y-coordinates musy be vectors."
    assert np.all(np.diff(xp) > 0), "Data x-coordinates must be increasing."
    assert np.shape(yp) == np.shape(xp), "Data x and y must be same length."

    # Run piecewise linear interpolation on each element of xq
    yq = np.nan*np.ones_like(xq)
    for k in range(xq.size):
        x = xq[k]
        if x < xp[0] or x > xp[-1]:
            continue # leave yq[k] as NaN

        for ind in range(xp.size): # search for bracketing interval
            if xp[ind] > x:
                break
        ind = ind - 1

        yq[k] = (yp[ind] +
            (yp[ind+1] - yp[ind])/(xp[ind+1] - xp[ind])*(x - xp[ind]))

    # ABYU
    if yq.size == 1:
        yq = yq[0]
    return yq

def lagrange_cubic(xq, xp, yp):
    """Piecewise-cubic interpolation with Lagrange polynomials.

    Parameters
    ----------
    xq : scalar or ndarray vector
        The x-coordinates at which to evaluate the inteprolated values.
    xp : ndarray vector
        The x-coordinates of the data points; must be increasing.
    yp : ndarray vector
        The y-coordinates of the data points; must be same length as xp.

    Returns
    -------
    yq : scalar or ndarray vector
        The interpolated value(s); same shape as xq.
    """

    # Input control
    xq = np.array(xq, ndmin=1) # now it's ndarray vector for sure
    xp, yp = np.array(xp), np.array(yp) # now they are ndarray for sure
    assert len(xp.shape) == 1, "Data x- and y-coordinates musy be vectors."
    assert np.all(np.diff(xp) > 0), "Data x-coordinates must be increasing."
    assert np.shape(yp) == np.shape(xp), "Data x and y must be same length."

    # Run piecewise cubic interpolation on each element of xq
    yq = np.nan*np.ones_like(xq)
    for k in range(xq.size):
        x = xq[k]
        if x < xp[1] or x >= xp[-2]: # leave yq[k] as NaN
            continue

        # search for bracketing interval
        for ind in range(xp.size):
            if xp[ind] > x:
                break
        ind = ind - 1

        x1, y1 = xp[ind-1], yp[ind-1]
        x2, y2 = xp[ind+0], yp[ind+0]
        x3, y3 = xp[ind+1], yp[ind+1]
        x4, y4 = xp[ind+2], yp[ind+2]

        f1 = ((x - x2)*(x - x3)*(x - x4))/((x1 - x2)*(x1 - x3)*(x1 - x4))
        f2 = ((x - x1)*(x - x3)*(x - x4))/((x2 - x1)*(x2 - x3)*(x2 - x4))
        f3 = ((x - x1)*(x - x2)*(x - x4))/((x3 - x1)*(x3 - x2)*(x3 - x4))
        f4 = ((x - x1)*(x - x2)*(x - x3))/((x4 - x1)*(x4 - x2)*(x4 - x3))

        yq[k] = y1*f1 + y2*f2 + y3*f3 + y4*f4

    # ABYU
    if yq.size == 1:
        yq = yq[0]
    return yq
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
def pixelfix2(I, pxq, copy=True):
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
        x = pxq[n][0]
        y = pxq[n][1]
        try:
            I[x,y,0] = (I[x+1,y,0]+I[x-1,y,0]+I[x,y-1,0]+I[x,y+1,0])/4 #replace red values
        except:
            continue
        try:   
            I[x,y,1] = (I[x+1,y,1]+I[x-1,y,1]+I[x,y-1,1]+I[x,y+1,1])/4 #replace green values
        except:
            continue
        try:  
            I[x,y,2] = (I[x+1,y,2]+I[x-1,y,2]+I[x,y-1,2]+I[x,y+1,2])/4 #replace blue values
        except:
            continue
    # Write your code here
    Iq = I
    return(Iq)
    
    
    
    
    
    
    
    