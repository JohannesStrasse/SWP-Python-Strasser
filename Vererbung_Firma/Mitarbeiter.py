from Person import Person

class Mitarbeiter(Person):
    abteilung: object

    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung
