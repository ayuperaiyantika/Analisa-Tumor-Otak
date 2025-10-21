# Analisa-Tumor-Otak

### 📊 Pembagian Dataset

Dataset citra MRI otak dibagi menjadi dua kategori utama: **No Tumor Otak** dan **Tumor Otak**.
Total keseluruhan dataset terdiri dari **253 gambar**, dengan rincian sebagai berikut:

* **Jumlah Data No Tumor Otak:** 98
* **Jumlah Data Tumor Otak:** 155

Dataset kemudian dibagi menjadi dua subset, yaitu **Data Train** dan **Data Validation**, dengan proporsi seperti berikut:

#### 🔹 Data Train
* No Tumor Otak: 78 gambar
* Tumor Otak: 124 gambar

#### 🔹 Data Validation
* No Tumor Otak: 20 gambar
* Tumor Otak: 31 gambar

<img width="898" height="137" alt="image" src="https://github.com/user-attachments/assets/1cd9585d-2185-479a-9534-f75d49463de7" />

### 🧠 Hasil Prediksi Model Klasifikasi Tumor Otak

Model diuji menggunakan dua jenis optimizer, yaitu **Nadam** dan **Adam**, pada citra MRI otak dengan nama file `3 no.jpg`.

* Optimizer **Nadam** memprediksi gambar tersebut sebagai **"Tumor Otak"**.
* Optimizer **Adam** memprediksi gambar yang sama sebagai **"No Tumor Otak"**.

Visualisasi hasil ditampilkan di bawah prediksi untuk menunjukkan perbedaan performa antara kedua optimizer dalam mendeteksi keberadaan tumor otak.
<img width="1018" height="352" alt="image" src="https://github.com/user-attachments/assets/c74b6920-207d-414a-98b7-77faa4f15297" />



