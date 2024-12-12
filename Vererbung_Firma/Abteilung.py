class Abteilung:
    name: str
    abteilungsleiter: object
    mitarbeiter: list

    def __init__(self, name):
        self.name = name
        self.abteilungsleiter = None
        self.mitarbeiter = []

    def set_abteilungsleiter(self, leiter):
        self.abteilungsleiter = leiter

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)
