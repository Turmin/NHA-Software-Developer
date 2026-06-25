from algemene_functies import mijn_functie_2

"""Opdracht 5
"""
def aanbieding_1(smaak, prijs, korting):
    aanbiedingsprijs = f"{prijs * (1 - korting):.2f}".replace(".", ",") # afronden op 2 decimalen en punt vervangen door komma
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:g} euro voor {aanbiedingsprijs} euro."

# print(aanbieding_1("aardbei", 4, 0.1)) # Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak aardbei, van 4 euro voor 3,60 euro.

"""Opdracht 6
"""
def inkomsten_totaal(inkomsten):
    return sum(inkomsten)

# print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345])) # 1575

"""Opdracht 7
"""
def inkomsten_totaal(inkomsten, btw):
    totale_inkomsten = sum(inkomsten)
    btw_bedrag = totale_inkomsten * btw
    return f"Het totaal van alle inkomsten van deze week is {totale_inkomsten:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."

# print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09)) # Het totaal van alle inkomsten van deze week is 1575.00 euro, waarover 141.75 euro btw betaald dient te worden.

"""Opdracht 8
"""
def laag_en_hoog(mijn_lijst):
    return [min(mijn_lijst), max(mijn_lijst)]

# print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345])) # [90, 430]

"""Opdracht 9
"""
def gemiddelde(mijn_lijst):
    return sum(mijn_lijst) / len(mijn_lijst)

# print(gemiddelde([220, 430, 125, 160, 205, 90, 345])) # 225.0

"""Opdracht 10
"""
def gemiddelde(mijn_lijst):
    return f"De gemiddelde inkomsten deze week zijn {sum(mijn_lijst) / len(mijn_lijst):.2f} euro."

# print(gemiddelde([220, 430, 125, 160, 205, 90, 345])) # De gemiddelde inkomsten deze week zijn 225.00 euro.

"""Opdracht 11
"""
def meervoudig(invoer_lijst):
    return [laag_en_hoog(invoer_lijst)]

# print(meervoudig([10,5,3,2,1,2,9])) # [[1, 10]]

"""Opdracht 12
"""

def combinatie(invoer_lijst2):
    korte_lijst = laag_en_hoog(invoer_lijst2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])

# print(combinatie([10,5,3,2,1,2,9])) # [11, -9, 10, 0.1]