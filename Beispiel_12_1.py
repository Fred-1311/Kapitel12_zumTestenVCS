# Beispiel 12.1
#
# Eine einfaches Beispiel zum Experimentieren
#
import Auto


def main():
    # Hauptprogramm
    auto_eins = Auto.Auto("Golf", "Schwarz", 110, 5)
    auto_zwei = Auto.Auto("Golf", "Grün", 50, 3)

    print("\nDaten von Auto eins:")
    auto_eins.zeige_daten()

    print("\nDaten von Auto zwei:")
    auto_zwei.zeige_daten()

    print("Neues Auto erzeugt")
    print("Der Fehler wurde behoben!")

    auto_eins.strecke_fahren(64)
    auto_zwei.strecke_fahren(128)

    print("Kilometerstand des ersten Autos:", auto_eins.kilometerstand)
    print("Kilometerstand des zweiten Autos:", auto_zwei.kilometerstand)


main()
