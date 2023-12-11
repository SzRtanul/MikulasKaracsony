class RenSzarvas:
    nev = []
    magassag = -1
    hely = -1
    leiras=""

    def __init__(self, sor):
        sorr=sor.split('@')
        self.nev = sorr[0].split(" – ")
        self.leiras = sorr[3]
        try:
            self.magassag = int(sorr[1])
        except:
            pass
            #print("An exception occurred")
        try:
            self.hely = int(sorr[2])
        except:
            pass
            #print("An exception occurred")

    def getNev(self):
        return self.nev
    def getMagassag(self):
        return self.magassag
    def getHely(self):
        return self.hely
    def getLeiras(self):
        return self.leiras


def Beolvas():
    tomb=[]
    with open("Mikulasszan.txt",  "r", encoding="UTF-8") as f:
        print("Beolvasás folyamatban...")
        i=0
        for item in f:
            if i >= 1:
                i += 1
                tomb.append(RenSzarvas(item))
            else:
                i += 1
        print("Beolvasás kész.")
    i = 0 # Mikulás törlése
    for item in tomb:
        if item.nev[1] == "Mikulás":
            tomb.pop(i)
        i += 1
    return tomb
def main():
    print("Ez a program a Mikulasszan.txt szövegesfájlból beolvassa és kiértékeli az adatokat.")
    tomb = Beolvas()
    # a. feladat:
    print("Rénszarvasok neve, magassága:")
    for item in tomb:
        print(f"\t{item.nev[0]}: {item.magassag} cm")
    # b. feladat:
    print(f"Rénszarvasok száma: {len(tomb)}")
    # c. feladat:
    for item in tomb:
        if item.nev[1] != None and item.nev[1] == "Pompás":
            print(f"\t{item.nev[0]}")
    # d. feladat:
    print("Szavak előfordulása a leírásokban: :")
    for item in tomb:
        print(f"\t{item.nev[0]}: {len(item.leiras.lower().split('mikulás'))-1}")
    # e. feladat:
    atlag = 0
    osszeg = 0
    darab = 0
    for item in tomb:
        if item.magassag > 0:
            osszeg += item.magassag
            darab += 1
    print(f"A rénszarvasok átlagos magassága: {float(osszeg)/float(darab)}")
    # f. feladat:
    print("Páros helyen lévő rénszarvasok neve: ")
    for item in tomb:
        if item.hely % 2 == 0:
            print(f"\t{item.nev[0]}")
    # g. feladat:
    maxHossz = 0
    nev=""
    for item in tomb:
        if len(item.getLeiras()) > maxHossz:
            maxHossz = len(item.getLeiras())
            nev = item.nev[0]
    print(f"Leghosszabb leírás: {nev}")
    # h. feladat:
    minHely = tomb[0].hely
    nev = ""
    for item in tomb:
        if minHely >= item.hely:
            minHely = item.hely
            nev = item.nev[0]
    print(f"Legkisebb számú hely: {nev}")

if __name__ == '__main__':
    main()