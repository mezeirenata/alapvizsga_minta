class Mez:
    def __init__(self, row: str) -> None:
        #code,totalprod,stocks,priceperlb,year,state
        #0code,1numcol,2yieldpercol,3totalprod,4stocks,5priceperlb,6prodvalue,7year,8state
        splitted1: list = row.split(';')
        splitted: str = splitted1[0].split(',')
        self.code = splitted[0]
        self.totalprod = int(splitted[3])
        self.stocks = int(splitted[4])
        self.priceperlb = float(splitted[5])
        self.year = int(splitted[7])
        self.state = splitted[8]
        self.sold = self.totalprod - self.stocks



    