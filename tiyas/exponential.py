import numpy as np
import matplotlib.pyplot as plt

def kualitas_produk(Q0, k, batas_kualitas):
    """
    Fungsi untuk menghitung waktu saat kualitas produk turun ke batas tertentu
    dan menampilkan grafik penurunan kualitas produk.

    Parameter:
    Q0 : float
        Kualitas awal produk (misal 100)
    k : float
        Konstanta peluruhan kualitas (misal 0.05)
    batas_kualitas : float
        Batas kualitas yang ingin diketahui waktunya (misal 80)

    Output:
    t_batas : float
        Waktu (bulan) saat kualitas turun ke batas_kualitas
    """

    # Hitung waktu saat kualitas turun ke batas_kualitas
    import math
    if batas_kualitas >= Q0:
        print("Batas kualitas harus lebih kecil dari kualitas awal.")
        return None

    t_batas = -math.log(batas_kualitas / Q0) / k

    # Buat array waktu untuk grafik
    t = np.linspace(0, t_batas * 2, 500)
    Q = Q0 * np.exp(-k * t)

    # Plot grafik
    plt.figure(figsize=(8,5))
    plt.plot(t, Q, label='Kualitas Produk $Q(t)$')
    plt.axhline(batas_kualitas, color='red', linestyle='--', label=f'Batas Kualitas {batas_kualitas}%')
    plt.axvline(t_batas, color='green', linestyle='--', label=f'Waktu = {t_batas:.2f} bulan')
    plt.scatter(t_batas, batas_kualitas, color='black')
    plt.title('Model Eksponensial Penurunan Kualitas Produk')
    plt.xlabel('Waktu (bulan)')
    plt.ylabel('Kualitas Produk (%)')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Kualitas produk turun menjadi {batas_kualitas}% setelah sekitar {t_batas:.2f} bulan.")
    return t_batas

# Contoh penggunaan aplikasi
if __name__ == "__main__":
    print("Model Eksponensial Penurunan Kualitas Produk")
    Q0 = float(input("Masukkan kualitas awal produk (misal 100): "))
    k = float(input("Masukkan konstanta peluruhan kualitas per bulan (misal 0.05): "))
    batas_kualitas = float(input("Masukkan batas kualitas yang diinginkan (misal 80): "))

    kualitas_produk(Q0, k, batas_kualitas)
