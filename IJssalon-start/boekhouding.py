import csv
from pathlib import Path
from presentatie import *
from helper import *

inkomsten = {"Aardbeien-ijs-totaal": 1000,
             "Vanille-ijs-totaal": 2000,
             "Chocolade-ijs-totaal": 1500,
             "Waterijsjes-totaal": 750}

totaal_inkomsten = som(inkomsten)

print(presenteer(inkomsten, totaal_inkomsten))

with open(Path(__file__).parent / 'boekhouding.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
        writer.writerow([key,value])