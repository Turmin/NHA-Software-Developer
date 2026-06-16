"""
Vraag 2
a. Maak een dictionary dat bestaat uit de volgende elementen:

Voornaam	Harry
Achternaam	van Winkel
Geboortedatum	27-3-1939

Voeg daaronder het commando toe waarmee dit dictionary wordt geprint.

b. Print met behulp van een commando het element met de sleutel voornaam uit.

c. Verander met behulp van een commando de voornaam in Henrikus. Voeg daarna opnieuw het commando toe waarmee dit dictionary geprint kan worden.
"""

persoonsgegevens = {
    "Voornaam": "Harry",
    "Achternaam": "van Winkel",
    "Geboortedatum": "27-3-1939"
}

# print dictionary
print(persoonsgegevens)

# print element met sleutel 'Voornaam'
print(persoonsgegevens["Voornaam"])

# verander voornaam in 'Henrikus'
persoonsgegevens["Voornaam"] = "Henrikus"

# print nieuwe dictionary
print(persoonsgegevens)