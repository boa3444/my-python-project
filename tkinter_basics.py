from tkinter import *

root=Tk()
root.title("BASICS OF TKINTER")
# root.maxsize(500,500)
root.geometry("500x500+150+150")
# root.config(background= "black")



#Label
Label(root, text="Tkinter Widgets", font= "Algerian", anchor = "e").grid(row=1,column=2)



Label(root, text= "Image Widget:", font = "Calibiri", anchor= 'e').grid(row=2,column=1)
#add an image through Label
image= PhotoImage(file= r"C:\Users\newon\Downloads\tomato.png").subsample(3)
Label(root,image=image, anchor= 'e').grid(row=2,column=2)




#widgets in tkinter
# widgets = [
#     Label,
#     Checkbutton,
#     Entry,
#     Button,
#     Radiobutton,
#     Scale,
#     Spinbox,
# ]

# for widget in widgets:
#     try:
#         w= widget(root, text= widget.__name__, font = "Algerian")

#     except TclError:
#         w= widget(root)

#     w.pack(padx= 10, pady= 10)



#CHECKBUTTON
def once_checked():
    if myvar.get() == 1:
        checkbox.config(text= f"Check Me! (Checked)")
    else:
        checkbox.config(text= "Check Me!")


    

myvar = IntVar()
checkbox = Checkbutton(root,text= "Check Me!", command= once_checked, variable=myvar)
checkbox.grid(row= 3,column= 2)




#listbox important
counting_numbers = [1,2,3]
listbox = Listbox(height=len(counting_numbers))



def change_selection(info):
    change_to = listbox.get(listbox.curselection())
    selection.config(text= f"Selected: {change_to}")


for number in counting_numbers:
    listbox.insert(END,number)
    listbox.grid(row= 5, column = 2)


listbox.bind("<<ListboxSelect>>", change_selection)
    
selection = Label(root, text = "Selected:")
selection.grid(row= 6 , column = 2)






def greetings(greet):
    name = type_here.get()
    Hey.config(text=f"Hey there! {name}")

#label for name
Hey= Label(root, text= "")
Hey.grid(row= 8, column = 2)

#Entry in Tkinter

type_here  = Entry(root)
type_here.insert(END, "Type your name...")
type_here.bind("<Return>",greetings)
type_here.grid(row= 7, column= 2)


def int_selected():
    selected = spinbox.get()
    int_label.config(text= f"You chose: {selected}")
#spinbox
spinbox = Spinbox(root, from_ = 0, to= 100)
spinbox.grid(row = 9, column = 2)
spinbox.config(command= int_selected)


int_label =Label(root, text= "You chose:")
int_label.grid(row= 10 , column = 2)




def scale_int_label(motion):
    selected = scale.get()
    scale_label.config(text= f"You chose: {selected}")

#scale
scale = Scale(root, from_= 0, to = 100)
scale.bind("<Motion>", scale_int_label)
scale.grid(row = 11, column = 2)

scale_label = Label(root, text= "You chose:")
scale_label.grid(row= 12, column = 2)








root.mainloop()