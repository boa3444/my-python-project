from tkinter import *

screen= Tk()
screen.title("My First Tkinter Screen")
screen.minsize(300,400)


showcasethis = Label(text = 'Hello World!', font = ('Times New Roman',30,'bold'))
showcasethis.pack()


# showcasethis.config(font= ('Ariel'))


def clicked():
    # print('I got clicked')
    showcasethis["text"]= 'OH i changed'


button= Button(text = "Hey, click me", command = clicked)
button.pack()

entry = Entry(width=10)
entry.pack()


    # return user_typed

def user_value(typed):
    user_typed['text']= f"Value: {typed}"
    return user_typed

def get_str():
    get_used = entry.get()
    # print(get_used)
    user_value(get_used)

butt= Button(text= 'Enter', command= get_str)
butt.pack()



user_typed = Label(text= 'Value: ', font= ('Algerian', 29, 'bold'))
user_typed.pack()



screen.mainloop()
