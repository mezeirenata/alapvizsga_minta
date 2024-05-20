import random
import os

honey = 100
red = (1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36)
black = (2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35)
green = 0
even = (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36)
odd = (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35)

def main(honey):
    while True:
        print('Kilépés = 0')
        print('Piros = 1')
        print('Fekete = 2')
        print('Zöld(0) = 3')
        print('Páratlan = 4')
        print('Páros = 5')
        print(f'Egyenleged: {honey} csupor méz')
        player = int(input('Tedd meg a tipped 0-5: '))
        if player == 0:
            break
        else:
            tet = int(input('Hány csupor méz a tét? '))
            eredmeny = roll()
            print(f'Pörgetés eredménye: {eredmeny}')
            honey = win_loss(player, eredmeny, honey, tet)
            input('<ENTER>')
            os.system('cls')
        

def roll():
    spin = random.randint(0,36)
    return spin
    

def win_loss(szam, eredmeny, honey, tet):
    if eredmeny in red and szam == 1:
        honey += tet*2
        print(f'Nyertél {tet*2} csupor mézet!')
    elif eredmeny in black and szam == 2:
        honey += tet*2
        print(f'Nyertél {tet*2} csupor mézet!')
    elif eredmeny == green and szam == 3:
        honey += tet*10
        print(f'Nyertél {tet*10} csupor mézet!')
    elif eredmeny in odd and szam == 4:
        honey += tet*2
        print(f'Nyertél {tet*2} csupor mézet!')
    elif eredmeny in even and szam == 5:
        honey += tet*2
        print(f'Nyertél {tet*2} csupor mézet!')
    else:
        print('Vesztettél')
        honey -= tet
    return honey


main(honey)