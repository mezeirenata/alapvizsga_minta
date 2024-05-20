from fun import *

def main():
    load_from_file('forras.csv')
    print(f'3. feladat: West Virginia államban {west_virginia()} lb mézet termeltek')
    print('4.feladat: Legdrágább méz(ek)')
    leg: list[Mez] = legdragabb()
    for i in range(len(leg)):
        print(f'\t{leg[i-1].state} {leg[i-1].year} {leg[i-1].priceperlb}')
    inp = float(input('5. feladat: Adjon meg egy keresési értéket pl: 2.50 (usd): '))
    eredmeny: list[Mez] = keres(inp)
    for i in range(len(eredmeny)):
        print(f'\t{eredmeny[i-1].state} {eredmeny[i-1].year} {eredmeny[i-1].priceperlb}')
    print('6. feladat:')
    mostsold = legtobb_eladott_mez()
    for k,v in mostsold.items():
        print(f'\t{k} {v}')
    print(f'7. feladat A mézek kilógrammonkénti átlagára: {round(lb_to_kg(usd_to_huf(atlagar())), 2)} Ft {round(lb_to_kg(atlagar()), 2)} Usd')
    write_file('mez-ar-forint.csv')
main()