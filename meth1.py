import random
def replacer(s, strNew, index):
    return s[:index] + strNew + s[index + 1:]

def fenyofa(szint: int, diszit: bool):
    szoveg=""
    levego=szint
    for i in range(szint+1):
        if i == szint:
            szoveg += f"{(szint-1)*' '}{3*'|'}" if szint > 3 else f"{szint *' '}{'|'}"
            break
        idSzoveg = f"{levego*' '}{(i*2+1) * '*'}\n"
        if diszit and i>0 and random.randint(1, 10) > 6: idSzoveg = replacer(idSzoveg, 'O', random.randint(levego, len(idSzoveg)-2))
        szoveg += idSzoveg
        levego -= 1
    return szoveg

def main():
    print(fenyofa(4, False))


if __name__ == '__main__':
    main()