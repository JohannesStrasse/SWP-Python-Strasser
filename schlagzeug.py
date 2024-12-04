from instrumente import Instrumente

# Unterklasse: Schlagzeug
class Schlagzeug(Instrumente):
    def __init__(self, name, material, trommeln):
        super().__init__(name, material)
        self.trommeln = trommeln

    def beschreibung(self):
        super().beschreibung()
        print(f"Es besteht aus {self.trommeln} Trommeln.")