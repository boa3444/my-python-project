from tkinter import *


page = Tk()
page.minsize(400,400)
page.title("VIRUAL NOTEPAD")
page.withdraw()


def save_as():
    file_name = 







def user_input():
    # print()
    save_as = Entry





save_button= Button(text="Click here to save this", command= user_input)
save_button.pack()

type_area = Text()
type_area.insert(END,"Type here...")
type_area.pack()

with open("notepad_txt.txt", mode = 'w') as user_file:
    user_file.write(type_area.get("1.0","end-1c"))











page.mainloop()