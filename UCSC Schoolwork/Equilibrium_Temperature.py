# Equilibrium temperature - this module defines a number of functions that
# calculate the equilibrium temperature of isotropically radiating bodies in
# orbit

import sys
from math import pi

sigma = 5.67e-8 # Stefan-Boltzmann constant [W/m^2/K^4]
L_sun = 3.8e26  # [J/s] average solar luminosity
AU = 150*1e6*1e3 # astronomical unit [m]

def blackbody(d, L=1.0, printout=False):
    """Return eq. temp. of perfect absorber/emitter in orbit.

    Returns temperature of a perfect absorber/emitter in thermodynamic
    equilibrium a distance d form a star of luminosity L. We assume isotropic
    re-radiation of absorbed flux.

    Parameters
    ----------
    d : positive scalar
        distance from star, in astronomical units (1 AU ~ 150 million km).
    L : nonnegative scalar, optional (default 1.0)
        stellar luminosity, in units of solar luminosity (1 L_sun ~ 3.8e26 J/s).
    printout : flag, optional (default False)
        If True also print a formatted output message.

    Returns
    -------
    T : nonnegative scalar
        Calculated temperature, in Kelvin
    """

    T = (1/(4*sigma)*(L*L_sun)/(4*pi*(d*AU)**2))**(1/4)
    if printout:
        output = f"""\
        At a distance of {d} AU from a star of luminosity L = {L} solar,
        the equilibrium temperature of a perfectly absorbing and
        isotropically radiating black body is {T:.1f} K.
        """
        print(output)
    return T


def absorber(d, albedo, emissivity=1.0, luminosity=1.0) :
    """Return eq. temp. of non-perfect absorber/emitter in orbit

    Returns temperature of a real absorber/emitter in thermodynamic equilibrium
    a distance d from a star of known luminosity. We assume isotropic
    re-radiation of absorbed flux

    Parameters
    -------------
    d : positive scalar
        distance from star, in astronomical units (1 AU~150 million km)
    albedo : scalar in [0,1]
        fraction of incident radiation that is reflected away (dimensionless)
    emissivity : scalar in (0,1] (default 1.0)
        fraction of Stefan-Boltzmann radiation emitted at temperature T. Note 
        that this makes the calculation not entirely self-consistent. We may
        specify an order-of-magnitude emissivity for expected temperature
        regime.
    Luminosity : nonnegative scalar, optional (default 1.0)
        Stellar luminosity, in units of solar luminosity (1 L_sun ~ 3.8e26 J/s)
        
    Returns
    ----------
    T : nonnegative scalar
        Calculated temperature, in Kelvin
    """
    # short names for local variables
    L = luminosity
    A = albedo
    eps = emissivity
    assert L >= 0, "Luminosity must be non-negative."
    assert (A >= 0) and (A <=1), "Emissivity must be in [0,1]."
    assert (eps > 0) and (eps <= 1), "Emissivity must be in (0,1]"

    T = (1/(eps*4*sigma)*((1-A)*L*L_sun)/(4*pi*(d*AU)**2))**(1/4)
    return T
def tabulate_absorber(d_start, d_end, N, A=0.0, eps=1.0, L=1.0): 
    """
    call absorber() N times and print a formatted table
    parameters
    -----------
    d_start : positive scalard_end : positive scalar
    """
    print("  d [AU] |  T [K]  ") 
    print("-----------------------")
    delta_d = (d_end-d_start) / (N-1) 
    for i in range(N):
        d_curr = d_start + i * delta_d
        t_eq = absorber(d_curr, A, emissivity=eps, luminosity=L)
        print(f'{d_curr:8.2f} | {t_eq:8.2f}')
        
