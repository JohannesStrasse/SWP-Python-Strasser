import random

# Konstanten
anzahl_karten = 52
anzahl_symbole = 13
anzahl_farben = 4

symbole = {0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9',
           8: '10', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'}

farben = {0: 'Kreuz', 1: 'Pik', 2: 'Herz', 3: 'Karo'}

# Funktionen
def get_symbol(karte):
    symbol_index = karte % anzahl_symbole
    return symbole[symbol_index]

def get_farbe(karte):
    farben_index = karte % anzahl_farben
    return farben[farben_index]

def get_5(karten_anzahl):
    gezogene_karten = random.sample(range(anzahl_karten), karten_anzahl)
    return [(get_symbol(karte), get_farbe(karte)) for karte in gezogene_karten]

def pair(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    return any(symbole_der_karten.count(symbol) == 2 for symbol in set(symbole_der_karten))

def two_pair(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    return sum(1 for symbol in set(symbole_der_karten) if symbole_der_karten.count(symbol) == 2) == 2

def three_of_a_kind(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    return any(symbole_der_karten.count(symbol) == 3 for symbol in set(symbole_der_karten))

def quads(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    return any(symbole_der_karten.count(symbol) == 4 for symbol in set(symbole_der_karten))

def flush(karten_liste):
    farbe_der_karten = [karte[1] for karte in karten_liste]
    return any(farbe_der_karten.count(farbe) == 5 for farbe in set(farbe_der_karten))

def straight(karten_liste):
    symbol_werte = {symbol: index for index, symbol in symbole.items()}
    werte_der_karten = sorted(symbol_werte[karte[0]] for karte in karten_liste)
    return all(werte_der_karten[i] == werte_der_karten[i - 1] + 1 for i in range(1, len(werte_der_karten)))

def full_house(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    has_pair = any(symbole_der_karten.count(symbol) == 2 for symbol in set(symbole_der_karten))
    has_three = any(symbole_der_karten.count(symbol) == 3 for symbol in set(symbole_der_karten))
    return has_pair and has_three

def straight_flush(karten_liste):
    return straight(karten_liste) and flush(karten_liste)

def royal_flush(karten_liste):
    royal_symbols = {'10', 'J', 'Q', 'K', 'A'}
    if flush(karten_liste):
        return royal_symbols == {karte[0] for karte in karten_liste}
    return False

def simulate_games(anzahl_spiele):
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
    for _ in range(anzahl_spiele):
        karten = get_5(5)
        if royal_flush(karten):
            kombinationen["Royal Flush"] += 1
        elif straight_flush(karten):
            kombinationen["Straight Flush"] += 1
        elif quads(karten):
            kombinationen["Four of a Kind"] += 1
        elif full_house(karten):
            kombinationen["Full House"] += 1
        elif flush(karten):
            kombinationen["Flush"] += 1
        elif straight(karten):
            kombinationen["Straight"] += 1
        elif three_of_a_kind(karten):
            kombinationen["Three of a Kind"] += 1
        elif two_pair(karten):
            kombinationen["Two Pair"] += 1
        elif pair(karten):
            kombinationen["Pair"] += 1
    return kombinationen

def main():
    anzahl_spiele = int(input("Geben Sie die Anzahl der Spiele ein: "))
    kombinationen = simulate_games(anzahl_spiele)
    print(f"Ergebnisse nach {anzahl_spiele} Spielen:")
    for kombination, anzahl in kombinationen.items():
        prozent = (anzahl / anzahl_spiele) * 100
        print(f"{kombination}: {anzahl}, {prozent:.2f}%")

if __name__ == "__main__":
    main()
