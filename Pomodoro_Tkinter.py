from tkinter import *
import winsound


root = Tk()
root.geometry("730x700+0+0")
root.config(bg="lightGreen")


# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# root.grid_columnconfigure(2, weight=1)

#TOMATO
tomato = PhotoImage(file = r"C:\Users\newon\Downloads\tomato.png")
Label(root, image = tomato, bg= "light green").place(x= 230, y=250)



####timer properties
start_click_count = 0
time= [24,59]                                                          
time_label= Label(root, text= "25:00", bg= "#f26849" ,font= ("Kristen ITC", 23,"bold"))
time_label.place(x=293, y=354)
timer_run = True
timer_reset= False
start_for_reset = False
run_rest_timer = True
run_focus_timer =False
pomodoro_count= 0
restart_count = False
focus_count = []
set_x = 220
set_y = 500


def set_up_pom_count():
        global set_x
        global count
        count = Label(root, text = "🌳",font= ("Kristen ITC", 23,"bold"), bg = "light green")
        count.place(x= set_x, y = set_y )
        set_x += 50
        focus_count.append(count)
        # count += 1
        
def restart_pom_count():     
        global set_x 
        if restart_count:
            for each in focus_count:
                each.destroy()

            focus_count.clear()
            set_x = 210
            

             
        
     



#Labels or Remainder
started_reminder = Label(root, text= "",bg="light green", width = 50)
started_reminder.place(x= 0 , y= 550)

reset_reminder = Label(root, text = "", bg= "light green", width = 50)
reset_reminder.place(x= 10, y = 620)


rest_work_reminder = Label(root, text = '💻 Time to focus! Deep work mode on.', bg = "light green", width = 50 ,font= ("Kristen ITC", 23,"bold"))
rest_work_reminder.place(x= -200, y= 15)

def set_rest_mode():
    rest_work_reminder.config(text="🌿 Time to rest! Stretch, hydrate, and relax.", bg="light green")

def set_focus_mode():
    rest_work_reminder.config(text="💻 Time to focus! Deep work mode on.", bg="light green")


def rest_timer():
    # if run_rest_timer:
        global time
        time = [4, 59]  
        set_rest_mode() 
        # run_focus_timer= True
        
            
def focus_timer():
    # if run_focus_timer:
        global time
        time = [24,59]
        set_focus_mode()



def run_timer():
    global timer_run, timer_reset, time, run_focus_timer, run_rest_timer, pomodoro_count, restart_count
    
      # timer_reset = True

        
    if timer_run:
        

        if time[0] == 0 and time[1] ==0 and run_focus_timer:    ###to start rest timer
            time_label.config(text= "00:00")
            winsound.Beep(800, 900)
            focus_timer()
            run_focus_timer= False
            run_rest_timer = True
            # set_up_pom_count()
            if pomodoro_count == 4 :
                # run_timer()
                pomodoro_count= 0
                restart_count= True
                restart_pom_count()

            
        

        
            

        if time[0] == 0 and time[1] ==0 and run_rest_timer:
            time_label.config(text= "00:00")
            winsound.Beep(800, 900)
            rest_timer()
            run_rest_timer = False
            # pomodoro_count += 1
            set_up_pom_count()
            if pomodoro_count ==4 :
                # run_timer()
                pomodoro_count= 0
                restart_count= True
                restart_pom_count()

            pomodoro_count += 1
            run_focus_timer= True
        
        
            
            
            
            
        ####add up here , only ticks now, label for rest and work

        time_label.config(text= f"{time[0]:02d}:{time[1]:02d}")
        # rest_work_reminder.config(text = "FOCUS TIME📖💻")

        if time[1] != 0 :
            time[1] -= 1

        elif time[1] ==0 :
            time_label.config(text= f"{time[0]}:00")
            time[1]= 59
            time[0] -= 1
                
        root.after(1000, run_timer)

    if timer_reset:
        time = [24, 59]
        reset_reminder.config(text = "Your timer has been resetted😇😇", font = ("Kristen ITC", 13,"bold"))            ###############
        root.after(2000,reset_reminder)
        timer_reset= False


#START timer

def timer_started():
    # try:
        global start_click_count
        start_click_count+= 1
        global start_for_reset
        

        if start_click_count == 1 or start_for_reset:
        

            global timer_run
            timer_run = True
            start_for_reset= False

            run_timer()

        if not start_for_reset and start_click_count !=1:
            started_reminder.config(text= "Already Started!!\nGet to the Work", font = ("Kristen ITC", 13,"bold"))         ##############
            # to_work.grid(row=4, column=1,padx = 5, pady=5)    ####to make sure it doesnot shift Start button when it operates
            root.after(1000, started_reminder.place_forget)
            


Button(root, text= "START", command = timer_started, width= 5, height = 10).place(x= 100, y=309)



####RESET Timer
def timer_reseted():
    time_label.config(text= "25:00")
    global timer_reset
    timer_reset= True
    global timer_run
    timer_run = False
    global start_for_reset
    start_for_reset = True

Button(root, text= "RESET", command= timer_reseted, width = 5, height = 10).place(x= 520, y=313)







root.mainloop()
