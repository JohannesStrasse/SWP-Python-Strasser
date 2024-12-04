from instrumente import Instrumente

# Unterklasse: Klavier
class Klavier(Instrumente):
    def __init__(self, name, material, tasten):
        super().__init__(name, material)
        self.tasten = tasten

    def beschreibung(self):
        super().beschreibung()
        print(f"Es hat {self.tasten} Tasten.")
