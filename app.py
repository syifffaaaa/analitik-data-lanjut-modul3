import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Streamlit Simple App')

# Menambahkan navigasi di sidebar
page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])

if page == "Dataset":
    st.header("Halaman Dataset")
     # Baca file CSV
    data = pd.read_csv("pddikti_example.csv")

    # Tampilkan data di Streamlit
    st.write(data)
    
elif page == "Visualisasi":
    st.header("Halaman Visualisasi")
    
    # Baca file CSV
    data = pd.read_csv("pddikti_example.csv")

    # Filter berdasarkan universitas
    selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data = data[data['universitas'] == selected_university]

    # Buat figure dan axis baru
    fig, ax = plt.subplots(figsize=(12, 6))

    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]
        subset = subset.sort_values(by='id', ascending=False)

        ax.plot(subset['semester'], subset['jumlah'], label=prog_studi)

    ax.set_title(f"Visualisasi Data untuk {selected_university}")
    ax.set_xlabel('Semester')
    ax.set_ylabel('Jumlah')
    ax.legend()
    plt.xticks(rotation=90)  # Rotasi label sumbu x menjadi vertikal

    # Tampilkan figure di Streamlit
    st.pyplot(fig)
    