import random
import os
class Ajandek:
    azons=[]
    def __init__(self):
        for i in range(20):
            self.azons.append(int((random.random()*90)-10))
    def getMindenHarmadik(self):
        tomb = []
        for i in range(2, len(self.azons), 3):
            tomb.append(self.azons[i])
        return tomb


def main():
    print("6. Feladat:\nEz a program ajándékokat generál -10 és " +
          "80 közötti azonosítószámmal. Ezek közül minden harmadikat kiírja." +
          " Készít két fájlt, amik közül az egyikben minden aándék benne van," +
          " a másikban csak minden harmadik.")
    ajandekok = Ajandek()
    szoveg = "\tMinden 3. ajándék: "
    for item in ajandekok.getMindenHarmadik():
        szoveg += f"{item}, "
    print(szoveg.rstrip(','))
    try:
        os.mkdir("meth6Files")
    except:
        pass
    with open("meth6Files/minden3dikCsomag.txt", "w") as f:
        for item in ajandekok.getMindenHarmadik():
            f.write(f"{item}\n")
        f.close()
    with open("meth6Files/mindenCsomag.txt", "w") as f:
        for item in ajandekok.azons:
            f.write(f"{item}\n")
        f.close()



if __name__ == '__main__':
    main()