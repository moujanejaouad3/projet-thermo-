import numpy as np
import sympy as sp

R = 8.314462618
a = 0.364
b = 4.267e-5
T = 320.0
v = 1.0e-3

def p_vdw(T, v):
    if np.any(np.asarray(v) <= b):
        raise ValueError("Le volume doit etre superieur a b")
    return R*T/(v-b) - a/v**2

# 1. Dérivées symboliques
Ts, vs, Rs, aa, bb = sp.symbols("T v R a b", positive=True)
P = Rs*Ts/(vs-bb) - aa/vs**2
dP_dT = sp.diff(P, Ts)
dP_dv = sp.diff(P, vs)
print("dP/dT =", sp.simplify(dP_dT))
print("dP/dv =", sp.simplify(dP_dv))

# 2. Controle par differences finies centrees
h = 0.01
dP_dT_num = (p_vdw(T+h,v)-p_vdw(T-h,v))/(2*h)
dP_dT_exact = R/(v-b)
erreur = abs(dP_dT_num-dP_dT_exact)/abs(dP_dT_exact)

print("Derivee numerique :", dP_dT_num)
print("Derivee exacte :", dP_dT_exact)
print("Erreur relative :", erreur)

# Test plusieurs h
print("\nTest de h :")
for h in [1, 0.1, 0.01, 1e-4, 1e-6]:
    d_num = (p_vdw(T+h,v)-p_vdw(T-h,v))/(2*h)
    err = abs(d_num-dP_dT_exact)/abs(dP_dT_exact)
    print(f"h={h} -> erreur={err:.2e}")