import math

def discriminant(a, b, c):
    """
    Args:
        a (int): de coëfficiënt van x^2;
        b (int): de coëfficiënt van x;
        c (int): het constante getal.
    """
    try:
        a = int(a)
        b = int(b)
        c = int(c)

        D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
        D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)

    except (ValueError, ZeroDivisionError):
        D1 = D2 = "geen oplossing"

    uitvoer = [D1, D2]
    return uitvoer


print("Voor de formule ax^2 + bx + c, geef a, b en c:")

a = input("Geef de waarde van a: ")
b = input("Geef de waarde van b: ")
c = input("Geef de waarde van c: ")

uitkomst = discriminant(a, b, c)

D1 = uitkomst[0]
D2 = uitkomst[1]

print(f"Voor de formule {a}x^2 + {b}x + {c}, zijn de oplossingen D1: {D1} en D2: {D2}")