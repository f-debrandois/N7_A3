## Text

On étudie le systeme suivant :

$$
\begin{cases}
-\Delta \phi = 0 & \text{dans } \Omega \\
\frac{\partial \phi}{\partial n} = 0 & \text{sur } \Gamma \\
\phi = 0 & \text{sur } \gamma_1 \\
\frac{\partial \phi}{\partial n} = g & \text{sur } \gamma_2
\end{cases}
$$

1. Montrer que la formulation variationnelle correspondant à ce problème est :

$$
\text{Trouver } \phi \in V = \{ w \in H^1(\Omega) \text{ tel que } \text{Tr}_{\gamma_1}(w) = 0 \} \text{ tel que } \forall v \in V, \int_{\Omega} \nabla \phi \nabla v = \int_{\gamma_2} g v
$$

2. On note $\phi_h$ la solution numérique obtenue sur $V_h = \{ w \in V \text{ tel que } \forall T \in \mathcal{T}_h, w_{h|T} \in \mathbb{R}^2\[x\] \}$.
Quelles estimations a-t-on pour les erreurs $\| \phi - \phi_h \|_{H^1}$ et $\| \phi - \phi_h \|_{L^2}$ ?
On prendra soin de préciser la régularité de la solution $\phi$ nécessaire à l'obtention de ces estimations.
