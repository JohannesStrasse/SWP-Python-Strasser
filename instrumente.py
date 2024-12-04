class Instrumente:
    def __init__(self, name, material):     #des is da Konstruktor
        self.name = name
        self.material = material

    def spielen(self):
        print(f"{self.name} wird gespielt.")

    def beschreibung(self):
        print(f"Das {self.name} ist aus {self.material} hergestellt.")


