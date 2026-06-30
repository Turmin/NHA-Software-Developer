1.	a. Via command  
    Bij een OptionMenu kunt u met command=functie een functie laten uitvoeren zodra de keuze verandert.
2.	b. ```var = StringVar()```  
    Een StringVar object moet u aanmaken met haakjes. Daarna koppelt u die aan de Entry met textvariable=var.
3.	a. ```destroy()```  
    Met bijvoorbeeld command=root.destroy sluit u het Tkinter-venster netjes af.
4.	b. Openen met "w" betekent schrijven. Daarna schrijft u de inhoud van de textbox naar het bestand.
5.	a. ```win.bind('<Return>', handler)```  
    De Return/Enter-toets koppelt u met .bind() aan een functie.
6.	b. Het geeft aan hoe groot het scherm zal worden.  
    Bijvoorbeeld root.geometry("800x600"). Het kan óók positie bevatten, zoals "800x600+100+100", maar van deze keuzes is b de beste.
7.	d. Al deze antwoorden zijn juist.  
    Met .config() kunt u eigenschappen aanpassen zoals bg, fg, text, enzovoort.
8.	a. justify  
    Bijvoorbeeld Entry(..., justify="right").
9.	a. padx en pady  
    Daarmee stelt u ruimte rondom een widget in bij grid() of pack().
10.	b. U geeft het bovenliggende frame mee als variabele.  
    Een widget of frame zet u in een parent/container, bijvoorbeeld Frame(root) of Frame(dashboard).