"""
Functions
    parameter
    Return : mengembalikan nilai
    keyword argument
    *Args, **Kwargs : nilainya bisa multi
"""
from multiprocessing.sharedctypes import Value
from unicodedata import name


def printYow():
    print('-----')
    print(' Yow')
    print('-----')

printYow()

def printNiceText(text = 'kosong'): 
    print('-----')
    print(text)
    print('-----')

printNiceText('Gas')

def hitung(a, b): 
    print('jumlah dari a & b adalah ', a + b)

hitung(10,20)

def jumlah(c, d):
    return c + d

jumlah1 = jumlah(30, 40)
print(jumlah(jumlah1,50))

#keyword argument
def printData(name, hobby):
    print("Nama :" + name + " - Hobi :" + hobby)

printData(hobby = 'nyanyi', name='asa')

#args
def printData2(*args):
    for nama in args:
        print(nama)

printData2('hilman','andi','budi')

def printBiodata(**kwargs):
    for key, value in kwargs.items():
        print(key + " - " + value)

printBiodata(siapa ='aan', kapan='kemis', kenapa='mbojo')