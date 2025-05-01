import streamlit as st
import numpy as np

st.set_page_config(page_title="Perceptrón demo", page_icon="🤖", layout="wide")

st.title("Perceptrón sencillo")

# ──‒ Layout: dos columnas (60 % – 40 %) ‒──
left, right = st.columns([3, 2])

with left:
    st.subheader("🔢 Entradas")
    x1 = st.number_input("x₁", value=0.0, step=1.0, key="x1")
    x2 = st.number_input("x₂", value=0.0, step=1.0, key="x2")
    w1 = st.number_input("w₁ (peso de x₁)", value=1.0, step=0.1, key="w1")
    w2 = st.number_input("w₂ (peso de x₂)", value=1.0, step=0.1, key="w2")
    bias = st.number_input("bias / umbral b", value=0.0, step=0.1, key="b")

    calcular = st.button("Calcular")

with right:
    st.subheader("⚙️  Salida")
    if calcular:
        # perceptrón: y = f(w·x + b), con f = unidad escalón
        z = np.dot([w1, w2], [x1, x2]) + bias
        y = 1 if z >= 0 else 0
        st.metric("Resultado ŷ", y)
        st.caption(f"z = {z:.2f}  →  y = {y}")
    else:
        st.info("Introduce valores y pulsa **Calcular**")

