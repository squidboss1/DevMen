
with open("przyklad.txt", encoding="utf-8") as plik:
    print(plik.tell())
    print(plik.seek(43))
    print(plik.read(1))
