from tkinter import *
import requests 

def searchDrink():
    userEntry = entry.get() # this gets anything the user inputs from the cocktail dictionary
    response = requests.get(f'http://www.thecocktaildb.com/api/json/v1/1/search.php?s={userEntry}') # this is where the .json data of the dictionary is stored
    data = response.json() # generates the cocktail that the user types down
    frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

    # the information of the user input will be shown as the order below
    if data['drinks']: # if statement once the user inputs the correct data, this will be shown below
        cocktails = data['drinks'][0]
        name = cocktails['strDrink']
        glass = cocktails['strGlass']
        alcohol = cocktails['strAlcoholic']
        instructions = cocktails['strInstructions']

        Label(frame2, text = f"Name: {name}").pack()
        Label(frame2, text = f"Type of Glass: {glass}").pack()

        # prompt allowing the users to see if the drink they have chosen is alcoholic or not
        if alcohol == "Alcoholic": # the alcoholic content varies depending on the cocktail the user has chosen
            alcoholic = "Yes"
            Label(frame2, text = f"Alcoholic: {alcoholic}").pack()
        else: 
            alcoholic = "Non Alcoholic"
            Label(frame2, text = f"Alcoholic: {alcoholic}").pack()
        
        
        Label(frame2, text = f"Instructions: {instructions}", wraplength=250).pack()
    else:
        Label(frame2, text = f"No cocktail found for '{userEntry}'").pack()

# overall appearance of the GUI 
root = Tk()
root.title("Cocktail Generator")
root.geometry("350x350")
root.configure(bg = '#DC143C')

frame1 = Frame(root, bg = '#DC143C')
frame1.place(relx=0.5, rely=0.1, anchor=CENTER)

#  the main title of the API
title = Label(frame1, text = "Cocktail Mixes",  bg=('#DC143C')) 
title.grid(row = 0, columnspan=2)

# the user input box 
entry = Entry(frame1, width=35)
entry.grid(row = 1, column = 0, padx=(0,5))

# the button to confirm the users drink
btn = Button(frame1, text="Generate!", command=searchDrink)
btn.grid(row = 1, column = 1, padx=(5,0))
frame2 = Frame(root, bg='#89CFF0')

root.mainloop()

