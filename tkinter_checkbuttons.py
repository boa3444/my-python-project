from tkinter import *

root = Tk()
root.minsize(600,600)
root.title("Bake your Cake")

root.columnconfigure(0, weight=2)  # Left padding column
root.columnconfigure(1, weight=2)  # Label column
root.columnconfigure(2, weight=2)
Label(root, text= "Choose the options you would like in your cake!", font= ("Ariel", 15)).grid(row= 0, column=1, padx= 5 , pady=5)


cake_var1 = StringVar(root, value="False")
opt1 = Checkbutton(root, text="Butter🧈", font=13, variable=cake_var1, onvalue="True", offvalue="False")
opt1.grid(row=1, column=1, padx=5, pady=5)

cake_var2 = StringVar(root, value="False")
opt2 = Checkbutton(root, text="Chocolate🍫", font=13, variable=cake_var2, onvalue="True", offvalue="False")
opt2.grid(row=2, column=1, padx=5, pady=5)

cake_var3 = StringVar(root, value="False")
opt3 = Checkbutton(root, text="Vanilla🍨", font=13, variable=cake_var3, onvalue="True", offvalue="False")
opt3.grid(row=3, column=1, padx=5, pady=5)

cake_var4 = StringVar(root, value="False")
opt4 = Checkbutton(root, text="Pineapple🍍", font=13, variable=cake_var4, onvalue="True", offvalue="False")
opt4.grid(row=4, column=1, padx=5, pady=5)

cake_var5 = StringVar(root, value="False")
opt5 = Checkbutton(root, text="Strawberry🍓", font=13, variable=cake_var5, onvalue="True", offvalue="False")
opt5.grid(row=5, column=1, padx=5, pady=5)

cake_var6 = StringVar(root, value="False")
opt6 = Checkbutton(root, text="Cream🍦", font=13, variable=cake_var6, onvalue="True", offvalue="False")
opt6.grid(row=6, column=1, padx=5, pady=5)



variables = [cake_var1, cake_var2, cake_var3, cake_var4, cake_var5, cake_var6]
options = ['butter', 'chocolate', 'vanilla','pineapple', 'strawberry', 'cream']



def bake():
    chosen_list= []

    for each in variables:
        if each.get() == 'True':
            index = variables.index(each)

            chosen_list.append(options[index])

    # for item in chosen_list:
            Label(root, text = f"Here's your {' '.join(chosen_list)} cake!!\n🍰🎂\nHope you enjoy it", font= 14).grid(row=8, column= 1)

        else:
            Label(root, text = f"Here's your simple but palatable cake!!\n🍰🎂\nHope you enjoy it", font= 14).grid(row=8, column= 1)


Button(root, text="Click me! to start baking", command = bake).grid(row=7, column=1)






root.mainloop()