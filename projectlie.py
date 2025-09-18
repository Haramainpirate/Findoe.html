import math


# Constants
g = 9.8  # gravity m/s^2

# Inputs
v0 = float(input("Initial velocity (m/s): "))
angle_deg = float(input("Launch angle (degrees): "))
angle_rad = math.radians(angle_deg)

# Time step
dt = 0.1
t = 0

print("Time (s)\tX (m)\tY (m)")

while True:
    x = v0 * math.cos(angle_rad) * t
    y = v0 * math.sin(angle_rad) * t - 0.5 * g * t**2
    if y < 0:
        break
    print(f"{t:.2f}\t\t{x:.2f}\t{y:.2f}")
    t += dt
