
def launch_angle_range(ve_v0, alpha, tol_alpha):
 


 """Description of function.
 Parameters
 ----------
 Returns
 -------
 """

 
 # ...
 # implementation of Equations (17) and (18)

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
        dy = (((2*x)^2*n)/(n^2(np.math.factorial(2*n)/(np.math.factorial(n)^2))))                
        #(np.math.factorial(2*n) / (4**n * np.math.factorial(n)**2 * (2*n + 1))) * x**(2*n + 1)
        result += dy
        eps_a = np.abs(dy / result)
        n += 1

    result = sign * np.sqrt(0.5 * result)
    return result


 # ...
 #return phi_range : (phi_low, phi_upper)

 