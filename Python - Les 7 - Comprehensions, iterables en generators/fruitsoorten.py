"""
Maak een string van tien fruitsoorten.
Gebruik de functie split() om uw string om te zetten naar een list.
Gebruik iteratie om de eerste vijf fruitsoorten los te vertonen aan de gebruiker.
"""

fruit_string = "appel, banaan, sinaasappel, peer, druif, kiwi, mango, ananas, watermeloen, blauwe bes"
fruit_list = fruit_string.split(", ")
for i in range(5):
    print(fruit_list[i])

print()

"""
Wilt u wat extra uitdaging? Probeer dan ook de volgende stap uit te voeren. Dit is echter geen verplichting.
Maak een iterator die een reeks getallen retourneert (beginnend met 1) en de getoonde waarde telkens met 1 verhoogt (1, 2, 3, 4, 5, …).
"""
def number_iterator():
    current = 0
    while True:
        current += 1
        yield current

print("Getallen tot en met 10 met functie")
for number in number_iterator():
    if number > 10:
        break
    print(number)

print()
        
print("Getallen tot en met 10 met class")
class NumberIterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current

number_iterator = NumberIterator()
for _ in range(10):
    print(next(number_iterator))
