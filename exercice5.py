import sympy as sp
R = 8.314462618
a = 0.364
b = 4.267e-5
T = 320.0
v = 1.0e-3
Ts, vs, Rs, aa, bb = sp.symbols("T v R a b", positive=True)
P = Rs*Ts/(vs-bb) - aa/vs**2
dP_dT = sp.diff(P, Ts)
dP_dv = sp.diff(P, vs)
dvdT_P = sp.simplify(-dP_dT/dP_dv)
valeur = dvdT_P.subs({Ts:T, vs:v, Rs:R, aa:a, bb:b})
print("(dv/dT)P symbolique :", dvdT_P)
print("(dv/dT)P VdW :", float(valeur))
print("(dS/dP)T VdW :", -float(valeur))
# Gaz parfait
valeur_ideal = dvdT_P.subs({Ts:T, vs:v, Rs:R, aa:0, bb:0})
print("(dv/dT)P ideal :", float(valeur_ideal))
print("(dS/dP)T ideal :", -float(valeur_ideal))