"""
Maak een weekmenu-dictionary met zeven keys (voor de zeven dagen van de week).
Voeg per key een gerecht toe als waarde.
Maak een vraag aan die de gebruiker een dag laat selecteren/invullen.
Schrijf een code die ervoor zorgt dat het juiste gerecht aan de gebruiker wordt getoond.
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

dag = input("Welke dag van de week wil je weten wat er op het menu staat? ").lower()
gerecht = weekmenu.get(dag, "Sorry, dat is geen geldige dag van de week.")
print(f"Op {dag} staat er {gerecht} op het menu.")