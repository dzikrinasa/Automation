"""
Perulangan
    - While
    - for in
"""
#while
count = 0

while count < 5:
    print("Yeay mbojoo!")
    count = count+1
else:
    print("dah lah, udah sebanyak :", count)

#for in
text ='python'

for huruf in text:
    print(huruf)

orang = ["adi", "budi", "caca"]
for nama in orang:
    print(nama) 

#nested loop
a=1
while a < 5 :
    b=0
    while b < a:
        print('*', end='')
        b = b+1
    print()
    a = a+1

for x in range(1,6):
    for y in range(1,6):
        z = x*y
        print(z, end="  ")
    print()

"""
Sequences
    List []
    Tuples(immutable)
    Dictionary{}
    Sets{}tanpa index
"""
panggilan = ['pepeng', 'tegar', 'apoy']#list
panggilan.append('bambang')
panggilan[1] = 'tegar ra ndue ndog'
del panggilan[2]
print(panggilan)

panggilan2 = ('bob','nigga','cj')#tuples
print(list(panggilan2))#convert tuple ke list
print(tuple(panggilan))#convert list ke tuple

#dictionary
data ={
    'nama':'andi',
    'umur':'22',
    'hobby':'nyanyi'
    }
data['nama'] = 'Nauy' #edit
data['cita'] = 'pilot'#tambah
del data['umur'] #hapus
print(data['nama'])#select
print(data)
for judul, isi in data.items():
    print(judul + " = " + isi)
#nested dictionary
data2 = {
    1:{'nama':'andi','umur':'22','hobby':'nyanyi'},
    2:{'nama':'budi','umur':'44','hobby':'main'}
}
print(data2[2]['nama'])
for key, value in data2.items():
    print("\nKeynya :", key)

    for key2 in value:
        print(key2 + "-", value[key2])

#sets
hewan = {'babi','anjing', 'nyomet'}
hewan.add('setan')
hewan.remove('nyomet')
print(hewan)

angka1 = {1,2,3,4,5}
angka2 = {4,5,6,7,8}
print(angka1 & angka2)# & - | 
