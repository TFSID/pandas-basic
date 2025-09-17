import pandas as pd


def open1():
    # buka data sample-data.txt
    with open('sample-data.txt', 'r') as file:
        data = file.readlines()
        print(data)

def open2():
    with open('Kerentanan Asset Internal.csv', 'r') as file:
        df = pd.read_csv(file)
        print(df)

def open3():
    file_csv = 'data/Kerentanan Asset Internal.csv'
    df = pd.read_csv(file_csv)
    print(df.columns)
open3()
