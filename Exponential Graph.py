import numpy as np
import matplotlib.pyplot as plt

# Values
P0 = 100
r = 0.3662040962
t_max = 25
num_points = 1000

# Time Range
t = np.linspace(0, t_max, num_points)

# Equation Solution
P = P0 * np.exp(r * t)

# Plotting Graph
plt.figure(figsize=(10, 6))
plt.plot(t, P, label=f"Rabbit Population (r = {r})", color="green")
plt.yticks(np.arange(0, max(P) + 100, 100000))
plt.title("Exponential Growth of Rabbit Population")
plt.xlabel("Time (Years)")
plt.ylabel("Population (P)")
plt.grid(True)
plt.legend()
plt.show()