import matplotlib.pyplot as plt
import numpy as np

# Given/chosen parameters for a clear demonstration
lam = 632.8e-9  # wavelength (e.g., 632.8 nm He-Ne laser)
a = 1e-3  # aperture radius (1 mm)
k = 2 * np.pi / lam
I0 = 1.0  # reference incident intensity

# Propagation distance z range from close (0.1 m) to far-field (10 m)
z = np.linspace(0.1, 10.0, 2000)

# 1. Exact Solution
arg_exact = (k / 2) * (np.sqrt(a**2 + z**2) - z)
I_exact = 4 * I0 * (np.sin(arg_exact)) ** 2

# 2. Fresnel Approximation
arg_fresnel = (k * a**2) / (4 * z)
I_fresnel = 4 * I0 * (np.sin(arg_fresnel)) ** 2

# 3. Fraunhofer Approximation
I_fraunhofer = 4 * I0 * (arg_fresnel) ** 2

# Plotting the three expressions
plt.figure(figsize=(10, 5))
plt.plot(z, I_exact, label='Exact Solution', color='black', lw=2)
plt.plot(
    z, I_fresnel, label='Fresnel Approximation', color='blue', ls='--', lw=1.5
)
plt.plot(
    z,
    I_fraunhofer,
    label='Fraunhofer Approximation',
    color='red',
    ls=':',
    lw=2,
)

plt.xlabel('Propagation Distance z (m)')
plt.ylabel('On-Axis Intensity $I(0, 0, z) / I_0$')
plt.title('Comparison of On-Axis Intensity Models for a Circular Aperture')
plt.xlim(0.1, 10.0)
plt.ylim(0, 5)
plt.legend()
plt.grid(True)
plt.show()