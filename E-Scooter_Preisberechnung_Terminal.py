def berechne_preis_dauer(dauer):
    grundgebuehr = 1.00  # Grundgebühr in Euro
    preis_pro_minute = 0.15  # Preis pro Minute in Euro
    return grundgebuehr + (preis_pro_minute * dauer)

def berechne_preis_strecke(strecke):
    grundgebuehr = 1.00  # Grundgebühr in Euro
    preis_pro_km = 0.50  # Preis pro Kilometer in Euro
    return grundgebuehr + (preis_pro_km * strecke)

def main():
    print("Willkommen bei der E-Scooter Preisberechnung!")
    print("Möchten Sie den Preis basierend auf der Nutzungsdauer oder Nutzungsstrecke berechnen?")
    print("1: Nutzungsdauer (in Minuten)")
    print("2: Nutzungsstrecke (in Kilometern)")

    wahl = input("Bitte wählen Sie 1 oder 2: ")

    if wahl == "1":
        dauer = float(input("Bitte geben Sie die Nutzungsdauer in Minuten ein: "))
        preis = berechne_preis_dauer(dauer)
        print(f"Der Fahrpreis beträgt: {preis:.2f} Euro")
    elif wahl == "2":
        strecke = float(input("Bitte geben Sie die Nutzungsstrecke in Kilometern ein: "))
        preis = berechne_preis_strecke(strecke)
        print(f"Der Fahrpreis beträgt: {preis:.2f} Euro")
    else:
        print("Ungültige Auswahl. Bitte starten Sie das Programm erneut und wählen Sie 1 oder 2.")

if __name__ == "__main__":
    main()
    
