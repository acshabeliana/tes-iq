import streamlit as st
import pandas as pd
import numpy as np

# Function to calculate the Z-score
def calculate_z_score(X, mu, sigma):
    return (X - mu) / sigma

# Function to calculate IQ
def calculate_iq(z_score):
    return 100 + 15 * z_score

# Function to categorize the IQ
def categorize_iq(iq):
    if iq < 100:
        return "Di Bawah Rata-Rata"
    elif iq == 100:
        return "Rata-Rata"
    else:
        return "Di Atas Rata-Rata"

# Load the CSV data
@st.cache_data
def load_data():
    # Sample data, replace with the full dataset CSV as needed
    data = pd.read_csv("iq_test_data.csv", delimiter=";")
    return data

# Streamlit UI
st.title("Aplikasi Tes IQ")

# Load and display the dataset
data = load_data()

# Show a preview of the data
st.write("Preview Data CSV:", data.head())

# Input for raw score (X)
raw_score = st.number_input("Masukkan Skor Mentah Anda:", min_value=0, max_value=200)

# Get the mean (μ) and standard deviation (σ) from the dataset
mu = data['Skor Mentah'].mean()
sigma = data['Skor Mentah'].std()

# Calculate the Z-score
z_score = calculate_z_score(raw_score, mu, sigma)

# Calculate IQ
iq = calculate_iq(z_score)

# Categorize the IQ
category = categorize_iq(iq)

# Display the results
st.write(f"Skor Mentah Anda: {raw_score}")
st.write(f"Z-score: {z_score:.2f}")
st.write(f"Nilai IQ Anda: {iq:.2f}")
st.write(f"Kategori IQ: {category}")

# Update the CSV data with the new IQ and Category information
new_data = pd.DataFrame({
    'Skor Mentah': [raw_score],
    'Nilai IQ': [iq],
    'Keterangan': [category],
    'Outcome': [1 if category == "Di Bawah Rata-Rata" else (2 if category == "Rata-Rata" else 3)]
})

# Show the updated results
st.write("Hasil Tes Anda telah ditambahkan ke CSV data:", new_data)
