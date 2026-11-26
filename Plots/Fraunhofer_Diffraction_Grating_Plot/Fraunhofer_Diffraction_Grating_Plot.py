import matplotlib.pyplot as plt
import numpy as np
from scipy.special import jv

# Given Parameters
f = 1.0  # focal length (m)
lam = 1e-6  # wavelength (m) -> 1 um
a = 2e-6  # aperture radius (m) -> 2 um
hx = 5e-6  # column spacing (m) -> 5 um
hy = 10e-6  # row spacing (m) -> 10 um
N = 5  # number of columns

# Corrected grid window: Let's span across several grating orders (~0.4 meters)
span = 0.25  # meters (+/- 25 cm)
x = np.linspace(-span, span, 1000)
y = np.linspace(-span, span, 1000)
X, Y = np.meshgrid(x, y)
rho = np.sqrt(X**2 + Y**2)


# Function to calculate intensity pattern for a given M
def calculate_intensity(M):
  # 1. Single Aperture Term (Airy Pattern Envelope)
  arg = (2 * np.pi * a * rho) / (lam * f)

  with np.errstate(divide='ignore', invalid='ignore'):
    bessel_term = 2 * jv(1, arg) / arg
    bessel_term[arg == 0] = 1.0

  I_single = (np.pi * a**2 / (lam * f)) ** 2 * bessel_term**2

  # 2. Array Interference Terms
  alpha = (np.pi * hx * X) / (lam * f)
  beta = (np.pi * hy * Y) / (lam * f)

  with np.errstate(divide='ignore', invalid='ignore'):
    term_x = np.sin(N * alpha) / np.sin(alpha)
    term_x[np.sin(alpha) == 0] = N

    term_y = np.sin(M * beta) / np.sin(beta)
    term_y[np.sin(beta) == 0] = M

  I_array = (term_x**2) * (term_y**2)

  return I_single * I_array


# Case values for M
M_values = [1, 5, 10]

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for idx, M in enumerate(M_values):
  I = calculate_intensity(M)

  # Normalize intensity for visualization
  max_val = np.max(I)
  I_norm = I / max_val if max_val > 0 else I

  ax = axes[idx]
  im = ax.imshow(
      I_norm,
      extent=[x[0] * 100, x[-1] * 100, y[0] * 100, y[-1] * 100],
      origin='lower',
      cmap='hot',
      vmin=0,
      vmax=1,
  )
  ax.set_title(f'M = {M}, N = {N}')
  ax.set_xlabel('x (cm)')
  ax.set_ylabel('y (cm)')
  fig.colorbar(im, ax=ax, label='Normalized Intensity')

fig.suptitle(
    r'Far-Field (Fraunhofer) Intensity of Diffraction Grating'
    '\n'
    r'$M \times N$ holes, radius $a = 2\,\mathrm{um}$, '
    r'spacing $h_x = 5\,\mathrm{um}$, $h_y = 10\,\mathrm{um}$, '
    r'$\lambda = 1\,\mathrm{um}$',
    fontsize=13,
    fontweight='bold',
)
plt.tight_layout(rect=[0, 0, 1, 0.91])
plt.show()