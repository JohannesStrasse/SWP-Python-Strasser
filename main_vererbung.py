from gitarre import Gitarre
from klavier import Klavier
from schlagzeug import Schlagzeug

def main():
    # Erstelle Objekte der verschiedenen Instrumente
    gitarre = Gitarre("Taylor", "Buchenholz", 6)
    klavier = Klavier("Steinway", "Feinstes Südtiroler Holz", 50)
    schlagzeug = Schlagzeug("Yamaha Schlagzeug", "Metall", 10)

    # Teste die Methoden
    gitarre.spielen()
    gitarre.beschreibung()

    klavier.spielen()
    klavier.beschreibung()

    schlagzeug.spielen()
    schlagzeug.beschreibung()

if __name__ == "__main__":
    main()