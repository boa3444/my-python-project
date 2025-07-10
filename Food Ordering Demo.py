from tkinter import *
root= Tk()
# root.minsize(350, 650)
root.geometry("350x650+30+0")

foodchart = PhotoImage(file =r"C:\Users\newon\OneDrive\Documents\fast_food_tkinter.png")
Label(root, image = foodchart).grid(row = 0, column=0, columnspan= 6)

Label(root, text= "What would you like to order:", font= ("Ariel",9, 'bold')).grid(row=1, column = 0)

fast_food = ['Burger', 'Pizza', 'Nuggets', 'French Fries', 'Samosa']
payment_methods = ['Cash', 'UPI', 'Credit/Debit Card']
r= 2

for item in fast_food:
    Checkbutton(root, text= f"{item}", font= ("Ariel",9 )).grid(row = r, column = 0, padx=5, pady=5, sticky= W)
    r+= 1

Label(root, text= "What payment method would you like to choose?", font= ("Ariel",9, 'bold')).grid(row=8, column = 0,padx = 5 , pady= 5, sticky = NSEW)

x= 9
for method in payment_methods:
    Checkbutton(root, text= f"{method}", font= ("Ariel", 9)).grid(row= x, column = 0, padx= 5, pady = 5, sticky = W)
    x+=1
    

def order_complete():
    root.destroy()
    new_root = Tk()
    final_image= PhotoImage(file = r"C:\Users\newon\Downloads\dive_thru_tkinter.png")
    Label(new_root, text= "Have a great day sir/ma'am!", font = ('Ariel', 11, 'italic')).grid(row=0, column = 0)
    label= Label(new_root, image = final_image)
    label.image_names= final_image
    label.grid(row=1, column = 0)


Button(root, text = "Check Out!", command = order_complete).grid(row = 13, column = 0)



root.mainloop()
