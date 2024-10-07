import numpy as np
from src.lab01.launch_angle_range import launch_angle_range

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



import numpy as np
import matplotlib.pyplot as plt
from src.lab01.launch_angle_range import launch_angle_range

def main():
    ve_v0 = 2.0
    tol_alpha = 0.04
    alpha_values = np.linspace(0.01, 0.5, 100)
    
    min_angles = []
    max_angles = []
    
    for alpha in alpha_values:
        phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_angles.append(phi_range[0])
        max_angles.append(phi_range[1])
    
    plt.plot(alpha_values, min_angles, label='Min Launch Angle')
    plt.plot(alpha_values, max_angles, label='Max Launch Angle')
    plt.xlabel('Alpha (fraction of Earth\'s radius)')
    plt.ylabel('Launch Angle (radians)')
    plt.legend()
    plt.savefig('figures/launch_angles_vs_alpha.png')
    plt.show()

if __name__ == "__main__":
    main()
