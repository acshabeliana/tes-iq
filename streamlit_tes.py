import streamlit as st
import pandas as pd

# Fungsi untuk menghitung nilai IQ berdasarkan skor mentah
def hitung_iq(skor_mentah, rata_rata, std_deviasi):
    z = (skor_mentah - rata_rata) / std_deviasi
    iq = 100 + 15 * z
    return iq

# Mengunggah file CSV
def load_data():
    data = pd.read_csv('data.csv', delimiter=';')
    return data

# Tampilan aplikasi
st.title('Aplikasi Tes IQ')

# Input skor mentah
skor_mentah = st.number_input("Masukkan Skor Mentah Anda", min_value=0, max_value=200)

# Jika skor mentah dimasukkan, tampilkan IQ dan kategori
if skor_mentah:
    # Load data dari CSV
    data = load_data()
    
    # Hitung rata-rata dan standar deviasi dari skor mentah di data
    rata_rata = data['Skor Mentah'].mean()
    std_deviasi = data['Skor Mentah'].std()
    
    # Hitung IQ dari skor mentah yang dimasukkan
    iq = hitung_iq(skor_mentah, rata_rata, std_deviasi)
    
    # Tentukan kategori berdasarkan IQ
    if iq < 100:
        kategori = "Di Bawah Rata-Rata"
        outcome = 1
    elif iq == 100:
        kategori = "Rata-Rata"
        outcome = 2
    else:
        kategori = "Di Atas Rata-Rata"
        outcome = 3
    
    # Menampilkan hasil
    st.write(f"Nilai IQ Anda: {iq:.2f}")
    st.write(f"Kategori: {kategori}")
    st.write(f"Outcome: {outcome}")
    
    # Menampilkan data terkait dari CSV
    hasil = data[data['Skor Mentah'] == skor_mentah]
    if not hasil.empty:
        st.write("Data Terkait:")
        st.dataframe(hasil[['Skor Mentah', 'Nilai IQ', 'Keterangan', 'Outcome']])
    else:
        st.write("Tidak ada data terkait dengan skor mentah yang dimasukkan.")
