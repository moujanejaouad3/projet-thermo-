import numpy as np
import matplotlib.pyplot as plt

R = 8.314462618
a = 0.364
b = 4.267e-5

v1 = 1.0e-3
v2 = 2.0e-3

delta_U_vdw = a*(1/v1 - 1/v2)
delta_U_ideal = 0.0

print("Delta U Van der Waals (J/mol) :", delta_U_vdw)
print("Delta U Gaz parfait (J/mol) :", delta_U_ideal)

v2_range = np.linspace(v1, 5e-3, 200)
delta_U_range = a*(1/v1 - 1/v2_range)

plt.figure()
plt.plot(v2_range, delta_U_range)
plt.axhline(0, color='k', linestyle='--')
plt.xlabel("v2 (m3/mol)")
plt.ylabel("Delta U (J/mol)")
plt.title("Delta U vs v2 - T=320K")
plt.grid(True)
plt.show()