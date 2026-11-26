import matplotlib.pyplot as plt
import numpy as np
from scipy.special import fresnel

# Given parameters
lam = 1.0e-6  # wavelength = 1 um in meters
z = 100.0e-6  # distance = 100 um in meters

# Observation coordinates x2 across the knife edge (from -20 um to +20 um)
x2 = np.linspace(-20e-6, 20e-6, 1000)

# Calculate u1 = -x2 * sqrt(k / (pi * z)) = -x2 * sqrt(2 / (lambda * z))
u1 = -x2 * np.sqrt(2.0 / (lam * z))

# scipy.special.fresnel(u) returns (S(u), C(u))
S, C = fresnel(u1)

# Calculate normalized intensity I / I_0
I_norm = 0.5 * ((0.5 - C) ** 2 + (0.5 - S) ** 2)

# Plotting the normalized intensity
plt.figure(figsize=(9, 5))
plt.plot(
    x2 * 1e6,
    I_norm,
    color="blue",
    linewidth=2,
    label="Normalized Intensity of Fresnel Diffraction Through Knife-Edge Aperture",
)

plt.title(
    "Fresnel Diffraction Normalized Intensity: Knife Edge (0 for -∞ < x1 < 0, 1 for 0 ≤ x1 < ∞)\n"
    "(lambda = 1 um, z = 100 um)"
          )
plt.xlabel("Position x2 (um)")
plt.ylabel("Normalized Intensity (I / I_0)")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()