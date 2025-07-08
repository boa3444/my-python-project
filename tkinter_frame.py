from tkinter import *
from tkinter import ttk

window= Tk()
window.config(bg= "black")
window.minsize(700,700)





frame_org = Frame(window, bg= "light blue", width= 300, height= 300)
frame_org.pack(padx= 5, pady= 5 , side= LEFT, fill= Y)



image_org= PhotoImage(file = r"C:\Users\newon\Downloads\tomato.png")   #use this later







minimized_img = image_org.subsample(2,2)   #shown as the org
org_image_heading= Label(frame_org, bg= "light blue" ,text= "Original Image")
org_image_heading.config(font= ("Times new roman", 17))
org_image_heading.pack(padx= 20)

org_image= Label(frame_org,image= minimized_img)
org_image.pack(padx= 5, pady= 0)


notebook = ttk.Notebook(frame_org)
notebook.pack(expand= True, fill = 'both', padx= 5, pady= 25)


#tools tab in notebook
tools_tab= Frame(notebook)
toolvar= StringVar(value= None)
for tool in ["Resize", "Replace"]:
    Radiobutton(tools_tab, text = tool, value= tool, variable= toolvar). pack(padx= 5)
tools_tab.pack(anchor= W, padx=20, pady= 5)


notebook.add(tools_tab, text= 'Tools')


#filters tab in notebook
filters_tab = Frame(notebook)
filt_var = StringVar(value= None)
for filter in ["Original", "B&W"]:
    Radiobutton(filters_tab, text = filter, value= filter, variable= filt_var ).pack(padx=5)
filters_tab.pack(anchor= W, padx= 20, pady= 5)
notebook.add(filters_tab, text = 'Filters')


edited_img_frame = Frame(window, bg= "light yellow", width= 500, height= 700)
edited_img_frame.pack(anchor= E, padx= 5, pady= 5)


edited_img_heading = Label(edited_img_frame, text= "Edited Image", bg = "light yellow")
edited_img_heading.config(font= ("Times new roman", 17))
edited_img_heading.pack(padx=5, pady= 5)

# zoomed_org_image = image_org.zoom(6,6)
edited_img= Label(edited_img_frame, image= image_org)
edited_img.config(width=500, height=600)
edited_img.pack(padx=225, pady= 25)


#to zoom the image




window.mainloop()