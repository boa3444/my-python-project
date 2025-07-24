###

from tkinter import *
import pandas as pd
root= Tk()
root.geometry("600x600+55+45")
root.config(bg = "#6caa92")

# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)




french_words = pd.read_csv( r"C:\Users\newon\OneDrive\Documents\Tkinter\french_words.csv")
fc = {word['French']:word['English'] for index,word in french_words.iterrows()}



fc_img = PhotoImage(file =r"C:\Users\newon\OneDrive\Documents\Tkinter\fc_mages\card_front.png" )
resized_front = fc_img.subsample(2,2)
# frame.destroy()
# font.destroy()
frame = Frame(root, height= 350, width = 600, bg= '#6caa92')
frame.place(relx=0.6, rely=0.4, anchor='center') 
back_fc = PhotoImage(file = r"C:\Users\newon\OneDrive\Documents\Tkinter\fc_mages\card_back.png")
resized_back = back_fc.subsample(2,2)
    

index = 0
fc_french_list = []
fc_eng_list = []
revision_eng= []
revision_french= []

def show_back():
    Label(frame, image = resized_back, bg = '#6caa92').place(relx= 0.05, rely = 0.15)
    Label(frame, text = fc_eng_list[index -1], font = ('Ariel', 27, 'bold')).place(relx=0.37, rely=0.57, anchor='center')
    root.after(1000, front_fc.place_forget())


def revision_fc():
    if variable.get() == 'Cross':
        revision_french.append(fc_french_list[index])
        revision_eng.append(fc_eng_list[index])
        # fc_french_list.clear()
        # fc_eng_list.clear()


def do_this():

    global index, resized_front,front_fc
    
    front = Label(frame, image = resized_front,bg ='#6caa92' )
    front.place(relx= 0.05, rely = 0.15)
    
    for french,english in fc.items():
        fc_french_list.append(french)
        fc_eng_list.append(english)

    front_fc = Label(frame, text = f'{fc_french_list[index]}', bg= '#91c2af', font = ('Ariel', 27, 'bold') )
    front_fc.place(relx=0.37, rely=0.57, anchor='center')
    root.after(3000, show_back)

          

    
    if len(fc_french_list) == index:
        revision_fc()
        return


       

    index += 1
    

variable = StringVar(value = '')
def chose_tick():
    variable.set('Tick')
    do_this()

def chose_cross():
    variable.set('Cross')
    do_this()



do_this()
tick_mark= PhotoImage(file = r"C:\Users\newon\OneDrive\Documents\Tkinter\fc_mages\right.png")
resized_tick_mark = tick_mark.subsample(2,2)
cross_mark = PhotoImage(file = r"C:\Users\newon\OneDrive\Documents\Tkinter\fc_mages\wrong.png")
resized_cross_mark = cross_mark.subsample(2,2)
tick_button = Button(root, command = chose_tick, image = resized_tick_mark, bg = '#6caa92')
tick_button.place(relx = 0.75, rely = 0.75)
cross_button = Button(root, command = chose_tick, image = resized_cross_mark, bg = '#6caa92')
cross_button.place(relx = 0.2, rely = 0.75)

root.mainloop()
