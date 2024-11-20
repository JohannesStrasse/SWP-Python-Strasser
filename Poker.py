import random


def get_symbol(karte, anzahl_symbole, symbole):
    symbol_index = karte % anzahl_symbole
    return symbole[symbol_index]


def get_farbe(karte, anzahl_farben, farben):
    farben_index = karte % anzahl_farben
    return farben[farben_index]


def get_5(anzahl_karten, anzahl_symbole, anzahl_farben, symbole, farben, hand_anzahl):
    gezogene_karten = random.sample(range(anzahl_karten), hand_anzahl)
    karten_liste = [(get_symbol(karte, anzahl_symbole, symbole), get_farbe(karte, anzahl_farben, farben)) for karte in
                    gezogene_karten]
    return karten_liste


def pair(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    symbole_haeufigkeit = {symbol: symbole_der_karten.count(symbol) for symbol in symbole_der_karten}
    return any(count == 2 for count in symbole_haeufigkeit.values())


def two_pair(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    symbole_haeufigkeit = {symbol: symbole_der_karten.count(symbol) for symbol in symbole_der_karten}
    paar_count = sum(1 for count in symbole_haeufigkeit.values() if count == 2)
    return paar_count == 2


def three_of_a_kind(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    symbole_haeufigkeit = {symbol: symbole_der_karten.count(symbol) for symbol in symbole_der_karten}
    return any(count == 3 for count in symbole_haeufigkeit.values())


def quads(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    symbole_haeufigkeit = {symbol: symbole_der_karten.count(symbol) for symbol in symbole_der_karten}
    return any(count == 4 for count in symbole_haeufigkeit.values())


def flush(karten_liste):
    farbe_der_karten = [karte[1] for karte in karten_liste]
    return any(farbe_der_karten.count(farbe) == 5 for farbe in farbe_der_karten)


def straight(karten_liste, symbole):
    symbol_werte = {symbol: index for index, symbol in symbole.items()}
    symbole_der_karten = [karte[0] for karte in karten_liste]
    werte_der_karten = sorted(symbol_werte[symbol] for symbol in symbole_der_karten)
    return all(werte_der_karten[i] == werte_der_karten[i - 1] + 1 for i in range(1, len(werte_der_karten)))


def full_house(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    symbole_haeufigkeit = {symbol: symbole_der_karten.count(symbol) for symbol in symbole_der_karten}
    has_pair = any(count == 2 for count in symbole_haeufigkeit.values())
    has_three_of_a_kind = any(count == 3 for count in symbole_haeufigkeit.values())
    return has_pair and has_three_of_a_kind


def straight_flush(karten_liste, symbole):
    return straight(karten_liste, symbole) and flush(karten_liste)


def royal_flush(karten_liste, symbole):
    royal_symbols = {'10', 'J', 'Q', 'K', 'A'}
    if flush(karten_liste):
        symbole_der_karten = {karte[0] for karte in karten_liste}
        return royal_symbols == symbole_der_karten
    return False


def main():
    # Lokale Definitionen der vorher globalen Variablen
    anzahl_karten = 52
    anzahl_symbole = 13
    anzahl_farben = 4
    symbole = {0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9',
               8: '10', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'}
    farben = {0: 'Kreuz', 1: 'Pik', 2: 'Herz', 3: 'Karo'}

    # Benutzereingabe
    anzahl_spiele = int(input("Bitte die Anzahl der Spiele eingeben: "))
    kombinationen = {
        "Pair": 0,
        "Two Pair": 0,
        "Three of a Kind": 0,
        "Straight": 0,
        "Flush": 0,
        "Full House": 0,
        "Four of a Kind": 0,
        "Straight Flush": 0,
        "Royal Flush": 0,
    }

    # Simulation
    for _ in range(anzahl_spiele):
        karten = get_5(anzahl_karten, anzahl_symbole, anzahl_farben, symbole, farben, 5)
        if royal_flush(karten, symbole):
            kombinationen["Royal Flush"] += 1
        elif straight_flush(karten, symbole):
            kombinationen["Straight Flush"] += 1
        elif quads(karten):
            kombinationen["Four of a Kind"] += 1
        elif full_house(karten):
            kombinationen["Full House"] += 1
        elif flush(karten):
            kombinationen["Flush"] += 1
        elif straight(karten, symbole):
            kombinationen["Straight"] += 1
        elif three_of_a_kind(karten):
            kombinationen["Three of a Kind"] += 1
        elif two_pair(karten):
            kombinationen["Two Pair"] += 1
        elif pair(karten):
            kombinationen["Pair"] += 1

    # Ergebnisse ausgeben
    print(f"Ergebnisse nach {anzahl_spiele} Spielen:")
    for kombination, anzahl in kombinationen.items():
        prozent = (anzahl / anzahl_spiele) * 100
        print(f"{kombination}: {anzahl}, {prozent:.2f}%")


if __name__ == "__main__":
    main()
