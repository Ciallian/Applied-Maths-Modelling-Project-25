import numpy as np
import matplotlib.pyplot as plt

# Values
P0 = 100
r_l = 0.7324081924
r_e = 0.3662040962
K = 200000
t_e = 21
t_max = 25
num_points = 1000
t = np.linspace(0, t_max, num_points)


# Disease Values
alpha = 0.998
sigma = 1
t_disease = 15  # Disease introduced
t_remove = 17   # Disease removed

# Exponential
P_exp = np.where(t <= t_e,P0 * np.exp(r_e * t),np.nan)

# Logistic
P_log = (K * P0 * np.exp(r_l * t)) / (K - P0 + P0 * np.exp(r_l * t))

# Logistic with Disease (Piecewise)
A = r_l - alpha * sigma
B = r_l / K

def logistic_growth(t, P0, r_l, K):
    return (K * P0 * np.exp(r_l * t)) / (K + P0 * (np.exp(r_l * t) - 1))

def logistic_growth_with_disease(t, P1, A, B, t1):
    return (A * P1 * np.exp(A * (t - t1))) / (A + B * P1 * (np.exp(A * (t - t1)) - 1))

P_piecewise = []
for time in t:
    if time < t_disease:
        P = logistic_growth(time, P0, r_l, K)
    elif t_disease <= time < t_remove:
        P1 = logistic_growth(t_disease, P0, r_l, K)
        P = logistic_growth_with_disease(time, P1, A, B, t_disease)
    else:
        P2 = logistic_growth_with_disease(t_remove, P1, A, B, t_disease)
        P = logistic_growth(time - t_remove, P2, r_l, K)
    P_piecewise.append(P)


plt.figure(figsize=(10, 6))
# Exponential
plt.plot(t, P_exp, label="Exponential Growth", color="green", linestyle="-", )

# Logistic
plt.plot(t, P_log, label="Logistic Growth", color="red", linestyle="-", )

# Piecewise (Logistic + Disease)
plt.plot(t, P_piecewise, label="Logistic with Disease", color="blue", linestyle="-", alpha=0.6, )

plt.axhline(y=K, color="purple", linestyle="--", alpha=0.4, label="Carrying Capacity (K)")
plt.title("Comparison of Rabbit Population Growth Models", fontsize=14)
plt.xlabel("Time (Years)", fontsize=12)
plt.ylabel("Population (P)", fontsize=12)
plt.grid(True, alpha=0.7)
plt.legend(fontsize=10, loc='upper left')
max_pop = max(max(P_exp), max(P_log), max(P_piecewise))
plt.ylim(0, max_pop * 1.1)
plt.tight_layout()
plt.show()