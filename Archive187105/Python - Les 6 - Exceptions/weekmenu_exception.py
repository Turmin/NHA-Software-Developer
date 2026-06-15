"""
Neem de code van de huiswerkopgave van vorige les. Integreer in deze code een van de uitzonderingen uit deze les.
"""

weekmenu = {
    "maandag": "pasta carbonara",
    "dinsdag": "rijst met kip",
    "woensdag": "aardappelen met groenten",
    "donderdag": "salade met tonijn",
    "vrijdag": "pizza margherita",
    "zaterdag": "hamburger met friet",
    "zondag": "soep met brood"
}

def toon_menu(dag):
    try:
        gerecht = weekmenu[dag]
        print(f"Op {dag} staat er {gerecht} op het menu.")
    except KeyError:
        print(f"Sorry, {dag} is geen geldige dag van de week.")

dag = input("Welke dag van de week wil je weten wat er op het menu staat? ").lower()
toon_menu(dag)