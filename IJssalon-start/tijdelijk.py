"""
Vraag 1
Voeg een nieuw bestand toe aan de map 'IJssalon-start'. Geef deze map de naam tijdelijk.py.
Plaats in het bestand 'tijdelijk.py' een dictionary genaamd prijzen. Zorg ervoor dat deze dictionary de volgende key-value pairs bevat:

Key	Value
aardbei	3
vanille	4
chocolade	5
Plaats in het bestand 'tijdelijk.py' een variabele met de naam aanbieding. Deze variabele heeft de waarde van het dictionary-element aardbei, vermenigvuldigd met 0.8.
Plaats in het bestand 'tijdelijk.py' een variabele met de naam reclame_tekst. Deze variabele heeft de volgende zin als waarde:

Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € <aanbieding>

Daar waar nu <aanbieding> staat, plaatst u de variabele met de naam aanbieding. Dat doet u door het maken van een formatted string. Voeg ook een print-statement toe dat de waarde van de variabele reclame_tekst uitvoert naar het scherm.
Als u de variabele reclame_tekst uitprint, ziet u dat die er een beetje raar uitziet:


Er zijn meerdere oplossingen mogelijk. U verwijdert de print-opdracht uit de code en creëert een extra variabele met de naam reclame_tekst2. Die variabele geeft u de waarde reclame_tekst[:_____]. Op de open plek na de dubbele punt plaatst u de index die hoort bij de eerste 0 na de komma.

Print daarna de waarde van deze nieuwe variabele reclame_tekst2.
Een oom van Ellie heeft een sportvliegtuigje, waarachter hij een spandoek kan hangen. Dan moeten de letters van de reclametekst wel allemaal in hoofdletters.

Verwijder de print-opdracht uit de code en voeg een extra variabele toe met de naam reclame_tekst3. Die variabele heeft als waarde dezelfde tekst als de variabele reclame_tekst2, maar dan in hoofdletters.

Print daarna de waarde van deze nieuwe variabele reclame_tekst3.
Voor de drukker van het spandoek is het handiger als de reclametekst voor achter het vliegtuigje een list van woorden is.

Verwijder de print-opdracht uit de code en voeg een extra variabele toe met de naam reclame_tekst4. Die variabele heeft als waarde een list van alle woorden van de string reclame_tekst3.

Print daarna de waarde van deze nieuwe variabele reclame_tekst4.
Ellie wil zien hoe de woorden eruitzien als ze onder elkaar afgedrukt worden. Dat zou goed kunnen werken voor een flyer die ze in de buurt wil verspreiden.

Verwijder de print-opdracht uit de code en creëer een for-loop die door de elementen van de list reclame_tekst4 itereert. Gebruik de naam el als variabele voor de for-loop.

Print daarna alle elementen op het scherm.
Het resultaat van de print-opdracht staat in hoofdletters. Voor de flyer wil Ellie echter liever geen hoofdletters. Pas daarom de string-method .lower() toe op de variabele el.
Ellie is nog niet helemaal tevreden, het kan nog beter. Ze wil dat alleen de elementen die vijf of meer karakters hebben in hoofdletters worden geprint (en bij vier of minder karakters in kleine letters).

Voeg een if-statement toe aan de for-loop die de lengte van de variabele el controleert en het juiste formaat print.
Maak een nieuwe lokale versie van het project aan. Gebruik daarvoor twee commando's, waarbij u bij het tweede commando deze tekst tussen aanhalingstekens plaatst:

"bestand tijdelijk.py gecodeerd"
Update uw remote repo op GitHub.
Stuur de URL van uw remote repo op GitHub via Plaza naar uw docent. Die kan dan niet alleen het eindresultaat zien, maar ook alle tussentijdse wijzigingen.
"""

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
# print(reclame_tekst)

# 5. variabele reclame_tekst2 met waarde reclame_tekst[:index]
reclame_tekst2 = reclame_tekst[:reclame_tekst.find("0")+1] # of reclame_tekst[:63]
# print(reclame_tekst2)

# 6. variabele reclame_tekst3 met waarde reclame_tekst2 in hoofdletters
reclame_tekst3 = reclame_tekst2.upper()
# print(reclame_tekst3)

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

