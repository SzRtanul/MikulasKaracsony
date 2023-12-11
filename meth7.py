class RenSzarvas:
    nev = []
    magassag = 0
    hely = 0
    leiras=""

    def __init__(self, sor):
        sorr=sor.split('@')
        self.nev = sorr[0].split(" – ")
        self.leiras = sorr[3]
        try:
            self.magassag = int(sorr[1])
        except:
            print("An exception occurred")
        try:
            self.hely = int(sorr[2])
        except:
            print("An exception occurred")

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
                i+=1
                tomb.append(RenSzarvas(item))
            else:
                i+=1
        print("Beolvasás kész.")
    return tomb

def main():
    print("Ez a program a Mikulasszan.txt szövegesfájlból beolvassa és kiértékeli az adatokat.")
    tomb = Beolvas()
    print("Rénszarvasok neve, magassága")
    for item in tomb:
        print(f"{item.nev[0]}, {item.magassag}")
    print(f"Rénszarvasok száma: {len(tomb)}")
    for item in tomb:
        if item.nev[1] != None and item.nev[1] == "Pompás":
            print(item.nev[0])



if __name__ == '__main__':
    main()