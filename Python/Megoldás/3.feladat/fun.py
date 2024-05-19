from amerika import Mez

osszmez : list[Mez] = []

def load_from_file(filename):
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for f in file:
        osszmez.append(Mez(f.strip()))
    file.close()


def west_virginia():
    count = 0
    for m in osszmez:
        if m.year > 1998 and m.year < 2007 and m.state == 'West Virginia':
            count += m.totalprod
    return count

def legdragabb():
    lista = []
    legnagyobb = 0
    for m in osszmez:
        if m.priceperlb > legnagyobb:
            legnagyobb = m.priceperlb
    for m in osszmez:
        if m.priceperlb == legnagyobb:
            lista.append(m)
    return lista

def keres(ar):
    lista = []
    for m in osszmez:
        if ar + 0.50 > m.priceperlb and ar - 0.50 < m.priceperlb:
            lista.append(m)
    else:
        print('Nincs találat')
    return lista


def legtobb_eladott_mez():
    stat = {}
    for i in range(1998, 2013):
        legtobb = osszmez[0]
        for m in osszmez:
            if m.sold > legtobb.sold:
                legtobb = m
                stat[i] = m.state
    return stat

def atlagar():
    count = 0
    for m in osszmez:
        count += m.priceperlb
    return count / len(osszmez)

def usd_to_huf(usd):
    return usd * 358.02

def lb_to_kg(lb):
    return lb * 0.45

def write_file(filename):
    file = open(filename, 'w', encoding='utf8')
    file.write('state;priceperlb(huf);year\n')
    for m in osszmez:
        file.write(f'{m.state};{round(usd_to_huf(m.priceperlb), 2)};{m.year}\n')
    print('8. feladat: Fájl létrehozva')