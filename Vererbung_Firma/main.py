from Firma import Firma
from Abteilung import Abteilung
from Abteilungsleiter import Abteilungsleiter
from Mitarbeiter import Mitarbeiter

# Firma erstöhn
firma = Firma()

# Abteilungen erstöhn
it_abteilung = Abteilung("IT")
hr_abteilung = Abteilung("HR")

# Abteilungsleiter erstöhn
it_leiter = Abteilungsleiter(name="Alice", geschlecht="Frau", abteilung=it_abteilung)
hr_leiter = Abteilungsleiter(name="Bob", geschlecht="Mann", abteilung=hr_abteilung)

# Mitarbeiter erstöhn
it_mitarbeiter = [
    Mitarbeiter(name="Clara", geschlecht="Frau", abteilung = it_abteilung),
    Mitarbeiter(name="David", geschlecht="Mann", abteilung = it_abteilung),
    Mitarbeiter(name="Eva", geschlecht="Frau", abteilung = it_abteilung),
]

hr_mitarbeiter = [
    Mitarbeiter(name="Frank", geschlecht="Mann", abteilung = hr_abteilung),
    Mitarbeiter(name="Grace", geschlecht="Frau", abteilung = hr_abteilung),
]

# Abteilungsleiter zu de Abteilungen zuaordnen
it_abteilung.set_abteilungsleiter(it_leiter)
hr_abteilung.set_abteilungsleiter(hr_leiter)

# Mitarbeiter zu de Abteilungen dazuadoa
for mitarbeiter in it_mitarbeiter:
    it_abteilung.add_mitarbeiter(mitarbeiter)

for mitarbeiter in hr_mitarbeiter:
    hr_abteilung.add_mitarbeiter(mitarbeiter)

# Abteilungen zua Firma dazuadoa
firma.add_abteilung(it_abteilung)
firma.add_abteilung(hr_abteilung)

# Firma-Statistiken uzoang
print("Anzahl Mitarbeiter:", firma.anzahl_mitarbeiter())
print("Anzahl Abteilungsleiter:", firma.anzahl_abteilungsleiter())
print("Anzahl Abteilungen:", firma.anzahl_abteilungen())

groesste_abteilung = firma.groesste_abteilung()
if groesste_abteilung:
    print(f"Die größte Abteilung ist: {groesste_abteilung.name} mit {len(groesste_abteilung.mitarbeiter)} Mitarbeitern.")
else:
    print("Keine Abteilungen vorhanden.")

print("Prozent Frauen/Männer:", firma.prozent_frauen_maenner())
