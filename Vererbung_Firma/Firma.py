class Firma:
    abteilungen: list

    def __init__(self):
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def anzahl_mitarbeiter(self):
        return sum(len(abteilung.mitarbeiter) for abteilung in self.abteilungen)

    def anzahl_abteilungsleiter(self):
        return sum(1 for abteilung in self.abteilungen if abteilung.abteilungsleiter)

    def anzahl_abteilungen(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        if not self.abteilungen:
            return None

        groesste = None
        max_mitarbeiter = 0

        for abteilung in self.abteilungen:
            anzahl_mitarbeiter = len(abteilung.mitarbeiter)
            if anzahl_mitarbeiter > max_mitarbeiter:
                groesste = abteilung
                max_mitarbeiter = anzahl_mitarbeiter

        return groesste

    def prozent_frauen_maenner(self):
        frauen, maenner = 0, 0
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.geschlecht.lower() == 'frau':
                    frauen += 1
                elif mitarbeiter.geschlecht.lower() == 'mann':
                    maenner += 1
        total = frauen + maenner
        return {
            "Frauen": (frauen / total) * 100 if total > 0 else 0,
            "Männer": (maenner / total) * 100 if total > 0 else 0,
        }
    
