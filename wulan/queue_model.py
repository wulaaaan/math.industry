import streamlit as st
import matplotlib.pyplot as plt

def run_queue_model():
    st.title("Model Antrian M/M/1")
    lambd = st.number_input("Tingkat kedatangan rata-rata (λ)", value=5.0)
    mu = st.number_input("Tingkat pelayanan rata-rata (μ)", value=8.0)

    if lambd >= mu:
        st.error("λ harus lebih kecil dari μ agar sistem stabil.")
        return

    rho = lambd / mu
    L = rho / (1 - rho)
    Lq = rho ** 2 / (1 - rho)
    W = 1 / (mu - lambd)
    Wq = lambd / (mu * (mu - lambd))

    st.markdown(f"**Tingkat Utilisasi (ρ)**: {rho:.2f}")
    st.markdown(f"**Rata-rata jumlah dalam sistem (L)**: {L:.2f}")
    st.markdown(f"**Rata-rata jumlah dalam antrian (Lq)**: {Lq:.2f}")
    st.markdown(f"**Rata-rata waktu dalam sistem (W)**: {W:.2f} satuan waktu")
    st.markdown(f"**Rata-rata waktu dalam antrian (Wq)**: {Wq:.2f} satuan waktu")

    plt.bar(["L", "Lq"], [L, Lq], color=["blue", "orange"])
    plt.title("Jumlah rata-rata dalam sistem dan antrian")
    st.pyplot(plt)