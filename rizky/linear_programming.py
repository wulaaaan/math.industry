import streamlit as st
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

def run_linear_programming():
    st.title("Optimasi Produksi (Linear Programming)")
    st.write("Contoh: Maksimalkan Z = 40x + 30y dengan kendala:")
    st.latex("2x + y \leq 100")
    st.latex("x + y \leq 80")
    st.latex("x, y \geq 0")

    c = [-40, -30]  # koefisien fungsi tujuan (maksimasi)
    A = [[2, 1], [1, 1]]
    b = [100, 80]
    x0_bounds = (0, None)
    x1_bounds = (0, None)

    res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')
    
    if res.success:
        st.success(f"Solusi optimal: x = {res.x[0]:.2f}, y = {res.x[1]:.2f}")
        st.info(f"Nilai maksimum Z = {-res.fun:.2f}")

        # Visualisasi
        x = np.linspace(0, 100, 200)
        y1 = (100 - 2 * x)
        y2 = (80 - x)
        
        plt.figure(figsize=(8, 6))
        plt.plot(x, y1, label=r'$2x + y \leq 100$')
        plt.plot(x, y2, label=r'$x + y \leq 80$')
        plt.fill_between(x, np.minimum(y1, y2), color='skyblue', alpha=0.3)
        plt.plot(res.x[0], res.x[1], 'ro', label='Solusi Optimal')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Wilayah Feasible dan Solusi Optimal')
        plt.legend()
        st.pyplot(plt)
    else:
        st.error("Tidak ditemukan solusi optimal.")