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
### 5. Model Machine Learning
PneumoCare AI menggunakan algoritma **Extra Gradient Boosting**. Model ini diguakan untuk melakukan proyeksi tingkat keparahan pneumonia berdasarkan parameter klinis yang dimasukkan ke dalam sistem.
Secara umum, alur pemrosesan sistem adalah:

```text
Data Klinis Pasien
        │
        ▼
Preprocessing Data
        │
        ▼
Model Extra Gradient Boosting
        │
        ▼
Proses Prediksi
        │
        ▼
Tingkat Keparahan Pneumonia
```
### 6. Parameter Klinis

Parameter klinis yang digunakan dalam sistem meliputi:

| Parameter | Keterangan |
|---|---|
| Kode Pasien | Identitas/kode data pasien |
| Umur Pasien | Kategori usia pasien |
| Jenis Kelamin | Jenis kelamin pasien |
| Riwayat Tuberkulosis | Riwayat TB pasien |
| Riwayat Penyakit Pernapasan | Riwayat penyakit pernapasan |
| Riwayat Diabetes | Riwayat diabetes |
| Riwayat Kardiovaskular | Riwayat penyakit kardiovaskular |
| Tekanan Darah | Kondisi tekanan darah pasien |
| Kebingungan | Kondisi kebingungan pasien |
| Laju Pernapasan | Frekuensi pernapasan |
| Kadar Urea | Kadar urea pasien |
| Suhu | Suhu tubuh pasien |
| Saturasi Oksigen | Tingkat saturasi oksigen |
| Jumlah Leukosit | Jumlah sel darah putih |
| Status Anemia | Status anemia pasien |

### 7. Medical Disclaimer

> **PENTING:**

PneumoCare AI adalah **Clinical Decision Support System (CDSS)** yang membantu proses analisis dan memberikan proyeksi awal berdasarkan data yang dimasukkan.

Sistem ini **bukan alat diagnosis medis**.

Hasil prediksi:

- Tidak menggantikan diagnosis dokter.
- Tidak menggantikan pemeriksaan medis.
- Tidak boleh digunakan sebagai satu-satunya dasar pengambilan keputusan medis.
- Harus dipertimbangkan bersama kondisi klinis pasien dan penilaian tenaga medis profesional.

 ## Teknologi
 Project ini menggunakan beberapa teknologi berikut:
 - Python
 - Flask
 - Machine Learning
 - XGBoost
 - HTML
 - CSS
 - JavaScript

## 🎓 Academic Project

Project ini dikembangkan sebagai bagian dari:

**Penelitian/Skripsi**

**Judul:**  
`[Klasifikasi Tingkat Keparahan Pneumonia Mengunakan Algoritma XGBoost dengan Perbandingan Metrik Scoring pada GridSearch]`

**Nama:**  
`[Yuni Eka Nuraini]`

**Program Studi:**  
`[S1 Matematika]`

**Fakultas:**  
`[Fakultas Matematika dan Ilmu Pengetahuan Alam]`

**Universitas:**  
`[Universitas Negeri Malang]`

**Tahun:**  
`[2026]`

---

## 👤 Author

**[Yuni Eka Nuraini]**

GitHub: [@yyonee](https://github.com/yyonee)

---

## 📄 License

Project ini dikembangkan untuk keperluan penelitian dan akademik.

Lisensi penggunaan dapat disesuaikan dengan kebutuhan penelitian dan kebijakan institusi.
