import numpy as np
import matplotlib.pyplot as plt

# Données du sujet
R = 8.314462618
a = 0.364
b = 4.267e-5
T = 320.0
v = 1.0e-3

def cp_moins_cv_vdw(T, v):
    dpdt = R/(v-b)
    dpdv = -R*T/(v-b)**2 + 2*a/v**3
    if np.any(np.isclose(dpdv, 0, atol=1e-12)):
        raise ValueError("Derivee en volume proche de zero")
    # Phase stable seulement si dpdv < 0
    if np.any(dpdv >= 0):
        print("Attention: dpdv >= 0 -> phase instable")
    return -T*dpdt**2/dpdv

# 1. Gaz parfait -> R
print("Cp-Cv ideal :", R)

# 2. VdW au point demandé
print("Cp-Cv VdW :", cp_moins_cv_vdw(T,v))

# 3. Courbe pour le rapport (bonus pour ton graphe)
v_range = np.linspace(0.5e-3, 5e-3, 300)
CpCv_range = cp_moins_cv_vdw(T, v_range)

plt.plot(v_range*1e3, CpCv_range, label="VdW")
plt.axhline(R, color='k', linestyle='--', label="Ideal = R")
plt.xlabel("v [L/mol]")
plt.ylabel("Cp-Cv [J/mol/K]")
plt.legend()
plt.grid()
plt.show()