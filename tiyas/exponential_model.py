import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run_exponential_model():
    st.title("Model Eksponensial (Decay/Growth)")
    A = st.number_input("Nilai awal (A)", value=100.0)
    r = st.number_input("Laju pertumbuhan (positif) atau peluruhan (negatif) (r)", value=-0.1)
    t = np.linspace(0, 50, 200)
    y = A * np.exp(r * t)

    st.line_chart({"Waktu": t, "Nilai": y})
    plt.plot(t, y)
    plt.title("Model Eksponensial")
    plt.xlabel("Waktu")
    plt.ylabel("Nilai")
    st.pyplot(plt)