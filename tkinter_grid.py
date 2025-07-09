from tkinter import *


root= Tk()
root.minsize(700, 700)
root.title("Customize your Tkinter Profile")



# Label(root, text= "").grid(row=0, column=0, columnspa/n=3)


user_portrait= PhotoImage(file = r"C:\Users\newon\OneDrive\Documents\user_png.png")
final_portrait= user_portrait.subsample(2,2)
border = Frame(root, bg= "black")
border.grid(row=0, column=0, padx= 5, pady=5, rowspan=3)
Label(border, image= final_portrait).grid( pady= 5, padx=5)


# Label(root, text= "").grid(row=1, column=1)


Label(root, text= "Name: ", font= ("Ariel", 13)).grid(row=0, column=1,padx= 5, pady= 5, sticky= E)
Entry(root, width= 35).grid(row= 0, column= 2)



Label(root, text= "Gender: ", font= ("Ariel", 13)).grid(row= 1, column = 1, padx= 5 , pady= 5, sticky = E)
# gender_menu.grid(row=1, column=2)
gender_var = StringVar(root)
gender_options= ['Female', 'Male', 'Rather Not Defined']
gender_menubox = OptionMenu(root,gender_var,*gender_options)
gender_menubox.config(width=30)
gender_menubox.grid(row=1, column=2)




Label(root, text= "Eye color: ", font= ("Ariel", 13)).grid(row= 2, column = 1, padx= 5 , pady= 5, sticky = E)
# gender_menu.grid(row=1, column=2)
eye_var = StringVar(root)
eye_options= ['Brown', 'Green', 'Black', 'Blue']
eye_menubox = OptionMenu(root,eye_var,*eye_options)
eye_menubox.config(width=30)
eye_menubox.grid(row=2, column=2, padx=5, pady=5)




Label(root, text= "Height(cm): ", font= ("Ariel", 13)).grid(row= 3, column = 1, padx= 5 , pady= 7, sticky = E)
Entry(root, width=35).grid(row=3, column=2, padx=5, pady=7)

Label(root, text= "Weight(kg): ", font= ("Ariel", 13)).grid(row= 4, column = 1, padx= 5 , pady= 7, sticky = E)
Entry(root, width=35).grid(row=4, column=2, padx=5, pady=7)


root.mainloop()