# 💰 Sistem Prediksi Pelunasan Piutang Pajak Daerah

## 📋 Deskripsi Project
Project ini adalah aplikasi machine learning untuk memprediksi status pelunasan piutang pajak daerah. 
Menggunakan algoritma Random Forest Classifier dengan akurasi 99.89%.

## 🎯 Business Case
**Masalah**: Pemerintah daerah menghadapi tantangan dalam pengelolaan piutang pajak dengan 60% piutang masih belum lunas.

**Solusi**: Sistem prediksi berbasis ML untuk:
- Prioritas penagihan yang lebih efektif
- Alokasi sumber daya penagihan optimal
- Early warning system piutang bermasalah
- Strategi penagihan personal

## 📊 Dataset
- **Sumber**: Data penagihan piutang pajak daerah 2012-2025
- **Jumlah records**: 4,539
- **Features**: 
  - TAHUN (tahun pajak)
  - KATEGORI PAJAK (8 kategori)
  - SALDO AWAL (nilai piutang)
  - REALISASI PIUTANG (pembayaran)
  - PERSENTASE_TERBAYAR

## 🤖 Model Machine Learning

### Model yang Diuji
1. **Logistic Regression** - Accuracy: 89.10%
2. **Random Forest** - Accuracy: 99.89% ✅ (Dipilih)
3. **Decision Tree** - Accuracy: 99.89%

### Performa Model Terbaik (Random Forest)
- **Accuracy**: 99.89%
- **Precision**: 99.89%
- **Recall**: 99.89%
- **F1-Score**: 0.9989

### Feature Importance
1. PERSENTASE_TERBAYAR: 51.88%
2. REALISASI PIUTANG: 23.49%
3. TAHUN: 12.24%
4. SALDO AWAL: 10.53%
5. KATEGORI PAJAK: 1.85%

## 🚀 Cara Menjalankan

### Prerequisites
```bash
Python 3.8+
pip
```

### Instalasi
```bash
# Clone atau download repository
cd project-folder

# Install dependencies
pip install -r requirements.txt
```

### Menjalankan Aplikasi Streamlit
```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`

## 📁 Struktur Project
```
project-folder/
│
├── app.py                        # Aplikasi Streamlit
├── model_terbaik_piutang.pkl     # Model Random Forest
├── scaler_piutang.pkl            # StandardScaler
├── encoder_kategori.pkl          # Label Encoder
├── model_metadata.pkl            # Metadata model
├── piutang_clean.csv             # Dataset cleaned
├── requirements.txt              # Dependencies
└── README.md                     # Dokumentasi
```

## 💻 Cara Menggunakan Aplikasi

1. Buka aplikasi di browser
2. Di sidebar, masukkan:
   - Tahun pajak
   - Kategori pajak
   - Saldo awal piutang
   - Realisasi pembayaran
3. Klik tombol "PREDIKSI STATUS PELUNASAN"
4. Lihat hasil prediksi dan rekomendasi

## 📈 Hasil Evaluasi

### Confusion Matrix (Test Set)
```
                Predicted
Actual      Belum Lunas  Lunas
Belum Lunas     544        1
Lunas             0      363
```

### Classification Report
```
              precision    recall  f1-score   support
Belum Lunas     1.00      1.00      1.00       545
Lunas           1.00      1.00      1.00       363
```

## 🎓 Informasi Akademik
- **Mata Kuliah**: Machine Learning
- **Program Studi**: Magister Informatika
- **Universitas**: Universitas Islam Indonesia
- **Dosen**: Dr. Syarif Hidayat, S.Kom., M.I.T.
- **Ujian**: UTS Semester Ganjil 2025/2026

## 📝 Catatan
- Model ini dilatih dengan data historis tahun 2012-2025
- Prediksi bersifat probabilistik dan sebaiknya dikombinasikan dengan analisis manual
- Untuk deployment production, pertimbangkan retraining berkala dengan data terbaru

## 📧 Kontak
Untuk pertanyaan atau feedback, silakan hubungi melalui platform pembelajaran.

---
© 2025 - Sistem Prediksi Piutang Pajak Daerah
