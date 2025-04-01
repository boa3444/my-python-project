print("Your personal To-Do List Application")



user_input1= int(input("Press(1) to Add a task\n"
"Press (2) to View tasks\n"
"press (3) to Remove a task\n"
"Press (4) to Exit\n"))


tasks= []
if user_input1 == 1:
    while True:
        user_input2= input("Type your task here ( or type 'done' to stop): ")
        if user_input2== 'done':
            break
        else:
            tasks.append(user_input2)
        
tasks_str= '\n'.join(tasks)



if user_input1== 2:
    print(f"Your tasks are: {tasks_str}")

if user_input1==3 :
    user_input3= input("Type the name of task to remove it...")
    tasks.remove(user_input3)

if user_input1==4:
    while True:
        print("Exiting the application. Goodbye!")
        break
    





 
