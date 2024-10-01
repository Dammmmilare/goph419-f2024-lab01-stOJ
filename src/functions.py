###

import numpy as np

def asin(x):


    """
    Compute inverse sine function
    Input:  
    x: float
    Returns: float
    """
    

    sign = -1 if x < 0 else 1
    x = np.abs(x)
    eps_a = 1.0
    tol = 1e-8  # error tolerance, Es = 0.5 * 10 ^ -N
    n = 1

    result = 0.0
    while eps_a > tol:
        dy = (((2*x)**(2*n)) / (n**2 * (np.math.factorial(2*n) / (np.math.factorial(n)**2))))
        result += dy
        eps_a = np.abs(dy / result)
        n += 1

    result = sign * np.sqrt(0.5 * result)
    return result


##

##

def launch_angle(ve_v0, alpha):
    """Compute the launch angle based on ve/v0 and alpha."""
    term = (ve_v0**2 - 1) * alpha
    if term < 0:
        raise ValueError("Invalid input: term under square root is negative.")
    return asin(np.sqrt(term))


###


###
def launch_angle_range(ve_v0, alpha, tol_alpha):
 

 """
 
 Description of function.
 Computing the range of launch angles for the values of ve_vo, alpha, and tol_alpha.

 Parameters
 ----------
 ve_vo : float
    Ratio of escape velovity to the terminal velocity.

 alpha : float
    the desires maximum altitude with respect to the fraction of the earths radius.

 tol_alpha : float
    The tolerance for maximum altitude.


 Returns
 -------

 numpy.array 

    A two-component array containing the minimum and maximum desirable launch angles.

 """

alpha_low = alpha * (1 - tol_alpha)
alpha_upper = alpha * (1 + tol_alpha)
    
phi_low = launch_angle(ve_v0, alpha_low)
phi_upper = launch_angle(ve_v0, alpha_upper)

phi_range : (phi_low, phi_upper)
#return phi_range

 