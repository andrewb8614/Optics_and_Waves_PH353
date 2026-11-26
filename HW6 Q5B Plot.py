import numpy as np
import matplotlib.pyplot as plt

# Constants
epsilon_0 = 8.854e-12
c = 3.0e8
E0 = 1.0  # Arbitrary field amplitude

# Pulse parameters
T1 = 10.0          # fs
T2 = 20.0          # fs
omega1 = 0.4*np.pi  # rad/fs
omega2 = 0.48*np.pi # rad/fs

# Delay axis
tau = np.linspace(-100, 100, 10000)  # fs

#  intensity expression
I = (epsilon_0*c/2) * abs(E0)**2 * T1 * np.sqrt(np.pi) * (
    2
    + np.exp(-tau**2/(4*T1**2))*np.cos(omega1*tau)
    + np.exp(-tau**2/(4*T2**2))*np.cos(omega2*tau)
)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(tau, I)
plt.xlabel(r'$\tau$ (fs)')
plt.ylabel(r'$I(\tau)$ (intensity)')
plt.title('Two-Pulse Interferogram')
plt.grid(True)
plt.tight_layout()
plt.show()