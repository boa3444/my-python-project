from tkinter import *

root = Tk()
root.minsize(600, 600)
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)


canvas = Canvas(root)
# canvas.config(bg = "white")
canvas.grid(row=0, column = 0, sticky = NSEW)


def start(event):
    global curr_x, curr_y
    curr_x = event.x
    curr_y = event.y

def draw_line(event):
    canvas.create_line((curr_x, curr_y), (event.x, event.y), fill = "black")
    start(event)



canvas.bind("<Button-1>", start)
canvas.bind("<B1-Motion>", draw_line)




root.mainloop()