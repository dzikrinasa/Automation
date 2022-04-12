player1 = {"name":"goku", "power":100}
player2 = {"name":"vegeta", "power":250}

def train(player):
    player['power'] += 100

def attact(attacker, defender):
    if(attacker['power'] > defender['power']):
        print("serangan berhasil selamat untuk", attacker['name'])
    else:
        print("serangan gagal kamu lemah", attacker['name'])

train(player1)
train(player1)
attact(player1,player2)

nama = input("nama monsternya siapa? ")

monster = {"nama" : nama, 'kekuatan' : 100}

def startGame():
    pilihan = input('silahkan pilih apa yang akan dilakukan 1. makan 2. lihat status 3. keluar ')
    if pilihan == '1':
        goEat()
    elif pilihan =='2':
        goStatus()
    else:
        goExit()


def goEat():
    print("nyam nyam ...")
    monster['kekuatan'] += 100
    startGame()

def goStatus():
    print('Kekuatan monster: ') 
    print(monster)
    startGame()

def goExit():
    print("bye byee")
    
startGame()