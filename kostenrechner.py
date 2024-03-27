class Verbrauch:
    def __init__(self, strecke_km, verbrauch_pro_100km):
        self.strecke_km = strecke_km
        self.verbrauch_pro_100km = verbrauch_pro_100km

    def berechne_verbrauch(self):
        verbrauch = (self.strecke_km / 100) * self.verbrauch_pro_100km
        return verbrauch

class Reichweite:
    def __init__(self, verbrauch_pro_100km, energiemenge):
        self.verbrauch_pro_100km = verbrauch_pro_100km
        self.energiemenge = energiemenge

    def berechne_reichweite(self):
        reichweite_km = (self.energiemenge / self.verbrauch_pro_100km) * 100
        return reichweite_km

class Kostenrechner:
    def __init__(self, preis_pro_einheit, strecke_km, verbrauch_pro_100km):
        self.preis_pro_einheit = preis_pro_einheit
        self.verbrauch_obj = Verbrauch(strecke_km, verbrauch_pro_100km)

    def berechne_kosten(self):
        verbrauch = self.verbrauch_obj.berechne_verbrauch()
        kosten = verbrauch * self.preis_pro_einheit
        return kosten

# Beispielverwendung für Verbrennungsmotor- und Elektrofahrzeug
if __name__ == "__main__":
    # Verbrennungsmotorfahrzeug E10 --> z.B. Mercedes Benz B-Klasse
    strecke_verbrennung = 46.7 * 2  # in km
    verbrauch_verbrennung = 7.2  # in Liter / 100km (typischer Wert für einen Verbrennungsmotor)
    treibstoffpreis_pro_liter = 1.7  # in Euro pro Liter (Beispielwert)
    kostenrechner_verbrennung = Kostenrechner(treibstoffpreis_pro_liter, strecke_verbrennung, verbrauch_verbrennung)

    # Diesel --> z.B. Opel Astra
    strecke_diesel = strecke_verbrennung # in km
    verbrauch_diesel = 4.2  # in Liter / 100km (typischer Wert für einen Verbrennungsmotor)
    dieselpreis_pro_liter = 1.62  # in Euro pro Liter (Beispielwert)
    kostenrechner_diesel = Kostenrechner(dieselpreis_pro_liter, strecke_diesel, verbrauch_diesel)

    # Elektrofahrzeug --> z.B. Dacia Spring
    strecke_elektro = strecke_verbrennung # in km
    verbrauch_elektro = 14.5  # in kWh / 100km (typischer Wert für ein Elektrofahrzeug)
    energiepreis_pro_kwh = 0.30  # in Euro pro kWh (Beispielwert)
    kostenrechner_elektro = Kostenrechner(energiepreis_pro_kwh, strecke_elektro, verbrauch_elektro)

    # Berechnung der Kosten für Verbrennungsmotor- und Elektrofahrzeug
    kosten_verbrennung = kostenrechner_verbrennung.berechne_kosten()
    kosten_diesel = kostenrechner_diesel.berechne_kosten()
    kosten_elektro = kostenrechner_elektro.berechne_kosten()

    print("Kosten für Verbrennungsmotorfahrzeug (E10):", kosten_verbrennung, "Euro")
    print("Kosten für Diesel:", kosten_diesel, "Euro")
    print("Kosten für Elektrofahrzeug:", kosten_elektro, "Euro")

    print("Bei 221 Arbeitstagen pro Jahr:")
    print(kosten_verbrennung * 221, "Euro")
    print(kosten_diesel * 221, "Euro")
    print(kosten_elektro * 221, "Euro")
