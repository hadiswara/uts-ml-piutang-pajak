
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Pelunasan Piutang Pajak", 
    page_icon="💰",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 36px;
    font-weight: bold;
    color: #1E88E5;
    text-align: center;
    padding: 20px;
}
.metric-card {
    background-color: #f0f2f6;
    padding: 20px;
    border-radius: 10px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# Load model dan preprocessor
@st.cache_resource
def load_models():
    model = joblib.load('model_terbaik_piutang.pkl')
    scaler = joblib.load('scaler_piutang.pkl')
    encoder = joblib.load('encoder_kategori.pkl')
    with open('model_metadata.pkl', 'rb') as f:
        metadata = pickle.load(f)
    return model, scaler, encoder, metadata

model, scaler, encoder, metadata = load_models()

# Header
st.markdown('<p class="main-header">💰 Sistem Prediksi Pelunasan Piutang Pajak Daerah</p>', unsafe_allow_html=True)
st.markdown("---")

# Informasi singkat
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Model", metadata['model_name'])
with col2:
    st.metric("Akurasi", f"{metadata['accuracy']*100:.2f}%")
with col3:
    st.metric("F1-Score", f"{metadata['f1_score']:.4f}")

st.markdown("---")

# Layout 2 kolom
col_input, col_output = st.columns([1, 1])

with col_input:
    st.subheader("📋 Input Data Piutang")

    # Input fields
    tahun = st.selectbox(
        "Tahun Pajak",
        options=list(range(2012, 2026)),
        index=13  # default 2025
    )

    kategori_pajak = st.selectbox(
        "Kategori Pajak",
        options=list(metadata['kategori_mapping'].keys())
    )

    saldo_awal = st.number_input(
        "Saldo Awal (Rp)",
        min_value=0,
        value=1000000,
        step=100000,
        format="%d"
    )

    realisasi_piutang = st.number_input(
        "Realisasi Piutang / Sudah Dibayar (Rp)",
        min_value=0,
        max_value=saldo_awal,
        value=0,
        step=100000,
        format="%d"
    )

    # Hitung persentase terbayar
    if saldo_awal > 0:
        persentase_terbayar = (realisasi_piutang / saldo_awal) * 100
    else:
        persentase_terbayar = 0

    st.info(f"💡 Persentase Terbayar: **{persentase_terbayar:.2f}%**")

    # Tombol prediksi
    predict_button = st.button("🔮 PREDIKSI STATUS PELUNASAN", use_container_width=True, type="primary")

with col_output:
    st.subheader("📊 Hasil Prediksi")

    if predict_button:
        # Encode kategori pajak
        kategori_encoded = metadata['kategori_mapping'][kategori_pajak]

        # Persiapkan data input
        input_data = pd.DataFrame({
            'TAHUN': [tahun],
            'SALDO AWAL': [saldo_awal],
            'REALISASI PIUTANG': [realisasi_piutang],
            'PERSENTASE_TERBAYAR': [persentase_terbayar],
            'KATEGORI_PAJAK_ENCODED': [kategori_encoded]
        })

        # Scaling
        input_scaled = scaler.transform(input_data)

        # Prediksi
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0]

        # Tampilkan hasil
        st.markdown("### 🎯 Prediksi:")

        if prediction == 1:
            st.success("### ✅ PIUTANG DIPREDIKSI AKAN LUNAS")
            confidence = probability[1] * 100
            st.metric("Confidence Level", f"{confidence:.2f}%")

            st.info("""
            **💡 Rekomendasi:**
            - Piutang ini memiliki potensi tinggi untuk dilunasi
            - Tetap lakukan monitoring rutin
            - Berikan apresiasi kepada wajib pajak yang tertib
            """)
        else:
            st.error("### ⚠️ PIUTANG DIPREDIKSI TIDAK LUNAS")
            confidence = probability[0] * 100
            st.metric("Confidence Level", f"{confidence:.2f}%")

            st.warning("""
            **💡 Rekomendasi Tindakan:**
            - Prioritaskan untuk tindakan penagihan intensif
            - Hubungi wajib pajak untuk negosiasi pembayaran
            - Pertimbangkan skema cicilan atau insentif
            - Monitor secara berkala dan eskalasi jika perlu
            """)

        # Detail input
        with st.expander("📋 Detail Input Data"):
            st.write(input_data)

# Sidebar - Informasi tambahan
with st.sidebar:
    st.header("ℹ️ Informasi Sistem")

    st.markdown("""
    ### Tentang Aplikasi
    Aplikasi ini menggunakan **Machine Learning** untuk memprediksi 
    kemungkinan pelunasan piutang pajak daerah.

    ### Model
    - **Algoritma**: Random Forest Classifier
    - **Akurasi**: 99.89%
    - **F1-Score**: 0.9989

    ### Fitur Penting
    """)

    # Tampilkan feature importance
    for feature_info in metadata['feature_importance'][:3]:
        st.write(f"**{feature_info['Feature']}**: {feature_info['Importance']:.2%}")

    st.markdown("---")
    st.markdown("""
    ### Cara Menggunakan
    1. Pilih tahun pajak
    2. Pilih kategori pajak
    3. Masukkan saldo awal piutang
    4. Masukkan realisasi pembayaran
    5. Klik tombol prediksi

    ### Status Output
    - ✅ **Lunas**: Saldo akhir = 0
    - ⚠️ **Belum Lunas**: Saldo akhir > 0
    """)

    st.markdown("---")
    st.caption("© 2025 - Sistem Prediksi Piutang Pajak")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Dibuat untuk UTS Machine Learning - Magister Informatika UII</p>
    <p>Model dilatih dengan 4,539 records data historis piutang pajak</p>
</div>
""", unsafe_allow_html=True)
