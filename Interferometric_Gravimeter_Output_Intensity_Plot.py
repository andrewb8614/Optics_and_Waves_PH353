import matplotlib.pyplot as plt
import numpy as np

# Physical parameters
g = 9.8  # Acceleration due to gravity (m/s^2)
lam = 632.8e-9  # HeNe laser wavelength (m)

# Time array for the first millisecond (0 to 1 ms)
# Using 50,000 points because t^2 causes the frequency to increase rapidly,
# requiring high temporal resolution to avoid aliasing (resolution drop due to undersampling).
t = np.linspace(0, 1e-3, 50000)

# Normalized output intensity (I_out / I_0)
# I_out = (I_0 / 2) * (1 + cos(2 * pi * g * t^2 / lambda))
# Dividing by I_0 gives values ranging between 0 and 1:
I_norm = 0.5 * (1 + np.cos((2 * np.pi * g * t**2) / lam))

# Plotting the results
plt.figure(figsize=(9, 5))
plt.plot(t * 1000, I_norm, color="crimson", lw=1)
plt.title(
    "Interferometric Gravimeter Output Intensity (First Millisecond)",
    fontsize=12,
)
plt.xlabel("Time ($t$ in milliseconds)", fontsize=11)
plt.ylabel("Normalized Intensity ($I_{out} / I_0$)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.5)
plt.ylim(-0.05, 1.05)
plt.tight_layout()
plt.show()