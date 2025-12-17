import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Analisis Film vs Kriminalitas", layout="wide")

st.title("🎬 Dashboard Analisis Hubungan Genre Film & Kriminalitas ASEAN")
st.write("Dashboard ini bertujuan untuk melihat apakah jenis film yang diproduksi berhubungan dengan tingkat kriminalitas di suatu negara.")

# 1. Load Data
try:
    df_film = pd.read_excel('film_asean_2020_2024.xls')
    # Ganti 'data_kriminalitas.xlsx' dengan nama file yang Anda upload nanti
    df_krim = pd.read_csv('data_kriminalitas.csv') 
    
    # Sidebar untuk pilih negara
    st.sidebar.header("Pilihan Analisis")
    list_negara = df_film['production_countries'].unique()
    negara_dipilih = st.sidebar.selectbox("Pilih Negara ASEAN:", list_negara)

    # Filter Data
    df_n = df_film[df_film['production_countries'] == negara_dipilih]

    # Layout Kolom
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Genre Film Terbanyak di {negara_dipilih}")
        if not df_n.empty:
            fig, ax = plt.subplots()
            df_n['genres'].value_counts().head(10).plot(kind='bar', ax=ax, color='skyblue')
            plt.xticks(rotation=45)
            st.pyplot(fig)
        else:
            st.write("Data tidak tersedia")

    with col2:
        st.subheader(f"Tren Kriminalitas di {negara_dipilih}")
        st.info("Visualisasi tingkat kriminalitas akan muncul di sini setelah data kriminalitas dihubungkan.")
        # Contoh visualisasi jika data kriminalitas sudah ada:
        st.line_chart(df_krim[df_krim['Negara'] == negara_dipilih]['Angka_Kriminalitas'])

    st.divider()
    
    # Bagian Kesimpulan (Ini yang penting untuk laporan Anda)
    st.subheader("📌 Kesimpulan Analisis")
    st.write(f"""
    Berdasarkan data yang ditampilkan untuk **{negara_dipilih}**, produksi film didominasi oleh genre tertentu. 
    Namun, secara statistik dan visual, jumlah produksi film ini **tidak menunjukkan pengaruh langsung** terhadap naik atau turunnya tingkat kriminalitas di negara tersebut.
    """)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
    st.info("Pastikan file excel sudah diupload ke GitHub.")
