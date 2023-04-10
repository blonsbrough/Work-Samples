# This module contains various functions relating to the study of solar system
# comets. This module uses mostly SI units, and sometimes convenient planetary
# units like AU and earth mass etc.

import math
from math import sqrt

## Some physical constants and other useful quantities
G = 6.67430e-11       # universal gravitational constant [m^3/(kg s^2)]
M_sun = 1.9884e+30    # solar mass [kg]
M_earth = 5.9722e+24  # earth mass [kg]
GM = 1.32712440041e20 # precise solar mass parameter [m^3/s^2]
AU = 149597870700     # astronomical unit [m]
day = 24*60*60        # day in seconds
year = 365.24*day     # year in seconds

## Some functions of cometary orbits
def perihelion_velocity(a, e):
    """Return velocity magnitude at perihelion of elliptical orbit.

    Return maximum orbital velocity of a reduced two-body elliptical solar
    orbit. Give 

    Parameters
    ----------
    a : scalar, positive
      orbit semi-major axis, given in AU
    e : scalar, in [0,1)
      orbit eccentricity (dimensionless)

    Returns
    -------
    V : scalar, positive
      magnitude of orbital velocity at perihelion, in m/s
    """

    assert a > 0, "semi-major axis must be positive"
    assert a < 1e6, "that's a VERY long orbit, did you specify a in AU?"
    assert e >= 0, "eccentricity must be non-negative"
    assert e < 1, "parabolic and hyperbolic orbits not currently supported"

    V = (sqrt(abs((G*M_sun*(1+e))/((1-e)*a*AU))))/1000 # your turn, calculate the velocity here
    return V


## Some analysis helper functions
def tabulate_perihelion_velocity(a0, a1, N_a=10, e0=0, e1=0.9, N_e=10):
    """Print a nicely formatted table of orbital perihelion velocities.
    
    Return a table of maxiumum orbital velocities of a reduced two-body elliptical 
    solar orbit. Give
    
    Parameters
    -------------
    a0 : positive scalar   
        Initial orbit semi-major axis, given in AU
    a1 : positive scalar
        Final orbit semi-major axis, given in AU
    N_a : positive integer
        Total values of a, determines number of equally spaced columns
    N_e : positive integer
        Total values of e, determines number of equally spaced rows
    e0 : scalar, in {0,1)
        Initial orbit eccentricity (dimensionless)
    e1 : scalar, in {0,1)
        Final orbit eccentricity (dimensionless)
       
    returns a table composed of various orbital velocities (positive scalar values
    of the magnitude of the orbital velocity at the parahelion, in m/s
    
    
    """

    # I'll get you started with the table header and row header
    header  = "Velocity magnitude at perihelion [km/s]\n"
    header += "---------------------------------------"
    print(header)

    rowheader = r' \ a [AU] |'
    for k in range(N_a):
        a = a0 + k*(a1 - a0)/(N_a - 1)
        rowheader += f' {a:6.2f} |'
    print(rowheader)  #prints header for rows
    colheader = r'e \       |'
    print(colheader)   #prints header for column after header for row
    for i in range(N_e): #makes N_e rows, using the second loop to format each row individually
        e = e0 + i*(e1-e0)/(N_e-1)  
        row = f'{e:8.2f}  |'
        for j in range(N_a): #adds N_a velocities one after another to form a row
            a = a0 + j*(a1 - a0)/(N_a - 1)
            v = perihelion_velocity(a,e)
            row += f' {v:6.2f} |'
        print(row)    #prints each row formatted by the loop above

    # OKAY NOW IT'S YOUR TURN
    # My suggestion: go row by row with a for loop, and for each row, create it
    # column by column in another for loop. Print each row when it's ready.
    # Another suggestion: as you work, test the function often, and test on
    # small tables first so they print nicely in a small terminal window. Test
    # with, say, 5 columns instead of the default 10. When you're done maximize
    # the terminal window and test with 10 columns.
