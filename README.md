EXERCICE 1

On travaille sur 1 mole avec v = 1.0e-3 m³/mol. On a b = 4.267e-5 m³/mol, donc v > b condition vérifiée, le modèle VdW est défini.2. Calcul gaz parfait: D'après P = RT/v, avec R=8.314 et T=320K,
P = 8.314*320 / 1e-3 = 2.66e6 Pa = 26.6 bar.3. Calcul Van der Waals: P = RT/(v-b) - a/v²
v-b = 9.57e-4 m³/mol
RT/(v-b) = 27.79 bar
a/v² = 3.64 bar
P = 27.79 - 3.64 = 24.15 bar = 2.415e6 Pa.4. Comparaison: P_vdw < P_ideal. Le terme répulsif 1/(v-b) augmente la pression, mais le terme attractif -a/v² la diminue plus fortement à ce volume.
EXERCICE 2;

Gaz parfait: P=RT/v
On dérive à v constant, R/v est constante:(∂P/∂T)v​=R/vVan der Waals: P=RT/(v−b)−a/v2
Le terme −a/v2 ne dépend pas de T, sa dérivée est 0. R/(v−b) est constant à v constant:(∂P/∂T)v​=R/(v−b)
Unité et cohérence
[P]=Pa=J/m3
=K[T][(∂P/∂T)v​]=Pa/K=J/(m3⋅K)Or (∂S/∂v)T​:
=J/K, [v]=m3/mol[S][(∂S/∂v)T​]=m3/molJ/K​=J/(K⋅m3)C'est la même unité. C'est cohérent, c'est pour ça que Maxwell dF=−SdT−Pdv peut égaler les deux dérivées croisées. En molaire on a bien Pa/K=J/(K⋅m3).
Valeur numérique au point T=320K,v=1e−3:
Idéal: R/v=8.314/1e−3=8314Pa/KVdW: R/(v−b)=8.314/9.573e−4=8685Pa/K
EXERCICE 3;

Formule du cours: (∂U/∂v)T​=T(∂P/∂T)v​−P
Avec P=RT/v, on a (∂P/∂T)v​=R/v(∂U/∂v)T​=T⋅R/v−RT/v=0Interprétation: L'énergie interne d'un gaz parfait ne dépend que de T, pas de v. Pas d'interactions entre molécules. C'est la 1ère loi de Joule: en détente isotherme, ΔU=0.
2. Van der Waals - Démonstration
P=RT/(v−b)−a/v2, donc (∂P/∂T)v​=R/(v−b)(∂U/∂v)T​=Tv−bR​−[v−bRT​−v2a​]=v2a​Le RT/(v−b) se simplifie, il ne reste que le terme d'attraction.
Intégration à T constant de v1​ à v2​:ΔU=∫v1​v2​​v2a​dv=a[−v1​]v1​v2​​=a(v1​1​−v2​1​)3. Calcul numérique T=320K, v1​=1e−3→v2​=2e−3
À la main:
a=0.364
1/v1​=1000, 1/v2​=500
ΔUvdw​=0.364×(1000−500)=182J/mol
ΔUideal​=0J/mol
EXERCICE 4

Démonstration
Gaz parfait: (∂P/∂T)v​=R/v, (∂P/∂v)T​=−RT/v2Cp​−Cv​=−T−RT/v2(R/v)2​=RVdW: (∂P/∂T)v​=R/(v−b), (∂P/∂v)T​=−RT/(v−b)2+2a/v3Cp​−Cv​=−T−RT/(v−b)2+2a/v3R2/(v−b)2​=1−RTv32a(v−b)2​R​Condition: (∂P/∂v)T​=0 sinon divergence, et stable seulement si <0.
Calcul T=320K,v=1e−3
Idéal: 8.314 J/mol/K
VdW: 11.10 J/mol/Kdpdv=−2.17×109<0 donc stable.