naam = input("Wat is je naam? ")
geboorteplaats = input("Wat is je geboorteplaats? ")

leeftijd = input("Wat is je leeftijd? ")

if leeftijd.isdigit():
    leeftijd = int(leeftijd)

    print()
    print("Leuk om je te ontmoeten!")
    print("Naam:", naam)
    print("Geboorteplaats:", geboorteplaats)
    print("Leeftijd:", leeftijd)

    if leeftijd > 50:
        print()
        print("Je bent niet oud, je bent gewoon een klassieker met ervaring!")
else:
    print("Dat lijkt geen geldige leeftijd te zijn.")