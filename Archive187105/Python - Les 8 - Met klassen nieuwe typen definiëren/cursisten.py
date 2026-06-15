"""
Maak een klasse met de naam CursistenRegister. Deze klasse zal met vier gegevens werken, namelijk voornaam, achternaam, adres en e-mail.
Maak een methode in uw klasse die een welkomstbericht toont aan de gebruiker, bijvoorbeeld:

Welkom Tom Tomassen. Uw boekenpakket is verstuurd naar Giraffestraat 4 in Amsterdam. U krijgt hiervan een bevestiging op het door u opgegeven e-mailadres: tom@python123.nl.

(Dit is slechts een voorbeeldbericht. U mag de gegevens van de gebruiker en het bericht natuurlijk zelf verzinnen.)
"""

class CursistenRegister:
    def __init__(self, voornaam, achternaam, adres, email):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.adres = adres
        self.email = email

    def welkomstbericht(self):
        print(f"Welkom {self.voornaam} {self.achternaam}. Uw boekenpakket is verstuurd naar {self.adres}. U krijgt hiervan een bevestiging op het door u opgegeven e-mailadres: {self.email}.")
cursist = CursistenRegister("Tom", "Tomassen", "Giraffestraat 4 in Amsterdam", "tom@python123.nl")
cursist.welkomstbericht()
