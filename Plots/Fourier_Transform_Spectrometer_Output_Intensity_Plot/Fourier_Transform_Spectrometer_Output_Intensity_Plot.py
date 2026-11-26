
import numpy as np
import matplotlib.pyplot as plt

# Given parameters
T1 = 10e-15                 # Pulse width (seconds)
omega1 = 2 * np.pi * 200e12 # Angular frequency (rad/s)

# Convert parameters to femtosecond units
T1_fs = T1 * 1e15
omega1_fs = omega1 * 1e-15  # rad/fs

# Create delay time array (femtoseconds)
tau = np.linspace(-50, 50, 10000)

# Calculate normalized output intensity
I_norm = 0.5 * (
    1 + np.exp(-tau**2 / (4 * T1_fs**2))
    * np.cos(omega1_fs * tau)
)

# Plot interferogram
plt.figure(figsize=(10, 5))
plt.plot(tau, I_norm, linewidth=1.2)

plt.xlabel(r'$\tau$ (fs)', fontsize=13)
plt.ylabel(r'Output Intensity $I(\tau)/I(0)$', fontsize=13)
plt.title('Fourier Transform Spectrometer Interferogram')

plt.grid(True, alpha=0.3)
plt.xlim(-50, 50)
plt.ylim(0, 1.05)

plt.tight_layout()
plt.show()
