print('1. feladat:')
meh = int(input('\tMéhek száma kaptáronként kb. (50 e - 100 e, ezresekben megadva): '))
kaptar = int(input('\tKaptárok száma: '))
meh_termeles = 30

n = meh*1000 * kaptar
termeles = meh_termeles * meh*1000
print(f'2. feladat: Az összes méh száma: {n} db')
print(f'3. feladat: Jelenleg összesen várható termelés kaptáronként: {termeles} ml')

osszes_mez = 0.0
print('4. feladat:')
for i in range(1,6):
    osszes_mez += 4.67
    print(f'\t {i}. hét: {osszes_mez} ml')
print(f'5. feladat: Egy méh 5 hét alatt {osszes_mez} ml mézet termel.')

