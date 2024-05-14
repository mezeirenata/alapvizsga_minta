meh = int(input('Méhek száma kaptáronként kb. (50 e - 100 e, ezresekben megadva): '))
kaptar = int(input('Kaptárok száma: '))
meh_termeles = 30

n = meh*1000 * kaptar
termeles = meh_termeles * meh*1000
print(f'Az összes méh száma: {n} db')
print(f'Jelenleg összesen várható termelés kaptáronként: {termeles} ml')

osszes_mez = 0.0
for i in range(1,6):
    osszes_mez += 4.67
    print(f'{i}. hét: {osszes_mez} ml')
print(f'Egy méh átlagosan 5 hét alatt {osszes_mez} ml mézet termel.')

