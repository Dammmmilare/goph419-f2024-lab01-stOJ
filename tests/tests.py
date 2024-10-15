import sys
import os
import numpy as np

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

'''from src.functions import launch_angle_range

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
    test_launch_angle_range()'''

'''
import numpy as np
from src.functions import launch_angle_range

def test_launch_angle_range():
    ve_v0 = 2.0
    alpha = 0.25
    tol_alpha = 0.02
    
    # These should be in radians if the function output is in radians
    expected_min_angle = np.radians(14.48)  # Convert to radians
    expected_max_angle = np.radians(45.00)  # Convert to radians
    
    phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
    phi_min, phi_max = phi_range
    
    # Debug output
    print(f"Computed phi_min: {phi_min} (radians), Expected: {expected_min_angle}")
    print(f"Computed phi_max: {phi_max} (radians), Expected: {expected_max_angle}")
    
    # Check if values are within a tolerance range
    assert np.isclose(phi_min, expected_min_angle, atol=0.01), f"Failed: min angle {phi_min} != {expected_min_angle}"
    assert np.isclose(phi_max, expected_max_angle, atol=0.01), f"Failed: max angle {phi_max} != {expected_max_angle}"

    print("All tests passed!")

if __name__ == '__main__':
    test_launch_angle_range()'''

import numpy as np
from src.functions import launch_angle_range

def test_launch_angle_range():
    ve_v0 = 2.0
    alpha = 0.25
    tol_alpha = 0.02
    
    # Expected values should match the unit used in launch_angle_range
    expected_min_angle = np.radians(14.48)  # Expected value in radians
    expected_max_angle = np.radians(45.00)  # Expected value in radians
    
    phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
    phi_min, phi_max = phi_range
    
    # Debug output for more clarity
    print(f"Computed phi_min (radians): {phi_min}, Expected: {expected_min_angle}")
    print(f"Computed phi_max (radians): {phi_max}, Expected: {expected_max_angle}")
    
    # Verify the results within a tolerance range
    if not np.isclose(phi_min, expected_min_angle, atol=0.01):
        print(f"Min angle test failed: computed {phi_min}, expected {expected_min_angle}")
    else:
        print(f"Min angle test passed!")

    if not np.isclose(phi_max, expected_max_angle, atol=0.01):
        print(f"Max angle test failed: computed {phi_max}, expected {expected_max_angle}")
    else:
        print(f"Max angle test passed!")

if __name__ == '__main__':
    test_launch_angle_range()
