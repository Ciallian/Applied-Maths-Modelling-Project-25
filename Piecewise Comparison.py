import numpy as np
import matplotlib.pyplot as plt

# Values
r = 0.7324081924
r1 = 0.3662040962
r2 = 0.5
K = 200000
alpha = 0.998
sigma = 1
P0 = 100
t0 = 0
t_disease = 15   # Disease Introduced
t_remove = 17
t_end = 25

# Time Range
t_values = np.linspace(t0, t_end, 500)

# Equation without Disease Solution
def logistic_growth(t, P0, r, K):
    return (K * P0 * np.exp(r * t)) / (K + P0 * (np.exp(r * t) - 1))

# Equation with Disease Solution
def logistic_growth_with_disease(t, P1, A, B, t1):
    return (A * P1 * np.exp(A * (t - t1))) / (A + B * P1 * (np.exp(A * (t - t1)) - 1))

# Figure
plt.figure(figsize=(10, 6))

# Original Solution
A = r - alpha * sigma
B = r / K
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
plt.plot(t_values, P_values, label=f"r = {r}", color="blue")

# r1 Solution
A = r1 - alpha * sigma
B = r1 / K
P_values = []
for t in t_values:
    if t < t_disease:
        P = logistic_growth(t, P0, r1, K)
    elif t_disease <= t < t_remove:
        P1 = logistic_growth(t_disease, P0, r1, K)
        P = logistic_growth_with_disease(t, P1, A, B, t_disease)
    else:
        P2 = logistic_growth_with_disease(t_remove, P1, A, B, t_disease)
        P = logistic_growth(t - t_remove, P2, r1, K)
    P_values.append(P)
plt.plot(t_values, P_values, label=f"r = {r1}", color="green")

# r2 Solution
A = r2 - alpha * sigma
B = r2 / K
P_values = []
for t in t_values:
    if t < t_disease:
        P = logistic_growth(t, P0, r2, K)
    elif t_disease <= t < t_remove:
        P1 = logistic_growth(t_disease, P0, r2, K)
        P = logistic_growth_with_disease(t, P1, A, B, t_disease)
    else:
        P2 = logistic_growth_with_disease(t_remove, P1, A, B, t_disease)
        P = logistic_growth(t - t_remove, P2, r2, K)
    P_values.append(P)
plt.plot(t_values, P_values, label=f"r = {r2}", color="red")

# Plotting Graph
plt.axvline(x=t_disease, color="black", linestyle="--", alpha=0.6, label="Disease Introduced")
plt.axvline(x=t_remove, color="black", linestyle="-.", alpha=0.6, label="Disease Removed")
plt.axhline(y=K, color="purple", linestyle="--", alpha=0.6, label="Carrying Capacity")
plt.title("Logistic Growth with Disease Intervention")
plt.xlabel("Time (Years)")
plt.ylabel("Population (P)")
plt.grid(True)
plt.legend()
plt.show()