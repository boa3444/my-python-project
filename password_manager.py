from tkinter import *
import random
import pandas as pd
# from random_password_generator import password_generator, show_pass_var

root = Tk()
root.geometry("700x600+100+90")
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

#password generation
characters = ["!", "@","#", "$", "%", "^", "&", "*",  "<", "/", "_", "y", "p", "U", "W"]
password_list = []
character = 0
clicks_count = 0

def password_created():
    global  character, final_pass
    password.delete(0, END)


    for x in range(15):
      password_list.append(random.choice(characters))
      final_pass = ''.join(password_list)
    password.insert(END, final_pass )
    
    
    password_list.clear()
    character = 0
            

  

canvas = Canvas(root, height = 200, width = 205)
pass_png = PhotoImage(file = r"C:\Users\newon\Downloads\logo.png")
canvas.create_image(100, 100,image = pass_png)
canvas.grid(row= 0, column = 1)

Label(root, text = 'Website:', font = ("Ariel", 13, "bold")).grid(row= 1, column = 0, sticky =E, padx =50, pady = 10)
Website = Entry(root, width = 50)
Website.grid(row = 1,column = 1, sticky = E)


Label(root, text = 'Label/Username:', font = ("Ariel", 13, "bold")).grid(row= 2, column = 0, sticky =E, padx =50, pady = 10)
Username = Entry(root, width = 50)
Username.grid(row = 2,column = 1, sticky = E)


Label(root, text = 'Password:', font = ("Ariel", 13, "bold")).grid(row= 3, column = 0, sticky =E, padx =50, pady = 10)
password = Entry(root, width = 40)
password.grid(row = 3,column = 1, sticky = W)

generate_pass = Button(root, text = "Generate Password", command= password_created)
generate_pass.grid(row = 3, column = 2)


def data():
    info= {
       
    'Website': Website.get(),
    'Username':Username.get(),
    'Password':password.get()
  
    }
    df = pd.DataFrame(data = info)
    with open(file = r"C:\Users\newon\OneDrive\Documents\Tkinter\password_storage.txt", mode = 'w') as pass_storage:
      df.to_csv(pass_storage, index = False)
       


Button(root, text = "ADD", command = data).grid(row=4, column = 1, sticky = NSEW, padx = 5, pady = 7)


root.mainloop()