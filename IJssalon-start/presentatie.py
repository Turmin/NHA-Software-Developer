def presenteer(producten: dict, totaal: int):
    """
    Args:
        producten (dict): een dictionary met de te presenteren gegevens
        totaal (int): het totaalbedrag van de gegevens
    Returns:
        str: een string met de geformatteerde presentatie van de gegevens
    """
    output = ""
    for key, value in producten.items():
        output += f"{key} : {value} euro\n"
    output += "=" * 26 + "\n"
    output += f"totaal : {totaal} euro\n"
    return output

# mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}
# totaal = 50
# print(presenteer(mijn_dict, totaal))