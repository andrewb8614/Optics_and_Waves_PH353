import matplotlib.pyplot as plt
import numpy as np

# Parameters
T = 2.0
T0 = 2 * T
omega_0 = 2 * np.pi / T0

# Time array
t = np.linspace(-5, 5, 1000)

# Actual periodic function
def true_triangle(t_val):
    t_mod = (t_val + T / 2) % T0 - T / 2
    val = np.zeros_like(t_val)

    mask = np.abs(t_mod) < T / 2
    val[mask] = 1 - (4 * np.abs(t_mod[mask])) / T

    return val

# Fourier series approximation
def fourier_series_approx(t_vals, N):
    approx = np.zeros_like(t_vals, dtype=complex)

    # c0 = 0
    for n in range(-N, N + 1):
        if n == 0:
            continue

        arg = n * np.pi / 2

        # Correct Fourier coefficient
        cn = (
            -np.sin(arg) / (n * np.pi)
            + 4 * (1 - np.cos(arg)) / (n**2 * np.pi**2)
        )

        exp_term = np.exp(1j * n * omega_0 * t_vals)

        approx += cn * exp_term

    return np.real(approx)
# Plot
Ns = [1, 2, 5, 100]

fig, ax = plt.subplots(figsize=(10, 7.5))

ax.plot(t, true_triangle(t), 'k-', label='Actual Function', linewidth=2.5)

for N in Ns:
    ax.plot(
        t,
        fourier_series_approx(t, N),
        label=f'N = {N}',
        linestyle='--',
        alpha=0.85,
    )

ax.set_xlabel('Time (t)')
ax.set_ylabel('f(t)')
ax.set_title('Fourier Series Approximation')
ax.legend()
ax.grid(True)

# Make room at the bottom for the equations
fig.subplots_adjust(bottom=0.25)
# Original function (from image)
orig_func_text = (
    r'Original Function: $f(t) = 1 - 4|t|/T,\ \ |t| < T/2$'
    '\n'
    r'$\quad\quad f(t + T) = f(t - T),\ \ \mathrm{everywhere\ else.}$'
)

# Finite complex Fourier series (with T = 2.0)
fourier_text = (
    r'Fourier Series Approximation: $f_N(t) = \sum_{n=-N,\ n\neq 0}^{N} '
    r'\left[ -\frac{\sin(n\pi/2)}{n\pi} + \frac{4(1 - \cos(n\pi/2))}{n^2\pi^2} \right] '
    r'e^{j \frac{n\pi}{2} t}$'
)
fig.text(
    0.5,
    0.13,
    orig_func_text,
    ha='center',
    va='center',
    fontsize=10.5,
)
fig.text(
    0.5,
    0.045,
    fourier_text,
    ha='center',
    va='center',
    fontsize=11,
)

plt.show()