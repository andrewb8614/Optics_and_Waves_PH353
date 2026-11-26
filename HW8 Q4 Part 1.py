import numpy as np
import matplotlib.pyplot as plt

# Given parameters
N = 5                  # Number of slits
lam = 1e-6             # Wavelength: 1 um in meters
d = 2e-6               # Slit width (Delta x): 2 um in meters
h = 5e-6               # Slit spacing: 5 um in meters
f = 1e-2               # Focal length: 1 cm in meters
k = 2 * np.pi / lam    # Wave number

# Spatial coordinate x2 across the focal plane (e.g., from -0.05m to 0.05m)
# Let's set a window appropriate for seeing several orders
x = np.linspace(-0.03, 0.03, 5000)

# 1. Single-slit term (sinc^2 part)
# Argument of sinc: (pi * d / (lambda * f)) * x
# Note: NumPy's np.sinc(x) is sin(pi*x)/(pi*x), so we use np.sinc(x / (lam * f / d))
# or manually write out (sin(val)/val)^2 to avoid numpy definition confusion:
arg_sinc = (np.pi * d / (lam * f)) * x
# Handle division by zero at x = 0 safely
sinc_term = np.where(arg_sinc == 0, 1.0, (np.sin(arg_sinc) / arg_sinc)**2)

# 2. Array factor term (interference part)
# The image notes write the argument as (h * x * k N / 2 z) and (h * x * k / 2 z)
# Which simplifies to (k * h * x / (2 * f))
alpha = (k * h * x) / (2 * f)

# Handle division by zero at alpha = 0 (using l'Hopital's rule, limit is N^2)
array_term = np.where(
    np.isclose(np.sin(alpha), 0),
    N**2,
    (np.sin(N * alpha) / np.sin(alpha))**2
)

# Total unnormalized intensity
I_total = sinc_term * array_term

# Normalize intensity to a maximum of 1.0
I_normalized = I_total / np.max(I_total)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x * 1e3, I_normalized, color='b', lw=1.5)  # plotting x in millimeters
plt.title(f"Normalized Diffraction Pattern of  ($N = {N}$, $d = {d*1e6}\mu m$, $h = {h*1e6}\mu m$, $f = {f*100}cm$)", fontsize=12)
plt.xlabel("Position $x_2$ (mm)", fontsize=11)
plt.ylabel("Normalized Intensity ($I / I_{max}$)", fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(-25, 25)
plt.ylim(-0.05, 1.05)
plt.tight_layout()
plt.show()