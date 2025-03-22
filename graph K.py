import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 200000  # Carrying capacity
P0 = 100    # Initial population
r = 0.7324081924 # Intrinsic growth rate
t_max = 25# Maximum time (years)
num_points = 1000  # Number of points for the graph

# Time array
t = np.linspace(0, t_max, num_points)

# Logistic growth equation
P = (K * P0 * np.exp(r * t)) / (K - P0 + P0 * np.exp(r * t))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, P, label=f"Rabbit Population (r = {r}, K = {K})", color="purple")
plt.title("Logistic Growth of Rabbit Population")
plt.xlabel("Time (Years)")
plt.ylabel("Population")
plt.grid(True)
plt.legend()

# Add y-axis ticks and labels
plt.yticks(np.arange(0, max(P) + 100, 25000))

# Show the plot
plt.show()

