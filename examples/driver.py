import numpy as np
import matplotlib.pyplot as plt
from src.lab01.functions import launch_angle_range

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
