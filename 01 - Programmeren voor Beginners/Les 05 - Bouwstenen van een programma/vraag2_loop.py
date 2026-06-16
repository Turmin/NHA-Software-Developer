"""
Vraag 2
Schrijf een programma dat de volgende output zo efficiënt mogelijk genereert:

10 maal 2 is 20
11 maal 2 is 22
12 maal 2 is 24
13 maal 2 is 26
14 maal 2 is 28
15 maal 2 is 30
16 maal 2 is 32
17 maal 2 is 34
18 maal 2 is 36
19 maal 2 is 38
"""

for i in range(10, 20):
    resultaat = i * 2
    print(f"{i} maal 2 is {resultaat}")
    