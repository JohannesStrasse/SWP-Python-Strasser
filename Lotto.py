import random

anzahlZahlen = 1000
zahlen = list(range(1, 45))
statistik = {zahl: 0 for zahl in zahlen}
def ziehen():
    global anzahlZahlen
    while anzahlZahlen > 0:
        randomZahl = random.choice(zahlen)
        #print (randomZahl)
        #zahlen.remove(randomZahl)
        anzahlZahlen -=1
        statistik[randomZahl] +=1

    if anzahlZahlen <= 0:
        print("Es wurde 1000 Mal gezogen!")

    print("Statistik:")
    for zahl, anzahl in statistik.items():
        print(f"Zahl {zahl} wurde {anzahl} mal gezogen!")

ziehen()

