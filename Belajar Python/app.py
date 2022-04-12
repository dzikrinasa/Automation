import data # as d

print(data.person)
print(data.printNama("jack"))

from data import printNama
#print(person)
print(printNama("akmal"))

import datetime

now = datetime.datetime.now()
print(now)

date = datetime.datetime(2018, 1, 1)
print(date)

tanggal = datetime.datetime.now()
print(tanggal.strftime("%Y, %B, %d"))

"""
Local & global variable
"""

name = 'hilman' #global

def printName():
    #global name
    #name = name + " maulana"
    name = "aan"#lokal
    print("akses dari dalam "+ name)

printName()
print("akses dari luar "+ name)