import sys
import os
import numpy as np

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

from src.lab01.functions import launch_angle_range

def test_launch_angle_range():
    ve_v0 = 2.0
    alpha = 0.25
    tol_alpha = 0.02
    
    expected_phi_range = np.array([0.52359878, 0.55357436])  # Example expected values
    actual_phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
    
    assert np.allclose(actual_phi_range, expected_phi_range, atol=1e-5), \
        f"Test failed: expected {expected_phi_range}, got {actual_phi_range}"
    
    print("Test passed!")

if __name__ == "__main__":
    test_launch_angle_range()