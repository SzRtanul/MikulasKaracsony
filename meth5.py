import math
def sorozat(eleje: int, vege: int):
    szamok=[]
    for i in range(eleje, vege + (1 if eleje - vege <= 0 else -1), 1 if eleje - vege <= 0 else -1):
        szamok.append(i)
    szamok.sort()
    return szamok

def main():
    print("A feladat tetszőleges tartományban kiírja a számokat *-gal elválasztva.")
    szoveg=""
    for i in sorozat(int(input("Kérem a kiírandó sorozat elejét: ")), int(input("Kérem a kiírandó sorozat végét: "))):
        szoveg+=f"{i}*"
    print(szoveg.rstrip('*'))
