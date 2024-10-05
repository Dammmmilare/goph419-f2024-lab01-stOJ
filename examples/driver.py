#import numpy as np 
#{from my_python_package.operators import (
# add,
 #multiply,
 #)
#def main():# test for scalars
 #print(f'add(1, 3): {add(1, 3)}')
 #print(f'multiply(2, 12.): {multiply(2, 12.)}')
 # test for arrays
 #A = np.array([[1, 2, 3], [4, 5, 6]])
 #B = 2. * np.ones(A.shape)
 #print(f'A:\n{A}')
 #print(f'B:\n{B}')
 #print(f'add(A, B):\n{add(A, B)}')
 #print(f'multiply(A, B):\n{multiply(A, B)}')
#if __name__ == '__main__':
 #main()

import numpy as np
from src.launch_angle_range import launch_angle_range

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
from src.launch_angle_range import launch_angle_range

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
