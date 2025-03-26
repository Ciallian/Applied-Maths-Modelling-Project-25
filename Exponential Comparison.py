import numpy as np
import matplotlib.pyplot as plt

# Values
P0 = 100
r1 = 0.5
r2 = 0.15
r3 = 0.3662040962
t_stop1 = 15
t_stop2 = 20
t_max = 25
num_points = 1000

# Time Range
t = np.linspace(0, t_max, num_points)

# Equation Solution
P1= np.where(t <= t_stop1,P0 * np.exp(r1 * t),np.nan)
P2 = P0 * np.exp(r2 * t)
P3= np.where(t <= t_stop2,P0 * np.exp(r3 * t),np.nan)

# Plotting Graph
plt.figure(figsize=(10, 6))
plt.plot(t, P1, label=f"Rabbit Population (r = {r1})", color="green")
plt.plot(t, P2, label=f"Rabbit Population (r = {r2})", color="red")
plt.plot(t, P3, label=f"Rabbit Population (r = {r3})", color="blue")
plt.yticks(np.arange(0, max(P1) + 100, 50000))
plt.title("Exponential Growth of Rabbit Population")
plt.xlabel("Time (Years)")
plt.ylabel("Population (P)")
plt.grid(True)
plt.legend()
plt.show()