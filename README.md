# PneumoCare AI
Sistem Pendukung Keputusan Berbasis AI untuk Proyeksi Awal Tingkat Keparahan Pneumonia
PneumoCare AI merupakan **Clinical Decision Support System (CDSS)** berbasis **Artificial Intelegence** yang dikembangkan untuk membantu proses analisis parameter klinis pasien dalam memberikan **proyeksi awal tingkat keparahan pneumonia**.
Sistem memanfaatkan data klinis pasien sebagai input dan menggunakan model **Extra Gradient Boosting** untuk menghasilkan prediksi tingkat keparahan yang dapat digunakan sebagai bahan pertimbangan tambahan dalam proses pengambilan keputusan oleh tenaga medis.

**Medical Disclaimer**
PneumoCare AI merupakan sistem pendukung keputusan dan bukan alat diagnosis medis. Hasil prediksi tidak menggantikan diagnosis, pemeriksaan medis, maupun keputusan klinis dari tenaga medis profesional.

## Tentang Penelitian
Project ini dikembangkan sebagai bagian dari penelitian debgan topik "
**Klasifikasi Tingkat Keparahan Pneumonia Menggunakan Algoritma XGBoost dengan Perbandingan Metrik Scoring pada GridSearch**
Penelitian ini berfokus pada penerapan **Machine Learning** dan **GridSearch** dalam menentukan model terbaik untuk proyeksi awal tingkat keparahan pneumonia berdasarkan parameter klinis pasien.

## Tujuan
Pengembangan PneumoCare AI bertujuan untuk :
1. Mengembangkan sistem pendukung keputusan berbasis AI untuk membantu analisis tingkat keparahan pneumonia.
2. Menerapkan algoritma Machine Learning pada data tabular.
3. Mengintegrasikan model Machine Learning ke dalam aplikasi berbasis web.
4. menyediakan _interface_ sederhana sehingga proses input data dan prediksi dapat dilakukan dengan lebih mudah.

## Fitur Utama
### 1. Landing Page
Halaman utaman memperkenalkan PneumoCare AI sebagai sistem pendukung keputusan berbasis AI.
### 2. Input Parameter Klinis Pasien
sistem menyediakan formulir untuk memasukkan parameter klinis pasien, meliputi :
- Kode pasien
- Umur pasien
- Jenis kelamin
- Riwayat tuberkolosis
- Riwayat penyakit pernapasan
- Riwayat diabetes
- Riwayat penyakit kardiovaskular
- Tekanan Darah
- Kebingungan (Kesadaran Pasien)
- Laju Pernapasan
- Kadar Urea
- Suhu
- Saturasi Oksigen
- Jumlah Leukosit
- Status Anemia

### 3. Prediksi Tingkat Keparahan
Data klinis pasien yang dimasukkan pengguna diproses oleh Model untuk menghasilkanproyeksi tingkat keparahan pneumonia.
Output model meliputi 2, yaitu:
- Tinggi (ICU) : Pasien memenuhi kriteria untuk masuk ke kategori keparahan tinggi.
- Rendah (Non ICU) :Pasien memenuhi kriteria untuk masuk ke kategori keparahan rendah.

### 4. Informasi Teknis & Klinis
Aplikasi menyediakan informasi mengenai:
- Metodologi AI yang digunakan.
- Penjelasan model.
- Panduan interpretasi hasil.
- Informasi mengenai penggunaan sistem sebagai Clinical Decision Support System.
