import pandas as pd


def open1():
    """
    Fungsi ini mendemonstrasikan cara membuka dan membaca file teks (.txt) biasa
    menggunakan fungsi bawaan Python. Hasilnya adalah sebuah list (daftar)
    di mana setiap elemen adalah satu baris dari file tersebut.

    Panggil fungsi ini dengan `open1()` untuk membaca 'sample-data.txt'
    dan mencetak isinya sebagai sebuah list.
    """
    # buka data sample-data.txt
    with open('sample-data.txt', 'r') as file:
        data = file.readlines()
        print(data)

def open2():
    """
    Fungsi ini menunjukkan cara membaca file CSV menjadi DataFrame pandas
    dengan cara membuka file terlebih dahulu menggunakan fungsi bawaan Python.
    
    Panggil fungsi ini dengan `open2()` untuk membaca file CSV
    dan mencetak seluruh DataFrame ke layar.
    """
    with open('Kerentanan Asset Internal.csv', 'r') as file:
        df = pd.read_csv(file)
        print(df)

def open3():
    """
    Fungsi ini menunjukkan cara paling umum untuk membaca file CSV dengan pandas,
    yaitu dengan langsung memberikan path file ke fungsi pd.read_csv().
    Fungsi ini kemudian mencetak nama-nama kolom dari data tersebut.

    Panggil fungsi ini dengan `open3()` untuk membaca CSV dari subfolder 'data'
    dan hanya menampilkan nama-nama kolomnya.
    """
    file_csv = 'data/Kerentanan Asset Internal.csv'
    df = pd.read_csv(file_csv)
    print(df.columns)
open3()
