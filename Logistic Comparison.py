import numpy as np
import matplotlib.pyplot as plt

# Values
K = 1000000
P0 = 100
r = 0.7324081924
r1 = 0.3662040962
t_max = 25
num_points = 1000

# Time Range
t = np.linspace(0, t_max, num_points)

# Logistic Solution
P = (K * P0 * np.exp(r * t)) / (K - P0 + P0 * np.exp(r * t))
P1 = (K * P0 * np.exp(r1 * t)) / (K - P0 + P0 * np.exp(r1 * t))

# Exponential Solution
P2= P0 * np.exp(r1 * t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, P, label=f"Logistic 2 Population (r = {r})", color="blue")
plt.plot(t, P1, label=f"Logistic 1 Population (r = {r1})", color="purple")
plt.plot(t, P2, label=f"Exponential Population (r = {r1})", color="green")
plt.axhline(y=K, color="red", alpha = 0.4, linestyle="--", label="Carrying Capacity (K)")
plt.title("Logistic Growth of Rabbit Population")
plt.xlabel("Time (Years)")
plt.ylabel("Population (P)")
plt.grid(True)
plt.legend()

# Add y-axis ticks and labels
plt.yticks(np.arange(0, max(P) + 100, 50000))

# Show the plot
plt.show()
