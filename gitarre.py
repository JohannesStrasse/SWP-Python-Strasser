from instrumente import Instrumente

# Unterklasse: Gitarre
class Gitarre(Instrumente):
    def __init__(self, name, material, saiten):
        super().__init__(name, material)
        self.saiten = saiten

    def beschreibung(self):
        super().beschreibung()
        print(f"Es hat {self.saiten} Saiten.")
