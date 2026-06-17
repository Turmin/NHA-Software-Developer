from helper import decoreer

def print_aanbieding():
    # 2. dictionary met prijzen
    prijzen = {
        "aardbei": 3,
        "vanille": 4,
        "chocolade": 5
    }

    # 3. variabele aanbieding met waarde van aardbei vermenigvuldigd met 0.8
    aanbieding = prijzen["aardbei"] * 0.8

    # 4. variabele reclame_tekst met formatted string
    reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"

    # 5. variabele reclame_tekst2 met waarde reclame_tekst[:index]
    reclame_tekst2 = reclame_tekst[:reclame_tekst.find("0")+1] # of reclame_tekst[:63]

    # 6. variabele reclame_tekst3 met waarde reclame_tekst2 in hoofdletters
    reclame_tekst3 = reclame_tekst2.upper()

    # 7. variabele reclame_tekst4 met waarde list van woorden in reclame_tekst3
    reclame_tekst4 = reclame_tekst3.split()

    # 8. for-loop die door de elementen van reclame_tekst4 itereert
    # 9. print alle elementen op het scherm met lower()
    # 10. if-statement die de lengte van el controleert en het juiste formaat print
    for el in reclame_tekst4:
        if len(el) >= 5:
            print(el.upper())
        else:
            print(el.lower())

decoreer("Aanbieding")
print_aanbieding()