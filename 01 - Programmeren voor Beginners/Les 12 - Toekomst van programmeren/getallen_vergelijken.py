"""
Maak een computerprogrammaatje dat twee getallen als invoer accepteert en True uitvoert als de getallen gelijk aan elkaar zijn en False als deze niet gelijk aan elkaar zijn.

Maak vervolgens een testtabel, waarbij u van tevoren nadenkt over de waardes die u wil invoeren en de te verwachten uitkomst. Bijvoorbeeld:

Invoer	Verwachte uitvoer	Uitvoer	Opmerkingen
1,2     False
3,3     True
…       …
…       …
Zorg ervoor dat uw tabel uit minimaal tien rijen bestaat en vul de tabel compleet in. (Lees: vul niet alleen een verwachting in, maar controleer ook of uw verwachting klopt.)
"""

def getallen_vergelijken(getal1, getal2):
    return getal1 == getal2

testtabel = [
        {
            "getal1": 1,
            "getal2": 2,
            "verwachte_uitvoer": False,
            "uitvoer": getallen_vergelijken(1, 2),
            "opmerkingen": ""
        },
        {
            "getal1": 3,
            "getal2": 3,
            "verwachte_uitvoer": True,
            "uitvoer": getallen_vergelijken(3, 3),
            "opmerkingen": ""
        },
        {
            "getal1": -5,
            "getal2": -5,
            "verwachte_uitvoer": True,
            "uitvoer": getallen_vergelijken(-5, -5),
            "opmerkingen": ""
        },
        {
            "getal1": 0,
            "getal2": 0,
            "verwachte_uitvoer": True,
            "uitvoer": getallen_vergelijken(0, 0),
            "opmerkingen": ""
        },
        {
            "getal1": 10,
            "getal2": 20,
            "verwachte_uitvoer": False,
            "uitvoer": getallen_vergelijken(10, 20),
            "opmerkingen": ""
        },
        {
            "getal1": 100,
            "getal2": 100,
            "verwachte_uitvoer": True,
            "uitvoer": getallen_vergelijken(100, 100),
            "opmerkingen": ""
        },
        {
            "getal1": -1,
            "getal2": 1,
            "verwachte_uitvoer": False,
            "uitvoer": getallen_vergelijken(-1, 1),
            "opmerkingen": ""
        },
        {
            "getal1": 50,
            "getal2": 50.0,
            "verwachte_uitvoer": True,
            "uitvoer": getallen_vergelijken(50, 50.0),
            "opmerkingen": "Int en float worden als gelijk beschouwd als ze dezelfde waarde hebben."
        },
        {
            "getal1": 7.5,
            "getal2": 7.5,
            "verwachte_uitvoer": True,
            "uitvoer": getallen_vergelijken(7.5, 7.5),
            "opmerkingen": ""
        },
        {
            "getal1": -10.5,
            "getal2": -10.5,
            "verwachte_uitvoer": True,
            "uitvoer": getallen_vergelijken(-10.5, -10.5),
            "opmerkingen": ""
        }
]

print(f"{'Invoer':<15}{'Verwachte uitvoer':<22}{'Uitvoer':<12}{'Opmerkingen'}")
print("-" * 65)

for test in testtabel:
    invoer = f"{test['getal1']},{test['getal2']}"

    print(
        f"{invoer:<15}"
        f"{str(test['verwachte_uitvoer']):<22}"
        f"{str(test['uitvoer']):<12}"
        f"{test['opmerkingen']}"
    )