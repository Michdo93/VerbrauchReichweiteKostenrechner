# VerbrauchReichweiteKostenrechner
Ein Python-Skript um den Verbrauch, die Reichweite und die Kosten z.B. Spritkosten oder aber auch Stromkosten von Fahrzeugen zu berechnen.

## Verwendung

Du kannst das Skript ausführen mit:

```
python kostenrechner.py
```

Das Skript nutzt beispielhafte Werte einer Mercedes Benz B-Klasse (Benziner), Opel Astra (Diesel) und Dacia Spring (E-Auto).

Man erhält z.B.

```
Kosten für Verbrennungsmotorfahrzeug (E10): 11.43216 Euro
Kosten für Diesel: 6.354936000000001 Euro
Kosten für Elektrofahrzeug: 4.0629 Euro
Bei 221 Arbeitstagen pro Jahr:
2526.50736 Euro
1404.4408560000002 Euro
897.9009 Euro
```

Als tägliche Distanz werden 93,4 km Referenz genommen bei 221 Arbeitstagen.

Testwerte:

Benziner:
7,2 Liter auf 100 km
1,70€ pro Liter E10

Diesel:
4,2 Liter auf 100 km
1,62€ pro Liter Diesel

14,5 kwH auf 100 km
0.30€ pro kwH

Bei Schnellladestationen müsste man den Preis in etwa verdoppeln!
