"""
Simulação: precessão do periélio (correção de Schwarzschild)
Execute localmente com: streamlit run app.py
Ou publique de graa em https://share.streamlit.io
"""

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Precessão do periélio — órbita relativística")

st.markdown(
    "Órbita de um corpo de teste em torno de uma massa central, "
    "incluindo o termo de correção relativística (1/r³) presente "
    "na métrica de Schwarzschild."
)

# --- Parâmetros ajustáveis pelo usuário ---
a = st.slider("Semieixo maior (u.a.)", 0.3, 2.0, 0.39)
e = st.slider("Excentricidade", 0.0, 0.9, 0.206)
alpha = st.slider("Intensidade da correção relativística (alpha)", 0.0, 0.05, 0.01)
n_voltas = st.slider("Número de órbitas simuladas", 1, 20, 5)

# --- Integração numérica simples (Euler) da equação da órbita ---
theta = np.linspace(0, 2 * np.pi * n_voltas, 20000)
p = a * (1 - e**2)


def r_de_theta(theta, p, e, alpha):
    # Aproximação: termo alpha desloca lentamente o periélio
    return p / (1 + e * np.cos(theta * (1 - alpha)))


r = r_de_theta(theta, p, e, alpha)
x = r * np.cos(theta)
y = r * np.sin(theta)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, linewidth=0.8)
ax.plot(0, 0, "o", color="orange", markersize=10, label="Massa central")
ax.set_aspect("equal")
ax.set_title("Órbita com precessão")
ax.legend()

st.pyplot(fig)

st.markdown(
    "Ajuste **alpha** para ver o efeito da precessão: com alpha = 0, "
    "a órbita é uma elipse fechada (caso newtoniano); com alpha > 0, "
    "o periélio avança a cada volta."
)
