import shutil

def main():
    shutil.copy("KariVers.txt", "KariVers2.txt")
    print("Ez a program hozzáad egy versszakot a KariVers.txt állományban lévő dalhoz. A kimenet a KariVers2.txt-be kerül.")
    print("Versszak hozzáadása...")
    with open("KariVers2.txt", 'a', encoding='UTF-8') as kf:
        kf.writelines("\n\nTiszta öröm tüze átég\n" +
                      "a szemeken, a harangjáték\n" +
                      "szól, éjféli üzenet:\n" +
                      "Kis Jézuska született!")
        print("Versszak hozzáadva:")


if __name__ == '__main__':
    main()