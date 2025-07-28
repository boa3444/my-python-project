from tkinter import *
import requests as rq


def get_quote():
    global quote_text
    quote_connection = rq.get(url = "https://api.kanye.rest")
    quote= quote_connection.json()['quote']
    # quote_text = canvas.create_text(150, 207, text = , width=250, font=("Arial", 20, "bold"), fill="white")
    canvas.itemconfig(quote_text, text =f'{quote}' )
    print(quote)
    
    #Write your code here.



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file= r"C:\Users\newon\Downloads\kanye-quotes-start\background.png")
canvas.create_image(150, 190, image=background_img)
quote_text = canvas.create_text(150, 207, text = '', width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"C:\Users\newon\Downloads\kanye-quotes-start\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()