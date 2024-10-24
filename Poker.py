import random

anzahl_karten = 52
anzahl_symbole = 13
anzahl_farben = 4

symbole = {0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9',
           8: '10', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'}

farben = {0: 'Kreuz', 1: 'Pik', 2: 'Herz', 3: 'Karo'}

def get_symbol(karte):
    symbol_index = karte % anzahl_symbole
    return symbole[symbol_index]

def get_farbe(karte):
    farben_index = karte % anzahl_farben
    return farben[farben_index]

def get_5():
    gezogene_karten = random.sample(range(anzahl_karten), 5)
    karten_liste = [(get_symbol(karte), get_farbe(karte)) for karte in gezogene_karten]
    return karten_liste

def pair(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    symbole_haeufigkeit = {symbol: symbole_der_karten.count(symbol) for symbol in symbole_der_karten}

    for symbol, count in symbole_haeufigkeit.items():
        if count == 2:
            return True
    return False

def two_pair(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    symbole_haeufigkeit = {symbol: symbole_der_karten.count(symbol) for symbol in symbole_der_karten}

    paar_count = sum(1 for count in symbole_haeufigkeit.values() if count == 2)
    return paar_count == 2

def three_of_a_kind(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    symbole_haeufigkeit = {symbol: symbole_der_karten.count(symbol) for symbol in symbole_der_karten}

    for symbol, count in symbole_haeufigkeit.items():
        if count == 3:
            return True
    return False

def quads(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    symbole_haeufigkeit = {symbol: symbole_der_karten.count(symbol) for symbol in symbole_der_karten}

    for symbol, count in symbole_haeufigkeit.items():
        if count == 4:
            return True
    return False

def flush(karten_liste):
    farbe_der_karten = [karte[1] for karte in karten_liste]
    farbe_häufigkeit = {farbe: farbe_der_karten.count(farbe) for farbe in farbe_der_karten}

    for farbe, count in farbe_häufigkeit.items():
        if count == 5:
            return True
    return False

def straight(karten_liste):
    symbol_werte = {symbol: index for index, symbol in symbole.items()}
    symbole_der_karten = [karte[0] for karte in karten_liste]
    werte_der_karten = sorted(symbol_werte[symbol] for symbol in symbole_der_karten)

    for i in range(1, len(werte_der_karten)):
        if werte_der_karten[i] != werte_der_karten[i - 1] + 1:
            return False

    return True

def full_house(karten_liste):
    symbole_der_karten = [karte[0] for karte in karten_liste]
    symbole_haeufigkeit = {symbol: symbole_der_karten.count(symbol) for symbol in symbole_der_karten}

    has_pair = False
    has_three_of_a_kind = False

    for count in symbole_haeufigkeit.values():
        if count == 2:
            has_pair = True
        elif count == 3:
            has_three_of_a_kind = True

    return has_pair and has_three_of_a_kind

def straight_flush(karten_liste):
    return straight(karten_liste) and flush(karten_liste)

def royal_flush(karten_liste):
    royal_symbols = {'10', 'J', 'Q', 'K', 'A'}

    if flush(karten_liste):
        symbole_der_karten = {karte[0] for karte in karten_liste}
        return royal_symbols == symbole_der_karten
    return False

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

anzahl_spiele = 100000

for _ in range(anzahl_spiele):
    karten = get_5()
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

print(f"Ergebnisse nach {anzahl_spiele} Spielen:")
for kombination, anzahl in kombinationen.items():
    prozent = (anzahl / anzahl_spiele) * 100
    print(f"{kombination}: {anzahl}, {prozent:.2f}%")
