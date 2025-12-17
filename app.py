import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Film ASEAN 2020-2024", layout="wide")

# Judul Utama
st.title("🎬 Analisis Data Film ASEAN (2020-2024)")
st.markdown("Aplikasi ini dibuat untuk memenuhi tugas mata kuliah PSD.")

# 1. Load Data
@st.cache_data # Agar data tidak reload terus menerus
def load_data():
    # Pastikan file excel ini ada dalam satu folder yang sama di GitHub
    df = pd.read_excel('film_asean_2020_2024.xls')
    return df

try:
    df = load_data()
    
    # Sidebar untuk Filter
    st.sidebar.header("Filter Data")
    negara = st.sidebar.multiselect(
        "Pilih Negara:",
        options=df['production_countries'].unique(),
        default=df['production_countries'].unique()[:3]
    )
    
    df_selection = df[df['production_countries'].isin(negara)]

    # 2. Layout Utama (Tabs)
    tab1, tab2, tab3 = st.tabs(["📊 Visualisasi Data", "🔍 Eksplorasi Data", "🤖 Prediksi (Mockup)"])

    with tab1:
        st.subheader("Distribusi Film Per Negara")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.countplot(data=df_selection, x='production_countries', ax=ax, palette='viridis')
        plt.xticks(rotation=45)
        st.pyplot(fig)
        
        st.write("Grafik ini menunjukkan jumlah produksi film berdasarkan negara yang dipilih.")

    with tab2:
        st.subheader("Data Mentah")
        st.dataframe(df_selection, use_container_width=True)

    with tab3:
        st.subheader("Implementasi Model")
        st.info("Bagian ini digunakan untuk simulasi Model Serving (Bab 3.2 dalam laporan).")
        
        # Contoh Input untuk Prediksi
        input_judul = st.text_input("Masukkan Judul Film:")
        input_genre = st.selectbox("Pilih Genre Utama:", ["Action", "Drama", "Horror", "Comedy"])
        
        if st.button("Analisis"):
            # Di sini biasanya kita memanggil model.pkl
            # Untuk sementara kita buat logika dummy/sederhana
            st.success(f"Hasil Analisis untuk film '{input_judul}':")
            st.write(f"Berdasarkan algoritma, genre {input_genre} memiliki potensi popularitas tinggi di kawasan ASEAN.")

except Exception as e:
    st.error(f"Gagal memuat data. Pastikan file 'film_asean_2020_2024.xls' sudah diupload ke GitHub. Error: {e}")