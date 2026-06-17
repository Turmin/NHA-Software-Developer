"""Opdracht 2

Argumenten	Teruggeefwaarde
2           4
4	        16
10	        100
12	        144
"""

def mijn_functie_1(arg):
    return arg * arg

print(mijn_functie_1(2))
print(mijn_functie_1(4))
print(mijn_functie_1(10))
print(mijn_functie_1(12))

"""Opdracht 3

Argumenten	Teruggeefwaarde
12,3	    [15, 9, 36, 4]
12,2    	[14, 10, 24, 6]
10,5	    [15, 5, 50, 2]
100,20	    [120, 80, 2000, 5]
"""

def mijn_functie_2(arg1, arg2):
    return [arg1 + arg2, arg1 - arg2, arg1 * arg2, arg1 / arg2]

print(mijn_functie_2(12, 3))
print(mijn_functie_2(12, 2))
print(mijn_functie_2(10, 5))
print(mijn_functie_2(100, 20))