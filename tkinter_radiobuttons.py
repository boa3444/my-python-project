from tkinter import *


root= Tk()
root.minsize(400,400)
root.title("Demo for radiobuttons")


initial = Label(root, text= "Selected: None")
initial.grid(row=0, column= 0)


def chosen():
    # root.after(1000, initial.destroy)
    initial.config(text=f"Selected: {selected_country.get()}")
    # new_initial= Label(root, text= )
    # initial.grid(row=0, column= 0)
    # root.after(1000, new_initial.destroy)



selected_country = StringVar(root, value= False)  # Shared variable for all Radiobuttons

country1 = Radiobutton(root, text="USA", variable=selected_country, value="USA", command=chosen)
country1.grid(row=1, column=0)

country2 = Radiobutton(root, text="Switzerland", variable=selected_country, value="Switzerland", command=chosen)
country2.grid(row=2, column=0)

country3 = Radiobutton(root, text="Ohio", variable=selected_country, value="Ohio", command=chosen)
country3.grid(row=3, column=0)

country4 = Radiobutton(root, text="India", variable=selected_country, value="India", command=chosen)
country4.grid(row=4, column=0)

country5 = Radiobutton(root, text="Myanmar", variable=selected_country, value="Myanmar", command=chosen)
country5.grid(row=5, column=0)  # Changed row to avoid overlap





root.mainloop()