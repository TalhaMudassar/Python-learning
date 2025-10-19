import numpy as np
import matplotlib.pyplot as plt

# Define functions
f = lambda x: np.arctan(x)
P5 = lambda x: x - (x**3)/3 + (x**5)/5

# Range for x
x = np.linspace(-1, 1, 400)
y_true = f(x)
y_poly = P5(x)

# Highlight x=0.5
x_point = 0.5
y_true_point = f(x_point)
y_poly_point = P5(x_point)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y_true, label=r"$f(x)=\tan^{-1}(x)$", linewidth=2)
plt.plot(x, y_poly, '--', label=r"$P_5(x)=x-\frac{x^3}{3}+\frac{x^5}{5}$", linewidth=2)
plt.scatter([x_point], [y_true_point], color='red', zorder=5, label=r"True value at $x=0.5$")
plt.scatter([x_point], [y_poly_point], color='green', zorder=5, label=r"Approx. $P_5(0.5)$")
plt.vlines(x_point, y_true_point, y_poly_point, colors='orange', linestyles='dashed', label="Error at x=0.5")

plt.title("Comparison of $f(x)=\\tan^{-1}(x)$ and its 5th-degree Taylor Polynomial", fontsize=13)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
