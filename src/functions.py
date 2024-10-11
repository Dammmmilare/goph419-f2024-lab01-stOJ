import numpy as np

def launch_angle_range(ve_v0, alpha, tol_alpha):
    """
    Computes the minimum and maximum allowable launch angles based on the ratio of escape velocity
    to terminal velocity and the desired maximum altitude.
    
    Parameters
    ----------
    ve_v0 : float
        Ratio of escape velocity to terminal velocity.
    alpha : float
        Desired maximum altitude as a fraction of Earth's radius.
    tol_alpha : float
        Tolerance for the maximum altitude.
    
    Returns
    -------
    np.array
        A two-element array containing the minimum and maximum allowable launch angles (in radians).
    """
    def launch_angle(ve_v0, alpha):
        # Equation (17) implementation
        sin_phi0 = np.sqrt(1 - (alpha / ve_v0)**2)
        return np.arcsin(sin_phi0)
    
    # Lower and upper bounds for maximum altitude
    lower_alpha = (1 - tol_alpha) * alpha
    upper_alpha = (1 + tol_alpha) * alpha
    
    # Calculate minimum and maximum allowable launch angles
    phi_min = launch_angle(ve_v0, upper_alpha)
    phi_max = launch_angle(ve_v0, lower_alpha)
    
    return np.array([phi_min, phi_max])

# Example usage and testing
ve_v0 = 2.0
alpha = 0.25
tol_alpha = 0.02
phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
print("Launch angle range:", np.degrees(phi_range), "degrees")

import numpy as np

def asin(x):
    """
    Compute inverse sine function
    Input:  
    x: float
    Returns: 
    float
    
    """
    sign = -1 if x < 0 else 1
    x = np.abs(x)
    eps_a = 1.0
    tol = 1e-8  # error tolerance
    n = 1

    result = 0.0
    while eps_a > tol:
        dy = (((2 * x) ** (2 * n)) / (n ** 2 * (np.math.factorial(2 * n) / (np.math.factorial(n) ** 2))))
        result += dy
        eps_a = np.abs(dy / result)
        n += 1

    result = sign * np.sqrt(0.5 * result)
    return result