def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    """
    Args:
        bedrag (int): het totaalbedrag van alle fooi, oftewel het bedrag dat verdeeld moet worden;
        personen (int): het aantal personen waarover het bedrag verdeeld dient te worden.
    """
    try:
        bedrag_pp = bedrag / personen # bedrag gedeeld door personen
    except:
        bedrag_pp = "??"
    return f"Het bedrag per persoon is {bedrag_pp} euro"

# b = int(input("Welk bedrag zit er in de fooienpot? "))
# p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))

# print(fooi_pp(b,p))

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def som(getallen: dict):
    """
    Args:
        getallen (dict): een dictionary met getallen als waarden

    Returns:
        int: de som van de waarden in de dictionary
    """
    if type(getallen) != dict: return
    return sum(getallen.values())