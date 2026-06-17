import streamlit as st
import pandas as pd

# 1. PENGATURAN HALAMAN (Harus ditaruh paling atas)
# Membuat tampilan melebar, memberi judul tab browser, dan ikon
st.set_page_config(page_title="Dashboard Pertamina", page_icon="⛽", layout="wide")

# 2. JUDUL DAN DESKRIPSI
st.title("⛽ Dashboard Data MyPertamina")
st.write("Visualisasi dan ringkasan data transaksi bahan bakar.")
st.markdown("---") # Membuat garis pembatas horizontal

# Membaca file CSV
data = pd.read_csv("MyPertamina1.csv")

# 3. SIDEBAR (Menu Samping)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/id/thumb/4/44/Logo_Pertamina.png/800px-Logo_Pertamina.png", width=150)
st.sidebar.header("Panel Kendali")
st.sidebar.info("Saat ini menampilkan keseluruhan data. Fitur filter bisa ditambahkan di sini nanti.")

# 4. KOTAK METRIK (Ringkasan Angka Penting)
st.subheader("📌 Ringkasan Utama")
col1, col2, col3 = st.columns(3)

# Menampilkan total baris data sebagai "Total Transaksi"
col1.metric("Total Transaksi Terdata", f"{len(data)} Baris")
col2.metric("Status Sistem", "Optimal", "+ Stabil")
col3.metric("Format Data", "CSV", "Valid")

st.markdown("---")

# 5. TATA LETAK DUA KOLOM (Kiri Tabel, Kanan Grafik)
kiri, kanan = st.columns(2)

with kiri:
    st.subheader("📋 Tabel Data Detail")
    # Tampilkan tabel yang menyesuaikan lebar kolom
    st.dataframe(data, use_container_width=True)

with kanan:
    st.subheader("📊 Visualisasi Data")
    st.info("Area ini siap diisi dengan grafik (bar chart/line chart).")
    st.write("Untuk memunculkan grafik, Streamlit perlu tahu kolom apa yang mau dijadikan acuan (misal: kolom X untuk Tanggal, kolom Y untuk Liter).")
    
    # KODE GRAFIK (Saat ini dimatikan pakai tanda '#' agar tidak error)
    # Hapus tanda '#' di bawah ini jika nama kolomnya sudah disesuaikan dengan datamu:
    # st.bar_chart(data, x="TANGGAL", y="JUMLAH_LITER")