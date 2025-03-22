import numpy as np
import matplotlib.pyplot as plt

# Values
r = 0.7324081924
K = 200000
alpha = 0.98
sigma = 1
P0 = 100
t0 = 0
t_disease = 15   #Disease Introduced
t_remove = 17
t_end = 25

A = r - alpha * sigma
B = r / K

# Time Range
t_values = np.linspace(t0, t_end, 500)

# Equation without Disease Solution
def logistic_growth(t, P0, r, K):
    return (K * P0 * np.exp(r * t)) / (K + P0 * (np.exp(r * t) - 1))

# Equation with Disease Solution
def logistic_growth_with_disease(t, P1, A, B, t1):
    return (A * P1 * np.exp(A * (t - t1))) / (A + B * P1 * (np.exp(A * (t - t1)) - 1))

# Piecewise Function
P_values = []
for t in t_values:
    if t < t_disease:
        P = logistic_growth(t, P0, r, K)
    elif t_disease <= t < t_remove:
        P1 = logistic_growth(t_disease, P0, r, K)
        P = logistic_growth_with_disease(t, P1, A, B, t_disease)
    else:
        P2 = logistic_growth_with_disease(t_remove, P1, A, B, t_disease)
        P = logistic_growth(t - t_remove, P2, r, K)
    P_values.append(P)

# Plotting Graph
plt.figure(figsize=(10, 6))
plt.plot(t_values, P_values, label=f"Rabbit Population (r = {r})", color="blue")
plt.axvline(x=t_disease, color="red", alpha = 0.6, linestyle="--", label="Disease Introduced")
plt.axvline(x=t_remove, color="green", alpha = 0.6, linestyle="--", label="Disease Removed")
plt.axhline(y=K, color="purple", alpha = 0.6, linestyle="--", label="Carrying Capacity (K)")
plt.xlabel("Time (Years)")
plt.ylabel("Population (P)")
plt.title("Piecewise Function of Rabbit Population (Logistic + Disease)")
plt.legend()
plt.grid()
plt.show()