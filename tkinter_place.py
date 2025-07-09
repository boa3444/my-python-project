from tkinter import *

root= Tk()
root.minsize(700, 700)
root.title("Make a Wish")
Label(root, text= "Your Name:").place(x=130, y=0)
name = Entry(root)
name.place(x=130, y=27 )
Label(root, text= "Which of the following places\nwould you wish to go to?", font= ("Ariel", 25, "bold")).place(x=130, y=50)

places = Listbox(root, width=50)
places.place(y=150, x=130)

places.insert(END, "Bali")
places.insert(END, "Italy")
places.insert(END, "London")
places.insert(END, "Rome")
places.insert(END, "Japan")

            
countries = ["Bali", "Italy", "London", "Rome", "Japan"]
greetings = ["Halo", "Ciao", "Hello", "Ciao", "こんにちは (Konnichiwa)"]

def greet(info):
    
    for country in countries:
        if places.get(places.curselection())== country:
            index = countries.index(country)
            label= Label(root, text = f"{greetings[index]}!, {name.get()}", font = ("Ariel", 15, "bold"))
            label.place(x=145, y= 400)

    root.after(1000, label.destroy) 


places.bind("<<ListboxSelect>>",greet )
root.mainloop()