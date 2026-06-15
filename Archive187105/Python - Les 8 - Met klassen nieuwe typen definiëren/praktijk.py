class Optellen():
    def __init__(self, nummer1, nummer2):
        self.nummer1 = nummer1
        self.nummer2 = nummer2

    def bereken(self):
        optelling = self.nummer1 + self.nummer2
        if optelling > 10:
            print("De uitkomst is groter dan 10.")
        else:
            print("De uitkomst is gelijk aan of kleiner dan 10.")
        return optelling

optelling = Optellen(5, 6)
optelling.bereken()