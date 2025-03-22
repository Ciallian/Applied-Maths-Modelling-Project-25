import numpy as np
import matplotlib.pyplot as plt

# Values
K = 200000
P0 = 100
r = 0.7324081924
t_max = 25
num_points = 1000

# Time Range
t = np.linspace(0, t_max, num_points)

# Equation Solution
P = (K * P0 * np.exp(r * t)) / (K - P0 + P0 * np.exp(r * t))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, P, label=f"Rabbit Population (r = {r})", color="purple")
plt.axhline(y=K, color="red", alpha = 0.4, linestyle="--", label="Carrying Capacity (K)")
plt.title("Logistic Growth of Rabbit Population")
plt.xlabel("Time (Years)")
plt.ylabel("Population (P)")
plt.grid(True)
plt.legend()

# Add y-axis ticks and labels
plt.yticks(np.arange(0, max(P) + 100, 25000))

# Show the plot
plt.show()

