# Contoh Skrip Pembaca Data dengan Python dan Pandas

Skrip ini berisi contoh sederhana untuk membaca data dari file teks (`.txt`) dan CSV (`.csv`) menggunakan Python. Terdapat tiga fungsi yang mendemonstrasikan cara-cara berbeda dalam membuka, membaca, dan menampilkan data dari file.

-----

## 📋 Kebutuhan

Pastikan Anda telah menginstal library yang diperlukan:

  * **Python 3.x**
  * **Pandas**

Untuk menginstal Pandas, jalankan perintah berikut di terminal Anda:

```bash
pip install pandas
```

-----

## 📂 Struktur File

Agar skrip dapat berjalan tanpa error, pastikan struktur file dan folder Anda sama seperti di bawah ini:

```
.
├── nama_script.py                   # File skrip Python Anda
├── sample-data.txt                  # File data teks sampel
└── data/
    └── Kerentanan Asset Internal.csv    # File data CSV di dalam folder 'data'
```

-----

## 🚀 Cara Menjalankan

1.  Siapkan semua file dan folder sesuai dengan struktur di atas.

2.  Buka terminal atau *command prompt*.

3.  Navigasi ke direktori tempat Anda menyimpan `nama_script.py`.

4.  Jalankan skrip dengan perintah berikut:

    ```bash
    python nama_script.py
    ```

Saat dijalankan, skrip akan mengeksekusi fungsi `open3()` dan menampilkan nama-nama kolom dari file `data/Kerentanan Asset Internal.csv`.

-----

## 🛠️ Penjelasan Fungsi

Skrip ini memiliki tiga fungsi utama:

### `open1()`

Fungsi ini mendemonstrasikan cara paling dasar untuk membuka file teks di Python.

  * Membuka file `sample-data.txt` dalam mode baca (`'r'`).
  * Menggunakan `file.readlines()` untuk membaca seluruh isi file dan menyimpannya sebagai *list* di mana setiap elemen adalah satu baris dari file.
  * Mencetak *list* tersebut ke konsol.

### `open2()`

Fungsi ini menunjukkan cara membaca file CSV langsung menjadi DataFrame Pandas.

  * Membuka file `Kerentanan Asset Internal.csv`.
  * Menggunakan `pd.read_csv(file)` untuk mengubah data CSV menjadi DataFrame Pandas.
  * Mencetak seluruh DataFrame ke konsol.

### `open3()`

Fungsi ini adalah cara yang paling umum digunakan untuk membaca file CSV dengan Pandas dan melakukan inspeksi awal.

  * Menentukan path file CSV ke dalam sebuah variabel.
  * Membaca file CSV menggunakan `pd.read_csv()` dari path yang sudah ditentukan.
  * Mencetak nama-nama kolom dari DataFrame menggunakan `df.columns`.

> **Catatan**: Dalam skrip yang diberikan, hanya fungsi `open3()` yang dipanggil dan akan dieksekusi secara otomatis saat skrip dijalankan.