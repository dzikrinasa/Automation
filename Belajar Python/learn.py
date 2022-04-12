#run python namafile
"""
ini komentar
beberapa baris
"""
"""
#input
nama =  input("siapa nama anda? ")
umur = input("umurmu berapa ? ")
print("oh nama kamu " + nama + ", Kamu sudah " + umur + " tahun")
"""
#boolean
nomor1 = 12
nomor2 = 12
print(nomor1 < nomor2)
text = "karakter"
print(text.isdigit())
print(text.isalnum())
#if else
if nomor1 == nomor2:
    print("betul sekali")
    print("angka ",nomor1,"sama")
else:
    print("salah woy")
#elif
uang = input("punya berapa? ")
utang = 10000

if int(uang) < utang:
    print("kurang woy")
elif int(uang) == utang:
    print("pas deh")
elif int(uang) > utang:
    print("Uangnya lebih nih, ini kembaliannya :", int(uang) - utang)
else:
    print("yo ndak tau")

"""
OPERATOR
Lebih dari 1 syarat
and or not
& | !=
"""
if (1<2) & (4<5):
    print ("benul")
else:
    print("salah men")

tamu = "pria"
baik = True
rajin = True
if baik & rajin:
    if tamu == "pria":
        print("gas mbojo")
    else:
        print("gk bisa lah")
else:
    print("moh")