# 📊 Data Statistik Project Analisa Tumor Otak

## 🧠 Overview
Project ini berfokus pada klasifikasi citra MRI otak untuk mendeteksi keberadaan tumor menggunakan Convolutional Neural Network (CNN) dengan dua optimizer berbeda (Adam dan Nadam).

## 📈 Statistik Dataset

### Total Dataset
- **Total Citra MRI:** 179 gambar
- **Format Gambar:** JPG, JPEG, PNG
- **Ukuran Input:** 150x150 pixel
- **Mode Warna:** RGB (3 channel)

### Distribusi Kelas
| Kelas | Jumlah Data | Persentase |
|-------|-------------|------------|
| **No Tumor** | 92 gambar | 51.4% |
| **Tumor** | 87 gambar | 48.6% |

### Data Splitting
| Split | No Tumor | Tumor | Total | Persentase |
|-------|----------|--------|-------|------------|
| **Training** | 78 gambar | 124 gambar | 202 gambar | 80% |
| **Validation** | 20 gambar | 31 gambar | 51 gambar | 20% |

*Catatan: Terdapat perbedaan antara data di notebook dan README. Dataset aktual yang tersimpan saat ini: 179 gambar total.*

## 🏗️ Arsitektur Model

### Struktur CNN (Kedua Model)
```
Input (150x150x3)
├── Conv2D (32 filters, 3x3, stride 4x4) + ReLU
├── MaxPooling2D (2x2, stride 2x2)
├── Conv2D (64 filters, 3x3) + ReLU
├── MaxPooling2D (2x2, stride 2x2)
├── Conv2D (128 filters, 3x3) + ReLU
├── Conv2D (256 filters, 3x3) + ReLU
├── MaxPooling2D (2x2, stride 2x2)
├── Flatten
└── Dense (1 unit) + Sigmoid
```

### Optimizer
- **Model 1:** Adam Optimizer
- **Model 2:** Nadam Optimizer

### Parameter Training
- **Loss Function:** Binary Crossentropy
- **Metrics:** Accuracy, Precision, Recall
- **Epochs:** 100
- **Batch Size:** 32

## 📊 Data Augmentation
- **Rescale:** 1./255 (normalisasi pixel)
- **Rotation Range:** 20 derajat
- **Horizontal Flip:** True
- **Shear Range:** 0.2
- **Fill Mode:** nearest

## 📁 Struktur Project
```
Analisa-Tumor-Otak/
├── brain_tumor_dataset/
│   ├── no/          # 92 gambar (no tumor)
│   └── yes/         # 87 gambar (tumor)
├── ModelAdam.json   # Arsitektur model Adam
├── ModelAdam.h5     # Bobot model Adam
├── ModelNadam.json  # Arsitektur model Nadam
├── ModelNadam.h5    # Bobot model Nadam
├── Tumor Classification.ipynb        # Notebook utama
├── Tumor_Classification_Model_Testing.ipynb  # Notebook testing
└── README.md        # Dokumentasi project
```

## 🎯 Hasil Prediksi (Contoh)
Berdasarkan README, hasil prediksi pada file `3 no.jpg`:
- **Model Adam:** "No Tumor Otak"
- **Model Nadam:** "Tumor Otak"

## 📈 Metrik Evaluasi
- **Accuracy:** Mengukur keseluruhan ketepatan klasifikasi
- **Precision:** Mengukur ketepatan prediksi positif
- **Recall:** Mengukur kemampuan menemukan semua kasus positif

## ⚙️ Lingkungan Development
- **Platform:** Google Colab
- **Library Utama:** TensorFlow, Keras, Scikit-learn
- **Sumber Dataset:** Kaggle (Brain MRI Images for Brain Tumor Detection)

## 🔄 Status Project
- ✅ Data collection dan preprocessing
- ✅ Model training (Adam & Nadam)
- ✅ Model evaluation
- ✅ Model deployment (testing)
- ✅ Documentation

---
*Statistik ini dibuat berdasarkan analisis project pada 21 Oktober 2025*