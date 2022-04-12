import random
import string

#Perulangan
penis = "kunam"
silit = 0
silitkebo = ['jembud', 'telek', 'ireng']

for i, kebo in enumerate(silitkebo):
    print(''.join([str(i+1), '.']), kebo)

#percabangan
nilai = 70
kkm = 75

if (nilai <= kkm):
    print('tolol')
elif (nilai >= kkm):
    print('goblok')
else: 
    print('yo')

#function
def crot():
    print("AHHHH")

crot()

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

id = id_generator()

print(id)

