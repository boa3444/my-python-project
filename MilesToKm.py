from tkinter import *

screen = Tk()
screen.title("MILES to KM convertor")
screen.minsize(width= 200, height=190)

def convertor():
    global input
    input = int(miles.get())
    input *= 1.60934
    output.config(text = input)
    


miles = Entry(width = 13)
miles.grid(row= 1, column = 2)

# hold_of_input()


is_equal_to = Label(text= "is equal to")
is_equal_to.grid(row= 2, column= 1)


calculate_button = Button(text= 'Calculate', command= convertor)
calculate_button.grid(row=3 ,column=2)

output = Label(text='')
output.grid(row=2,column=2)


kilometer_text= Label(text= 'kilometers')
kilometer_text.grid(row=2, column = 3)


miles_text= Label(text= 'miles')
miles_text.grid(row=1, column = 3)





screen.mainloop()
