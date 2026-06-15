#!/usr/bin/env python3

naam_gebruiker = input("Wat is uw naam? ")

def begroet(naam):
    """Dit is een functie.
    Deze functie begroet de gebruiker persoonlijk.
    """
    print(f"Hallo {naam}, welkom bij de Python-module les!")

begroet(naam_gebruiker)