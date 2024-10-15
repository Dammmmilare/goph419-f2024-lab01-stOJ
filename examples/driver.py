import sys
import os
import numpy as np

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 


# previous code before alterations and changes were made with AI to correct errors
'''import matplotlib.pyplot as plt
from src.functions import launch_angle_range

def main():
    ve_v0 = 2.0
    tol_alpha = 0.04
    alpha_values = np.linspace(0.01, 0.5, 100)
    
    min_angles = []
    max_angles = []
    
    for alpha in alpha_values:
        phi_range = np.degrees(launch_angle_range(ve_v0, alpha, tol_alpha))
        min_angles.append(phi_range[0])
        max_angles.append(phi_range[1])
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(alpha_values, min_angles, label='Minimum Launch Angle', color='blue')
    plt.plot(alpha_values, max_angles, label='Maximum Launch Angle', color='red')
    plt.xlabel('Alpha (maximum altitude as fraction of Earth’s radius)')
    plt.ylabel('Launch Angle (degrees)')
    plt.title('Launch Angle Range vs. Alpha')
    plt.legend()
    plt.grid(True)
    
    # Save the plot
    plt.savefig('figures/launch_angle_vs_alpha.png')
    plt.show()

if __name__ == "__main__":
    main()
'''

import os
import numpy as np
import matplotlib.pyplot as plt
from src.functions import launch_angle_range

def main():
    ve_v0 = 2.0
    tol_alpha = 0.04
    alpha_values = np.linspace(0.01, 0.5, 100)
    
    min_angles = []
    max_angles = []
    
    # Ensure the figures directory exists
    if not os.path.exists('figures'):
        os.makedirs('figures')
    
    for alpha in alpha_values:
        try:
            phi_range = np.degrees(launch_angle_range(ve_v0, alpha, tol_alpha))
            min_angles.append(phi_range[0])
            max_angles.append(phi_range[1])
        except Exception as e:
            print(f"Failed for alpha={alpha}: {e}")
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(alpha_values, min_angles, label='Minimum Launch Angle', color='blue')
    plt.plot(alpha_values, max_angles, label='Maximum Launch Angle', color='red')
    plt.xlabel('Alpha (maximum altitude as fraction of Earth’s radius)')
    plt.ylabel('Launch Angle (degrees)')
    plt.title('Launch Angle Range vs. Alpha')
    plt.legend()
    plt.grid(True)
    
    # Save the plot
    plt.savefig('figures/launch_angle_vs_alpha.png')
    plt.show()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
