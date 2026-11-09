print("číslo 3")

cisla = (input("Zadej celá čísla: "))
n = int(input("Zadejte délku listu: "))

delka = 0
nejdelsi = 0
i = 1

def rostouci_usek(cisla, n):
    cisla = int([cisla])
    n = len(cisla)
    return(n, cisla)

while True:
    if n == 0:
        print(nejdelsi)
        exit()
    else:
        delka = 1
        nejdelsi = 1

        for i in range(n-1):
            i += 1

        if cisla[i] > cisla[i - 1]:
            n += 1
            

        else:
            n = 1

            if delka > nejdelsi:
                nejdelsi = delka
            else:
                pass
        