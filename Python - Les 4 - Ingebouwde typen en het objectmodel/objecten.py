#!/usr/bin/env python3

# drie verschillende soorten objecten: tekst, cijfers en lijst
tekst = "Dit is een string."
cijfers = 1234
lijst = [1, 2, 3, 4]

# ingebouwde functies om het type, het id en de lengte van de objecten te tonen
print("Type %s" % type(tekst), "ID %s" % id(tekst), "Lengte %s" % len(tekst))  # Type <class 'str'> ID 2760527262512 Lengte 18
print("Type %s" % type(cijfers), "ID %s" % id(cijfers), "Lengte %s" % len(str(cijfers)))  # Type <class 'int'> ID 2760523232496 Lengte 4
print("Type %s" % type(lijst), "ID %s" % id(lijst), "Lengte %s" % len(lijst))  # Type <class 'list'> ID 2760523997248 Lengte 4

# een eigen functie naar eigen keuze die drie objecten als argumenten gebruikt en een bericht naar de gebruiker toont.
def toon_informatie(tekst, cijfers, lijst):
    """Deze functie toont informatie over de drie objecten."""
    print(f"De tekst is: {tekst}")
    print(f"De cijfers zijn: {cijfers}")
    print(f"De lijst is: {lijst}")

print("\nInformatie over de objecten:")
toon_informatie(tekst, cijfers, lijst)