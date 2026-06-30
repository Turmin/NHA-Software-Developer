1. Hoe roept u een functie of method aan met het OptionMenu-widget in Tkinter?  

    a. Via command  
    b. Via options  
    c. Via config  
    d. Via select  

2. Hoe gebruikt u een StringVar object bij een Entry widget? 

    a. var = StringVar  
    b. var = StringVar()  
    c. var = StringVar(value=)  
    d. var = []  

3. Hoe sluit u een Python-programma af, met behulp van een button?  

    a. destroy()  
    b. quit()  
    c. stop()  
    d. pause() 

4. Hoe bewaart u de inhoud van een Textbox of Entry in tkinter?  

    a.
    ```python
    text_file = open("test.txt", "r")  
    content = text_file.read()  
    my_text_box.insert(END, content)  
    text_file.close()
    ```

    b.
    ```python
    text_file = open("test.txt", "w")
    text_file.write(my_text_box.get(1.0, END))
    text_file.close()
    ```

    c.
    ```python
    text_file = open("test.txt", "a")
    content = text_file.read()
    my_text_box.insert(END, content)
    text_file.close()
    ```

    d.
    ```python
    text_file = open("test.txt", "r")
    text_file.write(my_text_box.get(1.0, END))
    text_file.close()
    ```

5. Hoe koppelt u de return toets aan een functie in tkinter? 

    a. ```win.bind('<Return>', handler)```  
    b. ```win.bind('<Enter>', handler)```  
    c. ```win.bind(handler, '<Return>')```  
    d. ```win.bind(handler, '<Enter>')```  

6. Geometry, wat doet dat in Tkinter?  

    a. Het geeft aan waar het scherm komt te staan.  
    b. Het geeft aan hoe groot het scherm zal worden.  
    c. Het geeft aan of er een sluitknop op het scherm komt.  
    d. Al deze antwoorden zijn juist.  

7. Waar is config voor?  

    a. Daarmee is het mogelijk de achtergrondkleur te bepalen.  
    b. Daarmee is het mogelijk om de voorgrond kleur te bepalen.  
    c. Daarmee kunt u de tekst koppelen aan een widget.  
    d. Al deze antwoorden zijn juist.  

8. Hoe stelt u de justification in bij een Entry- of een Textbox-widget?  

    a. justify  
    b. non_justify  
    c. middle_justify  
    d. top_justify  

9. Hoe stelt u de ruimte in rondom een widget?  

    a. padx en pady  
    b. marginx en marginy  
    c. spacex en spacey  
    d. framex en framey  

10. Als u frames wilt stacken, hoe doet u dat?  

    a. U geeft het onderliggende frame mee als variabele.  
    b. U geeft het bovenliggende frame mee als variabele.  
    c. U kunt gewoon, zonder onderliggend frame een nieuwe bouwen.  
    d. Dat kan niet.  